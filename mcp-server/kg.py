"""Knowledge graph mínimo para un corpus de documentación. Sin dependencias.

Cuatro etapas, cada una con su salida inspeccionable:
  1. TROCEAR  documentos -> secciones (el nodo)
  2. ENLAZAR  secciones  -> aristas (contiene, enlaza)
  3. BUSCAR   pregunta   -> secciones rankeadas (BM25)
  4. SERVIR   rankeadas  -> pasajes con cita, bajo presupuesto de tokens
"""
import re, sys, math, unicodedata
from pathlib import Path
from collections import Counter, defaultdict

# ---------------------------------------------------------------- 1. TROCEAR

def parse_sections(path: Path, root: Path):
    """Un documento -> lista de secciones. La sección ES el nodo del grafo."""
    lines = path.read_text(encoding="utf-8").splitlines()
    rel = path.relative_to(root).as_posix()
    marks, in_fence = [], False
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence          # no confundir ``` # comentario ``` con encabezado
        elif not in_fence and re.match(r"^#{1,3} ", line):
            marks.append((i, len(line) - len(line.lstrip("#")) - 1, line.lstrip("# ").strip()))
    out = []
    for n, (start, level, title) in enumerate(marks):
        end = marks[n + 1][0] if n + 1 < len(marks) else len(lines)
        body = "\n".join(lines[start + 1:end]).strip()
        out.append({
            "id": f"{rel}#{n}", "doc": rel, "title": title, "level": level,
            "line_start": start + 1, "line_end": end,       # 1-indexado, para citar
            "text": body,
        })
    return out


# ---------------------------------------------------------------- 2. ENLAZAR

LINK = re.compile(r"(?<!\!)\[[^\]]*\]\(\s*<?([^)\s>#]+)")

def build_edges(sections):
    """Dos clases de arista, con valor informativo MUY distinto."""
    edges = []
    by_doc = defaultdict(list)
    for s in sections:
        by_doc[s["doc"]].append(s)
    # (a) estructural: la sección de nivel N contiene a las de nivel N+1 que la siguen.
    for doc, secs in by_doc.items():
        stack = []
        for s in secs:
            while stack and stack[-1]["level"] >= s["level"]:
                stack.pop()
            if stack:
                edges.append((stack[-1]["id"], s["id"], "contiene"))
            stack.append(s)
    # (b) semántica: un enlace markdown a otro documento. ESTA es la que informa.
    docs = {s["doc"] for s in sections}
    for s in sections:
        src_dir = Path(s["doc"]).parent
        for raw in LINK.findall(s["text"]):
            if "://" in raw or not raw.endswith(".md"):
                continue
            tgt = _norm(src_dir, raw)          # resuelve ../ y ./ sin tocar el disco
            if tgt in docs and tgt != s["doc"]:
                edges.append((s["id"], tgt, "enlaza"))
    return edges

def _norm(src_dir: Path, raw: str) -> str:
    parts = []
    for p in (src_dir / raw).as_posix().split("/"):
        if p == "..":
            parts and parts.pop()
        elif p not in (".", ""):
            parts.append(p)
    return "/".join(parts)


# ----------------------------------------------------------------- 3. BUSCAR

def norm(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")   # quita tildes
    return re.findall(r"[a-z0-9_]+", t)

class BM25:
    """~20 líneas. Con 200 secciones supera a un índice vectorial en precisión y coste."""
    def __init__(self, docs, k1=1.5, b=0.75):
        self.k1, self.b = k1, b
        self.docs = [Counter(norm(d)) for d in docs]
        self.len = [sum(c.values()) for c in self.docs]
        self.avg = sum(self.len) / max(len(self.len), 1)
        self.df = Counter(w for c in self.docs for w in c)
        self.N = len(self.docs)

    def scores(self, query):
        out = [0.0] * self.N
        for w in norm(query):
            if w not in self.df:
                continue
            idf = math.log(1 + (self.N - self.df[w] + 0.5) / (self.df[w] + 0.5))
            for i, c in enumerate(self.docs):
                if w in c:
                    f = c[w]
                    out[i] += idf * f * (self.k1 + 1) / (
                        f + self.k1 * (1 - self.b + self.b * self.len[i] / self.avg))
        return out


# ----------------------------------------------------------------- 4. SERVIR

BOILERPLATE = {"fuentes", "glosario", "principios para el desarrollo"}

def answer(q, sections, edges, budget=800, expand=True):
    idx = {s["id"]: s for s in sections}
    bm = BM25([s["title"] + "\n" + s["text"] for s in sections])
    scored = sorted(zip(bm.scores(q), sections), key=lambda x: -x[0])
    scored = [(sc, s) for sc, s in scored
              if sc > 0 and s["title"].lower() not in BOILERPLATE]      # filtra andamiaje

    directos = [(sc, s, "directo") for sc, s in scored]

    # Expansión de 1 salto. CLAVE: los vecinos NO compiten en la misma escala que los
    # directos — se les reserva una fracción del presupuesto. Si compiten, la búsqueda
    # por texto siempre gana y el grafo no aporta nada.
    # Un documento "hub" (índice/resumen) enlaza a casi todo y menciona casi todo, así que
    # gana BM25 en cualquier consulta. Si anclas la expansión en él, sigues los enlaces del
    # índice en vez de los del tema. Se excluye como ancla.
    salida = Counter(idx[a]["doc"] for a, b, r in edges if r == "enlaza" and a in idx)
    umbral_hub = 0.5 * len({s["doc"] for s in sections})
    hubs = {d for d, n in salida.items() if n >= umbral_hub}

    vecinos = []
    if expand and directos:
        anclas = [s["doc"] for _, s, _ in directos if s["doc"] not in hubs]
        if not anclas:
            anclas = [directos[0][1]["doc"]]
        top_doc = anclas[0]
        docs_vecinos = {t for src, t, r in edges
                        if r == "enlaza" and idx.get(src, {}).get("doc") == top_doc}
        vistos_doc = set()
        for sc, s in scored:
            if s["doc"] in docs_vecinos and s["doc"] not in vistos_doc:
                vecinos.append((sc, s, f"vecino de {Path(top_doc).name} en el grafo"))
                vistos_doc.add(s["doc"])                 # una sección por documento vecino

    def llenar(cands, tope, seen, out):
        used = 0
        for sc, s, why in cands:
            if s["id"] in seen:
                continue
            p = (f"--- {s['doc']}:{s['line_start']}-{s['line_end']}  "
                 f"[{s['title']}]  ({why})\n{s['text']}")
            cost = len(p) // 4
            if used + cost > tope:
                continue
            out.append(p); seen.add(s["id"]); used += cost
        return used

    reserva = int(budget * 0.35) if vecinos else 0
    out, seen = [], set()
    u1 = llenar(directos, budget - reserva, seen, out)
    u2 = llenar(vecinos, reserva, seen, out) if vecinos else 0
    return "\n\n".join(out), u1 + u2, len(directos) + len(vecinos)


# ---------------------------------------------------------------------- main
if __name__ == "__main__":
    root = Path(sys.argv[1])
    sections = [s for p in sorted(root.rglob("*.md")) for s in parse_sections(p, root)]
    edges = build_edges(sections)
    q = sys.argv[2] if len(sys.argv) > 2 else "como modelo la ausencia de un valor sin usar null"
    budget = int(sys.argv[3]) if len(sys.argv) > 3 else 800
    text, used, cand = answer(q, sections, edges, budget)
    print(f"[{len(sections)} secciones · {len(edges)} aristas · {cand} candidatos · {used} tokens]\n")
    print(text)
