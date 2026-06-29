# ¿Qué es un buen modelo? — Los tres ejes

> **Propósito de este documento.** Es contexto base para diseñar y escribir software. Define qué
> significa "bueno" en software definiendo qué hace bueno a un modelo, y lo descompone en tres ejes
> independientes para evaluar y mejorar. Aplicá esto cada vez que juzgues, revises o mejores un
> diseño.

---

## Definición de trabajo

El buen software es un buen modelo. Un modelo es bueno a lo largo de **tres ejes independientes**,
y los tres importan:

> 1. **Eje Implementativo** — qué tan bien *ejecuta* en el ambiente técnico.
> 2. **Eje Descriptivo** — qué tan bien está *descrito* y se entiende el modelo.
> 3. **Eje Funcional** — qué tan buena es la *representación del dominio*.

Un modelo puede ser fuerte en un eje y débil en otro. Una evaluación completa mira los tres.

---

## Los tres ejes

### Eje Implementativo — cómo ejecuta

Un modelo es bueno en este eje cuando **ejecuta en el tiempo esperado usando los recursos definidos
como necesarios.** Abarca:

- **Performance** (velocidad)
- **Espacio** (memoria/almacenamiento)
- **Escalabilidad**
- Todo lo relacionado con los **requerimientos no funcionales** (atributos de calidad)

Es la **parte de "detalle"** del desarrollo. Responde *cómo* corre el modelo en el ambiente
técnico, no *qué* representa.

### Eje Descriptivo — qué tan bien está descrito

Un modelo es bueno en este eje cuando **"nos enseña"**: se lo puede *entender* y, por lo tanto,
*cambiar.* Claves:

- **Es importantísimo usar buenos nombres.**
- **Usar el mismo lenguaje que el del dominio de negocio** en el código.
- El código debe ser **agradable — "habitable".**

Es la **parte "artística"** del desarrollo. El código que no se puede entender no se puede cambiar
con seguridad, así que este eje gobierna directamente la mantenibilidad.

### Eje Funcional — qué tan bien representa el dominio

Un modelo es bueno en este eje cuando puede **representar correctamente toda observación de aquello
que modela.** En concreto:

- Si **aparece algo nuevo en el dominio**, debe **aparecer** algo nuevo en el modelo —se le *agrega*,
  no se modifica lo que ya existe—.
- Si **se modifica algo del dominio**, solo se debe cambiar **su** representación en el modelo —nada
  más—.
- El objetivo es una **relación 1:1 entre dominio y modelo (un isomorfismo).**

Es la **parte "observacional"** del desarrollo. (La regla "agregar para lo nuevo, cambiar solo la
representación afectada" es el principio abierto–cerrado en acción: abierto a la extensión, cerrado
a la modificación.)

---

## Un buen modelo corresponde 1:1 con su dominio

El eje funcional es el más profundo para el diseño con objetos. Buscá un **isomorfismo**: cada cosa
del dominio de problema tiene exactamente una representación en el modelo, y cada representación
corresponde a exactamente una cosa del dominio. Cuando eso se cumple:

- Los conceptos nuevos del dominio mapean a elementos nuevos del modelo (extensión), no a ediciones
  de los existentes.
- Un cambio en un concepto del dominio toca exactamente un lugar del modelo.

Perder esta correspondencia es una fuente primaria de fragilidad: un cambio del dominio fuerza
ediciones en muchos lugares no relacionados, y los casos nuevos exigen modificar código existente
en vez de agregarle.

---

## Principios para el desarrollo

Aplicá esto directamente.

1. **Evaluá un diseño en los tres ejes.** Implementación, descripción y representación funcional son
   independientes; un diseño rápido pero ilegible, o legible pero mala representación del dominio,
   no es un buen modelo.
2. **Tratá los requerimientos no funcionales como el eje implementativo.** Performance, espacio y
   escalabilidad son reales, pero son la capa de *detalle* — no dejes que manejen todo el diseño.
3. **Invertí fuerte en los nombres.** Los buenos nombres no son cosméticos; son cómo el modelo
   enseña y se mantiene cambiable.
4. **Hablá el lenguaje del dominio en el código.** Usá el mismo vocabulario que el negocio; evitá
   inventar un dialecto técnico paralelo.
5. **Mantené el código habitable.** Optimizá para quien debe entenderlo antes de cambiarlo.
6. **Preferí agregar antes que modificar.** Cuando aparece un caso nuevo en el dominio, extendé el
   modelo con un elemento nuevo en vez de editar código existente (abierto–cerrado).
7. **Localizá el cambio.** Estructurá el modelo para que un cambio del dominio mapee a un cambio del
   modelo.
8. **Apuntá a una correspondencia 1:1 dominio–modelo (isomorfismo).** Usala como test del eje
   funcional.

---

## Glosario

| Término                     | Definición                                                                          |
| --------------------------- | ----------------------------------------------------------------------------------- |
| **Eje Implementativo**      | Qué tan bien ejecuta el modelo en el ambiente técnico (la parte de "detalle").       |
| **Eje Descriptivo**         | Qué tan entendible y bien descrito está el modelo (la parte "artística").            |
| **Eje Funcional**           | Qué tan fielmente representa el modelo al dominio (la parte "observacional").        |
| **Atributos de calidad**    | Requerimientos no funcionales (performance, espacio, escalabilidad); el eje implementativo. |
| **Código habitable**        | Código lo bastante agradable como para ser entendido y habitado por quien debe cambiarlo. |
| **Isomorfismo (dominio–modelo)** | Una correspondencia 1:1 entre las cosas del dominio y los elementos del modelo. |

---

## Fuentes

- Hernán Wilkinson, Máximo Prieto, Luciano Romeo, *A Point-Based Model of the Gregorian Calendar*
  (Computer Languages, Systems & Structures, Elsevier, 2005) — un ejemplo trabajado de buen modelado
  de dominio y uso de metáforas.
- Eric Evans, *Domain-Driven Design* (Addison-Wesley, 2003) — *lenguaje ubicuo*: hablar el lenguaje
  del dominio en el código.
- Kent Beck, *Implementation Patterns* (Addison-Wesley, 2007) — nombres y comunicación de intención
  en el código.
- Richard P. Gabriel, *Patterns of Software* (Oxford University Press, 1996) — la *habitabilidad*
  del código.
- Bertrand Meyer, *Object-Oriented Software Construction*, 2.ª ed. (Prentice Hall, 1997) — el
  principio abierto–cerrado; mapeo directo entre dominio y modelo.
- Robert C. Martin, *Agile Software Development: Principles, Patterns, and Practices* (2002) — el
  principio abierto–cerrado en la práctica.
- Blog de 10Pines, *The Art of Naming* y *About Names When Designing with Objects* (2012) —
  <https://blog.10pines.com/2012/02/02/the-art-of-naming/>,
  <https://blog.10pines.com/2012/01/12/about-names-when-designing-with-objects/>.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — curso sobre
  heurísticas de diseño de software con objetos.
