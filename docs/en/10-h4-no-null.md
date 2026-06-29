# H4 — Don't Use Null

> **Purpose of this document.** This is a design heuristic (read it as a heuristic — see
> [why-heuristics](06-why-heuristics.md)): apply it in context, expecting exceptions. It follows from
> [H1](07-h1-object-per-entity.md) (faithful representation) and [H3](09-h3-valid-objects.md) (only
> valid objects). Apply it whenever you are tempted to leave a reference at `null`/`nil`, or to check
> for it.

---

## The heuristic

> **H4: Don't use `null`/`nil`.**

If objects are created complete ([H2](08-h2-complete-objects.md)) and valid ([H3](09-h3-valid-objects.md)),
can there be an object that references `null`/`nil`? **No — or there shouldn't be.**

`null` leaks into the real world as bugs everyone has seen: a ticket screen showing `null95`, an
Apple Pay dialog "`(null)` could not be found", a budget option reading `100 null`, an "Undo null?"
prompt. These are `null` escaping the model into the user's face.

---

## Why null is a problem: it breaks H1

`null` is the canonical violation of [H1](07-h1-object-per-entity.md) (one object per entity). A
single symbol is overloaded to mean many unrelated domain things at once:

- an **uninitialized variable**,
- "**the customer has no address**",
- "**nothing**".

The same `null` represents all of them, so it represents none of them faithfully. The meaning lives
in the developer's head, not in the model — and the program "does nothing" (or crashes) when the
distinctions matter.

---

## Why does null exist?

`null` was introduced by Tony Hoare. In *Record Handling*, modeling **partial functional
relationships** (e.g. a person may have no father), he provided "a special `null` value … for
reference variables and fields" to indicate the relationship "is not defined (or not yet defined)".
Simula 67 had the same idea as `none`, "a reference to 'no object'".

Hoare later called it his **"billion-dollar mistake"** (QCon, 2009): he added it in 1965 "simply
because it was so easy to implement". *Every language having it does not make it right* — it is a
historical default, not a good model.

---

## The worked example: a customer that may have no address

Code riddled with `if customer.address.nil?` is the symptom. The cure is to **model the absence of
an address** so the `if`s disappear. Two implementations:

### 1. Null Object (a class hierarchy)

Introduce an abstract `Address` with two concrete kinds that both answer the same protocol
(`is_at(city)`):

- `ProvidedAddress` — a real address; `is_at(city)` compares its city.
- `NotProvidedAddress` — the *absence* of an address, modeled as an object; `is_at(city)` answers
  `false`.

Now `customers_at(city)` collapses from an `if/else` to one polymorphic message:

```ruby
def customers_at(city)
  @customers.select do |customer|
    customer.address.is_at city
  end
end
```

Naming matters (this is still [H1](07-h1-object-per-entity.md)): the absence is **not** called
`NullAddress` (it is a domain concept, "not provided", not a null), and the abstract parent is
**not** called `AbstractAddress` (name it `Address`, for what it is). The Null Object can be
implemented as a class hierarchy or as a single well-known instance.

> *Null Object Pattern* (Bobby Woolf): "provide a surrogate for another object that shares the same
> interface but does nothing", encapsulating how to "do nothing" and hiding it from collaborators.

### 2. Optional / Maybe (model that a variable may reference null)

Instead of modeling a special *nothing*, you can model the **fact that a reference may be absent** by
wrapping it in an `Optional`/`Maybe`:

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

- is a **Proxy** — like any proxy, it may or may not be polymorphic with the proxied object;
- represents that **a variable may reference null** (note the difference with Null Object, which
  models a *domain* absence);
- earns its keep mainly in **strongly, statically typed languages** (the type makes "maybe absent"
  visible at compile time).

---

## Never break encapsulation

Both solutions keep the absence **inside** the object. The anti-patterns below leak it:

### Explicit Absent Message (dynamic languages with non-local return)

Give the object a message that takes a block to run when the value is absent — the caller never sees
the `nil`:

```smalltalk
addressIfAbsent: absentBlock
    ^address ifNil: absentBlock ifNotNil: [ address ]

"usage"
pepeAddress := customer addressIfAbsent: [ ^'No address' ].
```

