# TDD — Test-Driven Development (additional material)

> **Purpose of this document.** This is **additional material**, not a heuristic. It describes a
> *practice* that supports the model: TDD is how the short feedback loop and "development as a
> learning process" from [04 — Software Development](04-software-development.md) become a concrete way
> of working. Use it as context for *how* to grow a faithful object model, day to day.

---

## What TDD is

Test-Driven Development is a practice with a small theory and a large amount of practice — roughly
**95% practice**. The theory is the cycle:

1. **Red** — write the simplest test you can think of for the next bit of behavior, and run it so it
   **fails**. (A test that passes before you write code tests nothing.)
2. **Green** — write the *minimal* code that makes the test pass. Not the elegant code, the smallest
   honest code.
3. **Refactor** — with the test green, improve the design: remove duplication, and **name the
   abstractions** you just discovered.

The cycle is small and repeats many times an hour. It *is* the short feedback loop in practice:
characterize a behavior (the test), predict (it should fail / then pass), experiment (run it), learn.

TDD also doubles as design: because you write the test first, you are forced to use the object's
*protocol* (its messages) before its implementation exists — which keeps the design honest with how
the object will actually be used (see [05 — What Is an Object?](05-what-is-an-object.md)).

---

## Tips for a powerful TDD session

1. **No analysis paralysis.** Don't over-think before acting. Design decisions are made *after* the
   test is green, not before; the cycle leads you to the answer.
2. **Don't skip step 3 (refactor).** Improve the code the moment it works — review names, refactor
   the tests — so you don't accumulate technical debt.
3. **Assertions first.** In Arrange-Act-Assert, write from the bottom up: state *what you want to
   achieve* (the assert) first, then build only the context that assert needs. Simpler tests, less
   setup.
4. **Break the anxiety.** Resist the urge to code the whole solution at once. Keep a steady pace
   through the cycle; rushing introduces bugs.
5. **Leave edge cases for last.** Do the happy path first — users reach for basic functionality
   before exceptional situations.
6. **Change course if you're stuck.** If you've been blocked on a test for 10–15 minutes, abandon it
   and try a different approach (a smaller test, a different starting point).

---

## What makes a test good (Test Desiderata)

Tests are not all equally valuable. A useful checklist of desirable properties (Kent Beck's *Test
Desiderata*, 12 properties) includes, among others: tests should be **isolated** (don't depend on
each other), **composable**, **fast**, **deterministic** (same result every run), **specific** (a
failure points to the cause), **behavioral** (sensitive to behavior changes, not to refactors),
**readable**, and **writable** (cheap to write). You rarely get all twelve at once; the point is to
choose consciously which properties matter for a given test.

---

## How TDD relates to the model and the heuristics

- **It feeds the learning loop** (04): each cycle is a tiny experiment that grows your understanding
  of the domain and bakes it into the model.
- **Step 3 protects the descriptive axis** (03) and **naming** ([14 — Naming](14-naming.md)): the
  refactor step is where you name the abstractions you discovered.
- **It surfaces the right objects** (H1): duplication you remove in refactor often reveals a missing
  domain object.
- **It pins down validity** (H3): tests for invalid creation are where you make invalid objects
  impossible and assert fail-fast behavior.

---

## Principles for development

Apply these as practices (judgment still applies — they are not rules).

1. **Write the test first, and watch it fail.** A failing test proves the test works before the code
   does.
2. **Write the minimal code to pass.** Defer design decisions to the refactor step.
3. **Never skip refactor.** Remove duplication and name abstractions while the test is green.
4. **Assert first, arrange last.** Let the desired outcome drive the setup.
5. **Happy path before edge cases.** Get the core behavior working, then harden it.
6. **Timebox being stuck.** After ~10–15 minutes blocked, take a smaller step or change approach.
7. **Choose test properties consciously.** Aim for fast, isolated, deterministic, specific tests.

---

## Glossary

| Term                 | Definition                                                                          |
| -------------------- | ----------------------------------------------------------------------------------- |
| **TDD**              | Test-Driven Development: red → green → refactor, repeated in short cycles.           |
| **Red/Green/Refactor** | Fail a test, make it pass minimally, then improve the design.                     |
| **Arrange-Act-Assert** | Test structure; write it assert-first to focus on the outcome.                    |
| **Test Desiderata**  | Kent Beck's 12 desirable properties of a test (fast, isolated, deterministic, …).   |
| **Happy path**       | The expected, non-exceptional flow; do it before edge cases.                        |

---

## Sources

- 10Pines blog, *6 Tips for a Powerful TDD Session* — https://blog.10pines.com/2018/01/29/6-tips-for-a-powerful-tdd-session/
- 10Pines blog, *Las 12 propiedades deseables de los tests según Kent Beck* — https://blog.10pines.com/2021/06/14/las-12-propiedades-deseables-de-los-tests-segun-kent-beck/
- 10Pines blog, *El primer test* — https://blog.10pines.com/2020/08/18/el-primer-test/ ; TDD tag — https://blog.10pines.com/tag/tdd/
- Kent Beck, *Test-Driven Development: By Example* (2002); *Test Desiderata* (2019).
- Steve Freeman & Nat Pryce, *Growing Object-Oriented Software, Guided by Tests* (2009).
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — course on
  object-oriented software design.
