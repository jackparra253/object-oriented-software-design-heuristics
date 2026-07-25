# Overview — Design Patterns

> **Purpose of this document.** A short tour of the whole catalog: what a design pattern is, why the
> classic (Gang of Four) patterns are grouped into three families, and a one-line intent for each of
> the 23 patterns. Read this first; each family is developed in its own chapter, linked inline. The
> closing **Principles for development** section is the short checklist to keep open while you design.

---

## Part I — What a pattern is (and is not)

A **design pattern** is a general, reusable solution to a commonly occurring problem in software
design. It is not a finished piece of code you paste in; it is a **description or blueprint** for how
to solve a problem, which you adapt to your program. (See
[01 — What Is a Design Pattern?](01-what-is-a-design-pattern.md).)

Patterns and the [design heuristics](../../docs/en/00-overview.md) work together: the heuristics tell
you how to build a *faithful model* of the domain; patterns give you *named, proven structures* for
recurring design problems. Like the heuristics, patterns are **tools, not rules** — apply each in
context, weigh cost vs. benefit, and never introduce a pattern where the problem does not exist.

---

## Part II — Design principles behind the patterns

Most patterns are concrete applications of a few universal principles (see
[02 — Software Design Principles](02-design-principles.md)):

- **Encapsulate what varies** — identify the aspects that change and separate them from what stays
  the same, so changes affect less code.
- **Program to an interface, not an implementation** — depend on abstractions, so collaborators are
  interchangeable.
- **Favor composition over inheritance** — build behavior by combining objects rather than by growing
  deep class hierarchies.
- **SOLID** — Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation,
  Dependency Inversion.

---

## Part III — The three families

### Creational patterns

Provide object-creation mechanisms that increase flexibility and reuse of existing code. (See
[03 — Creational Patterns](03-creational-patterns.md).)

- **Factory Method** — provides an interface for creating objects in a superclass, but lets
  subclasses alter the type of objects that will be created.
- **Abstract Factory** — lets you produce families of related objects without specifying their
  concrete classes.
- **Builder** — lets you construct complex objects step by step, producing different types and
  representations with the same construction code.
- **Prototype** — lets you copy existing objects without making your code depend on their classes.
- **Singleton** — ensures a class has only one instance, while providing a global access point to it.

### Structural patterns

Explain how to assemble objects and classes into larger structures while keeping them flexible and
efficient. (See [04 — Structural Patterns](04-structural-patterns.md).)

- **Adapter** — allows objects with incompatible interfaces to collaborate.
- **Bridge** — splits a large class (or set of related classes) into two hierarchies — abstraction
  and implementation — developed independently.
- **Composite** — composes objects into tree structures and lets you work with them as if they were
  individual objects.
- **Decorator** — attaches new behaviors to objects by placing them inside wrapper objects.
- **Facade** — provides a simplified interface to a library, framework, or complex set of classes.
- **Flyweight** — fits more objects into RAM by sharing common parts of state between them.
- **Proxy** — provides a substitute or placeholder that controls access to another object.

### Behavioral patterns

Concerned with algorithms and the assignment of responsibilities between objects. (See
[05 — Behavioral Patterns](05-behavioral-patterns.md).)

- **Chain of Responsibility** — passes requests along a chain of handlers; each decides to process it
  or pass it on.
- **Command** — turns a request into a stand-alone object, enabling queuing, logging, and undo.
- **Iterator** — traverses elements of a collection without exposing its underlying representation.
- **Mediator** — reduces chaotic dependencies by forcing objects to collaborate via a mediator.
- **Memento** — saves and restores an object's previous state without revealing its implementation.
- **Observer** — defines a subscription mechanism to notify multiple objects about events.
- **State** — lets an object alter its behavior when its internal state changes.
- **Strategy** — defines a family of interchangeable algorithms, each in its own class.
- **Template Method** — defines the skeleton of an algorithm in a superclass, letting subclasses
  override specific steps.
- **Visitor** — separates algorithms from the objects on which they operate.

---

## Principles for development

Apply these directly (as heuristics, not rules).

1. **Reach for a pattern only when the problem exists.** A pattern introduced without its problem is
   accidental complexity; it hurts the descriptive axis of the model.
2. **Learn the intent, not just the diagram.** Two patterns can share a structure yet solve different
   problems; the intent is what matters.
3. **Prefer the simplest option first.** Many designs start simple (e.g. Factory Method) and evolve
   toward more flexible patterns only as pressure appears.
4. **Patterns serve the model.** They are a means to a faithful, habitable model — never the goal.
5. **Name for the domain.** When a pattern appears in your code, still name classes for what they
   represent in the domain, not merely after the pattern.

---

## Glossary

- **Design pattern** — a reusable, general blueprint for a recurring design problem.
- **Intent** — the core problem a pattern solves, stated in one or two sentences.
- **Gang of Four (GoF)** — the four authors of *Design Patterns: Elements of Reusable
  Object-Oriented Software* (1994), which cataloged these 23 patterns.

---

## Sources

- Alexander Shvets, *Dive Into Design Patterns*, Refactoring.Guru, 2022.
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable
  Object-Oriented Software*, Addison-Wesley, 1994.
