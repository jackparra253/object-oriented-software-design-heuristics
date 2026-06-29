# Resumen — Diseñar software con objetos

> **Propósito de este documento.** Un recorrido de 15 minutos por toda la guía: qué *es* el software,
> cómo juzgar un modelo, cómo se relacionan diseño y aprendizaje, qué es realmente un objeto, y las
> seis heurísticas (H1–H6) para construir modelos de objetos fieles. Leelo primero; cada afirmación de
> acá se desarrolla en su propio capítulo, enlazado en el texto. La sección final **Principios para el
> desarrollo** es la lista corta para tener abierta mientras diseñás y programás.

---

## Parte I — Qué estamos haciendo cuando construimos software

### El software es un modelo de la realidad

El software es **un modelo computable de un dominio de problema de la realidad** — no "un conjunto de
instrucciones". Esta sola definición reorienta todo: no estás escribiendo pasos para una máquina,
estás construyendo un *modelo* que representa cierta porción de un dominio real (o conceptual) y que
una computadora puede ejecutar. Elegís deliberadamente qué porción de la realidad modelar y con qué
nivel de detalle. El modelo *representa* el dominio; no es el dominio mismo — mantené el mapa distinto
del territorio. (Ver [01 — ¿Qué es el software?](01-que-es-software.md).)

De ahí se siguen dos consecuencias. Primero, tenés que **especificar el *qué* e implementar el
*cómo***: el software debe ser ejecutable, así que el modelo es siempre un artefacto formal y
ejecutable, no una descripción. Segundo, **el diseño es el paso deliberado de un dominio ambiguo y
contextual a un modelo formal y ejecutable** — esa traducción *es* el trabajo difícil y valioso.

### El código fuente es el diseño

¿Dónde vive ese modelo? **En el código fuente.** El código es la única fuente de verdad del modelo;
los diagramas y documentos solo lo *visualizan*. Esta es la idea clásica de que *programar es
diseñar*: el acto de escribir código es el acto de diseñar el sistema. (Ver
[02 — ¿Cuál es el modelo?](02-cual-es-el-modelo.md).)

Un corolario práctico cambia cómo pensás el costo: **el build es gratis; el diseño es el costo.** La
compilación (el paso de "manufactura") es esencialmente gratuita y automática; todo el esfuerzo, la
habilidad y la estimación van a producir el código — el diseño. Y como el diseño es el código,
**testear y debuggear son actividades de diseño** — validación y refinamiento del modelo — no una
fase aparte pegada al final.

### Qué hace bueno a un modelo — tres ejes

Si el software es un modelo, "buen software" significa "buen modelo". Juzgá un modelo por **tres
ejes** (ver [03 — ¿Qué es un buen modelo?](03-buen-modelo.md)):

1. **Implementación** — *cómo ejecuta*: performance, uso de recursos, solidez técnica.
2. **Descriptivo** — *cuán entendible es*: nombres, lenguaje del dominio, habitabilidad — ¿puede un
   humano leerlo y aprender el dominio desde él?
3. **Funcional** — *cuán fielmente representa el dominio*: ¿el modelo se corresponde con la realidad?

El eje funcional es el ancla: **buscá una correspondencia 1:1 entre dominio y modelo.** Cuando la
correspondencia es correcta, un caso nuevo del dominio debería *agregarse* al modelo, no parchearse, y
un cambio en el dominio debería mapear a un cambio en el modelo. Es el ideal abierto–cerrado dicho en
términos de modelado.

### El desarrollo es un proceso de aprendizaje

Casi nunca entendés un dominio por completo de entrada, así que **el desarrollo es un proceso de
aprendizaje** — trabajá iterativa e incrementalmente, fundá tu conocimiento en hechos concretos, y
hacé explícito el conocimiento tácito del dominio *en el modelo mismo*. (Ver
[04 — El desarrollo de software como proceso de aprendizaje](04-desarrollo-de-software.md).)

