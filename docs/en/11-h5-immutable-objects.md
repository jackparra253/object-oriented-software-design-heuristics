# H5 — Favor Immutable Objects

> **Purpose of this document.** This is a design heuristic (read it as a heuristic — see
> [why-heuristics](06-why-heuristics.md)): apply it in context, expecting exceptions. It answers the
> question the previous heuristics raise — given complete ([H2](08-h2-complete-objects.md)), valid
> ([H3](09-h3-valid-objects.md)), null-free ([H4](10-h4-no-null.md)) objects, **when and how should an
> object change?** Apply it whenever you decide whether an object is mutable, and how mutation happens.

---

## The heuristic

> **H5: Favor the use of immutable objects.**

Mutability is **not** primarily a technical choice — it is a **conceptual, modeling** choice (recall
[H1](07-h1-object-per-entity.md): faithful representation):

> An object should be **mutable if the entity it represents is mutable**, and **immutable if the
> entity it represents is immutable.**

Heraclitus ("no man steps in the same river twice") and Parmenides ("what is, cannot not-be") frame
the two poles. Most domain entities you think of as "things" are actually immutable: numbers
(integers, fractions), a date, a time, a day-of-month, a credit card, an invoice, a contract, a
string. The heuristic says: **start from immutability**, and make something mutable only when the
entity genuinely changes.

---

## Reality as a sequence of events generating immutable objects

There is a deeper reframing: much of what looks "mutable" is better modeled as a **sequence of events
producing immutable objects**, each faithful at its instant in time.

*Example — a `PhoneCall`.* An *ongoing* call knows `origin`, `destination`, `start`. Asking it
`duration()` should **not compile / not be understood** — the call hasn't ended, so duration is not a
faithful question yet (this is also [H2](08-h2-complete-objects.md) and [H4](10-h4-no-null.md):
no `end = null`, no `setEnd(...)`). When the call finishes, that event produces a *finished* call — a
**new, immutable** object with `end` that *does* answer `duration()`. Time passing becomes new
objects, not mutated ones.

---

## Advantages of immutable objects

- **You stop worrying about the passage of time.** The object can never become invalid or surprising
  later; it is what it was at creation.
- **You stop worrying about the consequences of "handing out" the object.** You can share a reference
  freely — no one can mutate it behind your back, so no defensive copies, no aliasing bugs, safe to
  use as a key, naturally thread-safe.

Related distinctions worth keeping straight:

- **Immutable object ≠ immutable variable** (`const`/`final`). A `final` reference can still point to
  a mutable object; an immutable object stays immutable however many variables reference it.
- **An immutable object whose collaborators are mutable is not really immutable** — immutability must
  reach all the way down.
- **Language/VM support is not required** to have immutable objects; it helps enforce them, but
  immutability is a design property you can uphold by discipline.

---

## When the entity really changes: handling mutation safely

Some entities do change — or we must model them as changing. Mutable objects are legitimate; the
point is to **model change deliberately, conscious of its consequences.** Four concerns:

### 1. Keep changes valid (H3) and atomic

- **Don't use setters.** A bare `setX` invites invalid, half-changed states. Expose intention-
  revealing domain operations instead.
- **Make changes atomic.** A change that touches several fields must leave the object valid as a
  whole — never observable mid-change.
- **Allow free change only where no validation is needed.**

### 2. Control the change

- **The owner of the object is responsible for changing it.** Mutation goes through whoever owns the
  object's lifecycle, not arbitrary collaborators.
- **Don't hand out mutable objects — or hand out copies.** If you expose internal mutable state,
  callers can corrupt your invariants; give them an immutable view or a copy.

### 3. Mind the impact on other objects

- **Don't hold onto objects that aren't yours.** Keeping a reference to someone else's mutable object
  couples you to changes you don't control.
- **Don't change identity.** Mutation must not alter what makes the object *that* entity.
- **Beware the impact on equality and hashing.** If a mutable object is a key in a hash structure and
  its hash changes, you corrupt the structure — another reason immutability is safer.

### 4. User input errors

- **Separate identity from "accidental" information.** What the user can mistype and correct is not
  the object's identity.
- **Keep a history of changes and always modify the same object.** Corrections become recorded
  events, not a silent overwrite — preserving the audit trail and the object's identity over time.

---

## Principles for development

Apply these directly (as heuristics).

1. **Decide mutability by the entity, not by convenience.** Mutable iff the represented entity is
   mutable.
2. **Default to immutable.** Make an object mutable only when the domain entity genuinely changes.
3. **Model change as new immutable objects when you can.** Prefer an event producing a new object
   (finished call) over mutating one in place.
4. **For genuinely mutable objects, avoid setters; use atomic, validity-preserving operations.**
5. **Control who mutates.** The owner changes the object; don't hand out mutable internals — hand out
   copies or immutable views.
6. **Protect identity, equality, and hashing.** Don't mutate what defines the object or what its hash
   depends on.
7. **Record corrections as history on the same object.** Separate identity from accidental,
   user-editable information.

---

## Glossary

| Term                     | Definition                                                                       |
| ------------------------ | -------------------------------------------------------------------------------- |
| **H5**                   | Favor immutable objects; be mutable only if the represented entity is.           |
| **Immutable object**     | An object whose state never changes after creation.                              |
| **Immutable variable**   | A `const`/`final` binding — distinct from an immutable object.                    |
| **Atomic change**        | A mutation that leaves the object valid as a whole, never observable mid-change. |
| **Identity**             | What makes an object *that* entity, independent of accidental, editable data.    |

---

## Sources

- Heraclitus and Parmenides — the classical framing of change vs. permanence.
- Joshua Bloch, *Effective Java* — "Minimize mutability" / favor immutable classes; immutables are
  simple, thread-safe, and freely shareable.
- Eric Evans, *Domain-Driven Design* (2003) — Value Objects modeled as immutable.
- Martin Fowler — *Event Sourcing* / events producing new state; *Value Object*.
- Michael Feathers & the functional-programming tradition — reasoning simplified by immutability.
- Andrew Hunt & David Thomas, *The Pragmatic Programmer* — beware aliasing; don't hand out mutable
  internals.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — course on
  object-oriented software design heuristics.
