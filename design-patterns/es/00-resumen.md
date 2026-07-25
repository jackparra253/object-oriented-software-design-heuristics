# Resumen — Patrones de Diseño

> **Propósito de este documento.** Un recorrido breve por todo el catálogo: qué es un patrón de
> diseño, por qué los patrones clásicos (Gang of Four) se agrupan en tres familias, y una intención
> de una línea para cada uno de los 23 patrones. Léelo primero; cada familia se desarrolla en su
> propio capítulo, enlazado en línea. La sección final **Principios para el desarrollo** es la lista
> corta que conviene tener abierta mientras diseñas.

---

## Parte I — Qué es un patrón (y qué no)

Un **patrón de diseño** es una solución general y reutilizable a un problema que ocurre con frecuencia
en el diseño de software. No es un trozo de código terminado que se pega; es una **descripción o
plano** de cómo resolver un problema, que adaptas a tu programa. (Ver
[01 — ¿Qué es un patrón de diseño?](01-que-es-un-patron.md).)

Los patrones y las [heurísticas de diseño](../../docs/es/00-resumen.md) trabajan juntos: las
heurísticas te dicen cómo construir un *modelo fiel* del dominio; los patrones te dan *estructuras
nombradas y probadas* para problemas de diseño recurrentes. Como las heurísticas, los patrones son
**herramientas, no reglas** — aplica cada uno en su contexto, sopesa costo vs. beneficio, y nunca
introduzcas un patrón donde el problema no existe.

En este catálogo, cada patrón se interpreta explícitamente contra **H1–H6**:

- **H1 (un objeto por ente):** evita representaciones ambiguas y responsabilidades mezcladas.
- **H2/H3 (objetos completos y válidos):** la creación/transición debe impedir estados imposibles.
- **H4 (no null):** ausencia y variación se modelan con objetos/protocolos, no con sentinelas.
- **H5 (inmutabilidad):** comparte y comunica con estado estable siempre que sea posible.
- **H6 (encapsulamiento):** prioriza "decir, no preguntar"; evita exponer internals para coordinar.

La pregunta práctica para elegir patrón no es "¿cuál conozco?", sino: **¿qué heurística está bajo
presión aquí y qué patrón la protege mejor?**

---

## Parte II — Principios de diseño detrás de los patrones

La mayoría de los patrones son aplicaciones concretas de unos pocos principios universales (ver
[02 — Principios de diseño de software](02-principios-de-diseno.md)):

- **Encapsular lo que varía** — identifica los aspectos que cambian y sepáralos de lo que permanece
  igual, para que los cambios afecten a menos código.
- **Programar hacia una interfaz, no hacia una implementación** — depende de abstracciones, para que
  los colaboradores sean intercambiables.
- **Favorecer la composición sobre la herencia** — construye comportamiento combinando objetos en
  lugar de crecer jerarquías de clases profundas.
- **SOLID** — Responsabilidad Única, Abierto/Cerrado, Sustitución de Liskov, Segregación de
  Interfaces, Inversión de Dependencias.

---

## Parte III — Las tres familias

### Patrones creacionales

Proveen mecanismos de creación de objetos que aumentan la flexibilidad y la reutilización del código
existente. (Ver [03 — Patrones creacionales](03-patrones-creacionales.md).)

- **Factory Method** — provee una interfaz para crear objetos en una superclase, pero permite a las
  subclases alterar el tipo de objetos que se crearán.
- **Abstract Factory** — permite producir familias de objetos relacionados sin especificar sus clases
  concretas.
- **Builder** — permite construir objetos complejos paso a paso, produciendo distintos tipos y
  representaciones con el mismo código de construcción.
- **Prototype** — permite copiar objetos existentes sin que el código dependa de sus clases.
- **Singleton** — asegura que una clase tenga una sola instancia, dando un punto de acceso global.

### Patrones estructurales

Explican cómo ensamblar objetos y clases en estructuras mayores manteniéndolas flexibles y
eficientes. (Ver [04 — Patrones estructurales](04-patrones-estructurales.md).)

- **Adapter** — permite que objetos con interfaces incompatibles colaboren.
- **Bridge** — divide una clase grande (o conjunto de clases relacionadas) en dos jerarquías —
  abstracción e implementación — desarrolladas de forma independiente.
- **Composite** — compone objetos en estructuras de árbol y permite trabajarlas como si fueran objetos
  individuales.
- **Decorator** — añade comportamientos nuevos a objetos colocándolos dentro de objetos envoltorio.
- **Facade** — provee una interfaz simplificada a una biblioteca, framework o conjunto complejo de
  clases.
- **Flyweight** — permite meter más objetos en la RAM compartiendo partes comunes de estado.
- **Proxy** — provee un sustituto o marcador de posición que controla el acceso a otro objeto.

### Patrones de comportamiento

Se ocupan de los algoritmos y de la asignación de responsabilidades entre objetos. (Ver
[05 — Patrones de comportamiento](05-patrones-de-comportamiento.md).)

- **Chain of Responsibility** — pasa solicitudes por una cadena de manejadores; cada uno decide
  procesarla o pasarla.
- **Command** — convierte una solicitud en un objeto autónomo, habilitando colas, registro y deshacer.
- **Iterator** — recorre los elementos de una colección sin exponer su representación interna.
- **Mediator** — reduce dependencias caóticas forzando a los objetos a colaborar vía un mediador.
- **Memento** — guarda y restaura el estado previo de un objeto sin revelar su implementación.
- **Observer** — define un mecanismo de suscripción para notificar a varios objetos sobre eventos.
- **State** — permite que un objeto altere su comportamiento cuando cambia su estado interno.
- **Strategy** — define una familia de algoritmos intercambiables, cada uno en su propia clase.
- **Template Method** — define el esqueleto de un algoritmo en una superclase, dejando a las subclases
  redefinir pasos concretos.
- **Visitor** — separa los algoritmos de los objetos sobre los que operan.

---

## Principios para el desarrollo

Aplica estos directamente (como heurísticas, no como reglas).

1. **Recurre a un patrón solo cuando el problema existe.** Un patrón introducido sin su problema es
   complejidad accidental; daña el eje descriptivo del modelo.
2. **Aprende la intención, no solo el diagrama.** Dos patrones pueden compartir estructura y resolver
   problemas distintos; lo que importa es la intención.
3. **Prefiere primero la opción más simple.** Muchos diseños empiezan simples (p. ej. Factory Method)
   y evolucionan hacia patrones más flexibles solo cuando aparece la presión.
4. **Los patrones sirven al modelo.** Son un medio hacia un modelo fiel y habitable — nunca el fin.
5. **Nombra por el dominio.** Cuando un patrón aparece en tu código, sigue nombrando las clases por lo
   que representan en el dominio, no solo por el patrón.

---

## Glosario

- **Patrón de diseño** — plano general y reutilizable para un problema de diseño recurrente.
- **Intención** — el problema central que resuelve un patrón, en una o dos frases.
- **Gang of Four (GoF)** — los cuatro autores de *Design Patterns: Elements of Reusable
  Object-Oriented Software* (1994), que catalogaron estos 23 patrones.

---

## Fuentes

- Alexander Shvets, *Dive Into Design Patterns*, Refactoring.Guru, 2022.
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable
  Object-Oriented Software*, Addison-Wesley, 1994.
