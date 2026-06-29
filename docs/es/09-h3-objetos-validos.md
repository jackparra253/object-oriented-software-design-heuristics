# H3 — Solo crear objetos válidos

> **Propósito de este documento.** Es una heurística de diseño (leela como heurística — ver
> [por-que-heuristica](06-por-que-heuristica.md)): aplicala en contexto, esperando excepciones.
> Se apoya en [H2](08-h2-objetos-completos.md): no alcanza con estar *completo* — el objeto también
> debe ser *válido*. Aplicala cada vez que diseñes creación, validación y manejo de errores.

---

## La heurística

> **H3: Solo se deben crear objetos válidos.**

Un objeto completo puede igual ser un disparate. El modelo debe hacer **imposible crear** objetos
inválidos. No deberías poder construir:

- un `31/Feb/2018`,
- una fracción `1/0`,
- una `TarjetaDeCrédito` con nombre del dueño vacío,
- un `Time` de `25:73:00`.

Entonces, extendiendo H2:

> Un objeto debe representar a su ente de manera **válida** desde el momento en que existe, debe
> **"enseñar" explícitamente** qué necesita, y debe **fallar si se lo crea incorrectamente — fail
> fast.**

*Ejemplo.* `LocalDate.of(2018, FEBRUARY, 31)` lanza excepción — correcto: el objeto inválido nunca
existe. El viejo `Calendar`/`SimpleDateFormat` "ajusta" silenciosamente el 31 de febrero a
`03/03/2018` — mal: produjo un objeto distinto y sorprendente en vez de fallar.

---

## Poner las validaciones en el modelo

El mayor beneficio de H3 es **dónde** vive la validación: en el propio objeto del modelo de negocio,
no en cada punto de entrada.

Si `Time.at(25, 10, 0)` valida dentro de `Time`, entonces falla igual venga la información de un
endpoint REST, de un proceso batch o de la UI. Consecuencias:

- **Una única validación**, sin importar de dónde viene la información.
- **Sin validaciones repetidas e inmantenibles** desparramadas por controllers y jobs.
- **Menos tests** para errores de entrada — la regla se prueba una sola vez, en el modelo.
- **No pueden existir modelos inconsistentes** en ninguna parte del sistema.

---

## Tips para crear objetos válidos

1. **Usar excepciones, no códigos de retorno, para indicar errores.** Una creación inválida debe
   lanzar, no devolver un flag que quien llama puede ignorar.
2. **Validar en un método de creación de instancia, no en el "constructor" crudo.** Cuando el
   constructor se ejecuta, la memoria ya se reservó; es mejor no reservar un objeto que vas a
   descartar enseguida. El constructor *acopla* reservar memoria con inicializarla — usá un método de
   creación que valide primero y recién entonces construya. (Ver el interludio sobre por qué ese
   método de creación debe ser un *método de clase*, no un *método estático*.)
3. **Tener claro qué objeto es responsable de validar qué.** Cada objeto valida sus propios
   invariantes; no dupliques una regla en colaboradores que ya confían en un objeto válido.
4. **Definir deliberadamente el modelo de validación:**
   - **SOFE (Stop On First Error)** — lanza ante el primer problema. Simple, pero pobre para UIs (el
     usuario corrige un error, reenvía, ve el siguiente).
   - **Recolectar todos los errores** — junta todos los problemas y los reporta juntos. Mejor para
     UIs (mostrar todos los errores de los campos a la vez).

---

## Interludio: método de clase vs. método estático

El método de creación de instancia (Tip 2) debería ser idealmente un **método de clase**, no un
**método estático**. Un *método estático*:

- no tiene `self`/`this`,
- no se puede redefinir,
- no puede reusar la implementación de la superclase vía `super`,
- no tiene polimorfismo,
- …no es realmente "objetos".