A richer variant handles both cases: `withAddress: existingBlock ifAbsent: absentBlock`. This idiom
is only valid in **dynamic languages with non-local return**.

### Safe navigation operator — breaks encapsulation

Ruby's `&.` (also JavaScript, PHP) lets you write `customer.address&.city == city`. It "works", but
it **breaks encapsulation**: the caller now knows the address can be `nil` and is reaching through
it. Prefer modeling the absence over reaching past it.

---

## When to use each

- **New system, where "something may not exist" is known up front:**
  - Dynamically typed: 1) Explicit Absent Message, 2) Null Object.
  - Statically typed: 1) Optional, 2) Null Object.
- **Existing system where it couldn't be absent before, and now it can:**
  - Dynamically typed: 1) Null Object, 2) Explicit Absent Message.
  - Statically typed: 1) Null Object, 2) Optional.
- **Existing system, encapsulation already broken, null checks everywhere:**
  - Dynamically typed: Explicit Absent Message — and go fix everything.
  - Statically typed: Optional — and go fix everything.

---

## Two clarifications

- **`null` vs. `nil` is syntax vs. objects.** In some languages `nil` is itself an object (it
  responds to messages); in others `null` is a bare reference value. The heuristic stands regardless:
  don't use it to represent domain absence.
- **Don't pepper methods with "is this parameter null?" checks.** Under H2/H3/H4 a valid object
  doesn't hand you `null`; defensive null-checks on every parameter are a symptom of a model that
  already broke these heuristics, not a fix.

---

## Principles for development

Apply these directly (as heuristics).

1. **Don't use `null`/`nil` to represent a domain entity.** Absence ("no address", "nothing") is a
   thing in the domain — model it with an object.
2. **Replace `if x.nil?` with polymorphism.** Use a Null Object (`NotProvidedAddress`) so callers
   send one message instead of branching.
3. **Name the absence for what it is.** `NotProvidedAddress`, not `NullAddress`; `Address`, not
   `AbstractAddress`.
4. **In statically typed languages, make "maybe absent" visible with `Optional`/`Maybe`.** Wrap the
   reference, don't return a bare nullable.
5. **Keep absence inside the object.** Never break encapsulation by forcing callers to null-check;
   prefer an Explicit Absent Message over a safe-navigation operator.
6. **Don't write defensive null-checks on parameters.** A valid object (H3) won't pass you `null`.

---

## Glossary

| Term                         | Definition                                                                          |
| ---------------------------- | ----------------------------------------------------------------------------------- |
| **H4**                       | Don't use `null`/`nil`; model absence as an object.                                 |
| **Null Object**              | An object sharing the interface that represents a domain absence and "does nothing".|
| **Optional / Maybe**         | A proxy that makes "this reference may be absent" explicit, esp. in typed languages. |
| **Explicit Absent Message**  | A message taking an "if absent" block, so callers never see the `nil`.              |
| **Safe navigation operator** | `&.` / `?.`; calls through a possibly-null reference — breaks encapsulation.        |

---

## Sources

- C. A. R. (Tony) Hoare, *Record Handling* (1968) — partial functional relationships and the
  introduction of the `null` reference.
- Tony Hoare, *Null References: The Billion Dollar Mistake* (QCon London, 2009).
- Ole-Johan Dahl & Kristen Nygaard, *Classes and Subclasses* / Simula 67 (1968) — `none` as "a
  reference to no object".
- Bobby Woolf, *The Null Object Pattern* (in *Pattern Languages of Program Design 3*, 1997).
- Martin Fowler & Kent Beck, *Refactoring* — *Introduce Null Object* / *Replace Conditional with
  Polymorphism*.
- `java.util.Optional` (Java 8); Haskell's `Maybe`; Scala's `Option` — modeling possibly-absent
  references.
- Kent Beck, *Smalltalk Best Practice Patterns* (1997) — `ifAbsent:`-style blocks and non-local
  return.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — course on
  object-oriented software design heuristics; *Design Principles Behind Patagonia* (ESUG, 2010).
