# Structural Patterns

> **Purpose of this document.** Define the seven structural patterns. Structural patterns explain how
> to assemble objects and classes into larger structures while keeping those structures flexible and
> efficient. For each: intent, the problem it solves, and when to apply it. Read them as heuristics.

---

## Working definition

> **Structural patterns describe how to compose objects and classes into larger structures** without
> losing flexibility or efficiency.

The seven: **Adapter**, **Bridge**, **Composite**, **Decorator**, **Facade**, **Flyweight**,
**Proxy**.

---

## Adapter

**Intent.** Allows objects with **incompatible interfaces** to collaborate.

**Problem it solves.** You want to use an existing class, but its interface doesn't match what your
code expects (e.g. a library that returns XML when your code needs JSON). An adapter wraps one object
and translates calls into a form the other understands.

**Apply when:**

- You want to use an existing class whose interface is incompatible with your code.
- You want to reuse several existing subclasses that lack some common functionality.

---

## Bridge

**Intent.** Lets you split a large class (or a set of closely related classes) into **two separate
hierarchies — abstraction and implementation —** which can be developed independently.

**Problem it solves.** When a class varies along two independent dimensions (e.g. shape *and* color),
combining them with inheritance causes a combinatorial explosion of subclasses. Bridge moves one
dimension into a separate hierarchy and links the two by composition.

**Apply when:**

- You want to divide and organize a monolithic class that has several variants of some functionality.
- You need to extend a class in several orthogonal (independent) dimensions.

---

## Composite

**Intent.** Lets you compose objects into **tree structures** and then work with these structures as
if they were individual objects.

**Problem it solves.** You have part-whole hierarchies (e.g. boxes containing products and other
boxes) and want to treat leaves and containers uniformly. Composite defines a common interface for
both, so client code can call one method (e.g. `getPrice()`) on any node.

**Apply when:**

- You need to implement a tree-like object structure.
- You want client code to treat simple and complex elements uniformly.

---

## Decorator

**Intent.** Lets you attach **new behaviors** to objects by placing them inside special **wrapper**
objects that contain the behaviors.

**Problem it solves.** You want to add responsibilities to individual objects, dynamically, without
subclassing for every combination. A decorator implements the same interface as the object it wraps
and adds behavior before/after delegating to it; decorators can be stacked.

**Apply when:**

- You need to add responsibilities to objects at runtime without breaking client code.
- Extending behavior with inheritance would be awkward or impossible.

---

## Facade

**Intent.** Provides a **simplified interface** to a library, a framework, or any other complex set
of classes.

**Problem it solves.** A subsystem is complex and hard to use directly. A facade offers a small,
convenient interface that covers the most common use cases, hiding the subsystem's complexity from
clients.

**Apply when:**

- You need a simple interface to a complex subsystem.
- You want to layer your subsystems and reduce coupling between them.

---

## Flyweight

**Intent.** Lets you fit **more objects into the available RAM** by **sharing** common parts of state
between multiple objects instead of keeping all the data in each object.

**Problem it solves.** Huge numbers of similar objects exhaust memory because each duplicates
constant, shareable data. Flyweight splits state into **intrinsic** (shared, immutable) and
**extrinsic** (unique, passed in), so the shared part exists once.

**Apply when:**

- Your program must support a huge number of objects that barely fit in memory.
- Many objects contain duplicate state that can be extracted and shared.

---

## Proxy

**Intent.** Lets you provide a **substitute or placeholder** for another object. A proxy controls
access to the original object, allowing you to do something before or after the request reaches it.

**Problem it solves.** You want to control access to an object — for lazy initialization, caching,
access control, logging, or working with a remote object — without changing the object or its
clients. The proxy implements the same interface and forwards requests, adding behavior around them.

**Apply when:**

- Lazy initialization (virtual proxy) of a heavy object.
- Access control, logging, caching, or a local stand-in for a remote object.

---

## Principles for development

1. **Choose by intent, not by structure.** Adapter, Decorator, and Proxy all wrap an object, but they
   solve different problems (compatibility, added behavior, controlled access).
2. **Use Facade to tame complexity,** not to hide poor design permanently.
3. **Prefer composition** (Bridge, Decorator, Composite) over deep inheritance hierarchies.
4. **Flyweight is an optimization** — reach for it only when memory is a proven problem; keep shared
   state immutable ([H5](../../docs/en/11-h5-immutable-objects.md)).

---

## Glossary

- **Wrapper** — an object that encloses another and implements the same interface (Adapter,
  Decorator, Proxy).
- **Abstraction / Implementation** — the two hierarchies linked by a Bridge.
- **Leaf / Composite** — the simple and container nodes of a Composite tree.
- **Intrinsic / extrinsic state** — shared vs. unique state in Flyweight.
- **Subsystem** — the complex set of classes a Facade simplifies.

---

## Sources

- Alexander Shvets, *Dive Into Design Patterns*, Refactoring.Guru, 2022 — "Structural Design
  Patterns".
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable
  Object-Oriented Software*, Addison-Wesley, 1994.