Esto replantea el cambio. **El cambio es esencial, no accidental**: el dominio cambia, tu comprensión
de él cambia, y tu modelado de él cambia — todo a lo largo del tiempo. Así que diseñá para que el
cambio sea barato y se preserve tu *capacidad de seguir aprendiendo*. El motor de ese aprendizaje es
un **ciclo de feedback corto**: tests rápidos y una consola viva te dejan aplicar el método científico
— caracterizar, hipotetizar, predecir, experimentar — muchas veces por hora. El modelo además es
**dinámico**: ejecuta y su estado cambia con el tiempo, así que diseñá teniendo en cuenta el paso del
tiempo.

### Qué es un objeto

La unidad del modelo es el objeto. **Un objeto es la representación esencial de un ente del dominio —
no "código + datos".** Un objeto se define por **los mensajes a los que responde** (su protocolo), no
por los datos que guarda adentro. La disciplina es capturar la *esencia* del ente y quitar lo
incidental. (Ver [05 — ¿Qué es un objeto?](05-que-es-un-objeto.md).)

Esta postura de "definido por mensajes, no por datos" es lo que hace coherentes a las heurísticas que
siguen: si un objeto *es* su protocolo, entonces ocultar sus datos, controlar su construcción y
rechazar estados inválidos son todas formas de mantener honesto ese protocolo.

### Por qué heurísticas, no reglas

La guía que sigue se entrega como **heurísticas, no principios ni reglas.** Una heurística se aplica
*en contexto*, espera excepciones y se sopesa por costo versus beneficio. Se espera que **pienses
críticamente** sobre cada una — nunca seguirla dogmáticamente ni por autoridad. (Ver
[06 — ¿Por qué heurísticas?](06-por-que-heuristica.md).) Tené presente este encuadre para todo lo de
abajo: H1–H6 son defaults fuertes con buenas razones, no leyes.

---

## Parte II — Las seis heurísticas

Las seis heurísticas se construyen una sobre otra. H1 fija el objetivo (representación fiel); H2 y H3
gobiernan cómo los objetos llegan a existir (completos, válidos); H4 elimina el peor agujero
representacional (null); H5 gobierna el cambio en el tiempo (inmutabilidad); H6 nombra la propiedad de
la que todas dependen en silencio (encapsulamiento).

### H1 — Un objeto por ente (representación fiel)

**Por cada ente de la realidad debe haber un objeto que lo represente fielmente.** Es el eje funcional
hecho concreto: buscá una correspondencia 1:1 entre los entes del dominio y los objetos del modelo.
Dos fallas la rompen, ambas dañinas: **un ente repartido en varios objetos/campos** (ej. la expiración
de una tarjeta modelada como `mes` y `año` separados), y **un objeto sobrecargado para significar
varios entes** (ej. un array pelado o un número codificado que reemplaza un concepto real — *Primitive
Obsession*). Nombrá el ente por lo que realmente es (el "número" de una tarjeta es un *identificador*,
no un número; la "fecha de expiración" es un *mes de año*, no una fecha), y preferí el tipo existente
correcto antes que inventar una clase innecesaria. (Ver [07 — H1](07-h1-objeto-por-ente.md).)

### H2 — Crear objetos completos

**Un objeto debe ser válido y fiel desde el momento en que existe.** Como el modelo es dinámico y el
tiempo transcurre, no hay un estado legítimo "a medio construir". Pedí lo que el objeto necesita **en
su constructor**, y evitá los setters post-construcción que terminan el trabajo después — esos generan
*acoplamiento temporal* (los mensajes deben enviarse en un orden oculto requerido) y estados inválidos
transitorios. Un síntoma revelador: **las variables sin inicializar suelen indicar que estás modelando
dos entes/estados como uno** — separalos en dos objetos completos (ej. una llamada *en curso* vs. una
llamada *terminada*). Para un ensamblado genuinamente complejo, usá un **Builder** para que el objeto
del dominio esté siempre completo. (Ver [08 — H2](08-h2-objetos-completos.md).)

### H3 — Solo crear objetos válidos

