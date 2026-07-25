# Design Patterns

Catalog of the 23 classic (Gang of Four) design patterns, plus the universal design principles that
motivate them. Each document defines the concepts and states them so they can be used directly as
context for development. Every document ends with its sources.

These documents complement the [object-oriented design heuristics](../README.md): the heuristics
say *how to model faithfully*; the patterns are *proven, reusable solutions* to recurring design
problems. Patterns are tools — apply them only when a real problem calls for them, never by
authority (see [06 — Why Heuristics, Not Principles or Rules?](../docs/en/06-why-heuristics.md)).

Documents are split by language into separate folders: [`en`](en) (primary, English) and
[`es`](es) (Spanish).

## Documents

| #   | Topic                          | English                                                          | Español                                                       |
| --- | ------------------------------ | --------------------------------------------------------------- | ------------------------------------------------------------- |
| 00  | Overview                       | [en/00-overview.md](en/00-overview.md)                          | [es/00-resumen.md](es/00-resumen.md)                          |
| 01  | What Is a Design Pattern?      | [en/01-what-is-a-design-pattern.md](en/01-what-is-a-design-pattern.md) | [es/01-que-es-un-patron.md](es/01-que-es-un-patron.md) |
| 02  | Software Design Principles     | [en/02-design-principles.md](en/02-design-principles.md)        | [es/02-principios-de-diseno.md](es/02-principios-de-diseno.md) |
| 03  | Creational Patterns            | [en/03-creational-patterns.md](en/03-creational-patterns.md)    | [es/03-patrones-creacionales.md](es/03-patrones-creacionales.md) |
| 04  | Structural Patterns            | [en/04-structural-patterns.md](en/04-structural-patterns.md)    | [es/04-patrones-estructurales.md](es/04-patrones-estructurales.md) |
| 05  | Behavioral Patterns            | [en/05-behavioral-patterns.md](en/05-behavioral-patterns.md)    | [es/05-patrones-de-comportamiento.md](es/05-patrones-de-comportamiento.md) |

## The 23 patterns at a glance

- **Creational (5)** — object creation mechanisms: Factory Method, Abstract Factory, Builder,
  Prototype, Singleton.
- **Structural (7)** — how to assemble objects and classes into larger structures: Adapter, Bridge,
  Composite, Decorator, Facade, Flyweight, Proxy.
- **Behavioral (11)** — algorithms and the assignment of responsibilities between objects: Chain of
  Responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method,
  Visitor.

## Structure of each document

1. **Working definition** — the concept stated as a usable definition.
2. **Core definitions** — the building blocks (intent, problem, applicability).
3. **Principles for development** — actionable guidance to apply while designing and coding.
4. **Glossary** — quick reference.
5. **Sources** — references, at the end.
