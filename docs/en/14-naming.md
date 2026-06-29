# Naming — Variables and Classes (additional material)

> **Purpose of this document.** This is **additional material**, not a heuristic. It is a *practice*
> that directly serves the **descriptive axis** of a good model
> ([03 — What Makes a Good Model?](03-good-model.md)) and reinforces
> [H1 — one object per entity](07-h1-object-per-entity.md): naming things for what they really are.
> Use it as context for choosing names while you design and code.

---

## Programming is the art of naming

A name **synthesizes the meaning** of what is named: it lets you grasp *what* something is without
having to think about *how* it works. So naming is one of the most important things a programmer does —
not decoration, but design.

Three core ideas:

- **Names are for humans, not for machines.** The computer treats every identifier as an opaque
  symbol; it would run just as well with `a`, `b`, `c`. The entire value of a good name accrues to the
  people reading and changing the code.
- **If you can't name something, you haven't fully understood it yet.** Difficulty naming is a signal
  that the concept isn't clear — naming pressure pushes you to understand the domain.
- **Understanding precedes naming.** You name well *after* you understand the entity, not before.

---

## Concrete recommendations

### Avoid

- **Generic, meaningless variables:** `x`, `y`, `i`, `n`, `tmp`, `data`, `obj` — they carry no domain
  meaning.
- **Vague "noise" class names:** `ObjectManager`, `ServiceHelper`, `ObjectDirector`, `…Util`,
  `…Processor`, `…Handler`. These usually mark a place where the real concept hasn't been found yet.

### Prefer

- **Name the entity for what it really is.** This is [H1](07-h1-object-per-entity.md) restated for
  names: a card "number" is an *identifier*; an "expiration date" is a *year-month*. The right name
  reveals the right object.
- **Use a deliberately meaningless placeholder when you don't yet understand the concept.** Naming
  something `XYZ` or `QQQ` on purpose is better than committing to a wrong, plausible-looking name —
  the placeholder *itches*, so you rename it once you understand it (often after playing with its
  instances).
- **Rename in the refactor step.** The third step of the TDD cycle
  ([13 — TDD](13-tdd.md)) is exactly where you turn discovered abstractions into good names; don't
  postpone it.

### Don't leave objects nameless

Anonymous structures — a bare hash/dictionary/tuple passed around to represent a concept — are objects
without a name. They hinder communication, make design hard to reason about, **breed duplicated code**,
and raise maintenance cost. When a structure represents a concept, **give it a class/type** (again,
[H1](07-h1-object-per-entity.md): replace Primitive Obsession with a real domain object).

### Make it a team practice

Naming is shared infrastructure. Agree on **naming conventions across the team** so the vocabulary of
the codebase stays consistent and teachable — the model should teach the domain to whoever reads it.

---

## Principles for development

Apply these as practices (judgment still applies — they are not rules).

1. **Treat naming as design, not decoration.** A name carries the meaning of the thing it names.
2. **Name for the human reader.** Optimize for understanding, not for the compiler.
3. **Understand before you name.** Trouble naming means the concept isn't clear yet.
4. **Avoid generic and "noise" names.** No `x`/`tmp`/`data`; no `…Manager`/`…Helper`/`…Util`.
5. **Name the entity for what it truly is** (ties to H1) — the right name surfaces the right object.
6. **Use a meaningless placeholder, then rename.** Don't cement a wrong name; let the placeholder
   force a later, better name in the refactor step.
7. **Give nameless objects a name.** Replace anonymous structures with classes/types representing the
   concept.
8. **Standardize naming across the team.** Keep the codebase's vocabulary consistent and habitable.

---

## Glossary

| Term                    | Definition                                                                       |
| ----------------------- | -------------------------------------------------------------------------------- |
| **Name**                | A synthesis of the meaning of what is named; serves human understanding.         |
| **Noise name**          | A vague class name (`Manager`, `Helper`, `Util`) hiding a missing real concept.  |
| **Meaningless placeholder** | A deliberately empty name (`XYZ`) used until the concept is understood.       |
| **Nameless object**     | An anonymous structure (bare hash/tuple) standing in for a concept that deserves a class. |
| **Descriptive axis**    | The "how understandable is it" axis of a good model (see 03), served by naming.   |

---

## Sources

- 10Pines blog, *The Art of Naming* — https://blog.10pines.com/2012/02/02/the-art-of-naming/
- 10Pines blog, *A case against nameless objects* — https://blog.10pines.com/2021/12/09/a-case-against-nameless-objects/
- 10Pines blog, object-design tag — https://blog.10pines.com/tag/object-design/
- Robert C. Martin, *Clean Code* (2008), ch. 2 "Meaningful Names"; Tim Ottinger, *Ottinger's Rules
  for Variable and Class Naming*.
- Eric Evans, *Domain-Driven Design* (2003) — the Ubiquitous Language.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — course on
  object-oriented software design.