Completo no alcanza; el objeto también debe ser **válido** — el modelo debe hacer **imposible
construir** objetos inválidos, y debe **fallar rápido** cuando la creación es incorrecta. No deberías
poder construir un 31 de febrero, una fracción sobre cero, ni una tarjeta con dueño vacío. La jugada de
mayor valor es **dónde** vive la validación: **ponela en el modelo de dominio**, no en los bordes, así
una sola regla sirve a REST, a procesos batch y a la UI por igual (menos tests, sin modelos
inconsistentes). Señalá errores con **excepciones, no códigos de retorno**; validá en un **método de
creación de instancia** (idealmente un método de clase polimórfico) en vez del constructor crudo; y
elegí tu estrategia de error según el consumidor — **parar en el primer error** para llamadas
internas, **recolectar todos los errores** para UIs. (Ver [09 — H3](09-h3-objetos-validos.md).)

### H4 — No usar null

Si los objetos son completos (H2) y válidos (H3), ¿debería una referencia ser alguna vez `null`/`nil`?
**No.** `null` es la violación canónica de H1: un solo símbolo sobrecargado para significar una
variable no inicializada, "el cliente no tiene dirección" y "nada" — todo a la vez — así que no
representa fielmente a ninguno, y se filtra al mundo real como los bugs que todos vimos (`null95` en
una pantalla, "(null) could not be found"). En cambio, **modelá la ausencia como un objeto**.
Reemplazá `if x.nil?` con **polimorfismo** vía un **Null Object** (nombralo por el dominio —
`NotProvidedAddress`, no `NullAddress`). En lenguajes estáticamente tipados, hacé explícito el "quizás
ausente" con **Optional/Maybe**. Mantené la ausencia *adentro* del objeto — preferí un *Explicit Absent
Message* antes que un safe-navigation operator que filtra — y no escribas chequeos defensivos por null
sobre parámetros que un objeto válido nunca te pasaría. (Ver [10 — H4](10-h4-no-usar-null.md).)

### H5 — Favorecer objetos inmutables

Dados objetos completos, válidos y sin null, **¿cuándo y cómo debe cambiar un objeto?** La mutabilidad
es una **decisión de modelado, no técnica**: un objeto debe ser mutable si y solo si el ente que
representa es mutable. La mayoría de las cosas que pensás como "objetos" son en realidad inmutables —
números, fechas, facturas, contratos, strings — así que **por defecto, inmutable**, y muchas veces
modelá el cambio como una **secuencia de eventos que producen objetos inmutables nuevos** (una llamada
en curso se vuelve una *nueva* llamada terminada). La inmutabilidad te compra mucho: dejás de
preocuparte por el paso del tiempo, y por las consecuencias de entregar el objeto (sin copias
defensivas, sin bugs de aliasing, seguro como clave de hash, naturalmente thread-safe). Cuando un ente
sí cambia, modelá el cambio deliberadamente: evitá setters, hacé los cambios **atómicos y válidos**
(H3), que el **owner** controle la mutación, entregá copias o vistas inmutables en vez de internals
mutables, y protegé identidad, igualdad y hash. (Ver [11 — H5](11-h5-objetos-inmutables.md).)

### H6 — No romper el encapsulamiento

Toda heurística anterior se apoyó en silencio en esta. **El encapsulamiento es otorgar
responsabilidades a los objetos correctamente** — no meramente ocultar campos. El *information hiding*
(el mecanismo de control de acceso) es solo la parte que queda cuando le sacás las responsabilidades.
Pensalo por lo que se rompe cuando lo violás: **generás acoplamiento** (quien llama depende de la
estructura interna — peor en lenguajes estáticamente tipados), y **le quitás responsabilidad al objeto
correcto**, filtrando su lógica hacia quienes lo llaman como **código repetido**. La cura es **Tell,
Don't Ask**: agregá un mensaje por cada cosa que un colaborador deba hacer (`card.isExpiredOn(date)`,
`card.isOwnedBy(person)`) en vez de exponer datos para decidir afuera, y *no* agregues getters/setters
indiscriminadamente. Cuando tengas que devolver un internal, preferí objetos inmutables, copias o
wrappers — aunque ninguno elimina el acoplamiento. Los lenguajes ayudan o dificultan (la privacidad
por objeto como en Smalltalk/Ruby ayuda; la privacidad por clase y los modificadores débiles
dificultan), pero al final el encapsulamiento es **una disciplina que el usuario del objeto debe
respetar**. (Ver [12 — H6](12-h6-encapsulamiento.md).)

---

## Cómo encaja todo

