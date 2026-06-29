# What Makes a Good Model? — The Three Axes

> **Purpose of this document.** This is foundational context for designing and writing software.
> It defines what "good" means for software by defining what makes a good model, and breaks that
> into three independent axes to evaluate and improve. Apply these whenever you judge, review, or
> improve a design.

---

## Working definition

Good software is a good model. A model is good along **three independent axes**, all of which
matter:

> 1. **Implementation axis** — how well it *executes* in the technical environment.
> 2. **Descriptive axis** — how well the model is *described* and understood.
> 3. **Functional axis** — how good the *representation of the domain* is.

A model can be strong on one axis and weak on another. A complete evaluation looks at all three.

---

## The three axes

### Implementation axis — how it executes

A model is good on this axis when it **executes within the expected time using the resources
defined as necessary.** This covers:

- **Performance** (speed)
- **Space** (memory/storage)
- **Scalability**
- Everything related to **non-functional requirements** (quality attributes)

This is the **"detail" part** of development. It answers *how* the model runs in the technical
environment, not *what* it represents.

### Descriptive axis — how well it is described

A model is good on this axis when it **teaches us**: it can be *understood*, and therefore
*changed.* Keys:

- **Good names are critically important.**
- **Use the same language as the business domain** in the code.
- The code must be **pleasant — "habitable".**

This is the **"artistic" part** of development. Code that cannot be understood cannot be safely
changed, so this axis directly governs maintainability.

### Functional axis — how well it represents the domain

A model is good on this axis when it can **correctly represent every observation of the thing it
models.** Concretely:

- If **something new appears in the domain**, something new should **appear** in the model — you
  *add* to it, you do not modify what already exists.
- If **something in the domain changes**, you should only need to change **its** representation in
  the model — nothing else.
- The goal is a **1:1 relationship between domain and model (an isomorphism).**

This is the **"observational" part** of development. (The "add for new, change only the affected
representation" rule is the open–closed principle in action: open for extension, closed for
modification.)

---

## A good model corresponds 1:1 to its domain

The functional axis is the deepest one for object design. Strive for an **isomorphism**: each
thing in the problem domain has exactly one representation in the model, and each representation
corresponds to exactly one thing in the domain. When that holds:

- New domain concepts map to new model elements (extension), not edits to existing ones.
- A change in one domain concept touches exactly one place in the model.

Loss of this correspondence is a primary source of fragility: one domain change forces edits in
many unrelated places, and new cases require modifying existing code instead of adding to it.

---

## Principles for development

Apply these directly.

1. **Evaluate a design on all three axes.** Implementation, description, and functional
   representation are independent; a design that is fast but unreadable, or readable but a poor
   domain representation, is not a good model.
2. **Treat non-functional requirements as the implementation axis.** Performance, space, and
   scalability are real, but they are the *detail* layer — do not let them drive the whole design.
3. **Invest heavily in names.** Good names are not cosmetic; they are how the model teaches and
   stays changeable.
4. **Speak the domain's language in the code.** Use the same vocabulary as the business; avoid
   inventing a parallel technical dialect.
5. **Keep the code habitable.** Optimize for a reader who must understand it before changing it.
6. **Prefer adding over modifying.** When a new case appears in the domain, extend the model with
   a new element rather than editing existing code (open–closed).
7. **Localize change.** Structure the model so that one domain change maps to one model change.
8. **Aim for a 1:1 domain–model correspondence (isomorphism).** Use it as the test of the
   functional axis.

---

## Glossary

| Term                    | Definition                                                                        |
| ----------------------- | --------------------------------------------------------------------------------- |
| **Implementation axis** | How well the model executes in the technical environment (the "detail" part).     |
| **Descriptive axis**    | How understandable and well-described the model is (the "artistic" part).          |
| **Functional axis**     | How faithfully the model represents the domain (the "observational" part).        |
| **Quality attributes**  | Non-functional requirements (performance, space, scalability); the implementation axis. |
| **Habitable code**      | Code pleasant enough to be understood and lived in by those who must change it.    |
| **Isomorphism (domain–model)** | A 1:1 correspondence between things in the domain and elements in the model. |

---

## Sources

- Hernán Wilkinson, Máximo Prieto, Luciano Romeo, *A Point-Based Model of the Gregorian Calendar*
  (Computer Languages, Systems & Structures, Elsevier, 2005) — a worked example of good domain
  modeling and the use of metaphors.
- Eric Evans, *Domain-Driven Design* (Addison-Wesley, 2003) — *ubiquitous language*: speaking the
  domain's language in the code.
- Kent Beck, *Implementation Patterns* (Addison-Wesley, 2007) — naming and communicating intent in
  code.
- Richard P. Gabriel, *Patterns of Software* (Oxford University Press, 1996) — *habitability* of
  code.
- Bertrand Meyer, *Object-Oriented Software Construction*, 2nd ed. (Prentice Hall, 1997) — the
  open–closed principle; direct mapping between domain and model.
- Robert C. Martin, *Agile Software Development: Principles, Patterns, and Practices* (2002) — the
  open–closed principle in practice.
- 10Pines blog, *The Art of Naming* and *About Names When Designing with Objects* (2012) —
  <https://blog.10pines.com/2012/02/02/the-art-of-naming/>,
  <https://blog.10pines.com/2012/01/12/about-names-when-designing-with-objects/>.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — course on
  object-oriented software design heuristics.
