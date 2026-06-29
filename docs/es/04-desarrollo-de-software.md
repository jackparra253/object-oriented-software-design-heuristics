# El desarrollo de software como proceso de aprendizaje

> **Propósito de este documento.** Es contexto base sobre cómo encarar la *actividad* de construir
> software. Define el desarrollo de software como un proceso de aprendizaje y deriva qué implica eso
> para planificar, trabajar y estructurar el feedback. Aplicá esto cada vez que organices el
> trabajo, estimes, iteres o te metas en un dominio nuevo.

---

## Definición de trabajo

Construir software no es principalmente manufactura, ni una cadena de ingeniería estrictamente
lineal. La analogía más precisa es un **proceso de aprendizaje**:

> **El desarrollo de software es el proceso de aprender un dominio de problema y formalizar ese
> conocimiento en un modelo computable.**

Como el resultado es un modelo computable expresado en código fuente, desarrollarlo significa
*adquirir y organizar conocimiento sobre un dominio* —y corregir continuamente ese conocimiento
contra la realidad—.

---

## El ciclo de aprendizaje

El desarrollo corre un bucle continuo entre el **dominio de problema** (`D`, expresado en lenguaje
natural, ambiguo y contextual) y el **modelo** (`M`, expresado en un lenguaje formal de
programación), mediado por el **modelo mental** del desarrollador:

1. **Observamos** el dominio.
2. Formamos/refinamos un **modelo mental** de él.
3. **Proyectamos** ese modelo mental en el modelo formal (el código).
4. **Reflexionamos** sobre el modelo resultante respecto de lo que se pretendía.
5. **Aprendemos** — devolvemos las correcciones a la observación del dominio.

Esto es **aprendizaje a través de la formalización del conocimiento**: mover un concepto desde el
lenguaje natural del dominio hacia el lenguaje formal y ejecutable del modelo, y usar las brechas
reveladas para aprender más.

---

## Qué implica realmente el desarrollo

- El dominio de problema suele estar especificado en **lenguaje ambiguo y contextual** (lenguaje
  natural).
- Por eso desarrollar implica **desambiguar y descontextualizar** el conocimiento del dominio.
- También implica hacer **explícito y externo** el conocimiento **implícito e internalizado** de los
  expertos de dominio —escribirlo como un modelo que se ejecuta—.
- **El cambio es esencial al software, no accidental**, porque con el tiempo:
  - cambia el dominio de problema,
  - cambia nuestro entendimiento del dominio, y
  - cambia la manera de modelar lo que entendemos.

Como el cambio es esencial, tratá la *capacidad de aprender* —poder seguir entendiendo y adaptando
el sistema— como un objetivo de diseño de primera clase. Gestionar la complejidad es lo que mantiene
viva esa capacidad.

---

## Propiedades del proceso

Visto como aprendizaje, el desarrollo de software es:

- **Iterativo** — el bucle corre muchas veces; el entendimiento se revisita, no se produce una sola
  vez.
- **Incremental** — el conocimiento se acumula por pasos; el modelo crece de a poco.
- **Anclado en hechos concretos** — el conocimiento se genera a partir de observaciones reales y
  código que funciona, no de especulación.
- **Organizado** — el conocimiento generado debe estructurarse deliberadamente, o se pierde.

Un enfoque de ingeniería para esto es la **aplicación práctica de un método científico y empírico**:
caracterizar (observar), formular una hipótesis (proponer un modelo), predecir y experimentar
(probar). Las raíces para volverse bueno en esto son **iteración, feedback, incrementalismo,
experimentación y empirismo.**

El **feedback inmediato** es fundamental: el feedback rápido te permite construir intuición, "jugar a
ser la computadora" en tu cabeza y encontrar errores antes. Cuanto más corto el bucle de feedback,
más rápido el aprendizaje.

---

## Principios para el desarrollo

Aplicá esto directamente.

1. **Tratá el desarrollo como aprendizaje, no como manufactura.** El objetivo de cada paso es
   *entender* mejor el dominio y capturar ese entendimiento en el modelo.
2. **Trabajá iterativa e incrementalmente.** Esperá revisitar decisiones; hacé crecer el modelo en
   pasos chicos y verificables, no en un gran diseño inicial.
