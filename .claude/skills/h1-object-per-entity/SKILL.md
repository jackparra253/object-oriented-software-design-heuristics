---
name: h1-object-per-entity
description: Un objeto por cada ente del dominio, con correspondencia 1:1. Úsala al detectar Primitive Obsession, datos de un mismo concepto repartidos en varios campos (mes/año, calle/ciudad/código postal), strings o enteros que codifican un concepto real, arrays pelados que reemplazan una abstracción, o una clase que representa dos cosas a la vez.
---

# H1 — Un objeto por ente (representación fiel)

**La heurística.** Por cada ente de la realidad debe haber un objeto que lo represente fielmente.
Es el eje funcional hecho concreto: buscá una correspondencia 1:1 entre los entes del dominio y los
objetos del modelo.

## Las dos fallas

1. **Un ente repartido en varios objetos o campos.** La expiración de una tarjeta modelada como `mes`
   y `año` sueltos: el ente "mes de año" existe en el dominio, pero no tiene objeto que lo represente.
2. **Un objeto sobrecargado para significar varios entes.** Un array pelado, un string o un número
   codificado que reemplaza un concepto real — *Primitive Obsession*.

## Qué hacer

- **Nombrá el ente por lo que realmente es.** El "número" de una tarjeta es un *identificador*, no un
  número: no se suma ni se promedia. La "fecha de expiración" es un *mes de año*, no una fecha.
- **Preferí el tipo existente correcto** antes que inventar una clase innecesaria. H1 no pide una
  clase nueva por cada cosa; pide que el tipo elegido represente fielmente al ente.
- Si dos conceptos del dominio comparten una misma clase y se distinguen por un flag o por
  convención, probablemente sean dos objetos.

## Cuidado

Esto es **sobre objetos, no sobre clases**. Dos objetos de la misma clase pueden representar entes
distintos, y eso ya es una violación aunque el diagrama de clases se vea limpio.

## Ver también

- `h2-complete-objects` — un ente partido en campos suele venir con construcción incompleta.
- `h4-no-null` — `null` es la violación canónica de H1: un símbolo con muchos significados.
- `naming` — nombrar el ente por lo que es *es* parte de representarlo fielmente.

## Texto completo

`docs/es/07-h1-objeto-por-ente.md` · `docs/en/07-h1-object-per-entity.md`
