# H4 — No usar null/nil

> **Propósito de este documento.** Es una heurística de diseño (leela como heurística — ver
> [por-que-heuristica](06-por-que-heuristica.md)): aplicala en contexto, esperando excepciones. Se
> desprende de [H1](07-h1-objeto-por-ente.md) (representación fiel) y [H3](09-h3-objetos-validos.md)
> (solo objetos válidos). Aplicala cada vez que te tiente dejar una referencia en `null`/`nil`, o
> chequear por ella.

---

## La heurística

> **H4: No usar `null`/`nil`.**

Si los objetos se crean completos ([H2](08-h2-objetos-completos.md)) y válidos
([H3](09-h3-objetos-validos.md)), ¿puede haber un objeto que referencie a `null`/`nil`? **No — o no
debería.**

El `null` se filtra al mundo real como bugs que todos vimos: una pantalla de turnos mostrando
`null95`, un diálogo de Apple Pay "`(null)` could not be found", una opción de presupuesto que dice
`100 null`, un cartel "Undo null?". Es `null` escapando del modelo a la cara del usuario.

---

## Por qué `null` es un problema: rompe H1

`null` es la violación canónica de [H1](07-h1-objeto-por-ente.md) (un objeto por ente). Un único
símbolo se sobrecarga para significar muchas cosas del dominio sin relación, todas a la vez:

- una **variable no inicializada**,
- "**el cliente no tiene dirección**",
- "**nada**".

El mismo `null` representa a todas, así que no representa fielmente a ninguna. El significado vive en
la cabeza del desarrollador, no en el modelo — y el programa "no hace nada" (o explota) cuando las
distinciones importan.

---

## ¿Por qué existe `null`?

Lo introdujo Tony Hoare. En *Record Handling*, modelando **relaciones funcionales parciales** (ej.
una persona puede no tener padre), proveyó "un valor especial `null` … para variables y campos de
referencia" para indicar que la relación "no está definida (o todavía no)". Simula 67 tuvo la misma
idea como `none`, "una referencia a 'ningún objeto'".

Hoare después lo llamó su **"error de mil millones de dólares"** (QCon, 2009): lo agregó en 1965
"simplemente porque era muy fácil de implementar". *Que todos los lenguajes lo tengan no lo hace
correcto* — es un default histórico, no un buen modelo.

---

## El ejemplo trabajado: un cliente que puede no tener dirección

El código plagado de `if customer.address.nil?` es el síntoma. La cura es **modelar la ausencia de
dirección** para que los `if` desaparezcan. Dos implementaciones:

### 1. Null Object (una jerarquía de clases)

Introducí un `Address` abstracto con dos tipos concretos que responden el mismo protocolo
(`is_at(city)`):

- `ProvidedAddress` — una dirección real; `is_at(city)` compara su ciudad.
- `NotProvidedAddress` — la *ausencia* de dirección, modelada como objeto; `is_at(city)` responde
  `false`.

Ahora `customers_at(city)` colapsa de un `if/else` a un único mensaje polimórfico:

```ruby
def customers_at(city)
  @customers.select do |customer|
    customer.address.is_at city
  end
end
```

El nombre importa (esto sigue siendo [H1](07-h1-objeto-por-ente.md)): la ausencia **no** se llama
`NullAddress` (es un concepto del dominio, "no provista", no un null), y el padre abstracto **no** se
llama `AbstractAddress` (llamalo `Address`, por lo que es). El Null Object puede implementarse como
jerarquía de clases o como una única instancia bien conocida.

> *Null Object Pattern* (Bobby Woolf): "proveer un sustituto de otro objeto que comparte la misma
> interfaz pero no hace nada", encapsulando cómo "no hacer nada" y ocultándolo a sus colaboradores.

### 2. Optional / Maybe (modelar que una variable puede referenciar null)

En vez de modelar una *nada* especial, podés modelar el **hecho de que una referencia puede estar
ausente** envolviéndola en un `Optional`/`Maybe`:

```java
private String name;
private Optional<Address> address;

public static Customer named(String name, Address address) {
    if (name.isEmpty()) throw new RuntimeException(INVALID_NAME);   // H3
    return new Customer(name, Optional.ofNullable(address));
}

public Optional<Address> getAddress() { return address; }
```

```ruby
def customers_at(city)
  @customers.select do |customer|
    customer.address.map { |address| address.city == city }.get_or_else(false)
  end
end
```

`Optional`:

- es un **Proxy** — como todo proxy, puede ser o no polimórfico con el objeto proxeado;
- representa que **una variable puede referenciar a null** (notá la diferencia con Null Object, que
  modela una ausencia *del dominio*);