Leída de arriba a abajo, la guía es un solo argumento. El software es un **modelo computable de la
realidad** (01), y ese modelo **es el código fuente** (02), juzgado por los ejes de implementación,
descriptivo y **funcional** (03), refinado mediante **aprendizaje iterativo** con un ciclo de feedback
corto (04). Su unidad es el **objeto**, definido por los **mensajes** que responde (05), y todo el
consejo de diseño son **heurísticas** para aplicar con criterio (06).

Las heurísticas después mantienen honesto el eje *funcional* a lo largo de la vida del sistema:
representá cada ente **fielmente y 1:1** (H1), traé los objetos a la existencia **completos** (H2) y
**válidos** (H3), rechazá la gran mentira representacional de **null** (H4), dejá que los objetos
cambien solo como cambian sus entes — **favoreciendo la inmutabilidad** (H5) — y protegé las
responsabilidades de cada objeto **no rompiendo el encapsulamiento** (H6).

---

## Principios para el desarrollo

La lista corta (cada uno es una heurística — aplicalo en contexto).

1. **Diseñá desde la definición.** El software es un modelo computable de un dominio de problema;
   construí el modelo, no solo guiones de comportamiento.
2. **Tratá el código fuente como el diseño.** Es la única fuente de verdad; programar es diseñar;
   testear y debuggear son diseño.
3. **Juzgá el modelo por tres ejes**, y anclá en el **funcional**: buscá una correspondencia 1:1
   dominio–modelo para que los casos nuevos se *agreguen*, no se parcheen.
4. **Trabajá como quien aprende.** Iterá, fundá decisiones en hechos, hacé explícito lo tácito, y
   mantené el ciclo de feedback corto; diseñá para que el cambio siga siendo barato.
5. **Definí los objetos por sus mensajes, no por sus datos.** Capturá la esencia; quitá lo incidental.
6. **H1 — un objeto por ente.** Ningún ente repartido en campos; ningún objeto/primitivo sobrecargado
   para significar varios entes; nombrá las cosas por lo que son.
7. **H2 — crear objetos completos.** Pedí lo necesario en el constructor; sin acoplamiento temporal;
   partí en dos los objetos con campos sin inicializar; usá un Builder para el ensamblado complejo.
8. **H3 — solo crear objetos válidos.** Hacé imposibles los objetos inválidos; fallá rápido; validá en
   el modelo de dominio vía métodos de creación de instancia; excepciones antes que códigos de retorno.
9. **H4 — no usar null.** Modelá la ausencia como objeto (Null Object / Optional); reemplazá los
   chequeos por null con polimorfismo; mantené la ausencia adentro del objeto.
10. **H5 — favorecer objetos inmutables.** Mutable si y solo si el ente lo es; por defecto, inmutable;
    modelá el cambio como objetos nuevos; controlá la mutación con cuidado cuando es real.
11. **H6 — no romper el encapsulamiento.** Otorgá responsabilidades correctamente; Tell, Don't Ask;
    evitá getters/setters indiscriminados; respetá el encapsulamiento aun cuando el lenguaje no lo
    imponga.
12. **Aplicá toda guía como heurística.** Sopesá costo vs. beneficio, esperá excepciones, pensá
    críticamente — nunca sigas por autoridad.

---

## Fuentes

- El tratamiento completo de cada tema, con sus propias fuentes, vive en los capítulos
  [01](01-que-es-software.md)–[12](12-h6-encapsulamiento.md) de esta guía.
- Jack Reeves, *What Is Software Design?* (1992) — el código fuente como el diseño.
- Frederick P. Brooks, *No Silver Bullet* (1986) — complejidad esencial vs. accidental.
- Arthur J. Riel, *Object-Oriented Design Heuristics* (1996) — las heurísticas como forma de enseñar
  diseño.
- Eric Evans, *Domain-Driven Design* (2003); Rebecca Wirfs-Brock, *Designing Object-Oriented Software*
  — modelos de dominio y diseño dirigido por responsabilidades.
- David L. Parnas, *On the Criteria To Be Used in Decomposing Systems into Modules* (1972) —
  information hiding.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — curso sobre
  heurísticas de diseño de software con objetos.
