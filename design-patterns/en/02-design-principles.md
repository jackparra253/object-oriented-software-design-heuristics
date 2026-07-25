# Software Design Principles

> **Purpose of this document.** State the universal design principles that motivate the patterns:
> three foundational principles and the five SOLID principles. Read them as heuristics — they guide,
> they do not command. The patterns in the catalog are largely concrete applications of these ideas.

---

## Working definition

> **Design principles are universal guidelines for making software flexible, stable, and easy to
> understand.** They describe *what good design looks like*; patterns are *reusable ways to achieve
> it*.

Good design is often characterized by three qualities:

- **Code reuse** — reusing existing code cuts cost and time, but usually raises coupling; patterns
  help reuse without tight coupling.
- **Extensibility** — change is the only constant; design so new requirements are *added*, not
  patched in.
- **Loose coupling** — the fewer things each part knows about others, the easier the system is to
  change.

---

## Three foundational principles

### 1. Encapsulate what varies

> Identify the aspects of your program that vary and separate them from what stays the same.

The goal is to isolate the parts that change so a change affects less code. You can encapsulate
variation **at the method level** (extract the changing logic into its own method) or **at the class
level** (extract it into its own class). This minimizes the "blast radius" of a change and keeps the
rest of the system stable.

*Example.* Moving tax calculation out of an `Order` class into a dedicated object means changing tax
rules never touches `Order`.

### 2. Program to an interface, not an implementation

> Depend on abstractions, not on concrete classes.

Your code is more flexible when it collaborates through interfaces (abstract types) rather than
concrete classes. Then any object that satisfies the interface is interchangeable, and you can add
new implementations without touching the client. This is the backbone of most patterns.

### 3. Favor composition over inheritance

> Build behavior by combining objects rather than by extending classes.

Inheritance is the most obvious way to reuse code, but it has costs: a subclass can't reduce the
superclass interface, overridden methods must stay compatible, inheritance breaks encapsulation, and
deep hierarchies become rigid. **Composition** — having an object hold references to others and
delegate work — is usually more flexible: you can swap collaborators at runtime and change behavior
without rewiring a class hierarchy.

---

## SOLID principles

Five principles introduced by Robert C. Martin to make designs more understandable, flexible, and
maintainable. Treat them as heuristics, not laws — pursued dogmatically they can produce needless
complexity.

### S — Single Responsibility Principle

> A class should have only one reason to change.

Keep each class focused on a single responsibility. When a class does several things, a change to one
concern risks breaking the others.

### O — Open/Closed Principle

> Classes should be open for extension but closed for modification.

You should be able to add new behavior (extend) without altering existing, working code (modify).
This maps directly to the modeling ideal of *adding* a new domain case rather than patching. The
Strategy pattern is a classic way to achieve it.

### L — Liskov Substitution Principle

> Subtypes must be substitutable for their base types.

A subclass must be usable anywhere its parent is expected, without breaking the client. Requirements
include: parameter types no stricter, return types no wider, no new exceptions the parent doesn't
throw, and preconditions not strengthened / postconditions not weakened.

### I — Interface Segregation Principle

> Clients shouldn't be forced to depend on methods they don't use.

Break wide, "fat" interfaces into narrower, more specific ones, so a class implements only the
methods that make sense for it.

### D — Dependency Inversion Principle

> High-level classes shouldn't depend on low-level classes. Both should depend on abstractions.

Depend on abstractions rather than concrete implementations, so business logic (high-level) is not
tied to details (low-level). Combined with "program to an interface", this keeps the important parts
of a system stable while details change.

---

## Principles for development

1. **Isolate what changes.** Before choosing a pattern, ask *what varies here?* and encapsulate it.
2. **Depend on abstractions.** Program to interfaces so collaborators are interchangeable.
3. **Prefer composition** for flexible reuse; use inheritance for genuine "is-a" relationships.
4. **Apply SOLID as guidance,** not as a checklist to satisfy mechanically.
5. **These principles serve the model.** They exist to keep the model faithful, habitable, and cheap
   to change — not for their own sake.

---

## Glossary

- **Encapsulate what varies** — separate the changing parts from the stable parts.
- **Program to an interface** — depend on an abstract type, not a concrete class.
- **Composition** — building behavior by holding and delegating to other objects.
- **SOLID** — Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation,
  Dependency Inversion.
- **Coupling** — the degree to which one part depends on another; loose coupling is the goal.

---

## Sources

- Alexander Shvets, *Dive Into Design Patterns*, Refactoring.Guru, 2022 — "Features of Good Design",
  "Design Principles", and "SOLID Principles".
- Robert C. Martin, *Agile Software Development, Principles, Patterns, and Practices*, Prentice Hall,
  2002.
