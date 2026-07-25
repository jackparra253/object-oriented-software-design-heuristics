# What Is a Design Pattern?

> **Purpose of this document.** Define what a design pattern is, what it is made of, why patterns are
> worth learning, and how they relate to the design heuristics in this repository. Read it before the
> catalog chapters.

---

## Working definition

> **A design pattern is a typical, reusable solution to a commonly occurring problem in software
> design.**

A pattern is **not** a specific piece of code. It is a general **concept** or blueprint for solving a
particular problem, which you tailor to the details of your own program. You cannot just copy a
pattern into your program the way you can copy a function from a library; you follow the pattern's
idea and adapt it to your situation.

Patterns are often confused with algorithms. An **algorithm** is a clear set of steps that achieves a
goal (like a cooking recipe). A **pattern** is more like a blueprint: it shows the result and its
features, but the exact steps of implementation are up to you.

---

## What a pattern description contains

Patterns are usually described formally so they can be reproduced in many contexts. A typical
description includes:

- **Intent** — briefly describes the problem and the solution.
- **Motivation** — explains the problem and how the pattern makes solving it possible.
- **Structure** — the classes involved and how they relate.
- **Applicability** — when the pattern is (and is not) a good fit.
- **Code example** — the solution shown in a concrete language.

Some catalogs also list applicability, implementation steps, and relations with other patterns.

---

## The classification

The classic catalog contains **23 patterns**, grouped into three families by intent:

1. **Creational** — object-creation mechanisms that increase flexibility and reuse.
2. **Structural** — how to assemble objects and classes into larger structures.
3. **Behavioral** — algorithms and the assignment of responsibilities between objects.

The most fundamental and low-level patterns are often called **idioms** (they apply to a single
language). The most universal, high-level ones are **architectural patterns** and can be implemented
in nearly any language.

---

## Why learn patterns?

- **They are a toolkit of tested solutions** to common problems. Even if you never meet the exact
  problem, knowing patterns teaches you to solve design problems using object-oriented principles.
- **They are a common language.** Saying "use a Factory" communicates a whole design in two words,
  provided your teammates know the pattern.

But learning patterns carries a risk: applying them where they are not needed. A pattern used without
its problem is **accidental complexity**. This is exactly why, in this repository, patterns are
treated the same way as [heuristics](../../docs/en/06-why-heuristics.md): apply each in context,
expect exceptions, and weigh cost vs. benefit.

---

## How patterns relate to the heuristics

- The [heuristics (H1–H6)](../../docs/en/00-overview.md) govern **faithful modeling** — one object
  per entity, complete and valid objects, no null, immutability, encapsulation.
- **Patterns** give **named structures** for recurring design pressures (creation, composition,
  communication).
- Patterns *serve* the model: reach for one only when it makes the model clearer or the design more
  flexible, never as an end in itself.

---

## Principles for development

1. **A pattern is a blueprint, not code.** Adapt it; don't copy it blindly.
2. **Know the intent first.** The problem a pattern solves matters more than its class diagram.
3. **Use patterns as shared vocabulary,** but only where the team shares the vocabulary.
4. **No problem, no pattern.** Introducing a pattern without its problem adds complexity for nothing.

---

## Glossary

- **Design pattern** — a general, reusable blueprint for a recurring design problem.
- **Idiom** — a low-level pattern specific to one programming language.
- **Architectural pattern** — a high-level, language-agnostic pattern.
- **Intent** — the short statement of the problem a pattern solves.
- **Algorithm vs. pattern** — an algorithm is a fixed set of steps; a pattern is a blueprint whose
  implementation you decide.

---

## Sources

- Alexander Shvets, *Dive Into Design Patterns*, Refactoring.Guru, 2022 — "What's a Design Pattern?"
  and "Why Should I Learn Patterns?".
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable
  Object-Oriented Software*, Addison-Wesley, 1994.
