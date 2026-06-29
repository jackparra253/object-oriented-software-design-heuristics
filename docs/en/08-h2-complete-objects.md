# H2 — Create Objects Complete

> **Purpose of this document.** This is a design heuristic (read it as a heuristic — see
> [why-heuristics](06-why-heuristics.md)): apply it in context, expecting exceptions. It governs
> *when* an object is allowed to exist and what it must know at that moment. Apply it whenever you
> design construction (constructors, factories, builders).

---

## The heuristic

> **H2: Objects must be created complete.**

Because a computable model is dynamic — **time passes** — an object must **represent its domain
entity from the very moment it exists**, and it must **explicitly "teach" what it needs** in order
to represent that entity. There is no valid "half-built" state.

In other words: after construction, the object is already a faithful representation (see
[H1](07-h1-object-per-entity.md)). It is never temporarily invalid, waiting for later setter calls
to finish it.

---

## The problem it prevents: temporal coupling and null holes

*Example.* A `PhoneCall` with `origin`, `destination`, `start`, and `end`. If you create it with
everything **except** `end` (because the call hasn't finished yet) and leave `end = null`, then
asking it `duration()` blows up — `NullPointerException` / `doesNotUnderstand:`. The object existed
before it was a complete, faithful phone call.

The usual "fix" — call `setEnd(...)` later — introduces **temporal coupling**: messages must be
sent in a hidden required order, and any code holding the object in between sees an invalid state.

A complete-object design avoids this. Either:

- the object is only created once everything it needs is known; or
- the lifecycle is split into **two objects** — e.g. an *ongoing* call (origin, destination, start)
  and a *finished* call (which also has an end and can answer `duration()`). Each is complete and
  faithful at all times.

---

## Tips for creating complete objects

1. **One primary constructor / instance-creation method.** Have a single main way to build the
   object; every other constructor or factory delegates to it. (One place enforces completeness.)
2. **Uninitialized instance variables are a smell → split into two objects.** If some fields can't
   be set at construction, that usually means you are modeling two different entities/states; model
   them as two complete objects rather than one half-empty one.
3. **Complex construction / much "passage of time" → use a Builder.** When assembling the object
   requires many steps over time, gather the parts in a separate **Builder** and produce the
   complete object at the end — keep the domain object itself always-complete.
4. **A framework forcing a no-arg constructor is not a reason to expose one.** Some tools (e.g.
   Hibernate) demand a parameterless constructor; that is a tooling constraint, not a design
   license to allow incomplete objects. Don't let it leak into your model's public contract.

---

## Why it matters — complete objects "teach"

A complete object communicates the model clearly. It:

- **Teaches how it must be instantiated** — its constructor lists exactly what it needs.
- **Teaches whom it relates to** — its required collaborators are explicit.
- **Helps the model evolve** — there is a single, honest creation path to change.
- **Has no temporal coupling between its messages** — any message is valid as soon as the object
  exists; callers never need to know a magic call order.

---

## Principles for development

Apply these directly (as heuristics).

1. **Make every object valid from creation.** After construction it must already represent its
   entity faithfully — never a half-built, "fill in later" state.
2. **Require what the object needs in its constructor.** Make dependencies and collaborators
   explicit at creation; the constructor should *teach* what the entity needs.
3. **Avoid post-construction setters that complete the object.** They create temporal coupling and
   transient invalid states.
4. **Funnel construction through one primary creation method.** Other constructors/factories
   delegate to it so completeness is enforced in one place.
5. **Treat uninitialized fields as a modeling signal.** They usually mean "this is really two
   objects/states" — split them.
6. **Use a Builder when construction spans time or many steps.** Keep the assembly outside the
   always-complete domain object.
7. **Don't let framework constraints dictate your model.** A required no-arg constructor is a
   tooling workaround, not a design choice — isolate it.

---

## Glossary

| Term                       | Definition                                                                       |
| -------------------------- | -------------------------------------------------------------------------------- |
| **H2**                     | Objects must be created complete — valid and faithful from the moment they exist. |
| **Complete object**        | An object that fully represents its entity right after construction.             |
| **Temporal coupling**      | A hidden requirement that messages be sent in a specific order to be valid.       |
| **Primary constructor**    | The single creation method all other constructors/factories delegate to.          |
| **Builder**                | A separate object that assembles a complex object and yields it complete.          |

---

## Sources

- Arthur J. Riel, *Object-Oriented Design Heuristics* (Addison-Wesley, 1996) — initialize objects
  fully; constructors should leave objects in a valid state.
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides (GoF), *Design Patterns* (1994) — the
  **Builder** pattern.
- Steve Freeman & Nat Pryce, *Growing Object-Oriented Software, Guided by Tests* (2009) — objects
  should be valid (fully formed) on creation.
- Kent Beck, *Implementation Patterns* (2007) — *Complete Constructor*.
- Andrew Hunt & David Thomas, *The Pragmatic Programmer* (1999) — temporal coupling.
- Yegor Bugayenko, *Elegant Objects* (2016) — complete, always-valid objects; no incomplete state.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — course on
  object-oriented software design heuristics.
