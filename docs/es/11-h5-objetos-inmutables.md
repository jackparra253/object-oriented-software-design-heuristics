# H5 — Favorecer objetos inmutables

> **Propósito de este documento.** Es una heurística de diseño (leela como heurística — ver
> [por-que-heuristica](06-por-que-heuristica.md)): aplicala en contexto, esperando excepciones.
> Responde la pregunta que abren las heurísticas anteriores — dados objetos completos
> ([H2](08-h2-objetos-completos.md)), válidos ([H3](09-h3-objetos-validos.md)) y sin null
> ([H4](10-h4-no-usar-null.md)), **¿cuándo y cómo debe cambiar un objeto?** Aplicala cada vez que
> decidas si un objeto es mutable, y cómo ocurre la mutación.

---

## La heurística

> **H5: Favorecer el uso de objetos inmutables.**

La mutabilidad **no** es ante todo una decisión técnica — es una decisión **conceptual, de modelado**
(recordá [H1](07-h1-objeto-por-ente.md): representación fiel):

> Un objeto debe ser **mutable si el ente que representa es mutable**, e **inmutable si el ente que
> representa es inmutable.**

Heráclito ("ningún hombre se sumerge dos veces en el mismo río") y Parménides ("lo que es, no puede
no ser") marcan los dos polos. La mayoría de los entes del dominio que pensamos como "cosas" son en
realidad inmutables: números (enteros, fracciones), una fecha, una hora, un día de mes, una tarjeta
de crédito, una factura, un contrato, un string. La heurística dice: **partí de la inmutabilidad**, y
hacé algo mutable solo cuando el ente realmente cambia.

---

## La realidad como secuencia de eventos que generan objetos inmutables

Hay un replanteo más profundo: mucho de lo que parece "mutable" se modela mejor como una **secuencia
de eventos que producen objetos inmutables**, cada uno fiel en su instante de tiempo.

*Ejemplo — una `LlamadaTelefónica`.* Una llamada *en curso* conoce `origin`, `destination`, `start`.
Pedirle `duration()` **no debería compilar / no debería entenderse** — la llamada no terminó, así que
la duración todavía no es una pregunta fiel (esto es también [H2](08-h2-objetos-completos.md) y
[H4](10-h4-no-usar-null.md): nada de `end = null`, nada de `setEnd(...)`). Cuando la llamada termina,
ese evento produce una llamada *terminada* — un objeto **nuevo e inmutable** con `end` que sí responde
`duration()`. El paso del tiempo se vuelve objetos nuevos, no objetos mutados.

---

## Ventajas de los objetos inmutables

- **Te despreocupás del paso del tiempo.** El objeto nunca puede volverse inválido o sorprendente más
  tarde; es lo que era al crearse.
- **Te despreocupás de las consecuencias de "entregar" el objeto.** Podés compartir la referencia
  libremente — nadie puede mutarlo a tus espaldas, así que no hay copias defensivas, no hay bugs de
  aliasing, es seguro como clave y naturalmente thread-safe.

Distinciones que conviene tener claras:

- **Objeto inmutable ≠ variable inmutable** (`const`/`final`). Una referencia `final` puede apuntar a
  un objeto mutable; un objeto inmutable sigue siendo inmutable sin importar cuántas variables lo
  referencien.
- **Un objeto inmutable cuyos colaboradores son mutables no es realmente inmutable** — la
  inmutabilidad debe llegar hasta el fondo.
- **No hace falta soporte del lenguaje/VM** para tener objetos inmutables; ayuda a hacerlos cumplir,
  pero la inmutabilidad es una propiedad de diseño que podés sostener por disciplina.

---

## Cuando el ente sí cambia: manejar la mutación con seguridad

Algunas cosas sí cambian — o debemos modelarlas como que cambian. Los objetos mutables son legítimos;
el punto es **modelar el cambio con cuidado, consciente de sus consecuencias.** Cuatro asuntos:

### 1. Que los cambios sean válidos (H3) y atómicos

- **No usar setters.** Un `setX` pelado invita a estados inválidos a medio cambiar. Exponé operaciones
  del dominio que revelen la intención.
- **Hacer los cambios atómicos.** Un cambio que toca varios campos debe dejar al objeto válido como un
  todo — nunca observable a mitad de cambio.
- **Permitir el cambio libre solo donde no se necesita validación.**

### 2. Controlar el cambio

- **El owner del objeto es el encargado de cambiarlo.** La mutación pasa por quien posee el ciclo de
  vida del objeto, no por colaboradores arbitrarios.
- **No entregar objetos mutables — o entregar copias.** Si exponés estado mutable interno, quien llama
  puede corromper tus invariantes; dale una vista inmutable o una copia.

### 3. Cuidar el impacto en otros objetos

- **No quedarse con objetos "no propios".** Guardar una referencia al objeto mutable de otro te acopla
  a cambios que no controlás.
- **No cambiar la identidad.** La mutación no debe alterar lo que hace que el objeto sea *ese* ente.
- **Atención al impacto en igualdad y hash.** Si un objeto mutable es clave en una estructura de hash
  y su hash cambia, corrompés la estructura — otra razón por la que la inmutabilidad es más segura.

### 4. Errores en el ingreso de información por parte del usuario

- **Separar la identidad de la información "accidental".** Lo que el usuario puede tipear mal y
  corregir no es la identidad del objeto.
- **Mantener historial de cambios y siempre modificar el mismo objeto.** Las correcciones se vuelven
  eventos registrados, no una sobreescritura silenciosa — preservando la traza de auditoría y la
  identidad del objeto a lo largo del tiempo.

---

## Principios para el desarrollo

Aplicá esto directamente (como heurísticas).

1. **Decidí la mutabilidad por el ente, no por conveniencia.** Mutable si y solo si el ente
   representado es mutable.
2. **Por defecto, inmutable.** Hacé un objeto mutable solo cuando el ente del dominio realmente
   cambia.
3. **Modelá el cambio como objetos inmutables nuevos cuando puedas.** Preferí un evento que produce un
   objeto nuevo (llamada terminada) antes que mutar uno en el lugar.
4. **Para los objetos genuinamente mutables, evitá los setters; usá operaciones atómicas que preserven
   la validez.**
5. **Controlá quién muta.** El owner cambia el objeto; no entregues internals mutables — entregá
   copias o vistas inmutables.
6. **Protegé identidad, igualdad y hash.** No mutes lo que define al objeto ni aquello de lo que
   depende su hash.
7. **Registrá las correcciones como historial sobre el mismo objeto.** Separá la identidad de la
   información accidental editable por el usuario.

---

## Glosario

| Término                  | Definición                                                                       |
| ------------------------ | -------------------------------------------------------------------------------- |
| **H5**                   | Favorecer objetos inmutables; ser mutable solo si el ente representado lo es.     |
| **Objeto inmutable**     | Un objeto cuyo estado nunca cambia después de su creación.                        |
| **Variable inmutable**   | Una ligadura `const`/`final` — distinta de un objeto inmutable.                   |
| **Cambio atómico**       | Una mutación que deja al objeto válido como un todo, nunca observable a mitad.    |
| **Identidad**            | Lo que hace que un objeto sea *ese* ente, independiente de datos accidentales editables. |

---

## Fuentes

- Heráclito y Parménides — el planteo clásico de cambio vs. permanencia.
- Joshua Bloch, *Effective Java* — "Minimizar la mutabilidad" / favorecer clases inmutables; los
  inmutables son simples, thread-safe y compartibles libremente.
- Eric Evans, *Domain-Driven Design* (2003) — Value Objects modelados como inmutables.
- Martin Fowler — *Event Sourcing* / eventos que producen nuevo estado; *Value Object*.
- Michael Feathers y la tradición de la programación funcional — el razonamiento se simplifica con la
  inmutabilidad.
- Andrew Hunt y David Thomas, *The Pragmatic Programmer* — cuidado con el aliasing; no entregues
  internals mutables.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — curso sobre
  heurísticas de diseño de software con objetos.
