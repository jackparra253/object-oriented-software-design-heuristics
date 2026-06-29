# Where Is the Model? — Source Code Is the Design

> **Purpose of this document.** This is foundational context for designing and writing software.
> It establishes *where* the model that software consists of actually lives, and what follows from
> that for how to work. Apply these definitions and principles whenever you write code, draw a
> diagram, estimate work, or decide what "designing" means.

---

## Working definition

The model that software consists of is **expressed in the source code** — and nowhere else.

> **Source code is the design of the software.**

Diagrams, documents, and specifications are *not* the model. They may help visualize or
communicate it, but the only complete, precise, executable expression of the design is the source
code itself. It follows that:

> **Programming is designing, and designing is programming.** They are the same activity.

---

## Core definitions

### Design

- **Design** is the definition used to build something: a description, drawing, or specification,
  related to the thing being designed and intended for its construction.

In most engineering disciplines the *design* is a document (a blueprint), and *construction* is a
separate, expensive, physical phase carried out from that document. Software does not work this
way.

### What we build, and what builds it

- The thing we actually deliver is **executable software**.
- What produces executable software from the design is the **compiler / build toolchain**.

So in software terms:

| Engineering concept                     | Software equivalent                |
| --------------------------------------- | ---------------------------------- |
| The design document                     | The **source code**                |
| The construction crew                   | The **compiler / build system**    |
| Construction (building from the design) | **Compilation / build**            |
| The finished product                    | The **running executable**         |

Construction — turning the design into a runnable artifact — is automated, fast, and effectively
free; the compiler does it. Therefore **the entire cost and difficulty of software is in the
design**, i.e. in writing the source code.

### Testing and debugging are design activities

- **Testing** and **debugging** are not separate from design; they are the **validation and
  refinement of a design**. They are part of producing a correct design, not a phase that comes
  after design is "done".

### Diagrams visualize the design — they are not the design

- Class diagrams, sequence diagrams, and similar artifacts **help visualize** the design.
- They are **not** the design and **not** the computable model. Neither is the documentation. Only
  the source code is.

### The model is dynamic — time passes in it

- A computable model **executes**, and execution means **the passage of time**: the modeled state
  changes from `t0` to `tn`.

This is the essential difference from static models in other disciplines. A blueprint models *a
house*; software models *what a house is* — a living definition that runs and changes over time.
**Be careful comparing software models with those of other professions:** ours are dynamic and
executable; theirs are usually static.

---

## Principles for development

Apply these directly.

1. **Treat the source code as the design.** It is the single source of truth for the model. Keep
   it clear, because clarity of code is clarity of design.
2. **Programming is designing.** Do not treat writing code as mere transcription of a "real"
   design that lives in diagrams or documents. The design happens as the code is written.
3. **Diagrams and docs visualize; they never replace the code.** Use them to think and
   communicate, but never treat them as the model, and never let them drift into being a second,
   contradictory source of truth.
4. **Treat testing and debugging as design.** They validate and refine the design; budget for them
   as core design work, not as an afterthought.
5. **The build is free; the design is the cost.** Optimize for the quality of the source code, not
   for the mechanics of compilation. Effort and estimates belong on the design, i.e. the code.
6. **Estimate discovery, not construction.** Estimating is hard because what is being estimated is
   *designing* (discovering the model), not *building* (which the compiler does for free).
   Separate "discover" from "deliver".
7. **Account for time in the model.** Because the model executes, design for state that changes
   over time; do not reason about it as if it were a static snapshot.
8. **Iterate; do not assume a single linear pass.** A strictly sequential, build-it-once-from-a-
   frozen-spec process is risky and invites failure. Expect to revisit earlier decisions as the
   design is validated.

---

## Glossary

| Term                    | Definition                                                                 |
| ----------------------- | -------------------------------------------------------------------------- |
| **Design**              | The definition used to build something, intended for its construction.     |
| **Source code**         | The complete, precise, executable expression of the software design.       |
| **Construction**        | Producing a runnable artifact from the design; done by the compiler/build. |
| **Compiler / build**    | The "construction crew" that turns the design into an executable.          |
| **Testing / debugging** | Validation and refinement of a design.                                     |
| **Diagram**             | A visualization of the design; not the design itself.                      |
| **Dynamic model**       | A model that executes, so its state changes as time passes.                |

---

## Sources

- Jack W. Reeves, *What Is Software Design?* (C++ Journal, 1992) — the thesis that the source code
  is the design and that construction is compilation. Mirror: <https://wiki.c2.com/?WhatIsSoftwareDesign>.
- Glenn Vanderburg, *Real Software Engineering* (Lone Star Ruby Conference, 2010) —
  <https://youtu.be/RhdlBHHimeM>.
- Winston W. Royce, *Managing the Development of Large Software Systems* (1970) — the paper that
  diagrams the sequential ("waterfall") process and warns that, as commonly applied, it "is risky
  and invites failure", arguing instead for iteration and early customer involvement.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — course on
  object-oriented software design heuristics.
- Frederick P. Brooks, *No Silver Bullet — Essence and Accidents of Software Engineering* (1986) —
  design is the essential, irreducible difficulty.
