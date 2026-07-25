# Primera ejecución — Poblar el grafo completo

Runbook para construir el grafo de conocimiento desde cero, en orden. Cada paso es una **orden que le
das al agente** (con el skill [`graph-builder/SKILL.md`](graph-builder/SKILL.md) cargado) y los
servidores MCP `github-extractor` y `knowledge-graph-memory` activos (ver [`SETUP.md`](SETUP.md)).

> **Orden recomendado:** conceptos base → heurísticas H1→H6 → prácticas → patrones. Así, cuando una
> heurística referencia a otra (p. ej. H6 → H3/H4/H5), los nodos destino **ya existen** y el agente
> solo crea la arista `RELACIONADO_CON` (aplicando H1 — no duplicar).

---

## Fase 0 — Preparación

1. Verifica que ambos servidores MCP responden en tu cliente.
2. Carga el skill `graph-builder/SKILL.md` como contexto/sistema del agente.
3. (Opcional) Parte de un grafo vacío para una ejecución limpia:

   > "Vacía el grafo de conocimiento antes de empezar."

Repositorio de origen: `jackparra253/object-oriented-software-design-heuristics`.

---

## Fase 1 — Conceptos base (docs 00–06)

Estos documentos definen el vocabulario (software, modelo, objeto, heurística) sobre el que se apoyan
las heurísticas. Poblarlos primero evita `Concepto` duplicados más adelante.

> "Ejecuta el plan para estos archivos, uno por uno, en este orden:
> `docs/es/00-resumen.md`, `docs/es/01-que-es-software.md`, `docs/es/02-cual-es-el-modelo.md`,
> `docs/es/03-buen-modelo.md`, `docs/es/04-desarrollo-de-software.md`,
> `docs/es/05-que-es-un-objeto.md`, `docs/es/06-por-que-heuristica.md`."

---

## Fase 2 — Heurísticas H1→H6 (docs 07–12)

El núcleo. Respeta el orden numérico: cada heurística tiende a apoyarse en las anteriores.

> "Ejecuta el plan para estos archivos, uno por uno, en este orden:
> `docs/es/07-h1-objeto-por-ente.md`, `docs/es/08-h2-objetos-completos.md`,
> `docs/es/09-h3-objetos-validos.md`, `docs/es/10-h4-no-usar-null.md`,
> `docs/es/11-h5-objetos-inmutables.md`, `docs/es/12-h6-encapsulamiento.md`.
> Cuando un documento se apoye en otra heurística ya creada, enlázala con `RELACIONADO_CON` sin
> duplicar nodos."

Resultado esperado por heurística: 1 nodo `Heuristica` + sus `Concepto`/`Problema`/`Solucion`, más
aristas `DEFINE`/`PREVIENE`/`IMPLEMENTA_CON`, aristas `RELACIONADO_CON` a heurísticas previas, y
nodos `Fuente` con `CITADO_EN`.

---

## Fase 3 — Prácticas complementarias (docs 13–14)

No son heurísticas, pero aportan `Concepto`/`Solucion` conectados (TDD, nombramiento).

> "Ejecuta el plan para `docs/es/13-tdd.md` y `docs/es/14-nombramiento.md`, uno por uno."

---

## Fase 4 — Catálogo de patrones de diseño

Puebla los nodos `Patron` (GoF) y conéctalos, cuando corresponda, con `IMPLEMENTA_CON` desde las
heurísticas ya existentes.

> "Ejecuta el plan para estos archivos, uno por uno, en este orden:
> `design-patterns/es/00-resumen.md`, `design-patterns/es/01-que-es-un-patron.md`,
> `design-patterns/es/02-principios-de-diseno.md`, `design-patterns/es/03-patrones-creacionales.md`,
> `design-patterns/es/04-patrones-estructurales.md`,
> `design-patterns/es/05-patrones-de-comportamiento.md`.
> Crea nodos `Patron` y enlázalos a las heurísticas relacionadas con `IMPLEMENTA_CON` (p. ej. H4 →
> Null Object; el wrapper de H6 → Decorator/Proxy; H5 → Value Object)."

---

## Fase 5 — Verificación del grafo

Usa el skill [`graph-query/SKILL.md`](graph-query/SKILL.md) para comprobar integridad:

1. **Cobertura de heurísticas:**
   > "Lista todos los nodos `Heuristica` y cuántas aristas tiene cada uno."
   Esperado: H1–H6 presentes, cada uno con `DEFINE`, `PREVIENE` y/o `IMPLEMENTA_CON`.

2. **Sin duplicados (H1):**
   > "Busca nodos con `name` repetido o muy similar y repórtalos."
   Esperado: ninguno; si aparecen, fusiónalos.

3. **Enlaces entre heurísticas:**
   > "¿En qué heurísticas se apoya H6?"
   Esperado: H3, H4, H5 vía `RELACIONADO_CON`.

4. **Conexión con patrones:**
   > "¿Qué heurísticas tienen `IMPLEMENTA_CON` hacia un nodo `Patron`?"
   Esperado: al menos H4 (Null Object) y H5 (Value Object).

5. **Trazabilidad:**
   > "Lista los nodos `Fuente` y a qué heurística/concepto respaldan."

---

## Variante en inglés (opcional)

Para poblar también el contenido en inglés, repite las Fases 1–4 usando las rutas `docs/en/...` y
`design-patterns/en/...`. **Reutiliza los nodos existentes** (mismos `id` slug); el idioma cambia el
texto de origen, no la entidad de dominio. Añade la ruta EN como `source` adicional en las
observaciones del nodo en lugar de crear nodos nuevos.

---

## Resumen de la secuencia

| Fase | Contenido                         | Archivos            |
| ---- | --------------------------------- | ------------------- |
| 0    | Preparación                       | —                   |
| 1    | Conceptos base                    | `docs/es/00`–`06`   |
| 2    | Heurísticas H1→H6                 | `docs/es/07`–`12`   |
| 3    | Prácticas (TDD, nombramiento)     | `docs/es/13`–`14`   |
| 4    | Patrones de diseño                | `design-patterns/es/00`–`05` |
| 5    | Verificación                      | — (skill de consulta) |
