# ¿Qué es un patrón de diseño?

> **Propósito de este documento.** Definir qué es un patrón de diseño, de qué se compone, por qué vale
> la pena aprenderlos, y cómo se relacionan con las heurísticas de diseño de este repositorio. Léelo
> antes de los capítulos del catálogo.

---

## Definición operativa

> **Un patrón de diseño es una solución típica y reutilizable a un problema que ocurre con frecuencia
> en el diseño de software.**

Un patrón **no** es un trozo de código específico. Es un **concepto** o plano general para resolver un
problema particular, que adaptas a los detalles de tu propio programa. No puedes simplemente copiar un
patrón como copias una función de una biblioteca; sigues la idea del patrón y la adaptas a tu
situación.

A menudo se confunde a los patrones con los algoritmos. Un **algoritmo** es un conjunto claro de pasos
que logra un objetivo (como una receta de cocina). Un **patrón** es más como un plano: muestra el
resultado y sus características, pero los pasos exactos de implementación los decides tú.

---

## Qué contiene la descripción de un patrón

Los patrones suelen describirse de forma que puedan reproducirse en muchos contextos. Una descripción
típica incluye:

- **Intención** — describe brevemente el problema y la solución.
- **Motivación** — explica el problema y cómo el patrón lo resuelve.
- **Estructura** — las clases involucradas y cómo se relacionan.
- **Aplicabilidad** — cuándo el patrón es (y cuándo no) una buena opción.
- **Ejemplo de código** — la solución mostrada en un lenguaje concreto.

---

## La clasificación

El catálogo clásico contiene **23 patrones**, agrupados en tres familias por su intención:

1. **Creacionales** — mecanismos de creación de objetos que aumentan flexibilidad y reutilización.
2. **Estructurales** — cómo ensamblar objetos y clases en estructuras mayores.
3. **De comportamiento** — algoritmos y asignación de responsabilidades entre objetos.

Los patrones más fundamentales y de bajo nivel suelen llamarse **modismos** (aplican a un solo
lenguaje). Los más universales y de alto nivel son **patrones arquitectónicos** y pueden implementarse
en casi cualquier lenguaje.

---

## ¿Por qué aprender patrones?

- **Son una caja de herramientas de soluciones probadas** a problemas comunes. Aunque nunca te
  encuentres el problema exacto, conocer patrones te enseña a resolver problemas de diseño usando
  principios de orientación a objetos.
- **Son un lenguaje común.** Decir "usa una Factory" comunica todo un diseño en dos palabras, siempre
  que tus compañeros conozcan el patrón.

Pero aprender patrones tiene un riesgo: aplicarlos donde no se necesitan. Un patrón usado sin su
problema es **complejidad accidental**. Por eso, en este repositorio, los patrones se tratan igual que
las [heurísticas](../../docs/es/06-por-que-heuristica.md): aplica cada uno en su contexto, espera
excepciones, y sopesa costo vs. beneficio.

---

## Cómo se relacionan los patrones con las heurísticas

- Las [heurísticas (H1–H6)](../../docs/es/00-resumen.md) gobiernan el **modelado fiel** — un objeto
  por ente, objetos completos y válidos, sin null, inmutabilidad, encapsulamiento.
- Los **patrones** dan **estructuras nombradas** para presiones de diseño recurrentes (creación,
  composición, comunicación).
- Los patrones *sirven* al modelo: recurre a uno solo cuando hace el modelo más claro o el diseño más
  flexible, nunca como un fin en sí mismo.

---

## Principios para el desarrollo

1. **Un patrón es un plano, no código.** Adáptalo; no lo copies a ciegas.
2. **Conoce primero la intención.** El problema que resuelve un patrón importa más que su diagrama de
   clases.
3. **Usa los patrones como vocabulario compartido,** pero solo donde el equipo comparte ese
   vocabulario.
4. **Sin problema, no hay patrón.** Introducir un patrón sin su problema añade complejidad para nada.

---

## Glosario

- **Patrón de diseño** — plano general y reutilizable para un problema de diseño recurrente.
- **Modismo (idiom)** — patrón de bajo nivel específico de un lenguaje.
- **Patrón arquitectónico** — patrón de alto nivel, independiente del lenguaje.
- **Intención** — el enunciado corto del problema que resuelve un patrón.
- **Algoritmo vs. patrón** — un algoritmo es un conjunto fijo de pasos; un patrón es un plano cuya
  implementación decides tú.

---

## Fuentes

- Alexander Shvets, *Dive Into Design Patterns*, Refactoring.Guru, 2022 — "What's a Design Pattern?" y
  "Why Should I Learn Patterns?".
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable
  Object-Oriented Software*, Addison-Wesley, 1994.
