# Creational Patterns

> **Purpose of this document.** Define the five creational patterns. Creational patterns provide
> object-creation mechanisms that increase flexibility and reuse of existing code. For each: intent,
> the problem it solves, and when to apply it. Read them as heuristics — reach for one only when its
> problem is real.

---

## Working definition

> **Creational patterns abstract the process of object creation,** so code depends less on the
> concrete classes it instantiates and more on the shape it needs.

The five: **Factory Method**, **Abstract Factory**, **Builder**, **Prototype**, **Singleton**.

---

## Factory Method

**Intent.** Provides an interface for creating objects in a superclass, but allows subclasses to
alter the type of objects that will be created.

**Problem it solves.** Client code needs to create objects but should not be tied to their concrete
classes. Factory Method replaces direct `new` calls with calls to a special *factory method* that
subclasses can override.

**Apply when:**

- You don't know beforehand the exact types your code should work with.
- You want to let users of a library or framework extend its internal components.
- You want to reuse existing objects instead of rebuilding them each time.

---

## Abstract Factory

**Intent.** Lets you produce **families of related objects** without specifying their concrete
classes.

**Problem it solves.** You must create sets of objects that are meant to be used together (e.g. a
matching chair, sofa, and table in a given style) while keeping the client independent of the
concrete variants.

**Apply when:**

- Your code needs to work with various families of related products.
- You want to enforce that products from one family are used together and not mixed with another.

---

## Builder

**Intent.** Lets you construct **complex objects step by step**, producing different types and
representations of an object using the same construction code.

**Problem it solves.** A constructor with many parameters (a "telescoping constructor") is hard to
read and use. Builder moves construction into a separate object and builds the product in a series of
steps, calling only the ones you need. An optional **Director** class defines reusable construction
sequences.

**Apply when:**

- You want to avoid a constructor with a large number of optional parameters.
- You need to create different representations of the same product.
- You need to construct composite trees or other complex objects step by step.

*Relation to the heuristics.* Builder is the standard tool the heuristics recommend for **complete
object construction** ([H2](../../docs/en/08-h2-complete-objects.md)) when construction is complex —
the object is still valid and complete once `build()` returns.

---

## Prototype

**Intent.** Lets you **copy existing objects** without making your code dependent on their classes.

**Problem it solves.** Cloning an object from the outside is hard: some fields may be private, and the
client would depend on the object's class. Prototype delegates cloning to the objects themselves via
a common `clone` interface, so copying is independent of concrete classes.

**Apply when:**

- Your code shouldn't depend on the concrete classes of objects you need to copy.
- You want to reduce subclasses that only differ in the way they initialize their objects.

---

## Singleton

**Intent.** Ensures a class has **only one instance**, while providing a **global access point** to
it.

**Problem it solves.** Some resources (a shared configuration, a database connection pool) should
have exactly one instance. Singleton makes the constructor private and exposes a static creation
method that returns the single instance.

**Apply when:**

- A class must have exactly one instance available to all clients.

**Caveats (read carefully).** Singleton violates the Single Responsibility Principle (it controls both
its own creation and its lifecycle), can mask bad design by letting components know too much about each
other, needs special handling in multithreaded environments, and makes unit testing harder. It is the
most frequently *overused* pattern — often a global variable in disguise. Prefer passing dependencies
explicitly (dependency injection) when you can.

---

## Principles for development

1. **Reach for a creational pattern only when creation is genuinely a pain point** (unknown types,
   families, complex construction, controlled copying, single instance).
2. **Start simple.** Many designs begin with Factory Method and evolve toward Abstract Factory,
   Prototype, or Builder as flexibility is actually needed.
3. **Prefer Builder over telescoping constructors,** while keeping objects complete and valid on
   creation ([H2](../../docs/en/08-h2-complete-objects.md), [H3](../../docs/en/09-h3-valid-objects.md)).
4. **Be skeptical of Singleton.** Consider explicit dependency injection first.

---

## Glossary

- **Factory method** — a method a subclass overrides to decide which concrete product to create.
- **Product family** — a set of related objects meant to be used together (Abstract Factory).
- **Director** — an optional class that encapsulates a reusable Builder construction sequence.
- **Clone** — a copy an object makes of itself (Prototype).
- **Global access point** — a single, well-known way to reach the sole instance (Singleton).

---

## Sources

- Alexander Shvets, *Dive Into Design Patterns*, Refactoring.Guru, 2022 — "Creational Design
  Patterns".
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable
  Object-Oriented Software*, Addison-Wesley, 1994.
