# SKILL: Consultas al Grafo de Heurísticas

Skill para explotar el grafo de conocimiento ya construido (ver `graph-builder/`). Úsalo cuando el
grafo ya esté poblado y quieras razonar sobre las heurísticas, problemas, soluciones y patrones.

Servidor MCP requerido: `knowledge-graph-memory`.

---

## Preguntas típicas (patrones de consulta)

Traduce la intención del usuario a recorridos del grafo usando las herramientas de lectura del
servidor (`search_nodes`, `open_nodes`, `read_graph`, o consultas del backend):

| Intención del usuario                                   | Recorrido en el grafo                                             |
| ------------------------------------------------------- | ---------------------------------------------------------------- |
| "¿Qué problemas previene H4?"                            | `Heuristica(H4) -PREVIENE-> Problema`                             |
| "¿Cómo implemento H5?"                                   | `Heuristica(H5) -IMPLEMENTA_CON-> (Solucion \| Patron)`          |
| "¿Qué heurística evita NullPointerException?"            | `Problema(NPE) <-PREVIENE- (Heuristica \| Concepto)`            |
| "¿Qué conceptos define H6?"                              | `Heuristica(H6) -DEFINE-> Concepto`                              |
| "¿Qué patrones se relacionan con inmutabilidad?"         | `Concepto(Inmutabilidad) -RELACIONADO_CON-> ... ; -IMPLEMENTA_CON` |
| "Muéstrame todo lo conectado a 'Estado'"                | vecindario de `Concepto(Estado)` a 1–2 saltos                    |
| "¿En qué heurísticas se apoya H6?"                       | `Heuristica(H6) -RELACIONADO_CON-> Heuristica`                   |
| "¿Qué heurísticas dependen de H3?"                       | `Heuristica(H3) <-RELACIONADO_CON- Heuristica`                  |
| "¿Qué patrón GoF implementa H4?"                         | `Heuristica(H4) -IMPLEMENTA_CON-> Patron`                        |
| "¿Qué heurísticas usan el patrón Decorator?"             | `Patron(Decorator) <-IMPLEMENTA_CON- Heuristica`               |
| "¿Qué fuente respalda el information hiding?"             | `Concepto(Information Hiding) <-CITADO_EN- Fuente`              |
| "¿Qué aporta Parnas (1972) al grafo?"                    | `Fuente(Parnas 1972) -CITADO_EN-> (Heuristica \| Concepto)`     |

---

## Buenas prácticas de respuesta

1. **Cita la fuente.** Cada nodo tiene `source`; incluye la ruta del documento de origen.
2. **Muestra el camino.** Explica el recorrido (nodos y aristas) que sustenta la respuesta.
3. **No inventes aristas.** Responde solo con lo que existe en el grafo; si falta, dilo y sugiere
   ejecutar `graph-builder` sobre el archivo relevante.
4. **Prioriza lo específico.** Ante ambigüedad, abre el nodo exacto (`open_nodes`) antes de un
   `read_graph` completo.

---

## Ejemplo

**Usuario:** "¿Qué problemas previene H4 y con qué solución se implementa?"

**Recorrido:**

```
Heuristica(h4_null)
  -PREVIENE-> Problema(NullPointerException)
  -IMPLEMENTA_CON-> Solucion(Null Object Pattern)
```

**Respuesta esperada:** H4 previene `NullPointerException` y se implementa con el `Null Object
Pattern` (fuente: `docs/es/10-h4-no-usar-null.md`).

---

## Ejemplo — recorrido multi-tipo (heurísticas y fuentes)

**Usuario:** "¿En qué heurísticas se apoya H6, con qué patrón se implementa y qué fuente lo respalda?"

**Recorrido:**

```
Heuristica(h6_encapsulamiento)
  -RELACIONADO_CON-> Heuristica(h3_validos), Heuristica(h4_null), Heuristica(h5_inmutabilidad)
  -IMPLEMENTA_CON--> Patron(Decorator), Solucion(Tell, Don't Ask)
  <-CITADO_EN------- Fuente(Parnas 1972)
```

**Respuesta esperada:** H6 se apoya en H3, H4 y H5; se implementa con "Tell, Don't Ask" y, al
devolver internals, con el patrón `Decorator` (wrapper inmutable). El concepto de *information
hiding* que sustenta H6 proviene de `Parnas (1972)` (fuente: `docs/es/12-h6-encapsulamiento.md`).
