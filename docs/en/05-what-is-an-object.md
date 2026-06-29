# What Is an Object?

> **Purpose of this document.** This is foundational context for designing with objects. It defines
> what an object *is* and what defines it, and lists the questions to answer when modeling one.
> Apply this whenever you create a class, decide what an object should do, or judge whether an
> abstraction is well-formed.

---

## Working definition

An object is **not** "code + data". That framing is wrong: it describes the implementation
mechanism, not what an object is.

> **An object is the essential representation of an entity of the problem domain.**

And the way it represents that entity is specific:

> **An object represents its entity through the messages it knows how to respond to.**

What defines an object is its **behavior — the set of messages it answers — not its internal data.**
Two objects with the same data but different protocols are different objects; the data is an
implementation detail behind the messages.

---

## Essence

The representation is **essential**, and *essence* means:

> **What makes something be what it is, and not something else.**

Modeling an object means capturing the **essence** of the domain entity — the messages that make it
*that* entity — and leaving out everything incidental. This is a deliberately minimalist standard:

> "Perfection is achieved not when there is nothing more to add, but when there is nothing left to
> take away." — Antoine de Saint-Exupéry

An object should respond to exactly the messages its essence requires: no accidental data exposure,
no operations the entity does not really have.

---

## The questions object design must answer

Designing with objects means answering two groups of questions.

### What do I model?

- **Which entities of reality must I represent?** Physical ones? Abstract ones? Both?

(Both physical and abstract entities are legitimate objects. If the domain talks about it, it can be
an object — see the definition of a *thing*: anything about which something can be said.)

### How do I model it?

- **What messages must the object respond to?** (its protocol / behavior)
- **Whom must the object know?** (its collaborators / relationships)
- **From when must the object represent the entity?** (its lifecycle — when it comes into being and
  starts standing for the entity)
- **How must the object "teach" what it represents?** (it should make its meaning legible through
  its protocol and names)

---

## Why "messages" and not "data"

Defining an object by the messages it answers, rather than by the data it holds, is what keeps the
model aligned with the domain and changeable:

- The **protocol** is the contract with the rest of the system; the **data** behind it can change
  freely as long as the messages still answer correctly.
- Thinking in messages forces you to ask *what the entity does/means* in the domain, not *how it is
  stored*.
- It preserves encapsulation: collaborators depend on what the object *responds*, never on what it
  *holds*.

---

## Principles for development

Apply these directly.

1. **Model objects as essential representations of domain entities, not as data records.** Start
   from "what entity is this?", not "what fields does it have?".
2. **Define objects by their messages.** An object *is* the protocol it answers; design that first,
   treat internal data as a hidden implementation detail.
3. **Capture the essence; remove the incidental.** Include only the messages the entity truly needs;
   strive for "nothing left to take away".
4. **Model both physical and abstract entities.** If the domain can talk about it, it can be an
   object.
5. **Decide each object's collaborators deliberately.** Be explicit about whom an object must know.
6. **Design the object's lifecycle.** Decide from when it validly represents its entity (it should
   represent it from creation onward).
7. **Make the object teach what it represents.** Use protocol and names so the object communicates
   its meaning without external explanation.

---

## Glossary

| Term            | Definition                                                                      |
| --------------- | ------------------------------------------------------------------------------- |
| **Object**      | The essential representation of an entity of the problem domain.                |
| **Entity**      | A thing in the domain that the object stands for (physical or abstract).        |
| **Message**     | A request an object knows how to respond to; the unit of its behavior.          |
| **Protocol**    | The full set of messages an object answers; what defines the object.            |
| **Essence**     | What makes something be what it is and not something else.                      |
| **Collaborator**| Another object that a given object must know to fulfill its responsibilities.   |

---

## Sources

- Alan Kay — on object orientation as messaging: the essence of objects is the messages they send
  and respond to, not their internal state. (E.g. *The Early History of Smalltalk*, 1993.)
- Rebecca Wirfs-Brock & Brian Wilkerson, *Object-Oriented Design: A Responsibility-Driven Approach*
  (OOPSLA, 1989); Wirfs-Brock & McKean, *Object Design* (2002) — objects defined by responsibilities
  and behavior.
- Antoine de Saint-Exupéry, *Terre des hommes* (1939) — "Perfection is achieved … when there is
  nothing left to take away."
- Eric Evans, *Domain-Driven Design* (Addison-Wesley, 2003) — modeling domain entities.
- Arthur J. Riel, *Object-Oriented Design Heuristics* (Addison-Wesley, 1996) — heuristics for what
  an object should know and do.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — course on
  object-oriented software design heuristics.
