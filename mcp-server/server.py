"""Servidor MCP sobre el grafo de conocimiento de este repositorio.

Expone tres herramientas de recuperación con presupuesto de tokens:
  buscar(pregunta)  -> pasajes con cita (la respuesta, no su dirección)
  abrir(seccion)    -> el texto íntegro de una sección concreta
  vecinos(documento)-> qué documentos enlaza y quién lo enlaza a él

El índice se construye en memoria al arrancar (~158 secciones, instantáneo) y se
reconstruye si algún .md cambió, para que editar un documento se refleje sin reiniciar.
"""
from __future__ import annotations

import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from kg import parse_sections, build_edges, answer

# Raíz del corpus: por defecto el repo que contiene este archivo.
ROOT = Path(os.environ.get("HEURISTICS_ROOT", Path(__file__).resolve().parent.parent))
SUBDIRS = ("docs", "design-patterns")

# Un solo idioma por índice (H1: docs/es/10-... y docs/en/10-... son el MISMO ente).
# Indexar ambos duplica cada nodo y degrada la relevancia: las dos versiones compiten
# entre sí en el ranking y ninguna gana con claridad.
LANG = os.environ.get("HEURISTICS_LANG", "es")

mcp = FastMCP("heuristics-kg")

_cache: dict = {"firma": None, "secciones": [], "aristas": []}


def _archivos() -> list[Path]:
    out: list[Path] = []
    for sub in SUBDIRS:
        d = ROOT / sub / LANG
        if d.is_dir():
            out += sorted(d.rglob("*.md"))
    return out


def _indice():
    """Devuelve (secciones, aristas), reconstruyendo solo si algún .md cambió."""
    archivos = _archivos()
    firma = tuple((p.as_posix(), p.stat().st_mtime_ns) for p in archivos)
    if firma != _cache["firma"]:
        secciones = [s for p in archivos for s in parse_sections(p, ROOT)]
        _cache.update(firma=firma, secciones=secciones, aristas=build_edges(secciones))
    return _cache["secciones"], _cache["aristas"]


@mcp.tool()
def buscar(pregunta: str, presupuesto: int = 800) -> str:
    """Busca en la guía de diseño con objetos (heurísticas H1-H6, TDD, nombramiento, patrones
    GoF) y devuelve los pasajes relevantes con su cita archivo:línea.

    Devuelve el TEXTO de las secciones, no solo referencias. Úsala para cualquier pregunta
    sobre diseño de objetos, null, encapsulamiento, inmutabilidad, validación, nombres o
    patrones de diseño.

    Args:
        pregunta: la pregunta en lenguaje natural.
        presupuesto: tope de tokens de la respuesta (por defecto 800).
    """
    secciones, aristas = _indice()
    texto, usados, candidatos = answer(pregunta, secciones, aristas, budget=presupuesto)
    if not texto:
        return "Sin resultados. Prueba con otros términos."
    cab = f"[{usados} tokens · {candidatos} candidatos · {len(secciones)} secciones indexadas]\n\n"
    return cab + texto


@mcp.tool()
def abrir(seccion: str) -> str:
    """Devuelve el texto íntegro de una sección, sin recortar por presupuesto.

    Args:
        seccion: el id que aparece en las citas (p. ej. "docs/es/10-h4-no-usar-null.md#5"),
                 o una ruta de documento para obtener su índice de secciones.
    """
    secciones, _ = _indice()
    exacta = [s for s in secciones if s["id"] == seccion]
    if exacta:
        s = exacta[0]
        return (f"# {s['title']}\n({s['doc']}:{s['line_start']}-{s['line_end']})\n\n{s['text']}")

    deldoc = [s for s in secciones if s["doc"] == seccion or s["doc"].endswith("/" + seccion)]
    if deldoc:
        líneas = [f"Secciones de {deldoc[0]['doc']}:"]
        líneas += [f"  {s['id']}  L{s['line_start']}-{s['line_end']}  {s['title']}"
                   for s in deldoc]
        return "\n".join(líneas)
    return f"No encontrado: {seccion}"


@mcp.tool()
def vecinos(documento: str) -> str:
    """Muestra las relaciones de un documento en el grafo: a qué documentos enlaza y cuáles
    lo enlazan. Úsala para saber en qué otras heurísticas o patrones se apoya un tema.

    Args:
        documento: ruta o nombre de archivo (p. ej. "12-h6-encapsulamiento.md").
    """
    secciones, aristas = _indice()
    idx = {s["id"]: s for s in secciones}
    docs = {s["doc"] for s in secciones}
    objetivo = next((d for d in sorted(docs)
                     if d == documento or d.endswith("/" + documento)), None)
    if objetivo is None:
        return f"No encontrado: {documento}"

    salientes, entrantes = set(), set()
    for a, b, r in aristas:
        if r != "enlaza":
            continue
        origen = idx.get(a, {}).get("doc")
        if origen == objetivo:
            salientes.add(b)
        if b == objetivo and origen:
            entrantes.add(origen)

    out = [objetivo]
    out += [f"  --enlaza--> {d}" for d in sorted(salientes)] or ["  (no enlaza a ningún documento)"]
    out += [f"  <--enlazado por-- {d}" for d in sorted(entrantes)] or ["  (nadie lo enlaza)"]
    return "\n".join(out)


if __name__ == "__main__":
    mcp.run()
