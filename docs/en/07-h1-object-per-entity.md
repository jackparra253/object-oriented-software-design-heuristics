# H1 — One Object per Entity (Faithful Representation)

> **Purpose of this document.** This is a design heuristic (read it as a heuristic — see
> [why-heuristics](06-why-heuristics.md)): apply it in context, expecting exceptions. It governs the
> correspondence between domain entities and the objects that represent them. Apply it whenever you
> decide how to represent a piece of the domain in code.

---

## The heuristic

> **H1: For every entity of reality there must be one object that represents it "faithfully".**

This is the **functional axis** made concrete: aim for a **1:1 correspondence (isomorphism)**
between entities in the domain and objects in the model. Each domain entity maps to exactly one
object, and each object stands for exactly one entity.

Two ways to break H1, both harmful:

1. **One entity represented by more than one object.**
2. **One object representing more than one entity.**

---

## Failure mode 1 — one entity, many objects

When a single domain entity is scattered across several objects/fields, the entity has no single
home in the model.

*Example.* A credit card's "expiration" is one entity (a year-month). Modeling it as two separate
fields — `expirationYear` and `expirationMonth` — splits one entity across two objects.

Consequences:

- **More accidental complexity.**
- **Duplicated code** (every operation must juggle both pieces).
- **Error-prone** (the two pieces can get out of sync).
- **Loss of cohesion** (behavior that belongs to one concept is spread out).

---

## Failure mode 2 — one object, many entities

When a single object is reused to stand for several distinct entities, the representation is no
longer faithful.

*Examples.*

- Encoding the expiration as an **array** `{2023, 8}`: the same shape could mean "August 2023",
  "the pair (2023, 8)", or "8 days since the start of 2023". The meaning lives in the developer's
  head, not in the model.
- Using a bare **number** or **string** to stand for an identifier, a measure (`1` as "1 dollar",
  "1 litre", "1 metre"), or an encoded `yyyymm`.
- The paradigmatic case: **`null`** standing for "uninitialized variable", "the customer has no
  address", "nothing", all at once. (Treated in depth in H4 — Avoid null.)

Consequences:

- **Does not represent the entity faithfully**; **information is lost**.
- **Not declarative / not explicit** — the meaning isn't in the code: *Which slot is the year and
  which the month? What if there are fewer or more elements?*
- **Primitive Obsession** — using language primitives instead of a domain object; it is a *hack*.
- **Models that do not teach** — the reader cannot learn the domain from the code.

---

## The worked example: a credit card

A credit card knows an owner name, a "number", and an "expiration date". Natural language is
**ambiguous**:

- We say "number", but the card number is **not a number — it is an identifier** (you never do
  arithmetic on it).
- We say "expiration date", but it is **not a date — it is a year-month** (an expiration month of a
  year).

Choosing the faithful entity matters:

| Representation of the expiration | Verdict                                                            |
| -------------------------------- | ----------------------------------------------------------------- |
| A **year-month** (e.g. `YearMonth`) | Faithful — beautiful, correct.                                  |
| A full **date**                  | Error-prone — you must "adjust" it, and it isn't a date.          |
| **Two numbers** (month + year)   | Breaks H1 (one entity, many objects).                            |
| **An array / encoded number**    | Breaks H1 (one object, many entities); a hack.                   |

---

## Caveat: this is about objects, not classes

H1 talks about **objects**, not necessarily new classes.

- The object that faithfully represents an entity **can be an instance of an existing class** — you
  do not have to invent a class for everything.
- A credit-card expiration is a `YearMonth`, **not** a custom `ExpirationDate` class.
- A fraction's numerator and denominator are **numbers**, not instances of `Numerator` and
  `Denominator`.

So: represent each entity faithfully with the *right* object — which is often a suitable existing
type — without over-modeling by minting needless classes.

Also avoid the opposite trap: do **not** excuse a poor model with "it's only a model, of course it
doesn't represent everything." Faithful representation is the goal.

---

## Why it matters

Complexity = **essential** + **accidental**. Breaking H1 adds *accidental* complexity for nothing.
If H1 is not met, you get:

- ad-hoc, particular solutions;
- reinventing the (flat) wheel;
- software that is hard to understand;
- duplicated, error-prone, non-declarative code.

---

## Principles for development

Apply these directly (as heuristics).

1. **Give each domain entity exactly one representing object.** Maintain the 1:1 correspondence.
2. **Do not split one entity across several fields/objects.** If two values always travel together
   and mean one concept, model them as one object (e.g. a year-month, not year + month).
3. **Do not overload one object/primitive to mean several entities.** Replace "clever" arrays,
   encoded numbers, and bare strings with a real domain object (fix Primitive Obsession).
4. **Name the entity for what it really is.** Push past ambiguous natural language: a card "number"
   is an identifier; an "expiration date" is a year-month.
5. **Prefer the right existing type over a new class.** Represent the object faithfully; only create
   a class when no suitable type exists.
6. **Make the model declarative.** The meaning of a value should be in the code, not in your head.
7. **Treat `null`-as-everything as a special case of breaking H1.** (See H4.)

---

## Glossary

| Term                     | Definition                                                                  |
| ------------------------ | --------------------------------------------------------------------------- |
| **H1**                   | For every entity of reality there must be one object representing it faithfully. |
| **Faithful representation** | A 1:1 correspondence between a domain entity and its object.             |
| **Primitive Obsession**  | Using language primitives (number, string, array) instead of a domain object. |
| **Accidental complexity**| Complexity introduced by the solution, not inherent to the problem.          |
| **Declarative code**     | Code whose meaning is explicit in itself, not implicit in the reader's head. |

---

## Sources

- Arthur J. Riel, *Object-Oriented Design Heuristics* (Addison-Wesley, 1996).
- Martin Fowler & Kent Beck, *Refactoring* (Addison-Wesley) — the *Primitive Obsession* code smell;
  *Replace Primitive with Object*.
- Eric Evans, *Domain-Driven Design* (Addison-Wesley, 2003) — Value Objects representing domain
  concepts.
- Frederick P. Brooks, *No Silver Bullet* (1986) — essential vs. accidental complexity.
- `java.time.YearMonth` (JSR-310 / Java 8) — a faithful model of a month-of-year, as used in the
  worked example.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — course on
  object-oriented software design heuristics.
