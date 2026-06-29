# What Is Software?

> **Purpose of this document.** This is foundational context for designing and writing software.
> Treat the definitions below as the working definition of "software" and apply the principles
> whenever you model a domain, structure code, or decide what "good" means for a system.

---

## Working definition

**Software** is *(knowledge expressed as)* a **computable model** of a **problem domain** of
**reality**.

A weaker, historically common definition — *software is a set of instructions that, given some
input, produces some output* — is true but useless for design. "A set of instructions" gives no
criterion for what makes software *good* or for how it should be *organized*. The model-based
definition does, and it is the one to use.

The direct consequence:

> **Good software is a good model.**
> Therefore software must be **organized according to the structure of the problem domain** — not
> according to the technology, framework, or tooling in use.

When these two views conflict — organizing code the way a framework imposes versus organizing it
the way the domain is actually structured — **favor the domain**.

---

## Core definitions

### Reality

- **Reality** is a set of *things*.
- A **thing** is anything about which something can be said.

Reality, as humans perceive and describe it, is **arbitrary** (we carve it up to suit us),
expressed in **natural language**, and therefore **ambiguous** and **context-dependent**: the
meaning of a statement depends on its context.

### Problem domain

- A **problem domain** (or **knowledge domain**) is a *slice of reality* that represents the
  **business** being modeled.
- Distinguish **business domains** from **natural domains**. Software does not model "all of
  reality"; it models the bounded portion relevant to the business.

### Model

- A **model** is a *representation of the knowledge* built about a domain.

Modeling is not copying reality; it is **constructing a representation** of it. Every model is
shaped by three questions, which must have deliberate answers:

- **Why** are we modeling? (the purpose the model serves)
- **In what language** are we modeling?
- **What kind** of model are we building?

A model **represents** a thing; it **is not** the thing. Keep the map distinct from the territory.

### Computable

- **Computable** means it can be executed on a Turing machine.

Unlike natural language (arbitrary, ambiguous, contextual), a computable model is expressed in a
**formal, executable language** — the **source code**. It is **formal** and **context-free**: it
does not depend on context to be interpreted.

> **Essential property:** a computable model not only specifies the *what*, it also **implements
> the *how*.** This is what separates software from other models (a diagram, an equation, a
> blueprint): software *runs*. If it does not execute, it is not software — it is a description of
> software.

---

## Principles for development

Apply these directly when designing and writing code.

1. **Treat software as a model, not as instructions.** The definition you adopt determines how you
   design. "Instructions" gives no design criterion; "model" does.
2. **Good software is a good model.** Before asking whether code is elegant, ask whether it
   **faithfully represents** the domain.
3. **Organize code around the domain, not the framework.** When in doubt, mirror the structure of
   the business, not the conventions of the tooling.
4. **Slice reality on purpose.** Model only the relevant business domain; do not try to represent
   all of reality.
5. **A model represents; it is not the thing.** Preserve the distinction between a domain thing and
   its representation in code.
6. **Specify the *what* and implement the *how*.** A model of software must be executable. If it
   cannot run, it is a diagram or an idea, not software.
7. **Move from ambiguous to formal deliberately.** Design *is* the act of translating an arbitrary,
   ambiguous, context-dependent domain into a formal, context-free model. The decisions made in
   that translation are the design.

---

## Glossary

| Term              | Definition                                                              |
| ----------------- | ----------------------------------------------------------------------- |
| **Software**      | A computable model of a problem domain of reality.                      |
| **Reality**       | A set of things.                                                        |
| **Thing**         | Anything about which something can be said.                             |
| **Problem domain**| A slice of reality representing the business being modeled.             |
| **Model**         | A representation of the knowledge built about a domain.                 |
| **Computable**    | Executable on a Turing machine; formal and context-free.               |
| **Good software** | A good model of the domain, organized after the domain's structure.    |

---

## Sources

- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — course on
  object-oriented software design heuristics.
- Alan Turing, *On Computable Numbers, with an Application to the Entscheidungsproblem* (1936) —
  the Turing machine and the notion of computability.
- Alonzo Church, *An Unsolvable Problem of Elementary Number Theory* (1936) — the lambda calculus;
  with Turing, the Church–Turing thesis.
- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*
  (Addison-Wesley, 2003) — modeling the business domain; ubiquitous language; model-driven design.
- Bertrand Meyer, *Object-Oriented Software Construction*, 2nd ed. (Prentice Hall, 1997) —
  software as a seamless model of real-world entities.
- Peter Naur, *Programming as Theory Building* (1985) — software as the theory a team builds about
  a domain.
- Frederick P. Brooks, *No Silver Bullet — Essence and Accidents of Software Engineering* (1986) —
  the essential difficulty is building the conceptual model.
- Arthur J. Riel, *Object-Oriented Design Heuristics* (Addison-Wesley, 1996) — heuristics for
  organizing object models.
