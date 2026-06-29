# H3 — Only Create Valid Objects

> **Purpose of this document.** This is a design heuristic (read it as a heuristic — see
> [why-heuristics](06-why-heuristics.md)): apply it in context, expecting exceptions. It builds on
> [H2](08-h2-complete-objects.md): being *complete* is not enough — the object must also be *valid*.
> Apply it whenever you design creation, validation, and error handling.

---

## The heuristic

> **H3: Only create valid objects.**

A complete object can still be nonsensical. The model must make invalid objects **impossible to
create**. You should not be able to build:

- a `31/Feb/2018`,
- a fraction `1/0`,
- a `CreditCard` with an empty owner name,
- a `Time` of `25:73:00`.

So, extending H2:

> An object must represent its entity **validly** from the moment it exists, must **explicitly
> teach** what it needs, and must **fail if created incorrectly — fail fast.**

*Example.* `LocalDate.of(2018, FEBRUARY, 31)` throws — correct: the invalid object never exists. The
old `Calendar`/`SimpleDateFormat` silently "adjusts" Feb 31 to `03/03/2018` — wrong: it produced a
different, surprising object instead of failing.

---

## Put validations in the model

The biggest payoff of H3 is **where** the validation lives: in the business model object itself, not
in each entry point.

If `Time.at(25, 10, 0)` validates inside `Time`, then it fails the same way whether the data arrives
from a REST endpoint, a batch job, or the UI. Consequences:

- **One single validation**, regardless of where the information comes from.
- **No repeated, unmaintainable validations** scattered across controllers and jobs.
- **Fewer tests** needed for input errors — you test the rule once, in the model.
- **No inconsistent models** can exist anywhere in the system.

---

## Tips for creating valid objects

1. **Use exceptions, not return codes, to signal errors.** An invalid creation should raise, not
   return a flag the caller may ignore.
2. **Validate in an instance-creation method, not in the raw "constructor".** When a constructor
   runs, memory has already been allocated; it is better not to allocate an object you will
   immediately discard. The constructor *couples* allocating memory with initializing it — use a
   creation method that validates first and only then builds. (See the interlude below on why this
   creation method should be a *class method*, not a *static method*.)
3. **Be clear about which object is responsible for validating what.** Each object validates its own
   invariants; don't duplicate a rule in collaborators that already trust a valid object.
4. **Choose a validation model deliberately:**
   - **SOFE (Stop On First Error)** — raise on the first problem. Simple, but poor for UIs (the user
     fixes one error, resubmits, sees the next).
   - **Collect all errors** — gather every problem and report them together. Better for UIs (show
     all field errors at once).

---

## Interlude: class method vs. static method

The instance-creation method (Tip 2) should ideally be a **class method**, not a **static method**.
A *static method*:

- has no `self`/`this`,
- cannot be overridden,
- cannot reuse a superclass implementation via `super`,
- has no polymorphism,
- …is not really "objects".

A *class method* has all of those — it *is* objects, so creation can be polymorphic and reusable.
Smalltalk and Ruby have true class methods; Java, C#, C++ have static methods; Python has both.
JavaScript's `static` is, by design, closer to a Smalltalk **class method** than to a Java static
method (inside it, `this` is the class, and you can write `return new this(...)`), even though the
keyword "static" suggests otherwise.

Takeaway: prefer creation methods that are polymorphic (class methods) where the language allows it.

---

## Why it matters — with valid objects

- The **model teaches what cannot be done** (invalid states are unrepresentable).
- **No inconsistent models** exist.
- The **error rate drops.**
- **Validation is single-sourced**, regardless of the information's origin.
- **Fail fast** — problems surface at creation, not deep in later processing.

---

## Principles for development

Apply these directly (as heuristics).

1. **Make invalid objects impossible to create.** Reject bad input at creation; never allow a
   nonsensical object to exist.
2. **Fail fast on invalid creation.** Surface the error at the point of construction, not later.
3. **Put validation in the domain model, not at the edges.** One rule in the model serves REST,
   batch, and UI alike.
4. **Signal creation errors with exceptions, not return codes.**
5. **Validate in an instance-creation method, not the raw constructor.** Don't allocate an object
   you'll immediately discard; keep "decide validity" separate from "allocate".
6. **Assign validation responsibility clearly.** Each object validates its own invariants; avoid
   duplicating rules.
7. **Pick SOFE vs. collect-all to fit the consumer.** Collect all errors for UIs; stop-on-first is
   fine for internal calls.
8. **Prefer polymorphic class methods for creation** where the language supports them.

---

## Glossary

| Term                         | Definition                                                                     |
| ---------------------------- | ------------------------------------------------------------------------------ |
| **H3**                       | Only create valid objects — invalid ones must be impossible to construct.      |
| **Fail fast**                | Surface an error at the earliest point (creation), not later.                  |
| **Instance-creation method** | A method (ideally a class method) that validates, then builds the object.      |
| **Class method**             | A polymorphic method on the class with `self`/`this`; "is objects".            |
| **Static method**            | A non-polymorphic procedure attached to a class; no `self`, no override.       |
| **SOFE**                     | "Stop On First Error" validation; vs. collecting all errors for UIs.           |

---

## Sources

- Arthur J. Riel, *Object-Oriented Design Heuristics* (Addison-Wesley, 1996).
- Steve Freeman & Nat Pryce, *Growing Object-Oriented Software, Guided by Tests* (2009) — objects
  valid on creation.
- Jim Shore, *Fail Fast* (IEEE Software, 2004); Martin Fowler, *FailFast* — failing at the source of
  the problem.
- Robert C. Martin, *Clean Code* (2008) — prefer exceptions to return codes for errors.
- Kent Beck, *Smalltalk Best Practice Patterns* (1997) — *Constructor Method* / instance-creation
  methods.
- Stephen Colebourne et al., JSR-310 `java.time` — validating factories (`LocalDate.of`) vs. the
  lenient legacy `Calendar`.
- Allen Wirfs-Brock & Brendan Eich, *JavaScript: The First 20 Years* (HOPL, 2020) — JS `static`
  methods as class methods (à la Smalltalk).
- Vaughn Vernon, *Implementing Domain-Driven Design* (2013); Yegor Bugayenko, *Elegant Objects*
  (2016) — the always-valid object/domain model.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — course on
  object-oriented software design heuristics.
