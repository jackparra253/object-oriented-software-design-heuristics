---
name: tdd
description: Ciclo red/green/refactor en pasos cortos, con el refactor como el momento de nombrar abstracciones. Úsala al empezar una funcionalidad nueva, al reproducir un bug antes de arreglarlo, al decidir qué testear y a qué granularidad, o al evaluar si una suite de tests es buena (Test Desiderata).
---

# TDD — Desarrollo guiado por tests

*Material adicional: es una práctica, no una de las seis heurísticas.*

**Qué es.** Escribir el test antes que el código, en ciclos cortos: **rojo** (un test que falla),
**verde** (el código mínimo que lo pasa), **refactor** (mejorar el diseño sin cambiar el
comportamiento).

## El paso que importa

**El refactor es donde nombrás las abstracciones.** Rojo y verde te dan comportamiento correcto; el
refactor es donde eso se convierte en un *modelo*. Saltarse el refactor es quedarse con código que
funciona y no representa nada.

## Por qué encaja con las heurísticas

TDD **encarna el proceso de aprendizaje**: es el ciclo de feedback corto que permite aplicar el método
científico —caracterizar, hipotetizar, predecir, experimentar— muchas veces por hora. Y como testear
y debuggear **son actividades de diseño**, la suite de tests no es una fase pegada al final: es parte
del modelo.

## Tips para una sesión potente

- Pasos chicos: si el rojo tarda en llegar, el paso era muy grande.
- Un test que falla **por la razón correcta** antes de escribir el código.
- Ante un bug: primero el test que lo reproduce, después el arreglo.
- Mantené la suite rápida — un ciclo lento deja de ser feedback.

## Qué hace bueno a un test (Test Desiderata)

El documento completo desarrolla la lista; en corto: un buen test es rápido, determinista, aislado,
legible, y **te dice qué se rompió**, no solo que algo se rompió.

## Ver también

- `development-as-learning` — el ciclo de feedback corto como motor del aprendizaje.
- `source-code-is-the-design` — testear y debuggear son diseño.
- `naming` — el refactor es el momento de nombrar.

## Texto completo

`docs/es/13-tdd.md` · `docs/en/13-tdd.md`
