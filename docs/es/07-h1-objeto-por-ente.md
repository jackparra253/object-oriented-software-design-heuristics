# H1 — Un objeto por ente (representación fiel)

> **Propósito de este documento.** Es una heurística de diseño (leela como heurística — ver
> [por-que-heuristica](06-por-que-heuristica.md)): aplicala en contexto, esperando excepciones.
> Gobierna la correspondencia entre los entes del dominio y los objetos que los representan.
> Aplicala cada vez que decidas cómo representar una parte del dominio en el código.

---

## La heurística

> **H1: Por cada ente de la realidad debe haber un objeto que lo represente "fielmente".**

Es el **eje funcional** hecho concreto: buscá una **correspondencia 1:1 (isomorfismo)** entre los
entes del dominio y los objetos del modelo. Cada ente del dominio mapea a exactamente un objeto, y
cada objeto representa exactamente a un ente.

Dos formas de romper H1, ambas dañinas:

1. **Un ente representado por más de un objeto.**
2. **Un objeto que representa más de un ente.**

---

## Falla 1 — un ente, muchos objetos

Cuando un único ente del dominio queda repartido en varios objetos/campos, el ente no tiene un único
lugar en el modelo.

*Ejemplo.* La "expiración" de una tarjeta de crédito es un ente (un mes de año). Modelarla como dos
campos separados —`añoDeExpiración` y `mesDeExpiración`— parte un ente en dos objetos.

Consecuencias:

- **Mayor complejidad accidental.**
- **Código repetido** (cada operación tiene que hacer malabares con las dos partes).
- **Propenso a error** (las dos partes pueden quedar desincronizadas).
- **Se pierde cohesión** (el comportamiento de un concepto queda disperso).

---

## Falla 2 — un objeto, muchos entes

Cuando un único objeto se reutiliza para representar varios entes distintos, la representación deja
de ser fiel.

*Ejemplos.*

- Codificar la expiración como un **array** `{2023, 8}`: la misma forma podría significar "agosto de
  2023", "el par (2023, 8)" o "8 días desde el inicio de 2023". El significado vive en la cabeza del
  desarrollador, no en el modelo.
- Usar un **número** o **string** pelado para representar un identificador, una medida (`1` como "1
  dólar", "1 litro", "1 metro") o un `aaaamm` codificado.
- El caso paradigmático: **`null`** representando "variable no inicializada", "el cliente no tiene
  dirección", "nada", todo a la vez. (Se trata en profundidad en H4 — No usar null.)

Consecuencias:

- **No representa fielmente** el ente; **se pierde información**.
- **No es declarativo / no es explícito** — el significado no está en el código: *¿en qué posición
  va el año y en cuál el mes? ¿Qué pasa si hay menos o más elementos?*
- **Primitive Obsession** — usar primitivos del lenguaje en vez de un objeto del dominio; es un
  *hack*.
- **Modelos que no nos enseñan** — quien lee no puede aprender el dominio desde el código.

---

## El ejemplo trabajado: una tarjeta de crédito

Una tarjeta de crédito conoce un nombre del dueño, un "número" y una "fecha de expiración". El
lenguaje natural es **ambiguo**:

- Decimos "número", pero el número de la tarjeta **no es un número, es un identificador** (nunca le
  hacés aritmética).
- Decimos "fecha de expiración", pero **no es una fecha, es un mes de año** (un mes de expiración de
  un año).

Elegir el ente fiel importa:

| Representación de la expiración     | Veredicto                                                          |
| ----------------------------------- | ----------------------------------------------------------------- |
| Un **mes de año** (ej. `YearMonth`) | Fiel — bello, correcto.                                           |
| Una **fecha** completa              | Propenso a error — tenés que "ajustarla", y no es una fecha.       |
| **Dos números** (mes + año)         | Rompe H1 (un ente, muchos objetos).                              |
| **Un array / número codificado**    | Rompe H1 (un objeto, muchos entes); un hack.                     |

---

## Cuidado: esto es sobre objetos, no sobre clases

H1 habla de **objetos**, no necesariamente de clases nuevas.

- El objeto que representa fielmente a un ente **puede ser instancia de una clase ya existente** — no
  hace falta inventar una clase para todo.
- La expiración de una tarjeta es un `YearMonth`, **no** una clase `ExpirationDate` a medida.
- El numerador y el denominador de una fracción son **números**, no instancias de `Numerador` y
  `Denominador`.

Entonces: representá cada ente fielmente con el objeto *correcto* —que muchas veces es un tipo
existente adecuado— sin sobre-modelar acuñando clases innecesarias.

Y evitá la trampa opuesta: **no** justifiques un mal modelo con "como es un modelo, lógico que no
represente todo". La representación fiel es el objetivo.

---

## Por qué importa

Complejidad = **esencial** + **accidental**. Romper H1 agrega complejidad *accidental* a cambio de
nada. Si H1 no se cumple, aparecen:

- soluciones particulares / ad-hoc;
- reinvención de la "rueda pinchada";
- software difícil de entender;
- código repetido, propenso a error y no declarativo.

---

## Principios para el desarrollo

Aplicá esto directamente (como heurísticas).

1. **Dale a cada ente del dominio exactamente un objeto que lo represente.** Mantené la
   correspondencia 1:1.
2. **No partas un ente en varios campos/objetos.** Si dos valores siempre viajan juntos y significan
   un concepto, modelalos como un objeto (ej. un mes de año, no año + mes).
3. **No sobrecargues un objeto/primitivo para que signifique varios entes.** Reemplazá los arrays
   "ingeniosos", los números codificados y los strings pelados por un objeto real del dominio (corregí
   Primitive Obsession).
4. **Nombrá el ente por lo que realmente es.** Superá el lenguaje natural ambiguo: el "número" de una
   tarjeta es un identificador; la "fecha de expiración" es un mes de año.
5. **Preferí el tipo existente correcto antes que una clase nueva.** Representá el objeto fielmente;
   creá una clase solo cuando no exista un tipo adecuado.
6. **Hacé el modelo declarativo.** El significado de un valor debe estar en el código, no en tu
   cabeza.
7. **Tratá el `null`-como-todo como un caso especial de romper H1.** (Ver H4.)

---

## Glosario

| Término                  | Definición                                                                  |
| ------------------------ | --------------------------------------------------------------------------- |
| **H1**                   | Por cada ente de la realidad debe haber un objeto que lo represente fielmente. |
| **Representación fiel**  | Una correspondencia 1:1 entre un ente del dominio y su objeto.              |
| **Primitive Obsession**  | Usar primitivos del lenguaje (número, string, array) en vez de un objeto del dominio. |
| **Complejidad accidental** | Complejidad introducida por la solución, no inherente al problema.        |
| **Código declarativo**   | Código cuyo significado es explícito en sí mismo, no implícito en la cabeza de quien lee. |

---

## Fuentes

- Arthur J. Riel, *Object-Oriented Design Heuristics* (Addison-Wesley, 1996).
- Martin Fowler y Kent Beck, *Refactoring* (Addison-Wesley) — el code smell *Primitive Obsession*;
  *Replace Primitive with Object*.
- Eric Evans, *Domain-Driven Design* (Addison-Wesley, 2003) — Value Objects que representan conceptos
  del dominio.
- Frederick P. Brooks, *No Silver Bullet* (1986) — complejidad esencial vs. accidental.
- `java.time.YearMonth` (JSR-310 / Java 8) — un modelo fiel de un mes de año, como en el ejemplo
  trabajado.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — curso sobre
  heurísticas de diseño de software con objetos.
