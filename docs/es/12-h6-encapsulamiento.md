# H6 — No romper el encapsulamiento

> **Propósito de este documento.** Es una heurística de diseño (leela como heurística — ver
> [por-que-heuristica](06-por-que-heuristica.md)): aplicala en contexto, esperando excepciones.
> Nombra la propiedad en la que se apoyan las heurísticas anteriores — cada vez que dijeron "no
> romper el encapsulamiento" (en [H3](09-h3-objetos-validos.md), [H4](10-h4-no-usar-null.md),
> [H5](11-h5-objetos-inmutables.md)), se referían a esto. Aplicala cada vez que diseñes la cara
> pública de un objeto y cómo la alcanzan sus colaboradores.

---

## La heurística

> **H6: No romper el encapsulamiento.**

El encapsulamiento agrupa, en un solo objeto, tanto los datos como las operaciones que afectan a esos
datos, de modo que cada objeto gestiona su porción de la complejidad del problema. El conocimiento
dentro de un objeto está **oculto desde afuera**: el objeto tiene una **cara pública** (*lo que*
puede hacer y decir — cómo otros pueden interactuar con él) y un **lado privado** (*cómo* lo hace).
Las demás entidades solo saben cómo pedirle; no pueden ver ni tocar la representación interna.

Esto es **information hiding** (Parnas, 1972): "ninguna parte de un sistema complejo debería depender
de los detalles internos de ninguna otra parte" (Ingalls). Abstracción y encapsulamiento son
complementarios — la abstracción es sobre el *comportamiento observable*, el encapsulamiento es sobre
*ocultar la implementación* que lo produce, de modo que un objeto es libre de cambiar su lado privado
sin afectar al resto del sistema. Como dice David West, "no se debe violar la integridad personal del
objeto"; en la práctica el encapsulamiento es **más una disciplina que una barrera** — corresponde al
*usuario* de un objeto respetarlo.

---

## El encapsulamiento es sobre responsabilidades, no solo ocultar campos

El planteo más profundo: **encapsular es otorgar responsabilidades a los objetos correctamente.** El
information hiding (el mecanismo de control de acceso) es solo la parte del encapsulamiento que queda
cuando le sacás las responsabilidades. Por eso conviene pensarlo por lo que sale mal cuando se rompe.

### Qué pasa cuando se rompe

1. **Se genera acoplamiento.** Quien llama ahora depende de la estructura interna del objeto. (El
   acoplamiento es *mayor* en lenguajes estáticamente tipados, donde la dependencia es de tipos
   concretos.)
2. **Se le quita responsabilidad al objeto correcto.** La lógica que va adentro del objeto se filtra
   hacia quienes lo llaman, produciendo **código repetido** en todos lados donde se necesita esa
   lógica.

*Ejemplo.* Una `CreditCard` que expone su expiración cruda para que quien llama la compare él mismo
duplica la lógica de "¿está vencida?" por todo el sistema. Darle al objeto la responsabilidad —
`isExpiredOn(date)` — la mantiene en un solo lugar.

---

## Técnicas para no romper el encapsulamiento

- **Crear un mensaje por cada cosa que se necesite de un colaborador — "Tell, Don't Ask".** En vez de
  pedirle los datos a un colaborador y decidir afuera, decile al colaborador que lo haga. Ejemplo:
  `card.isOwnedBy(person)` en vez de sacar el dueño y compararlo.
- **No se puede prever toda necesidad — por eso hay que poder extender clases.** Es imposible predecir
  todo mensaje que un colaborador va a necesitar alguna vez; poder *extender* una clase (ej. agregar
  `isExpiredOn:` más tarde) importa justamente porque el autor original no podía anticiparlo.

### Cuando tenés que devolver un colaborador: cuidá el acoplamiento

Si un método devuelve un objeto interno:

- **Si el objeto devuelto es inmutable** ([H5](11-h5-objetos-inmutables.md)) → *solo* genera
  acoplamiento.
- **Si es mutable** → genera acoplamiento **y** el owner pierde el control de los cambios (quien llama
  puede mutar `number` a espaldas de la tarjeta).

Técnicas para minimizar el daño (ninguna elimina el acoplamiento):

1. Usar objetos inmutables.
2. Devolver copias.
3. "Wrapear" el objeto en otro que sea inmutable.

---

## Cómo cada lenguaje ayuda o dificulta

Un buen lenguaje de objetos debería **favorecer el encapsulamiento y no su ruptura.** Un lenguaje
*dificulta* el encapsulamiento cuando:

1. **Los colaboradores no son privados por defecto** — los modificadores de visibilidad
   (`public`/`package`/…) dejan cosas de acceso público. *Ejemplo: una `CreditCard` típica en Java con
   campos expuestos.*
2. **El encapsulamiento es por clase, no por objeto** — una clase puede meterse en los privados de
   *otra instancia* de la misma clase. Fue una decisión de diseño intencional en C++ (la clase, no el
   objeto, es la unidad de protección — heredada del sistema CAP de Cambridge) y persiste en
   TypeScript, Java, etc.

Un lenguaje *ayuda* cuando los colaboradores son siempre privados y el encapsulamiento es **por
objeto** (ej. Smalltalk, Ruby). Ranking aproximado del curso: **bien** — Smalltalk, Ruby; **regular**
— Java, Kotlin, C#, C++, TypeScript; **mal** — Python (safa con `__var`), PHP (a partir de 7.1),
JavaScript (safa con `#`).

### Encapsulamiento y subclasificación

- **La subclasificación siempre rompe el encapsulamiento de la *superclase*** — una subclase depende
  de los internals de su padre; un objeto es lo que define toda la jerarquía de su clase. (Por eso,
  en parte, Smalltalk ofrece el código fuente.)
- **Los colaboradores deberían estar protegidos en la subclasificación** — una subclase necesita
  acceso protegido y disciplinado, no barra libre.

---

## Principios para el desarrollo

Aplicá esto directamente (como heurísticas).

1. **Ocultá la representación interna; exponé comportamiento.** Quien llama interactúa solo por la
   cara pública; el lado privado es libre de cambiar.
2. **Encapsulá otorgando responsabilidades correctamente.** Poné la lógica donde viven los datos, no
   en quien llama — eso es lo que evita el código repetido.
3. **Tell, don't ask.** Agregá un mensaje por cada cosa que un colaborador deba hacer
   (`isExpiredOn(date)`, `isOwnedBy(person)`) en vez de exponer datos para decidir afuera.
4. **No agregues getters/setters indiscriminadamente.** Cada uno es un agujero en el encapsulamiento;
   exponé solo operaciones que revelen la intención.
5. **Cuando tengas que devolver internals, preferí objetos inmutables, copias o wrappers** — y
   recordá que ninguno elimina el acoplamiento.
6. **Respetá el encapsulamiento aunque el lenguaje te deje romperlo.** Es una disciplina; en lenguajes
   por clase o de privacidad débil, el usuario debe sostenerlo.
7. **Tratá la subclasificación como acoplamiento a la superclase.** Subclasificá deliberadamente y
   protegé los colaboradores heredados.

---

## Glosario

| Término                 | Definición                                                                        |
| ----------------------- | --------------------------------------------------------------------------------- |
| **H6**                  | No romper el encapsulamiento; otorgar responsabilidades correctamente y ocultar internals. |
| **Encapsulamiento**     | Agrupar datos y las operaciones sobre ellos en un objeto; otorgar responsabilidades. |
| **Information hiding**  | Ocultar detalles internos para que ninguna parte dependa de los internals de otra (Parnas). |
| **Tell, Don't Ask**     | Decirle a un colaborador que actúe, en vez de pedirle datos para decidir afuera.   |
| **Cara pública / lado privado** | *Lo que* un objeto hace y dice vs. *cómo* lo hace.                         |

---

## Fuentes

- David L. Parnas, *On the Criteria To Be Used in Decomposing Systems into Modules* (CACM, 1972) —
  *information hiding*.
- Rebecca Wirfs-Brock y otros, *Designing Object-Oriented Software* — la cara pública / lado privado
  del objeto.
- Erich Gamma y otros (GoF), *Design Patterns* (1994) — las solicitudes como única forma de cambiar
  el estado interno encapsulado de un objeto.
- Grady Booch, *Object-Oriented Analysis and Design* — abstracción vs. encapsulamiento; interfaz vs.
  implementación; citando a Ingalls y Liskov.
- David West, *Object Thinking* — la integridad personal de los objetos; el encapsulamiento como
  disciplina.
- David A. Taylor, *Object-Oriented Technology: A Manager's Guide* — la metáfora de la célula; los dos
  tipos de protección de la comunicación por mensajes.
- Chamond Liu, *Smalltalk, Objects, and Design* — el exterior/interior de un objeto.
- Bjarne Stroustrup, *The Design and Evolution of C++* — la clase como unidad de protección (influencia
  del CAP).
- Alan Kay — la metáfora del objeto como célula.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — curso sobre
  heurísticas de diseño de software con objetos.