- rinde sobre todo en lenguajes **fuerte y estáticamente tipados** (el tipo hace visible "quizás
  ausente" en tiempo de compilación).

---

## Nunca romper el encapsulamiento

Ambas soluciones mantienen la ausencia **adentro** del objeto. Los anti-patrones de abajo la filtran:

### Explicit Absent Message (lenguajes dinámicos con non-local return)

Dale al objeto un mensaje que reciba un bloque a ejecutar cuando el valor está ausente — quien llama
nunca ve el `nil`:

```smalltalk
addressIfAbsent: absentBlock
    ^address ifNil: absentBlock ifNotNil: [ address ]

"uso"
pepeAddress := customer addressIfAbsent: [ ^'No tiene dirección' ].
```

Una variante más rica maneja ambos casos: `withAddress: existingBlock ifAbsent: absentBlock`. Este
idioma solo es válido en **lenguajes dinámicos con non-local return**.

### Safe navigation operator — rompe el encapsulamiento

El `&.` de Ruby (también JavaScript, PHP) te deja escribir `customer.address&.city == city`.
"Funciona", pero **rompe el encapsulamiento**: quien llama ahora sabe que la dirección puede ser
`nil` y la atraviesa. Preferí modelar la ausencia antes que esquivarla.

---

## Cuándo usar cada uno

- **Sistema nuevo, donde se sabe de antemano que "algo puede no existir":**
  - Dinámicamente tipado: 1) Explicit Absent Message, 2) Null Object.
  - Estáticamente tipado: 1) Optional, 2) Null Object.
- **Sistema existente donde antes no podía estar ausente y ahora sí:**
  - Dinámicamente tipado: 1) Null Object, 2) Explicit Absent Message.
  - Estáticamente tipado: 1) Null Object, 2) Optional.
- **Sistema existente, encapsulamiento ya roto, chequeos por null por todos lados:**
  - Dinámicamente tipado: Explicit Absent Message — y a arreglar todo.
  - Estáticamente tipado: Optional — y a arreglar todo.

---

## Dos aclaraciones

- **`null` vs. `nil` es sintaxis vs. objetos.** En algunos lenguajes `nil` es en sí un objeto
  (responde mensajes); en otros `null` es un valor de referencia pelado. La heurística vale igual: no
  lo uses para representar ausencia del dominio.
- **No llenes los métodos de chequeos "¿este parámetro es null?".** Bajo H2/H3/H4 un objeto válido no
  te entrega `null`; los chequeos defensivos en cada parámetro son síntoma de un modelo que ya rompió
  estas heurísticas, no un arreglo.

---

## Principios para el desarrollo

Aplicá esto directamente (como heurísticas).

1. **No uses `null`/`nil` para representar un ente del dominio.** La ausencia ("sin dirección",
   "nada") es algo del dominio — modelala con un objeto.
2. **Reemplazá `if x.nil?` por polimorfismo.** Usá un Null Object (`NotProvidedAddress`) para que
   quien llama envíe un mensaje en vez de ramificar.
3. **Nombrá la ausencia por lo que es.** `NotProvidedAddress`, no `NullAddress`; `Address`, no
   `AbstractAddress`.
4. **En lenguajes estáticamente tipados, hacé visible "quizás ausente" con `Optional`/`Maybe`.**
   Envolvé la referencia, no devuelvas un nullable pelado.
5. **Mantené la ausencia adentro del objeto.** Nunca rompas el encapsulamiento obligando a quien
   llama a chequear por null; preferí un Explicit Absent Message antes que un safe-navigation
   operator.
6. **No escribas chequeos defensivos por null en los parámetros.** Un objeto válido (H3) no te pasa
   `null`.

---

## Glosario

| Término                      | Definición                                                                          |
| ---------------------------- | ----------------------------------------------------------------------------------- |
| **H4**                       | No usar `null`/`nil`; modelar la ausencia como un objeto.                            |
| **Null Object**              | Un objeto que comparte la interfaz, representa una ausencia del dominio y "no hace nada". |
| **Optional / Maybe**         | Un proxy que hace explícito "esta referencia puede estar ausente", sobre todo en lenguajes tipados. |
| **Explicit Absent Message**  | Un mensaje que recibe un bloque "si ausente", para que quien llama nunca vea el `nil`. |
| **Safe navigation operator** | `&.` / `?.`; atraviesa una referencia posiblemente nula — rompe el encapsulamiento. |

---

## Fuentes

- C. A. R. (Tony) Hoare, *Record Handling* (1968) — las relaciones funcionales parciales y la
  introducción de la referencia `null`.
- Tony Hoare, *Null References: The Billion Dollar Mistake* (QCon Londres, 2009).
- Ole-Johan Dahl y Kristen Nygaard, *Classes and Subclasses* / Simula 67 (1968) — `none` como "una
  referencia a ningún objeto".
- Bobby Woolf, *The Null Object Pattern* (en *Pattern Languages of Program Design 3*, 1997).
- Martin Fowler y Kent Beck, *Refactoring* — *Introduce Null Object* / *Replace Conditional with
  Polymorphism*.
- `java.util.Optional` (Java 8); el `Maybe` de Haskell; el `Option` de Scala — modelar referencias
  posiblemente ausentes.
- Kent Beck, *Smalltalk Best Practice Patterns* (1997) — bloques al estilo `ifAbsent:` y non-local
  return.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — curso sobre
  heurísticas de diseño de software con objetos; *Design Principles Behind Patagonia* (ESUG, 2010).
