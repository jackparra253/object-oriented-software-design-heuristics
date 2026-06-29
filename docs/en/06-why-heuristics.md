# Why Heuristics, Not Principles or Rules?

> **Purpose of this document.** This sets the stance for applying every piece of design guidance
> that follows. It defines what a heuristic is, how it differs from a principle and a rule, and how
> to apply such guidance. Read the design guidance in this repo as *heuristics*: apply them with
> critical judgment, in context, expecting exceptions.

---

## Working definition

The design guidance here is framed as **heuristics**, deliberately — not as principles, laws, or
rules.

> **A heuristic is a rule that must be analyzed in context. It can have exceptions; it is not always
> worth applying.**

A heuristic is a strategy, method, or criterion that helps solve problems — a piece of empirical,
common-sense advice that has been observed to work in many cases, but is not guaranteed to work
always and is not mandatory to follow.

---

## Principle vs. rule vs. heuristic

| Concept       | What it claims                                                                 | How to treat it                          |
| ------------- | ------------------------------------------------------------------------------ | ---------------------------------------- |
| **Principle** | A fundamental truth or proposition serving as the base of a system of belief, behavior, or reasoning. | A foundation you reason *from*.           |
| **Rule / Law**| Something that always holds and must be followed.                              | Apply unconditionally.                   |
| **Heuristic** | A context-dependent, empirical guideline that usually helps but can have exceptions. | Apply with judgment; question it in context. |

The key distinction: a **rule** is meant to be obeyed; a **heuristic** is meant to be *weighed*. It
helps you find an effective, efficient solution, but you decide — for this context — whether it
applies.

---

## "Principles" are usually heuristics

Much of what the industry calls "principles" behaves like heuristics. The SOLID "principles" are a
clear example. As their own author, Robert C. Martin, puts it:

> The SOLID principles are not rules. They are not laws. They are not perfect truths. … This is a
> good principle, it is good advice, but it's not a pure truth, nor a rule.

And:

> These principles are heuristics. They are common-sense solutions to common problems. … like any
> heuristic, they are empirical in nature. They have been observed to work in many cases; but there
> is no proof that they always work, nor any proof that they should always be followed.

This raises two useful questions to keep in mind about any named "principle":

- If it is a heuristic, why was it called a principle?
- Was it known from the start to be a heuristic, or only recognized as one later?

The point is not to dismiss such guidance, but to read it for what it is.

---

## The stance: critical thinking over dogma

Treat all design guidance — including everything in this repo — as heuristics:

- **Not marketing.** A catchy name or acronym does not make guidance a law.
- **Not dogma.** Following a rule because "that's the rule" is not design.
- **Critical thinking.** For each situation, ask whether the heuristic helps *here*, what it costs,
  and whether this is one of its exceptions.

A heuristic earns its place by improving the model in context, not by authority.

---

## Principles for development

Apply these directly.

1. **Read design guidance as heuristics.** Including the heuristics in this repo: they are advice
   observed to work, not laws.
2. **Analyze every heuristic in context.** Ask whether it applies *here* before applying it; the
   same heuristic can be right in one context and wrong in another.
3. **Expect exceptions.** A case that violates a heuristic is not automatically a defect; it may be a
   legitimate exception. Decide deliberately.
4. **Do not follow a heuristic dogmatically.** "It's the rule" is not a justification; the
   justification is that it improves *this* model.
5. **Distrust authority and marketing.** A name, acronym, or famous author does not upgrade a
   heuristic to a law.
6. **Weigh costs and benefits.** Apply a heuristic when its benefit in context outweighs its cost,
   not by default.
7. **Think critically.** The goal is good judgment about the model, not compliance with a checklist.

---

## Glossary

| Term          | Definition                                                                       |
| ------------- | -------------------------------------------------------------------------------- |
| **Principle** | A fundamental truth or proposition used as the base for reasoning or behavior.    |
| **Rule / law**| A statement that always holds and must be followed.                              |
| **Heuristic** | A context-dependent, empirical guideline that usually helps but can have exceptions. |
| **Dogma**     | Following guidance as unquestionable truth, regardless of context.               |
| **Critical thinking** | Judging, in context, whether and how a heuristic should be applied.       |

---

## Sources

- Robert C. Martin (Uncle Bob) — on SOLID as heuristics, not rules: e.g. *Clean Architecture*
  (Prentice Hall, 2017) and his writings on the SOLID principles.
- George Pólya, *How to Solve It* (Princeton University Press, 1945) — the classic treatment of
  heuristics in problem solving.
- Billy Vaughn Koen, *Discussion of the Method: Conducting the Engineer's Approach to Problem
  Solving* (Oxford University Press, 2003) — engineering as the use of heuristics.
- Oxford English Dictionary — definition of *principle*: a fundamental truth or proposition serving
  as the base for a system of belief, behavior, or a chain of reasoning.
- Arthur J. Riel, *Object-Oriented Design Heuristics* (Addison-Wesley, 1996) — design guidance
  explicitly framed as heuristics.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — course on
  object-oriented software design heuristics.
