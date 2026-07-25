# Behavioral Patterns

> **Purpose of this document.** Define the eleven behavioral patterns. Behavioral patterns are
> concerned with algorithms and the assignment of responsibilities between objects. For each: intent,
> the problem it solves, and when to apply it. Read them as heuristics.

---

## Working definition

> **Behavioral patterns describe how objects communicate and distribute responsibilities,** improving
> flexibility in carrying out communication.

The eleven: **Chain of Responsibility**, **Command**, **Iterator**, **Mediator**, **Memento**,
**Observer**, **State**, **Strategy**, **Template Method**, **Visitor**.

---

## Chain of Responsibility

**Intent.** Lets you pass requests along a **chain of handlers**. On receiving a request, each handler
decides either to process it or to pass it to the next handler.

**Apply when:** several objects may handle a request and the handler isn't known in advance; you want
to process requests in a particular order; or the set of handlers changes at runtime.

---

## Command

**Intent.** Turns a request into a **stand-alone object** that contains all information about the
request. This lets you pass requests as method arguments, delay or queue execution, and support
undoable operations.

**Apply when:** you want to parametrize objects with operations, queue or schedule operations, or
implement reversible (undo/redo) operations.

---

## Iterator

**Intent.** Lets you **traverse elements** of a collection without exposing its underlying
representation (list, stack, tree, etc.).

**Apply when:** your collection has a complex internal structure you want to hide; you want to support
multiple traversals; or you want a uniform traversal interface over different collections.

---

## Mediator

**Intent.** Lets you reduce chaotic dependencies between objects. It restricts direct communication
and forces objects to collaborate only via a **mediator** object.

**Apply when:** components are tightly coupled by many direct connections; you can't reuse a component
because it depends on too many others; or you're subclassing just to reuse behavior across contexts.

---

## Memento

**Intent.** Lets you **save and restore** the previous state of an object without revealing the
details of its implementation.

**Apply when:** you want to produce snapshots of an object's state (for undo, history, or
transactions) while preserving encapsulation ([H6](../../docs/en/12-h6-encapsulation.md)).

---

## Observer

**Intent.** Lets you define a **subscription mechanism** to notify multiple objects about any events
that happen to the object they're observing.

**Apply when:** a change to one object requires changing others and you don't know how many; or some
objects must observe others only for a limited time or under changing conditions.

---

## State

**Intent.** Lets an object **alter its behavior when its internal state changes**. It appears as if
the object changed its class.

**Apply when:** an object behaves very differently depending on its state and has many states; or a
class is littered with large conditionals that depend on its state. Extract each state into its own
class.

---

## Strategy

**Intent.** Lets you define a **family of algorithms**, put each into a separate class, and make their
objects **interchangeable**.

**Apply when:** you want to switch algorithms at runtime; you have many similar classes differing only
in behavior; or you want to isolate business logic from the details of how a task is done. This is the
canonical Open/Closed pattern.

---

## Template Method

**Intent.** Defines the **skeleton of an algorithm** in a superclass but lets subclasses override
specific steps of the algorithm without changing its structure.

**Apply when:** subclasses should extend only particular steps of an algorithm, not its overall
structure; or you have several classes with almost identical algorithms and want to remove the
duplication.

---

## Visitor

**Intent.** Lets you **separate algorithms** from the objects on which they operate.

**Apply when:** you need to perform an operation on all elements of a complex object structure (e.g. a
tree); you want to move unrelated behavior out of the element classes; or a behavior makes sense only
for some classes in a hierarchy.

---

## Principles for development

1. **These patterns manage collaboration.** Choose them to clarify *who talks to whom* and *who owns
   which responsibility*.
2. **Prefer Strategy/State over sprawling conditionals.** Replacing big `if/switch` blocks with
   polymorphism keeps the model habitable and open for extension.
3. **Respect encapsulation.** Memento and Iterator exist precisely to expose behavior, not internal
   state ([H6](../../docs/en/12-h6-encapsulation.md)).
4. **"Tell, don't ask" aligns with these patterns.** Send a message for what you need rather than
   pulling data out and acting on it externally.

---

## Glossary

- **Handler** — a link in a Chain of Responsibility.
- **Command / Receiver** — the request-as-object and the object that performs the work.
- **Iterator** — an object that traverses a collection.
- **Mediator** — the hub that coordinates communication between components.
- **Memento** — a snapshot of an object's state.
- **Subject / Observer** — the watched object and its subscribers.
- **State / Strategy** — an interchangeable behavior extracted into its own class.

---

## Sources

- Alexander Shvets, *Dive Into Design Patterns*, Refactoring.Guru, 2022 — "Behavioral Design
  Patterns".
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable
  Object-Oriented Software*, Addison-Wesley, 1994.
