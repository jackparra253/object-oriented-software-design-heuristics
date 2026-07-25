# Ontología del Grafo de Heurísticas

Esquema **estricto** del grafo de conocimiento. Todo nodo y toda arista deben encajar en estos tipos.
No se permiten tipos fuera de esta lista (aplicación de **H3 — solo entidades válidas**).

---

## Tipos de nodos (etiquetas)

| Etiqueta      | Significado                                              | Ejemplo                               |
| ------------- | ------------------------------------------------------- | ------------------------------------- |
| `Heuristica`  | Principio o regla de diseño del repositorio             | "H4 — No usar Null"                   |
| `Concepto`    | Concepto de ingeniería de software                      | "Inmutabilidad", "Estado"             |
| `Problema`    | Bug o antipatrón que el software sufre                   | "NullPointerException", "Race Condition" |
| `Solucion`    | Patrón táctico de implementación                        | "Null Object Pattern", "Objetos Completos" |
| `Patron`      | Patrón de diseño (GoF o DDD)                            | "Strategy", "Builder", "Observer", "Value Object" |
| `Fuente`      | Referencia bibliográfica o autor citado                 | "Parnas (1972)", "GoF — Design Patterns" |

> Nota: `Patron` conecta el catálogo `design-patterns/` (patrones GoF) y los patrones tácticos de
> DDD (p. ej. Value Object, Entity, Repository) con las heurísticas. `Fuente` da trazabilidad
> académica a la sección de bibliografía de cada documento.

---

## Tipos de relaciones (aristas)

| Relación          | Dirección típica                         | Significado                              |
| ----------------- | ---------------------------------------- | ---------------------------------------- |
| `DEFINE`          | (Heuristica) → (Concepto)                | La heurística define/introduce el concepto |
| `PREVIENE`        | (Concepto \| Heuristica) → (Problema)    | Evita que ocurra el problema             |
| `IMPLEMENTA_CON`  | (Heuristica) → (Solucion \| Patron)      | Se lleva a la práctica con esa solución/patrón |
| `RELACIONADO_CON` | (Concepto) → (Concepto)  ·  (Heuristica) → (Heuristica) | Conexión conceptual entre ideas, o entre heurísticas que se apoyan mutuamente |
| `CITADO_EN`       | (Fuente) → (Heuristica \| Concepto)      | La fuente respalda/origina la heurística o concepto |

---

## Reglas de integridad

1. **Un nodo por entidad (H1).** No dupliques: si el concepto ya existe, enlaza a él.
2. **Nombres de dominio.** Nombra los nodos por lo que representan, no por su archivo o ID técnico.
3. **Propiedades mínimas por nodo:**
   - `name` — nombre canónico y legible.
   - `source` — ruta del archivo de origen (p. ej. `docs/es/10-h4-no-usar-null.md`).
4. **IDs estables.** Usa un `id` slug reproducible (p. ej. `h4_null`, `c_inmutabilidad`) para poder
   reconciliar en ejecuciones sucesivas.
5. **Sin aristas fuera de la ontología.** Cualquier relación no listada se descarta.
6. **Relaciones entre heurísticas.** Usa `RELACIONADO_CON` entre nodos `Heuristica` cuando un
   documento se apoye en otra heurística (p. ej. H6 se apoya en H3, H4 y H5).
7. **Patrones GoF.** Cuando una heurística se lleve a la práctica con un patrón del catálogo
   `design-patterns/`, enlázala con `IMPLEMENTA_CON` a un nodo `Patron` (p. ej. H4 → Null Object; el
   "wrapper" de H6 → Decorator/Proxy).
8. **Fuentes.** Los autores/obras de la sección de bibliografía se modelan como nodos `Fuente` y se
   enlazan con `CITADO_EN` hacia la heurística o concepto que respaldan.

---

## Ejemplo de subgrafo (H4 — No usar Null)

```
(Heuristica: H4 — Don't Use Null)
    ├── PREVIENE ─────────► (Problema: NullPointerException)
    ├── IMPLEMENTA_CON ───► (Solucion: Null Object Pattern)
    ├── IMPLEMENTA_CON ───► (Patron: Null Object)
    ├── DEFINE ───────────► (Concepto: Ausencia como objeto)
    └── RELACIONADO_CON ──► (Heuristica: H5 — Objetos Inmutables)

(Concepto: Ausencia como objeto) ── RELACIONADO_CON ──► (Concepto: Inmutabilidad)
(Fuente: GoF — Design Patterns) ── CITADO_EN ──► (Heuristica: H4 — Don't Use Null)
```

Payloads correspondientes (ver `graph-builder/SKILL.md` para el formato exacto de las herramientas):

```json
{
  "nodes": [
    {"id": "h4_null", "label": "Heuristica", "properties": {"name": "H4 — Don't Use Null", "source": "docs/es/10-h4-no-usar-null.md"}},
    {"id": "c_null_ptr", "label": "Problema", "properties": {"name": "NullPointerException"}},
    {"id": "s_null_obj", "label": "Solucion", "properties": {"name": "Null Object Pattern"}}
  ]
}
```

```json
{
  "edges": [
    {"source": "h4_null", "target": "c_null_ptr", "type": "PREVIENE"},
    {"source": "h4_null", "target": "s_null_obj", "type": "IMPLEMENTA_CON"}
  ]
}
```
