# ¿Por qué heurísticas y no principios o reglas?

> **Propósito de este documento.** Fija la postura para aplicar toda la guía de diseño que sigue.
> Define qué es una heurística, cómo se diferencia de un principio y de una regla, y cómo aplicar
> esa guía. Leé la guía de diseño de este repo como *heurísticas*: aplicalas con criterio crítico,
> en contexto y esperando excepciones.

---

## Definición de trabajo

La guía de diseño de acá está formulada como **heurísticas**, deliberadamente —no como principios,
leyes ni reglas—.

> **Una heurística es una regla que debe ser analizada contextualmente. Puede tener excepciones; no
> siempre conviene usarla.**

Una heurística es una estrategia, método o criterio que ayuda a resolver problemas —un consejo
empírico y de sentido común que se ha observado que funciona en muchos casos, pero que no está
garantizado que funcione siempre ni es obligatorio seguir—.

---

## Principio vs. regla vs. heurística

| Concepto         | Qué afirma                                                                        | Cómo tratarlo                              |
| ---------------- | --------------------------------------------------------------------------------- | ------------------------------------------ |
| **Principio**    | Una verdad o proposición fundamental que sirve de base para un sistema de creencias, comportamiento o cadena de razonamiento. | Un cimiento desde el cual razonás.         |
| **Regla / ley**  | Algo que siempre se cumple y debe seguirse.                                        | Se aplica incondicionalmente.              |
| **Heurística**   | Una guía contextual y empírica que en general ayuda pero puede tener excepciones.  | Se aplica con criterio; se la cuestiona en contexto. |

La distinción clave: una **regla** está hecha para obedecerse; una **heurística** está hecha para
*sopesarse*. Te ayuda a encontrar una solución eficaz y eficiente, pero vos decidís —para este
contexto— si aplica.

---

## Los "principios" suelen ser heurísticas

Mucho de lo que la industria llama "principios" se comporta como heurísticas. Los "principios"
SOLID son un ejemplo claro. Como dice su propio autor, Robert C. Martin:

> Los principios SOLID no son reglas. No son leyes. No son verdades perfectas. … Este es un buen
> principio, es un buen consejo, pero no es una pura verdad, ni es una regla.

Y:

> Estos principios son heurísticas. Son soluciones de sentido común para problemas comunes. … como
> cualquier heurística, son de naturaleza empírica. Se ha observado que funcionan en muchos casos;
> pero no hay ninguna prueba de que siempre funcionen, ni ninguna prueba de que siempre deban
> seguirse.

Esto deja dos preguntas útiles para tener presentes sobre cualquier "principio" con nombre:

- Si es una heurística, ¿por qué lo llamó principio?
- ¿Supo desde el principio que era una heurística, o lo reconoció como tal más tarde?

El punto no es descartar esa guía, sino leerla por lo que es.

---

## La postura: pensamiento crítico por sobre el dogma

Tratá toda la guía de diseño —incluido todo lo de este repo— como heurísticas:

- **No es marketing.** Un nombre o acrónimo pegadizo no convierte una guía en ley.
- **No es dogma.** Seguir una regla porque "es la regla" no es diseñar.
- **Pensamiento crítico.** Para cada situación, preguntá si la heurística ayuda *acá*, qué cuesta y
  si este es uno de sus casos de excepción.

Una heurística se gana su lugar mejorando el modelo en contexto, no por autoridad.

---

## Principios para el desarrollo

Aplicá esto directamente.

1. **Leé la guía de diseño como heurísticas.** Incluidas las heurísticas de este repo: son consejos
   que se ha observado que funcionan, no leyes.
2. **Analizá cada heurística en contexto.** Preguntá si aplica *acá* antes de aplicarla; la misma
   heurística puede ser correcta en un contexto e incorrecta en otro.
3. **Esperá excepciones.** Un caso que viola una heurística no es automáticamente un defecto; puede
   ser una excepción legítima. Decidí deliberadamente.
4. **No sigas una heurística de forma dogmática.** "Es la regla" no es justificación; la
   justificación es que mejora *este* modelo.
5. **Desconfiá de la autoridad y el marketing.** Un nombre, un acrónimo o un autor famoso no asciende
   una heurística a ley.
6. **Sopesá costos y beneficios.** Aplicá una heurística cuando su beneficio en contexto supera su
   costo, no por defecto.
7. **Pensá críticamente.** El objetivo es el buen criterio sobre el modelo, no cumplir una checklist.

---

## Glosario

| Término               | Definición                                                                       |
| --------------------- | -------------------------------------------------------------------------------- |
| **Principio**         | Una verdad o proposición fundamental usada como base para razonar o comportarse.  |
| **Regla / ley**       | Una afirmación que siempre se cumple y debe seguirse.                            |
| **Heurística**        | Una guía contextual y empírica que en general ayuda pero puede tener excepciones. |
| **Dogma**             | Seguir una guía como verdad incuestionable, sin importar el contexto.            |
| **Pensamiento crítico** | Juzgar, en contexto, si una heurística debe aplicarse y cómo.                  |

---

## Fuentes

- Robert C. Martin (Uncle Bob) — sobre SOLID como heurísticas, no reglas: por ejemplo *Clean
  Architecture* (Prentice Hall, 2017) y sus escritos sobre los principios SOLID.
- George Pólya, *How to Solve It* (Princeton University Press, 1945) — el tratamiento clásico de las
  heurísticas en la resolución de problemas.
- Billy Vaughn Koen, *Discussion of the Method: Conducting the Engineer's Approach to Problem
  Solving* (Oxford University Press, 2003) — la ingeniería como uso de heurísticas.
- Diccionario Oxford — definición de *principio*: una verdad o proposición fundamental que sirve de
  base para un sistema de creencias, comportamiento o cadena de razonamiento.
- Arthur J. Riel, *Object-Oriented Design Heuristics* (Addison-Wesley, 1996) — guía de diseño
  formulada explícitamente como heurísticas.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — curso sobre
  heurísticas de diseño de software con objetos.
