# H2 — Los objetos se crean completos

> **Propósito de este documento.** Es una heurística de diseño (leela como heurística — ver
> [por-que-heuristica](06-por-que-heuristica.md)): aplicala en contexto, esperando excepciones.
> Gobierna *desde cuándo* se le permite existir a un objeto y qué debe saber en ese momento.
> Aplicala cada vez que diseñes la construcción (constructores, factories, builders).

---

## La heurística

> **H2: Los objetos se deben crear completos.**

Como el modelo computable es dinámico —**el tiempo transcurre**—, un objeto debe **representar a su
ente del dominio desde el momento mismo en que existe**, y debe **"enseñar" explícitamente qué
necesita** para representar ese ente. No hay un estado válido "a medio construir".

Dicho de otro modo: después de la construcción, el objeto ya es una representación fiel (ver
[H1](07-h1-objeto-por-ente.md)). Nunca está temporalmente inválido esperando llamadas a setters
posteriores que lo terminen.

---

## El problema que evita: acoplamiento temporal y agujeros de null

*Ejemplo.* Una `LlamadaTelefónica` con `origin`, `destination`, `start` y `end`. Si la creás con
todo **salvo** `end` (porque la llamada todavía no terminó) y dejás `end = null`, entonces pedirle
`duration()` explota — `NullPointerException` / `doesNotUnderstand:`. El objeto existió antes de ser
una llamada telefónica completa y fiel.

El "arreglo" habitual —llamar a `setEnd(...)` después— introduce **acoplamiento temporal**: los
mensajes deben enviarse en un orden requerido oculto, y cualquier código que tenga el objeto en el
medio ve un estado inválido.

Un diseño de objetos completos evita esto. O bien:

- el objeto se crea recién cuando se conoce todo lo que necesita; o
- el ciclo de vida se parte en **dos objetos** —ej. una llamada *en curso* (origin, destination,
  start) y una llamada *terminada* (que además tiene end y sabe responder `duration()`)—. Cada uno
  es completo y fiel en todo momento.

---

## Tips para crear objetos completos

1. **Un único constructor principal / método de creación de instancia.** Tené una sola forma
   principal de construir el objeto; todo otro constructor o factory delega en él. (Un solo lugar
   garantiza la completitud.)
2. **Variables de instancia sin inicializar son un olor → separar en dos objetos.** Si algunos
   campos no se pueden setear en la construcción, eso suele indicar que estás modelando dos
   entes/estados distintos; modelalos como dos objetos completos en vez de uno a medio llenar.
3. **Construcción compleja / mucho "paso del tiempo" → usar un Builder.** Cuando ensamblar el objeto
   requiere muchos pasos a lo largo del tiempo, juntá las partes en un **Builder** aparte y producí
   el objeto completo al final — mantené al objeto del dominio siempre completo.
4. **Que un framework te obligue a un constructor sin parámetros no es razón para exponerlo.**
   Algunas herramientas (ej. Hibernate) exigen un constructor sin argumentos; eso es una restricción
   de la herramienta, no una licencia de diseño para permitir objetos incompletos. No dejes que se
   filtre al contrato público de tu modelo.

---

## Por qué importa — los objetos completos "enseñan"

Un objeto completo comunica el modelo con claridad. El objeto:

- **Enseña cómo debe ser instanciado** — su constructor lista exactamente qué necesita.
- **Enseña con quiénes se relaciona** — sus colaboradores requeridos son explícitos.
- **Ayuda a la evolución del modelo** — hay un único camino de creación, honesto, para cambiar.
- **No genera acoplamiento temporal entre sus mensajes** — cualquier mensaje es válido apenas existe
  el objeto; quien lo usa nunca necesita conocer un orden mágico de llamadas.

---

## Principios para el desarrollo

Aplicá esto directamente (como heurísticas).

1. **Hacé que todo objeto sea válido desde su creación.** Después de la construcción ya debe
   representar fielmente a su ente — nunca un estado a medio construir, "para completar después".
2. **Pedí lo que el objeto necesita en su constructor.** Hacé explícitas las dependencias y
   colaboradores en la creación; el constructor debe *enseñar* qué necesita el ente.
3. **Evitá setters post-construcción que completan el objeto.** Generan acoplamiento temporal y
   estados inválidos transitorios.
4. **Canalizá la construcción por un único método principal de creación.** Los otros
   constructores/factories delegan en él para que la completitud se garantice en un solo lugar.
5. **Tratá los campos sin inicializar como una señal de modelado.** Suelen significar "esto en
   realidad son dos objetos/estados" — separalos.
6. **Usá un Builder cuando la construcción abarca tiempo o muchos pasos.** Mantené el ensamblado
   fuera del objeto del dominio, que está siempre completo.
7. **No dejes que las restricciones del framework dicten tu modelo.** Un constructor sin argumentos
   requerido es un parche de la herramienta, no una decisión de diseño — aislalo.

---

## Glosario

| Término                    | Definición                                                                       |
| -------------------------- | -------------------------------------------------------------------------------- |
| **H2**                     | Los objetos se crean completos — válidos y fieles desde el momento en que existen. |
| **Objeto completo**        | Un objeto que representa plenamente a su ente apenas termina su construcción.     |
| **Acoplamiento temporal**  | Un requisito oculto de que los mensajes se envíen en cierto orden para ser válidos. |
| **Constructor principal**  | El único método de creación al que delegan los demás constructores/factories.     |
| **Builder**                | Un objeto aparte que ensambla un objeto complejo y lo entrega completo.            |

---

## Fuentes

- Arthur J. Riel, *Object-Oriented Design Heuristics* (Addison-Wesley, 1996) — inicializar los
  objetos por completo; los constructores deben dejar el objeto en un estado válido.
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides (GoF), *Design Patterns* (1994) — el
  patrón **Builder**.
- Steve Freeman y Nat Pryce, *Growing Object-Oriented Software, Guided by Tests* (2009) — los objetos
  deben ser válidos (completamente formados) en la creación.
- Kent Beck, *Implementation Patterns* (2007) — *Complete Constructor*.
- Andrew Hunt y David Thomas, *The Pragmatic Programmer* (1999) — acoplamiento temporal.
- Yegor Bugayenko, *Elegant Objects* (2016) — objetos completos y siempre válidos; sin estado
  incompleto.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — curso sobre
  heurísticas de diseño de software con objetos.
