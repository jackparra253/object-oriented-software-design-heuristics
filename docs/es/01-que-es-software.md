# ¿Qué es el Software?

> **Propósito de este documento.** Es contexto base para diseñar y escribir software. Tomá las
> definiciones de abajo como la definición de trabajo de "software" y aplicá los principios cada
> vez que modeles un dominio, estructures código o decidas qué significa "bueno" en un sistema.

---

## Definición de trabajo

**Software** es *(conocimiento expresado como)* un **modelo computable** de un **dominio de
problema** de la **realidad**.

Una definición más débil y habitual —*software es un conjunto de instrucciones que, dado cierto
input, produce cierto output*— es verdadera pero inútil para diseñar. "Un conjunto de
instrucciones" no da ningún criterio sobre qué hace que el software sea *bueno* ni sobre cómo
debe *organizarse*. La definición basada en modelos sí lo da, y es la que hay que usar.

La consecuencia directa:

> **El buen software es un buen modelo.**
> Por lo tanto, el software debe **organizarse según la estructura del dominio de problema**, y no
> según la tecnología, el framework o las herramientas en uso.

Cuando estas dos visiones entran en conflicto —organizar el código como impone un framework versus
organizarlo como está realmente estructurado el dominio— **se prioriza el dominio**.

---

## Definiciones centrales

### Realidad

- La **realidad** es un conjunto de *cosas*.
- Una **cosa** es todo aquello acerca de lo cual se puede decir algo.

La realidad, tal como la percibimos y describimos, es **arbitraria** (la recortamos según nos
conviene), se expresa en **lenguaje natural** y por eso es **ambigua** y **dependiente del
contexto**: el significado de una afirmación depende de su contexto.

### Dominio de problema

- Un **dominio de problema** (o **dominio de conocimiento**) es un *recorte de la realidad* que
  representa el **negocio** que se está modelando.
- Hay que distinguir **dominios de negocio** de **dominios naturales**. El software no modela
  "toda la realidad"; modela la porción acotada relevante para el negocio.

### Modelo

- Un **modelo** es una *representación del conocimiento* construido acerca de un dominio.

Modelar no es copiar la realidad; es **construir una representación** de ella. Todo modelo se
define por tres preguntas, que deben tener respuestas deliberadas:

- ¿**Para qué** modelamos? (el propósito al que sirve el modelo)
- ¿En **qué lenguaje** modelamos?
- ¿Qué **tipo** de modelo construimos?

Un modelo **representa** una cosa; **no es** la cosa. Mantené separado el mapa del territorio.

### Computable

- **Computable** significa que puede ejecutarse en una máquina de Turing.

A diferencia del lenguaje natural (arbitrario, ambiguo, contextual), un modelo computable se
expresa en un **lenguaje formal y ejecutable** —el **código fuente**—. Es **formal** y
**a-contextual**: no depende del contexto para interpretarse.

> **Propiedad esencial:** un modelo computable no solo especifica el *qué*, sino que además
> **implementa el *cómo*.** Eso es lo que separa al software de otros modelos (un diagrama, una
> ecuación, un plano): el software *se ejecuta*. Si no se ejecuta, no es software: es una
> descripción de software.

---

## Principios para el desarrollo

Aplicá esto directamente al diseñar y escribir código.

1. **Tratá al software como un modelo, no como instrucciones.** La definición que adoptás
   determina cómo diseñás. "Instrucciones" no da criterio de diseño; "modelo" sí.
2. **El buen software es un buen modelo.** Antes de preguntarte si el código es elegante,
   preguntate si **representa fielmente** el dominio.
3. **Organizá el código alrededor del dominio, no del framework.** Ante la duda, reflejá la
   estructura del negocio, no las convenciones de la herramienta.
4. **Recortá la realidad a propósito.** Modelá solo el dominio de negocio relevante; no intentes
   representar toda la realidad.
5. **El modelo representa; no es la cosa.** Conservá la distinción entre una cosa del dominio y su
   representación en el código.
6. **Especificá el *qué* e implementá el *cómo*.** Un modelo de software debe ser ejecutable. Si no
   puede correr, es un diagrama o una idea, no software.
7. **Pasá de lo ambiguo a lo formal de forma deliberada.** Diseñar *es* el acto de traducir un
   dominio arbitrario, ambiguo y contextual a un modelo formal y a-contextual. Las decisiones de
   esa traducción son el diseño.

---

## Glosario

| Término              | Definición                                                              |
| -------------------- | ----------------------------------------------------------------------- |
| **Software**         | Un modelo computable de un dominio de problema de la realidad.          |
| **Realidad**         | Un conjunto de cosas.                                                    |
| **Cosa**             | Todo aquello acerca de lo cual se puede decir algo.                      |
| **Dominio de problema** | Un recorte de la realidad que representa el negocio que se modela.    |
| **Modelo**           | Una representación del conocimiento construido acerca de un dominio.    |
| **Computable**       | Ejecutable en una máquina de Turing; formal y a-contextual.            |
| **Buen software**    | Un buen modelo del dominio, organizado según la estructura del dominio. |

---

## Fuentes

- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — curso sobre
  heurísticas de diseño de software con objetos.
- Alan Turing, *On Computable Numbers, with an Application to the Entscheidungsproblem* (1936) —
  la máquina de Turing y la noción de computabilidad.
- Alonzo Church, *An Unsolvable Problem of Elementary Number Theory* (1936) — el cálculo lambda;
  junto con Turing, la tesis de Church–Turing.
- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*
  (Addison-Wesley, 2003) — modelar el dominio del negocio; lenguaje ubicuo; diseño guiado por el modelo.
- Bertrand Meyer, *Object-Oriented Software Construction*, 2.ª ed. (Prentice Hall, 1997) — el
  software como modelo sin costura de entidades del mundo real.
- Peter Naur, *Programming as Theory Building* (1985) — el software como la teoría que un equipo
  construye sobre un dominio.
- Frederick P. Brooks, *No Silver Bullet — Essence and Accidents of Software Engineering* (1986) —
  la dificultad esencial es construir el modelo conceptual.
- Arthur J. Riel, *Object-Oriented Design Heuristics* (Addison-Wesley, 1996) — heurísticas para
  organizar modelos de objetos.
