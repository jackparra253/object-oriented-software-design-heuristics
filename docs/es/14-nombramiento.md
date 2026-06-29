# Nombramiento — Variables y clases (material adicional)

> **Propósito de este documento.** Es **material adicional**, no una heurística. Es una *práctica* que
> sirve directamente al **eje descriptivo** de un buen modelo
> ([03 — ¿Qué es un buen modelo?](03-buen-modelo.md)) y refuerza
> [H1 — un objeto por ente](07-h1-objeto-por-ente.md): nombrar las cosas por lo que realmente son.
> Usalo como contexto para elegir nombres mientras diseñás y programás.

---

## Programar es el arte de nombrar

Un nombre **sintetiza el significado** de lo que se nombra: te deja entender *qué* es algo sin tener
que pensar en *cómo* funciona. Por eso nombrar es una de las cosas más importantes que hace un
programador — no decoración, sino diseño.

Tres ideas centrales:

- **Los nombres son para humanos, no para máquinas.** La computadora trata cada identificador como un
  símbolo opaco; correría igual con `a`, `b`, `c`. Todo el valor de un buen nombre es para las personas
  que leen y cambian el código.
- **Si no podés nombrar algo, es porque todavía no lo entendiste del todo.** La dificultad para nombrar
  es una señal de que el concepto no está claro — la presión de nombrar te empuja a entender el
  dominio.
- **Entender precede a nombrar.** Nombrás bien *después* de entender el ente, no antes.

---

## Recomendaciones concretas

### Evitar

- **Variables genéricas y sin significado:** `x`, `y`, `i`, `n`, `tmp`, `data`, `obj` — no llevan
  significado del dominio.
- **Nombres de clase vagos, "ruido":** `ObjectManager`, `ServiceHelper`, `ObjectDirector`, `…Util`,
  `…Processor`, `…Handler`. Suelen marcar un lugar donde todavía no se encontró el concepto real.

### Preferir

- **Nombrá el ente por lo que realmente es.** Es [H1](07-h1-objeto-por-ente.md) dicho para los
  nombres: el "número" de una tarjeta es un *identificador*; la "fecha de expiración" es un *mes de
  año*. El nombre correcto revela el objeto correcto.
- **Usá un placeholder deliberadamente sin significado cuando aún no entendés el concepto.** Nombrar
  algo `XYZ` o `QQQ` a propósito es mejor que comprometerte con un nombre incorrecto de apariencia
  plausible — el placeholder *molesta*, así que lo renombrás cuando lo entendés (muchas veces después
  de jugar con sus instancias).
- **Renombrá en el paso de refactor.** El tercer paso del ciclo de TDD
  ([13 — TDD](13-tdd.md)) es justamente donde convertís las abstracciones descubiertas en buenos
  nombres; no lo postergues.

### No dejes objetos sin nombre

Las estructuras anónimas — un hash/diccionario/tupla pelado que se pasa de un lado a otro para
representar un concepto — son objetos sin nombre. Obstaculizan la comunicación, dificultan razonar el
diseño, **generan código duplicado** y suben el costo de mantenimiento. Cuando una estructura
representa un concepto, **dale una clase/tipo** (otra vez [H1](07-h1-objeto-por-ente.md): reemplazá la
Primitive Obsession por un objeto real del dominio).

### Hacelo una práctica de equipo

El nombramiento es infraestructura compartida. Acordá **convenciones de naming en el equipo** para que
el vocabulario del código se mantenga consistente y enseñable — el modelo debería enseñar el dominio a
quien lo lee.

---

## Principios para el desarrollo

Aplicalos como prácticas (sigue aplicando el criterio — no son reglas).

1. **Tratá el nombramiento como diseño, no decoración.** Un nombre lleva el significado de lo que
   nombra.
2. **Nombrá para quien lee.** Optimizá para la comprensión, no para el compilador.
3. **Entendé antes de nombrar.** Que te cueste nombrar significa que el concepto aún no está claro.
4. **Evitá nombres genéricos y de "ruido".** Nada de `x`/`tmp`/`data`; nada de `…Manager`/`…Helper`/`…Util`.
5. **Nombrá el ente por lo que realmente es** (conecta con H1) — el nombre correcto hace aflorar el
   objeto correcto.
6. **Usá un placeholder sin significado, después renombrá.** No cementes un nombre incorrecto; dejá que
   el placeholder fuerce un nombre mejor en el refactor.
7. **Dale nombre a los objetos sin nombre.** Reemplazá estructuras anónimas por clases/tipos que
   representen el concepto.
8. **Estandarizá el naming en el equipo.** Mantené el vocabulario del código consistente y habitable.

---

## Glosario

| Término                 | Definición                                                                       |
| ----------------------- | -------------------------------------------------------------------------------- |
| **Nombre**              | Una síntesis del significado de lo que se nombra; sirve a la comprensión humana.  |
| **Nombre de ruido**     | Un nombre de clase vago (`Manager`, `Helper`, `Util`) que esconde un concepto real ausente. |
| **Placeholder sin significado** | Un nombre deliberadamente vacío (`XYZ`) usado hasta entender el concepto.  |
| **Objeto sin nombre**   | Una estructura anónima (hash/tupla pelado) que reemplaza un concepto que merece una clase. |
| **Eje descriptivo**     | El eje "cuán entendible es" de un buen modelo (ver 03), al que sirve el nombramiento. |

---

## Fuentes

- Blog de 10Pines, *The Art of Naming* — https://blog.10pines.com/2012/02/02/the-art-of-naming/
- Blog de 10Pines, *A case against nameless objects* — https://blog.10pines.com/2021/12/09/a-case-against-nameless-objects/
- Blog de 10Pines, tag object-design — https://blog.10pines.com/tag/object-design/
- Robert C. Martin, *Clean Code* (2008), cap. 2 "Meaningful Names"; Tim Ottinger, *Ottinger's Rules
  for Variable and Class Naming*.
- Eric Evans, *Domain-Driven Design* (2003) — el Lenguaje Ubicuo.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — curso sobre diseño de
  software con objetos.
