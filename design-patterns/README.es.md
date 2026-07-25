# Patrones de Diseño

Catálogo de los 23 patrones de diseño clásicos (Gang of Four), más los principios de diseño
universales que los motivan. Cada documento define los conceptos y los enuncia de forma que puedan
usarse directamente como contexto de desarrollo. Cada documento termina con sus fuentes.

Estos documentos complementan las [heurísticas de diseño orientado a objetos](../README.md): las
heurísticas dicen *cómo modelar con fidelidad*; los patrones son *soluciones probadas y reutilizables*
a problemas de diseño recurrentes. Los patrones son herramientas — aplícalos solo cuando un problema
real lo requiera, nunca por autoridad (ver
[06 — ¿Por qué heurística, no principios ni reglas?](../docs/es/06-por-que-heuristica.md)).

Los documentos se dividen por idioma en carpetas separadas: [`en`](en) (principal, inglés) y
[`es`](es) (español).

## Documentos

| #   | Tema                           | Inglés                                                          | Español                                                      |
| --- | ------------------------------ | -------------------------------------------------------------- | ------------------------------------------------------------ |
| 00  | Resumen                        | [en/00-overview.md](en/00-overview.md)                         | [es/00-resumen.md](es/00-resumen.md)                         |
| 01  | ¿Qué es un patrón de diseño?   | [en/01-what-is-a-design-pattern.md](en/01-what-is-a-design-pattern.md) | [es/01-que-es-un-patron.md](es/01-que-es-un-patron.md) |
| 02  | Principios de diseño de software | [en/02-design-principles.md](en/02-design-principles.md)     | [es/02-principios-de-diseno.md](es/02-principios-de-diseno.md) |
| 03  | Patrones creacionales          | [en/03-creational-patterns.md](en/03-creational-patterns.md)   | [es/03-patrones-creacionales.md](es/03-patrones-creacionales.md) |
| 04  | Patrones estructurales         | [en/04-structural-patterns.md](en/04-structural-patterns.md)   | [es/04-patrones-estructurales.md](es/04-patrones-estructurales.md) |
| 05  | Patrones de comportamiento     | [en/05-behavioral-patterns.md](en/05-behavioral-patterns.md)   | [es/05-patrones-de-comportamiento.md](es/05-patrones-de-comportamiento.md) |

## Los 23 patrones de un vistazo

- **Creacionales (5)** — mecanismos de creación de objetos: Factory Method, Abstract Factory, Builder,
  Prototype, Singleton.
- **Estructurales (7)** — cómo ensamblar objetos y clases en estructuras mayores: Adapter, Bridge,
  Composite, Decorator, Facade, Flyweight, Proxy.
- **De comportamiento (11)** — algoritmos y asignación de responsabilidades entre objetos: Chain of
  Responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method,
  Visitor.

## Estructura de cada documento

1. **Definición operativa** — el concepto enunciado como definición utilizable.
2. **Definiciones base** — los bloques de construcción (intención, problema, aplicabilidad).
3. **Principios para el desarrollo** — guía accionable para aplicar al diseñar y programar.
4. **Glosario** — referencia rápida.
5. **Fuentes** — referencias, al final.
