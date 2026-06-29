# Software Development as a Learning Process

> **Purpose of this document.** This is foundational context for how to approach the *activity* of
> building software. It defines software development as a learning process and draws out what that
> means for how to plan, work, and structure feedback. Apply these whenever you organize work,
> estimate, iterate, or onboard a domain.

---

## Working definition

Building software is not principally manufacturing, and not a strictly linear engineering pipeline.
The most accurate analogy is a **learning process**:

> **Software development is the process of learning a problem domain and formalizing that
> knowledge into a computable model.**

Because the output is a computable model expressed in source code, developing it means *acquiring
and organizing knowledge about a domain* — and continually correcting that knowledge against
reality.

---

## The learning cycle

Development runs a continuous loop between the **problem domain** (`D`, expressed in natural,
ambiguous, contextual language) and the **model** (`M`, expressed in a formal programming language),
mediated by the developer's **mental model**:

1. **Observe** the domain.
2. Form/refine a **mental model** of it.
3. **Project** that mental model into the formal model (code).
4. **Reflect** on the resulting model against what was intended.
5. **Learn** — feed corrections back into observation of the domain.

This is **learning through the formalization of knowledge**: moving a concept from the natural
language of the domain into the formal, executable language of the model, and using the gaps
revealed to learn more.

---

## What development actually involves

- The problem domain is usually specified in **ambiguous, contextual language** (natural language).
- Development therefore means **disambiguating and de-contextualizing** the domain knowledge.
- It also means making the domain experts' **implicit, internalized knowledge explicit and
  external** — written down as a running model.
- **Change is essential to software, not accidental**, because over time:
  - the problem domain changes,
  - our understanding of the domain changes, and
  - the way we model what we understand changes.

Because change is essential, treat *learning capacity* — the ability to keep understanding and
adapting the system — as a first-class design goal. Managing complexity is what keeps that capacity
alive.

---

## Properties of the process

Software development, seen as learning, is:

- **Iterative** — the loop runs many times; understanding is revisited, not produced once.
- **Incremental** — knowledge accrues in steps; the model grows piece by piece.
- **Grounded in concrete facts** — knowledge is generated from real observations and working code,
  not from speculation.
- **Organized** — the knowledge generated must be deliberately structured, or it is lost.

An engineering approach to this is the **practical application of a scientific, empirical method**:
characterize (observe), hypothesize (propose a model), predict, and experiment (test). The roots of
becoming good at it are **iteration, feedback, incrementalism, experimentation, and empiricism.**

**Immediate feedback** is fundamental: fast feedback lets you build intuition, "play computer" in
your head, and find errors sooner. The shorter the feedback loop, the faster the learning.

---

## Principles for development

Apply these directly.

1. **Treat development as learning, not manufacturing.** The goal of each step is to *understand*
   the domain better and capture that understanding in the model.
2. **Work iteratively and incrementally.** Expect to revisit decisions; grow the model in small,
   verifiable steps rather than one big upfront design.
3. **Ground knowledge in concrete facts.** Prefer observations and running code over speculation;
   let reality correct the model.
4. **Make tacit domain knowledge explicit.** Disambiguate and de-contextualize the domain; write
   the experts' implicit knowledge into the model where it can be checked.
5. **Design for change as the normal case.** The domain, your understanding, and your modeling will
   all change; structure the system so change is cheap.
6. **Protect learning capacity by managing complexity.** Keep the system understandable so the team
   can keep learning and adapting; sustainable learning is the point.
7. **Shorten the feedback loop.** Optimize for immediate feedback (fast tests, a live REPL/console,
   quick runs) — it is the engine of the whole process.
8. **Apply the scientific method.** Characterize, hypothesize, predict, experiment — pragmatically,
   not with false precision.
9. **Organize the knowledge you generate.** Capture and structure what is learned in the model and
   its names, or it will be lost between iterations.

---

## Glossary

| Term                       | Definition                                                                        |
| -------------------------- | --------------------------------------------------------------------------------- |
| **Software development**   | The process of learning a domain and formalizing it into a computable model.      |
| **Learning cycle**         | Observe → mental model → project → reflect → learn, between domain and model.      |
| **Mental model**           | The developer's internal understanding that mediates domain and code.             |
| **Formalization of knowledge** | Moving a concept from ambiguous natural language into a formal, executable form. |
| **Essential change**       | Change inherent to software (domain, understanding, and modeling all shift).       |
| **Immediate feedback**     | Fast response that accelerates learning and error detection.                       |
| **Learning capacity**      | The sustained ability of a team to understand and adapt the system.               |

---

## Sources

- Frederick P. Brooks, *The Computer Scientist as Toolsmith II* (Communications of the ACM, March
  1996) — the scientist builds in order to learn; the engineer learns in order to build.
- Margaret Hamilton — coined the term "software engineering" to distinguish it from hardware and
  other engineering.
- *Software Engineering* — Report on a NATO Science Committee conference (Garmisch, 1968), eds.
  Peter Naur and Brian Randell; Mary Shaw, *Prospects for an Engineering Discipline of Software*
  (IEEE Software, 1990).
- Edsger W. Dijkstra, *EWD1305* — a skeptical view of "software engineering"; seeing a program as a
  formula. <http://www.cs.utexas.edu/users/EWD/transcriptions/EWD13xx/EWD1305.html>.
- Edward Yourdon — software engineering as a set of practical methods for the error-prone reality of
  projects, rather than an academic science.
- Richard W. Hamming, *The Art of Doing Science and Engineering* — "In science, if you know what you
  are doing, you should not be doing it; in engineering, if you do not know what you are doing, you
  should not be doing it."
- David Farley, *Modern Software Engineering* (Addison-Wesley, 2021) — engineering as the practical
  application of an empirical, scientific approach; iteration, feedback, incrementalism,
  experimentation, empiricism.
- Bret Victor, *Inventing on Principle* (2012) — the power of immediate feedback.
  <http://vimeo.com/36579366>.
- Harold Abelson & Gerald Jay Sussman, *Structure and Interpretation of Computer Programs* (MIT) —
  on the nature of computer "science". <http://groups.csail.mit.edu/mac/classes/6.001/abelson-sussman-lectures/>.
- Peter Naur, *Programming as Theory Building* (1985) — development as building a theory of the
  domain.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — course on
  object-oriented software design heuristics.