Un *método de clase* tiene todo eso — *es* objetos, así que la creación puede ser polimórfica y
reusable. Smalltalk y Ruby tienen verdaderos métodos de clase; Java, C#, C++ tienen métodos
estáticos; Python tiene ambos. El `static` de JavaScript es, por diseño, más cercano a un **método de
clase** de Smalltalk que a un estático de Java (adentro, `this` es la clase, y podés escribir
`return new this(...)`), aunque la palabra "static" sugiera lo contrario.

Conclusión: preferí métodos de creación polimórficos (métodos de clase) donde el lenguaje lo permita.

---

## Por qué importa — con objetos válidos

- El **modelo enseña lo que no se puede hacer** (los estados inválidos no son representables).
- **No existen modelos inconsistentes.**
- **Baja la tasa de error.**
- La **validación es única**, sin importar el origen de la información.
- **Fail fast** — los problemas afloran en la creación, no en pleno procesamiento posterior.

---

## Principios para el desarrollo

Aplicá esto directamente (como heurísticas).

1. **Hacé imposible crear objetos inválidos.** Rechazá la entrada mala en la creación; nunca permitas
   que exista un objeto disparatado.
2. **Fallá rápido ante una creación inválida.** Surgí el error en el punto de construcción, no
   después.
3. **Poné la validación en el modelo de dominio, no en los bordes.** Una regla en el modelo sirve a
   REST, batch y UI por igual.
4. **Señalá los errores de creación con excepciones, no con códigos de retorno.**
5. **Validá en un método de creación de instancia, no en el constructor crudo.** No reserves un
   objeto que vas a descartar enseguida; mantené separado "decidir validez" de "reservar".
6. **Asigná con claridad la responsabilidad de validar.** Cada objeto valida sus propios invariantes;
   evitá duplicar reglas.
7. **Elegí SOFE vs. recolectar-todo según el consumidor.** Recolectá todos los errores para UIs;
   stop-on-first está bien para llamadas internas.
8. **Preferí métodos de clase polimórficos para la creación** donde el lenguaje lo soporte.

---

## Glosario

| Término                          | Definición                                                                   |
| -------------------------------- | ---------------------------------------------------------------------------- |
| **H3**                           | Solo crear objetos válidos — los inválidos deben ser imposibles de construir. |
| **Fail fast**                    | Surgir un error en el punto más temprano (la creación), no después.          |
| **Método de creación de instancia** | Un método (idealmente de clase) que valida y luego construye el objeto.   |
| **Método de clase**              | Un método polimórfico sobre la clase con `self`/`this`; "es objetos".         |
| **Método estático**              | Un procedimiento no polimórfico atado a una clase; sin `self`, sin redefinir. |
| **SOFE**                         | "Stop On First Error"; vs. recolectar todos los errores para UIs.            |

---

## Fuentes

- Arthur J. Riel, *Object-Oriented Design Heuristics* (Addison-Wesley, 1996).
- Steve Freeman y Nat Pryce, *Growing Object-Oriented Software, Guided by Tests* (2009) — objetos
  válidos en la creación.
- Jim Shore, *Fail Fast* (IEEE Software, 2004); Martin Fowler, *FailFast* — fallar en la fuente del
  problema.
- Robert C. Martin, *Clean Code* (2008) — preferir excepciones a códigos de retorno para errores.
- Kent Beck, *Smalltalk Best Practice Patterns* (1997) — *Constructor Method* / métodos de creación
  de instancia.
- Stephen Colebourne y otros, JSR-310 `java.time` — factories validantes (`LocalDate.of`) vs. el
  `Calendar` legado y permisivo.
- Allen Wirfs-Brock y Brendan Eich, *JavaScript: The First 20 Years* (HOPL, 2020) — los métodos
  `static` de JS como métodos de clase (a la Smalltalk).
- Vaughn Vernon, *Implementing Domain-Driven Design* (2013); Yegor Bugayenko, *Elegant Objects*
  (2016) — el objeto/modelo de dominio siempre válido.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — curso sobre
  heurísticas de diseño de software con objetos.
