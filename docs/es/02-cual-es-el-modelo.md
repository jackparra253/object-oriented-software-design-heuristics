# ¿Cuál es el modelo? — El código fuente es el diseño

> **Propósito de este documento.** Es contexto base para diseñar y escribir software. Establece
> *dónde* vive realmente el modelo del que consiste el software y qué se desprende de eso para la
> forma de trabajar. Aplicá estas definiciones y principios cada vez que escribas código, dibujes
> un diagrama, estimes trabajo o decidas qué significa "diseñar".

---

## Definición de trabajo

El modelo del que consiste el software está **expresado en el código fuente** —y en ningún otro
lado—.

> **El código fuente es el diseño del software.**

Los diagramas, documentos y especificaciones *no* son el modelo. Pueden ayudar a visualizarlo o
comunicarlo, pero la única expresión completa, precisa y ejecutable del diseño es el código fuente
mismo. De ahí se sigue que:

> **Programar es diseñar, y diseñar es programar.** Son la misma actividad.

---

## Definiciones centrales

### Diseño

- El **diseño** es la definición que se usa para construir algo: una descripción, gráfico o
  especificación, relacionada con la cosa que se está diseñando y destinada a su construcción.

En la mayoría de las disciplinas de ingeniería el *diseño* es un documento (un plano) y la
*construcción* es una fase aparte, costosa y física, ejecutada a partir de ese documento. El
software no funciona así.

### Qué construimos y qué lo construye

- Lo que realmente entregamos es **software ejecutable**.
- Lo que produce software ejecutable a partir del diseño es el **compilador / cadena de build**.

Entonces, en términos de software:

| Concepto de ingeniería                      | Equivalente en software            |
| ------------------------------------------- | ---------------------------------- |
| El documento de diseño                      | El **código fuente**               |
| La cuadrilla de construcción                | El **compilador / sistema de build** |
| La construcción (construir desde el diseño) | La **compilación / build**         |
| El producto terminado                       | El **ejecutable corriendo**        |

La construcción —convertir el diseño en un artefacto ejecutable— está automatizada, es rápida y es
prácticamente gratis; la hace el compilador. Por lo tanto, **todo el costo y la dificultad del
software están en el diseño**, es decir, en escribir el código fuente.

### Testear y debuggear son actividades de diseño

- **Testear** y **debuggear** no están separados del diseño; son la **validación y el refinamiento
  de un diseño**. Son parte de producir un diseño correcto, no una fase posterior a que el diseño
  esté "terminado".

### Los diagramas visualizan el diseño — no son el diseño

- Los diagramas de clases, de secuencia y artefactos similares **ayudan a visualizar** el diseño.
- **No** son el diseño ni el modelo computable. La documentación tampoco. Solo el código fuente lo
  es.

### El modelo es dinámico — el tiempo transcurre en él

- Un modelo computable **se ejecuta**, y la ejecución implica **el paso del tiempo**: el estado
  modelado cambia de `t0` a `tn`.

Esta es la diferencia esencial respecto de los modelos estáticos de otras disciplinas. Un plano
modela *una casa*; el software modela *qué es una casa* —una definición viva que se ejecuta y
cambia con el tiempo—. **Hay que tener mucho cuidado al comparar los modelos de software con los de
otras profesiones:** los nuestros son dinámicos y ejecutables; los de ellas suelen ser estáticos.

---

## Principios para el desarrollo

Aplicá esto directamente.

1. **Tratá al código fuente como el diseño.** Es la única fuente de verdad del modelo. Mantenelo
   claro, porque la claridad del código es la claridad del diseño.
2. **Programar es diseñar.** No trates a escribir código como mera transcripción de un diseño
   "real" que viviría en diagramas o documentos. El diseño ocurre mientras se escribe el código.
3. **Los diagramas y la documentación visualizan; nunca reemplazan al código.** Usalos para pensar
   y comunicar, pero nunca los trates como el modelo ni dejes que se conviertan en una segunda
   fuente de verdad contradictoria.
4. **Tratá testear y debuggear como diseño.** Validan y refinan el diseño; presupuestalos como
   trabajo de diseño central, no como algo posterior.
5. **El build es gratis; el costo es el diseño.** Optimizá por la calidad del código fuente, no por
   la mecánica de la compilación. El esfuerzo y las estimaciones van sobre el diseño, es decir, el
   código.
6. **Estimá el descubrimiento, no la construcción.** Estimar es difícil porque lo que se estima es
   *diseñar* (descubrir el modelo), no *construir* (que el compilador hace gratis). Separá
   "descubrir" de "entregar".
7. **Tené en cuenta el tiempo en el modelo.** Como el modelo se ejecuta, diseñá para un estado que
   cambia con el tiempo; no razones sobre él como si fuera una foto estática.
8. **Iterá; no asumas una única pasada lineal.** Un proceso estrictamente secuencial, de
   construir-una-sola-vez a partir de una especificación congelada, es riesgoso e invita al
   fracaso. Esperá revisitar decisiones previas a medida que se valida el diseño.

---

## Glosario

| Término                  | Definición                                                                       |
| ------------------------ | -------------------------------------------------------------------------------- |
| **Diseño**               | La definición que se usa para construir algo, destinada a su construcción.        |
| **Código fuente**        | La expresión completa, precisa y ejecutable del diseño de software.              |
| **Construcción**         | Producir un artefacto ejecutable a partir del diseño; lo hace el compilador/build. |
| **Compilador / build**   | La "cuadrilla de construcción" que convierte el diseño en un ejecutable.         |
| **Testear / debuggear**  | Validación y refinamiento de un diseño.                                          |
| **Diagrama**             | Una visualización del diseño; no el diseño en sí.                                |
| **Modelo dinámico**      | Un modelo que se ejecuta, por lo que su estado cambia con el paso del tiempo.    |

---

## Fuentes

- Jack W. Reeves, *What Is Software Design?* (C++ Journal, 1992) — la tesis de que el código fuente
  es el diseño y de que la construcción es la compilación. Espejo: <https://wiki.c2.com/?WhatIsSoftwareDesign>.
- Glenn Vanderburg, *Real Software Engineering* (Lone Star Ruby Conference, 2010) —
  <https://youtu.be/RhdlBHHimeM>.
- Winston W. Royce, *Managing the Development of Large Software Systems* (1970) — el artículo que
  diagrama el proceso secuencial ("cascada") y advierte que, tal como se aplica habitualmente,
  "es riesgoso e invita al fracaso", proponiendo en cambio iteración e involucramiento temprano del
  cliente.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — curso sobre
  heurísticas de diseño de software con objetos.
- Frederick P. Brooks, *No Silver Bullet — Essence and Accidents of Software Engineering* (1986) —
  el diseño es la dificultad esencial e irreductible.
