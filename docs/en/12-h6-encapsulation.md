# H6 — Don't Break Encapsulation

> **Purpose of this document.** This is a design heuristic (read it as a heuristic — see
> [why-heuristics](06-why-heuristics.md)): apply it in context, expecting exceptions. It names the
> property the earlier heuristics keep relying on — every time they said "don't break encapsulation"
> (in [H3](09-h3-valid-objects.md), [H4](10-h4-no-null.md), [H5](11-h5-immutable-objects.md)), this is
> what they meant. Apply it whenever you design an object's public face and how collaborators reach it.

---

## The heuristic

> **H6: Don't break encapsulation.**

Encapsulation groups, in a single object, both the data and the operations that affect that data, so
each object manages its own slice of the problem's complexity. The knowledge inside an object is
**hidden from the outside**: the object has a **public face** (*what* it can do and tell — how others
may interact with it) and a **private side** (*how* it does it). Other entities know only how to ask;
they cannot see or touch the internal representation.

This is **information hiding** (Parnas, 1972): "no part of a complex system should depend on the
internal details of any other part" (Ingalls). Abstraction and encapsulation are complementary —
abstraction is about the *observable behavior*, encapsulation is about *hiding the implementation*
that produces it, so an object is free to change its private side without affecting the rest of the
system. As David West puts it, the object's "personal integrity should not be violated"; in practice
encapsulation is **more a discipline than a barrier** — it is up to the *user* of an object to
respect it.

---

## Encapsulation is about responsibilities, not just hiding fields

The deepest framing: **to encapsulate is to assign responsibilities to objects correctly.**
Information hiding (the access-control mechanism) is only the part of encapsulation that remains once
you take the responsibilities away. So think about it through what goes wrong when you break it.

### What happens when you break it

1. **It creates coupling.** The caller now depends on the object's internal structure. (Coupling is
   *worse* in statically typed languages, where the dependency is on concrete types.)
2. **It strips responsibility from the right object.** Logic that belongs inside the object leaks
   out to its callers, producing **repeated code** everywhere that logic is needed.

*Example.* A `CreditCard` exposing its raw expiration so callers compare it themselves duplicates the
"is it expired?" logic across the system. Giving the card the responsibility — `isExpiredOn(date)` —
keeps it in one place.

---

## Techniques to not break encapsulation

- **Create one message for each thing you need from a collaborator — "Tell, Don't Ask".** Instead of
  asking for a collaborator's data and deciding outside, tell the collaborator to do it. Example:
  `card.isOwnedBy(person)` instead of pulling the owner out and comparing.
- **You cannot foresee every need — so make classes extensible.** It is impossible to predict every
  message a collaborator will ever need; being able to *extend* a class (e.g. add `isExpiredOn:`
  later) matters precisely because the original author couldn't anticipate it.

### When you must return a collaborator: mind the coupling

If a method returns an internal object:

- **If the returned object is immutable** ([H5](11-h5-immutable-objects.md)) → it *only* creates
  coupling.
- **If it is mutable** → it creates coupling **and** the owner loses control of changes (a caller can
  mutate `number` behind the card's back).

Techniques to minimize the damage (none of which removes the coupling):

1. Use immutable objects.
2. Return copies.
3. Wrap the object in an immutable wrapper.

---

## How languages help or hinder

A good object language should **favor encapsulation and not its rupture.** A language *hinders*
encapsulation when:

1. **Collaborators aren't private by default** — visibility modifiers (`public`/`package`/…) leave
   things publicly accessible. *Example: a typical Java `CreditCard` with exposed fields.*
2. **Encapsulation is per-class, not per-object** — a class can reach into the privates of *another
   instance* of the same class. This was an intentional design decision in C++ (the class, not the
   object, is the unit of protection — inherited from the Cambridge CAP system) and persists in
   TypeScript, Java, etc.

A language *helps* when collaborators are always private and encapsulation is **per object** (e.g.
Smalltalk, Ruby). Rough ranking from the course: **good** — Smalltalk, Ruby; **fair** — Java, Kotlin,
C#, C++, TypeScript; **poor** — Python (mitigated with `__var`), PHP (since 7.1), JavaScript
(mitigated with `#`).

### Encapsulation and subclassing

- **Subclassing always breaks the *superclass's* encapsulation** — a subclass depends on its parent's
  internals; an object is what its whole class hierarchy defines. (This is part of why Smalltalk ships
  the source code.)
- **Collaborators should be protected under subclassing** — a subclass needs disciplined, protected
  access, not a free-for-all.

---

## Principles for development

Apply these directly (as heuristics).

1. **Hide the internal representation; expose behavior.** Callers interact only through the public
   face; the private side is free to change.
2. **Encapsulate by assigning responsibilities correctly.** Put the logic where the data lives, not
   in the caller — that's what prevents repeated code.
3. **Tell, don't ask.** Add a message for each thing a collaborator needs to do
   (`isExpiredOn(date)`, `isOwnedBy(person)`) instead of exposing data to decide outside.
4. **Don't add getters/setters indiscriminately.** Each one is a hole in encapsulation; expose only
   intention-revealing operations.
5. **When you must return internals, prefer immutable objects, copies, or wrappers** — and remember
   none of these removes the coupling.
6. **Respect encapsulation even when the language lets you break it.** It's a discipline; in
   per-class or weakly-private languages, the user must uphold it.
7. **Treat subclassing as coupling to the superclass.** Subclass deliberately and protect inherited
   collaborators.

---

## Glossary

| Term                    | Definition                                                                        |
| ----------------------- | --------------------------------------------------------------------------------- |
| **H6**                  | Don't break encapsulation; assign responsibilities correctly and hide internals.  |
| **Encapsulation**       | Grouping data and the operations on it in one object; assigning responsibilities. |
| **Information hiding**  | Hiding internal details so no part depends on another's internals (Parnas).       |
| **Tell, Don't Ask**     | Tell a collaborator to act, rather than asking for its data to decide outside.    |
| **Public face / private side** | *What* an object does and tells vs. *how* it does it.                      |

---

## Sources

- David L. Parnas, *On the Criteria To Be Used in Decomposing Systems into Modules* (CACM, 1972) —
  *information hiding*.
- Rebecca Wirfs-Brock et al., *Designing Object-Oriented Software* — the public face / private side
  of an object.
- Erich Gamma et al. (GoF), *Design Patterns* (1994) — requests as the only way to change an object's
  encapsulated internal state.
- Grady Booch, *Object-Oriented Analysis and Design* — abstraction vs. encapsulation; interface vs.
  implementation; citing Ingalls and Liskov.
- David West, *Object Thinking* — the personal integrity of objects; encapsulation as discipline.
- David A. Taylor, *Object-Oriented Technology: A Manager's Guide* — the cell metaphor; two kinds of
  protection from message-based communication.
- Chamond Liu, *Smalltalk, Objects, and Design* — the outside/inside of an object.
- Bjarne Stroustrup, *The Design and Evolution of C++* — the class as the unit of protection (CAP
  influence).
- Alan Kay — the object-as-cell metaphor.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — course on
  object-oriented software design heuristics.