3. **Anclá el conocimiento en hechos concretos.** Preferí observaciones y código que corre por sobre
   la especulación; dejá que la realidad corrija el modelo.
4. **Hacé explícito el conocimiento tácito del dominio.** Desambiguá y descontextualizá el dominio;
   escribí el conocimiento implícito de los expertos en el modelo, donde se puede verificar.
5. **Diseñá para el cambio como caso normal.** El dominio, tu entendimiento y tu forma de modelar van
   a cambiar; estructurá el sistema para que el cambio sea barato.
6. **Protegé la capacidad de aprender gestionando la complejidad.** Mantené el sistema entendible para
   que el equipo pueda seguir aprendiendo y adaptándose; el aprendizaje sostenible es el punto.
7. **Acortá el bucle de feedback.** Optimizá por feedback inmediato (tests rápidos, una consola/REPL
   viva, corridas rápidas) — es el motor de todo el proceso.
8. **Aplicá el método científico.** Caracterizar, formular hipótesis, predecir, experimentar — de
   forma pragmática, sin falsa precisión.
9. **Organizá el conocimiento que generás.** Capturá y estructurá lo aprendido en el modelo y sus
   nombres, o se perderá entre iteraciones.

---

## Glosario

| Término                        | Definición                                                                        |
| ------------------------------ | --------------------------------------------------------------------------------- |
| **Desarrollo de software**     | El proceso de aprender un dominio y formalizarlo en un modelo computable.          |
| **Ciclo de aprendizaje**       | Observar → modelo mental → proyectar → reflexionar → aprender, entre dominio y modelo. |
| **Modelo mental**              | El entendimiento interno del desarrollador que media entre dominio y código.       |
| **Formalización del conocimiento** | Mover un concepto del lenguaje natural ambiguo a una forma formal y ejecutable. |
| **Cambio esencial**            | Cambio inherente al software (cambian el dominio, el entendimiento y el modelado). |
| **Feedback inmediato**         | Respuesta rápida que acelera el aprendizaje y la detección de errores.             |
| **Capacidad de aprender**      | La habilidad sostenida de un equipo para entender y adaptar el sistema.            |

---

## Fuentes

- Frederick P. Brooks, *The Computer Scientist as Toolsmith II* (Communications of the ACM, marzo de
  1996) — el científico construye para aprender; el ingeniero aprende para construir.
- Margaret Hamilton — acuñó el término "ingeniería de software" para distinguirlo del hardware y
  otros tipos de ingeniería.
- *Software Engineering* — Reporte de la conferencia del Comité de Ciencia de la NATO (Garmisch,
  1968), eds. Peter Naur y Brian Randell; Mary Shaw, *Prospects for an Engineering Discipline of
  Software* (IEEE Software, 1990).
- Edsger W. Dijkstra, *EWD1305* — una mirada escéptica sobre la "ingeniería de software"; ver un
  programa como una fórmula. <http://www.cs.utexas.edu/users/EWD/transcriptions/EWD13xx/EWD1305.html>.
- Edward Yourdon — la ingeniería de software como un conjunto de métodos prácticos para la realidad
  propensa a errores de los proyectos, en lugar de una ciencia académica.
- Richard W. Hamming, *The Art of Doing Science and Engineering* — "En ciencia, si sabés lo que estás
  haciendo, no deberías estar haciéndolo; en ingeniería, si no sabés lo que estás haciendo, no
  deberías estar haciéndolo."
- David Farley, *Modern Software Engineering* (Addison-Wesley, 2021) — la ingeniería como aplicación
  práctica de un enfoque empírico y científico; iteración, feedback, incrementalismo, experimentación,
  empirismo.
- Bret Victor, *Inventing on Principle* (2012) — el poder del feedback inmediato.
  <http://vimeo.com/36579366>.
- Harold Abelson y Gerald Jay Sussman, *Structure and Interpretation of Computer Programs* (MIT) —
  sobre la naturaleza de la "ciencia" de la computación.
  <http://groups.csail.mit.edu/mac/classes/6.001/abelson-sussman-lectures/>.
- Peter Naur, *Programming as Theory Building* (1985) — el desarrollo como construcción de una teoría
  del dominio.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — curso sobre
  heurísticas de diseño de software con objetos.
