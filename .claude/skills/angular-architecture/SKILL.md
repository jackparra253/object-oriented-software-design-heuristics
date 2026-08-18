---
name: angular-architecture
description: Arquitectura Angular v22 con TDD aplicando H1-H6 — feature-first, núcleo de dominio sin @angular/*, puertos y adaptadores, Vitest. Angular architecture, signals, zoneless, OnPush, signal forms, httpResource, standalone components, DTO mapping, TestBed, Nx tags, Sheriff, dónde poner la lógica de negocio en una app Angular.
---

# Arquitectura Angular v22 — heurísticas + TDD

**La premisa.** Angular es un **adaptador de entrega**, no el modelo. Sus idiomas empujan en contra de
las heurísticas: componentes que nacen vacíos (H2), DTOs anémicos (H1), `undefined` mientras carga
(H4), señales mutables (H5), templates que leen campos y deciden (H6). No pelees: **contené**.

**Angular no define una arquitectura de aplicación.** Su style guide solo manda dos cosas: organizar
por feature y *evitar subdirectorios por tipo de código*. Todo lo demás de abajo es H1–H6 aplicadas —
arquitectura de autor, no documentación oficial.

## La forma: feature afuera, capa adentro

```
src/app/orders/          ← una feature, no un rol técnico
  domain/                entes, value objects, puertos   ← cero @angular/*, no depende de nada
  application/           casos de uso sobre los puertos
  data-access/           adaptadores HTTP + mapeadores; implementan los puertos
  feat-*/  ui-*/         páginas ruteadas · componentes presentacionales
src/app/shared/          depende solo de shared
```

`feat-*`/`ui-*`/`data-access` es la taxonomía de Nx; `domain/` y `application/` no — Nx los mete dentro
de `data-access`, y por eso ahí el DTO termina siendo el tipo de dominio. Esa es la diferencia.

Hacelo cumplir con **Sheriff** (app sola) o **module boundaries de Nx** (monorepo), con doble tag
`scope:*` + `type:*`. La regla que sostiene todo: **`type:domain` no depende de nada.**

## Las cinco decisiones que importan

| | Decisión |
| --- | --- |
| H1 | **El DTO muere en el mapeador.** Un solo lugar conoce el JSON; nada arriba ve `OrderDto`. |
| H3 | El validador de signal forms **le pregunta al ente** (`EmailAddress.isValid(...)`). Zod/`validateStandardSchema` cuida el **borde**, no la regla. |
| H4 | Los seis estados de `httpResource` (`status()`: idle/loading/reloading/error/resolved/local) se convierten en objetos en la frontera. Angostá con `hasValue()`, que es type predicate. |
| H5 | La señal es la única celda mutable y guarda **objetos inmutables**: `set` de uno nuevo, nunca mutar. |
| H6 | El template hace **una pregunta con nombre** — `computed(() => order().canBeCancelledBy(user()))` — no cinco lecturas de campos. |

Los puertos se nombran por el **rol de dominio** (`Orders`), no por la implementación (`OrderService`).
Un adaptador que además atás a un puerto va con `@Service({ autoProvided: false })` — si no, queda
registrado dos veces.

## TDD con Vitest, alineado a las capas

| Capa | Cómo | Costo |
| --- | --- | --- |
| `domain/` | Vitest pelado, sin `TestBed`. **La mayoría de los tests.** | ~1 ms |
| `application/` | Fakes en memoria de los puertos (`InMemoryOrders`), **no mocks**. | ~ms |
| `data-access/` | El mapeador, directo: un test por forma de DTO real. | ~ms |
| `feat-*`/`ui-*` | `TestBed` + harnesses, sobre comportamiento observable. Pocos. | ~100 ms |

Con zoneless por defecto: `await fixture.whenStable()`. Necesitar `fakeAsync` suele indicar que esa
lógica va en una capa sin fixture. **El refactor es donde nace y se nombra el ente.**

## Las únicas excepciones legítimas

Componentes vacíos (H2), DTOs anémicos (H1), `undefined`/`null` que vienen de la API (H4 — en v22 la
navegación segura devuelve `undefined`, no `null`), señales mutables (H5) — cada una **solo en su
capa**. Lo demás que rompa una heurística no es excepción: es una decisión que todavía no tomaste.

## Olores

`interface Order` como tipo de dominio · directorios de primer nivel `components/`, `services/` ·
reglas de negocio en un `@if` · un Zod que decide qué es válido · `value() ?? []` · un servicio con
`signal<Order | null>(null)` y setters · `TestBed` en casi todos los tests · `domain/` importando
`@angular/core` · `ChangeDetectionStrategy.Eager` que dejó `ng update`.

## Ver también

- `tdd` — el ciclo; `naming` — nombrar en el refactor.
- `h1-object-per-entity`, `h3-valid-objects`, `h4-no-null`, `h5-immutable-objects`, `h6-encapsulation`.
- `why-heuristics` — en una app chica, colapsar `application/` es un trade-off legítimo.

## Texto completo

`docs/es/15-arquitectura-angular.md` · `docs/en/15-angular-architecture.md`
