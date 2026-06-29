# TDD — Desarrollo Guiado por Tests (material adicional)

> **Propósito de este documento.** Es **material adicional**, no una heurística. Describe una
> *práctica* que apoya el modelo: TDD es cómo el ciclo de feedback corto y el "desarrollo como proceso
> de aprendizaje" de [04 — El desarrollo de software](04-desarrollo-de-software.md) se vuelven una
> forma concreta de trabajar. Usalo como contexto sobre *cómo* hacer crecer un modelo de objetos fiel,
> en el día a día.

---

## Qué es TDD

El Desarrollo Guiado por Tests es una práctica con poca teoría y mucha práctica — aproximadamente
**95% práctica**. La teoría es el ciclo:

1. **Rojo** — escribí el test más simple que se te ocurra para el próximo pedacito de comportamiento, y
   corrélo para que **falle**. (Un test que pasa antes de escribir el código no prueba nada.)
2. **Verde** — escribí el código *mínimo* que hace pasar el test. No el código elegante, el código
   honesto más chico.
3. **Refactor** — con el test en verde, mejorá el diseño: eliminá duplicación y **nombrá las
   abstracciones** que acabás de descubrir.

El ciclo es chico y se repite muchas veces por hora. *Es* el ciclo de feedback corto en la práctica:
caracterizar un comportamiento (el test), predecir (debería fallar / después pasar), experimentar
(correrlo), aprender.

TDD además funciona como diseño: como escribís el test primero, te obliga a usar el *protocolo* del
objeto (sus mensajes) antes de que exista su implementación — lo que mantiene el diseño honesto con
cómo se va a usar realmente el objeto (ver [05 — ¿Qué es un objeto?](05-que-es-un-objeto.md)).

---

## Tips para una sesión poderosa de TDD

1. **Nada de parálisis por análisis.** No pienses de más antes de actuar. Las decisiones de diseño se
   toman *después* de tener el test en verde, no antes; el ciclo te lleva a la respuesta.
2. **No saltearse el paso 3 (refactor).** Mejorá el código apenas funciona — revisá nombres,
   refactorizá los tests — para no acumular deuda técnica.
3. **Assertions primero.** En Arrange-Act-Assert, escribí de abajo hacia arriba: primero *qué querés
   lograr* (el assert), después construí solo el contexto que ese assert necesita. Tests más simples,
   menos setup.
4. **Romper la ansiedad.** Resistí el impulso de codear toda la solución de una. Mantené un ritmo
   constante a través del ciclo; apurarse mete bugs.
5. **Casos límite al final.** Hacé primero el happy path — los usuarios buscan la funcionalidad básica
   antes que las situaciones excepcionales.
6. **Cambiar de rumbo si te atascás.** Si estuviste trabado en un test 10–15 minutos, abandonalo e
   intentá otro enfoque (un test más chico, otro punto de partida).

---

## Qué hace bueno a un test (Test Desiderata)

No todos los tests valen lo mismo. Una checklist útil de propiedades deseables (el *Test Desiderata*
de Kent Beck, 12 propiedades) incluye, entre otras: los tests deberían ser **aislados** (no depender
entre sí), **componibles**, **rápidos**, **determinísticos** (mismo resultado en cada corrida),
**específicos** (un fallo apunta a la causa), **conductuales** (sensibles a cambios de comportamiento,
no a refactors), **legibles** y **fáciles de escribir** (baratos de escribir). Rara vez tenés las doce
a la vez; el punto es elegir conscientemente qué propiedades importan para cada test.

---

## Cómo se relaciona TDD con el modelo y las heurísticas

- **Alimenta el ciclo de aprendizaje** (04): cada ciclo es un experimento minúsculo que hace crecer tu
  comprensión del dominio y la hornea en el modelo.
- **El paso 3 protege el eje descriptivo** (03) y el **nombramiento**
  ([14 — Nombramiento](14-nombramiento.md)): el refactor es donde nombrás las abstracciones que
  descubriste.
- **Hace aflorar los objetos correctos** (H1): la duplicación que eliminás en el refactor suele
  revelar un objeto del dominio que falta.
- **Fija la validez** (H3): los tests de creación inválida son donde hacés imposibles a los objetos
  inválidos y verificás el comportamiento fail-fast.

---

## Principios para el desarrollo

Aplicalos como prácticas (sigue aplicando el criterio — no son reglas).

1. **Escribí el test primero, y miralo fallar.** Un test que falla prueba que el test funciona antes
   que el código.
2. **Escribí el código mínimo para pasar.** Diferí las decisiones de diseño al paso de refactor.
3. **Nunca te saltees el refactor.** Eliminá duplicación y nombrá abstracciones con el test en verde.
4. **Assert primero, arrange al final.** Que el resultado deseado guíe el setup.
5. **Happy path antes que casos límite.** Hacé andar el comportamiento central, después endurecelo.
6. **Ponele tiempo límite al atasco.** Tras ~10–15 minutos trabado, dá un paso más chico o cambiá de
   enfoque.
7. **Elegí las propiedades de los tests conscientemente.** Apuntá a tests rápidos, aislados,
   determinísticos y específicos.

---

## Glosario

| Término              | Definición                                                                          |
| -------------------- | ----------------------------------------------------------------------------------- |
| **TDD**              | Desarrollo Guiado por Tests: rojo → verde → refactor, repetido en ciclos cortos.    |
| **Rojo/Verde/Refactor** | Hacer fallar un test, hacerlo pasar mínimamente, y luego mejorar el diseño.       |
| **Arrange-Act-Assert** | Estructura del test; escribilo assert-first para enfocarte en el resultado.       |
| **Test Desiderata**  | Las 12 propiedades deseables de un test según Kent Beck (rápido, aislado, …).       |
| **Happy path**       | El flujo esperado, no excepcional; hacelo antes que los casos límite.               |

---

## Fuentes

- Blog de 10Pines, *6 Tips for a Powerful TDD Session* — https://blog.10pines.com/2018/01/29/6-tips-for-a-powerful-tdd-session/
- Blog de 10Pines, *Las 12 propiedades deseables de los tests según Kent Beck* — https://blog.10pines.com/2021/06/14/las-12-propiedades-deseables-de-los-tests-segun-kent-beck/
- Blog de 10Pines, *El primer test* — https://blog.10pines.com/2020/08/18/el-primer-test/ ; tag TDD — https://blog.10pines.com/tag/tdd/
- Kent Beck, *Test-Driven Development: By Example* (2002); *Test Desiderata* (2019).
- Steve Freeman y Nat Pryce, *Growing Object-Oriented Software, Guided by Tests* (2009).
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — curso sobre diseño de
  software con objetos.
