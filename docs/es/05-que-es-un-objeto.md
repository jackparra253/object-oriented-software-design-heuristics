# ¿Qué es un objeto?

> **Propósito de este documento.** Es contexto base para diseñar con objetos. Define qué *es* un
> objeto y qué lo define, y enumera las preguntas a responder al modelar uno. Aplicá esto cada vez
> que crees una clase, decidas qué debe hacer un objeto o juzgues si una abstracción está bien
> formada.

---

## Definición de trabajo

Un objeto **no** es "código + datos". Esa formulación es incorrecta: describe el mecanismo de
implementación, no qué es un objeto.

> **Un objeto es la representación esencial de un ente del dominio de problema.**

Y la forma en que representa a ese ente es específica:

> **Un objeto representa a su ente a través de los mensajes que sabe responder.**

Lo que define a un objeto es su **comportamiento —el conjunto de mensajes que responde—, no sus
datos internos.** Dos objetos con los mismos datos pero distinto protocolo son objetos distintos;
los datos son un detalle de implementación detrás de los mensajes.

---

## Esencia

La representación es **esencial**, y *esencia* significa:

> **Lo que hace que algo sea lo que es y no sea otra cosa.**

Modelar un objeto es capturar la **esencia** del ente del dominio —los mensajes que lo hacen ser
*ese* ente— y dejar afuera todo lo accidental. Es un estándar deliberadamente minimalista:

> "La perfección no se alcanza cuando no hay nada más que añadir, sino cuando no hay nada más que
> quitar." — Antoine de Saint-Exupéry

Un objeto debe responder exactamente a los mensajes que su esencia requiere: sin exponer datos de
forma accidental, sin operaciones que el ente realmente no tiene.

---

## Las preguntas que el diseño de objetos debe responder

Diseñar con objetos implica responder dos grupos de preguntas.

### ¿Qué debo modelar?

- **¿Qué entes de la realidad debo representar?** ¿Los físicos? ¿Los abstractos? ¿Ambos?

(Tanto los entes físicos como los abstractos son objetos legítimos. Si el dominio habla de algo,
puede ser un objeto —recordá la definición de *cosa*: todo aquello acerca de lo cual se puede decir
algo—.)

### ¿Cómo lo debo modelar?

- **¿Qué mensajes debe responder el objeto?** (su protocolo / comportamiento)
- **¿A quién debe conocer el objeto?** (sus colaboradores / relaciones)
- **¿Desde cuándo debe el objeto representar al ente?** (su ciclo de vida — cuándo nace y empieza a
  representar al ente)
- **¿Cómo debe el objeto "enseñar" qué representa?** (debe hacer legible su significado a través de
  su protocolo y sus nombres)

---

## Por qué "mensajes" y no "datos"

Definir un objeto por los mensajes que responde, en vez de por los datos que guarda, es lo que
mantiene el modelo alineado con el dominio y cambiable:

- El **protocolo** es el contrato con el resto del sistema; los **datos** detrás pueden cambiar
  libremente mientras los mensajes sigan respondiendo correctamente.
- Pensar en mensajes te obliga a preguntar *qué hace/significa el ente* en el dominio, no *cómo se
  almacena*.
- Preserva el encapsulamiento: los colaboradores dependen de lo que el objeto *responde*, nunca de
  lo que *guarda*.

---

## Principios para el desarrollo

Aplicá esto directamente.

1. **Modelá los objetos como representaciones esenciales de entes del dominio, no como registros de
   datos.** Arrancá desde "¿qué ente es esto?", no desde "¿qué campos tiene?".
2. **Definí los objetos por sus mensajes.** Un objeto *es* el protocolo que responde; diseñá eso
   primero y tratá los datos internos como detalle de implementación oculto.
3. **Capturá la esencia; quitá lo accidental.** Incluí solo los mensajes que el ente realmente
   necesita; buscá que "no quede nada más que quitar".
4. **Modelá entes físicos y abstractos.** Si el dominio puede hablar de algo, puede ser un objeto.
5. **Decidí los colaboradores de cada objeto deliberadamente.** Sé explícito sobre a quién debe
   conocer un objeto.
6. **Diseñá el ciclo de vida del objeto.** Decidí desde cuándo representa válidamente a su ente (debe
   representarlo desde su creación en adelante).
7. **Hacé que el objeto enseñe qué representa.** Usá el protocolo y los nombres para que el objeto
   comunique su significado sin explicación externa.

---

## Glosario

| Término          | Definición                                                                      |
| ---------------- | ------------------------------------------------------------------------------- |
| **Objeto**       | La representación esencial de un ente del dominio de problema.                   |
| **Ente**         | Una cosa del dominio que el objeto representa (física o abstracta).              |
| **Mensaje**      | Un pedido que un objeto sabe responder; la unidad de su comportamiento.         |
| **Protocolo**    | El conjunto completo de mensajes que un objeto responde; lo que define al objeto. |
| **Esencia**      | Lo que hace que algo sea lo que es y no sea otra cosa.                           |
| **Colaborador**  | Otro objeto que un objeto dado debe conocer para cumplir sus responsabilidades. |

---

## Fuentes

- Alan Kay — sobre la orientación a objetos como mensajería: la esencia de los objetos son los
  mensajes que envían y responden, no su estado interno. (Ej. *The Early History of Smalltalk*, 1993.)
- Rebecca Wirfs-Brock y Brian Wilkerson, *Object-Oriented Design: A Responsibility-Driven Approach*
  (OOPSLA, 1989); Wirfs-Brock y McKean, *Object Design* (2002) — objetos definidos por
  responsabilidades y comportamiento.
- Antoine de Saint-Exupéry, *Tierra de hombres* (1939) — "La perfección … cuando no hay nada más que
  quitar."
- Eric Evans, *Domain-Driven Design* (Addison-Wesley, 2003) — modelar entes del dominio.
- Arthur J. Riel, *Object-Oriented Design Heuristics* (Addison-Wesley, 1996) — heurísticas sobre qué
  debe saber y hacer un objeto.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — curso sobre
  heurísticas de diseño de software con objetos.
