# Overview — Designing Software with Objects

> **Purpose of this document.** A 15-minute tour of the whole guide: what software *is*, how to judge
> a model, how design and learning relate, what an object really is, and the six heuristics (H1–H6)
> for building faithful object models. Read this first; each claim here is developed in its own
> chapter, linked inline. The closing **Principles for development** section is the short checklist to
> keep open while you design and code.

---

## Part I — What we are doing when we build software

### Software is a model of reality

Software is **a computable model of a problem domain of reality** — not "a set of instructions". This
single definition reorients everything: you are not writing steps for a machine, you are building a
*model* that represents some slice of a real (or conceptual) domain and that a computer can execute.
You deliberately choose which slice of reality to model and at what level of detail. The model
*represents* the domain; it is not the domain itself — keep the map distinct from the territory. (See
[01 — What Is Software?](01-what-is-software.md).)

Two consequences follow. First, you must **specify the *what* and implement the *how***: software has
to be executable, so the model is always a formal, runnable artifact, not a description. Second,
**design is the deliberate move from an ambiguous, contextual domain to a formal, executable model**
— that translation *is* the hard, valuable work.

### The source code is the design

Where does that model live? **In the source code.** The code is the single source of truth for the
model; diagrams and documents only *visualize* it. This is the classic insight that *programming is
designing*: the act of writing code is the act of designing the system. (See
[02 — Where Is the Model?](02-where-is-the-model.md).)

A practical corollary reshapes how you think about cost: **the build is free; the design is the
cost.** Compilation (the "manufacturing" step) is essentially free and automated; all the effort,
skill, and estimation belong to producing the code — the design. And because the design is the code,
**testing and debugging are design activities** — validation and refinement of the model — not a
separate phase tacked on at the end.

### What makes a good model — three axes

If software is a model, "good software" means "a good model." Judge a model on **three axes** (see
[03 — What Makes a Good Model?](03-good-model.md)):

1. **Implementation** — *how it executes*: performance, resource use, technical soundness.
2. **Descriptive** — *how understandable it is*: names, domain language, habitability — can a human
   read it and learn the domain from it?
3. **Functional** — *how faithfully it represents the domain*: does the model correspond to reality?

The functional axis is the anchor: **aim for a 1:1 correspondence between domain and model.** When the
correspondence is right, a new case in the domain should be *added* to the model, not patched in, and
one change in the domain should map to one change in the model. This is the open–closed ideal stated
in modeling terms.

### Development is a learning process

You almost never understand a domain fully up front, so **development is a learning process** — work
iteratively and incrementally, ground your knowledge in concrete facts, and make tacit domain
knowledge explicit *in the model itself*. (See
[04 — Software Development as a Learning Process](04-software-development.md).)

This reframes change. **Change is essential, not accidental**: the domain shifts, your understanding
of it shifts, and your modeling of it shifts — all over time. So design so that change is cheap and
your *capacity to keep learning* is preserved. The engine of that learning is a **short feedback
loop**: fast tests and a live console let you apply the scientific method — characterize, hypothesize,
predict, experiment — many times an hour. The model is also **dynamic**: it executes and its state
changes over time, so design with the passage of time in mind.

### What an object is

The unit of the model is the object. **An object is the essential representation of a domain entity —
not "code + data".** You define an object by **the messages it responds to** (its protocol), not by
the data it holds inside. The discipline is to capture the *essence* of the entity and remove the
incidental. (See [05 — What Is an Object?](05-what-is-an-object.md).)

This "defined by messages, not data" stance is what makes the later heuristics coherent: if an object
*is* its protocol, then hiding its data, controlling its construction, and refusing invalid states are
all just ways of keeping the protocol honest.

### Why heuristics, not rules

The guidance that follows is delivered as **heuristics, not principles or rules.** A heuristic is
applied *in context*, expects exceptions, and is weighed by cost versus benefit. You are meant to
**think critically** about each one — never follow it dogmatically or by authority. (See
[06 — Why Heuristics?](06-why-heuristics.md).) Keep this framing in mind for everything below: H1–H6
are strong defaults with good reasons, not laws.

---

## Part II — The six heuristics

The six heuristics build on one another. H1 sets the goal (faithful representation); H2 and H3 govern
how objects come into existence (complete, valid); H4 removes the worst representational hole (null);
H5 governs change over time (immutability); H6 names the property all of them quietly depend on
(encapsulation).

### H1 — One object per entity (faithful representation)

**For every entity in reality there should be one object that represents it faithfully.** This is the
functional axis made concrete: seek a 1:1 correspondence between domain entities and model objects.
Two failures break it, both harmful: **one entity split across many objects/fields** (e.g. a
credit-card expiration modeled as separate `month` and `year`), and **one object overloaded to mean
many entities** (e.g. a bare array or encoded number standing in for a real concept — *Primitive
Obsession*). Name the entity for what it really is (a card "number" is an *identifier*, not a number;
an "expiration date" is a *year-month*, not a date), and prefer the right existing type over inventing
a needless class. (See [07 — H1](07-h1-object-per-entity.md).)

### H2 — Create objects complete

**An object must be valid and faithful from the moment it exists.** Because the model is dynamic and
time passes, there is no legitimate "half-built" state. Require what the object needs **in its
constructor**, and avoid post-construction setters that finish the job later — those create *temporal
coupling* (messages must be sent in a hidden required order) and transient invalid states. A telling
symptom: **uninitialized fields usually mean you are modeling two entities/states as one** — split
them into two complete objects (e.g. an *ongoing* call vs. a *finished* call). For genuinely complex
assembly, use a **Builder** so the domain object itself is always complete. (See
[08 — H2](08-h2-complete-objects.md).)

### H3 — Only create valid objects

Complete is not enough; the object must also be **valid** — the model must make invalid objects
**impossible to construct**, and must **fail fast** when creation is wrong. You should not be able to
build a February 31st, a fraction over zero, or a credit card with an empty owner. The highest-value
move is **where** validation lives: **put it in the domain model**, not at the edges, so one rule
serves REST, batch jobs, and the UI alike (fewer tests, no inconsistent models). Signal errors with
**exceptions, not return codes**; validate in an **instance-creation method** (ideally a polymorphic
class method) rather than the raw constructor; and choose your error strategy to fit the consumer —
**stop-on-first-error** for internal calls, **collect-all-errors** for UIs. (See
[09 — H3](09-h3-valid-objects.md).)

### H4 — Don't use null

If objects are complete (H2) and valid (H3), should a reference ever be `null`/`nil`? **No.** `null`
is the canonical violation of H1: a single symbol overloaded to mean an uninitialized variable, "the
customer has no address", and "nothing" — all at once — so it faithfully represents none of them, and
it leaks into the real world as the bugs everyone has seen (`null95` on a screen, "(null) could not be
found"). Instead, **model the absence as an object**. Replace `if x.nil?` with **polymorphism** via a
**Null Object** (name it for the domain — `NotProvidedAddress`, not `NullAddress`). In statically
typed languages, make "maybe absent" explicit with **Optional/Maybe**. Keep the absence *inside* the
object — prefer an *Explicit Absent Message* over a leaky safe-navigation operator — and don't write
defensive null-checks on parameters a valid object would never pass you. (See
[10 — H4](10-h4-no-null.md).)

### H5 — Favor immutable objects

Given complete, valid, null-free objects, **when and how should an object change?** Mutability is a
**modeling choice, not a technical one**: an object should be mutable if and only if the entity it
represents is mutable. Most things you think of as "objects" are actually immutable — numbers, dates,
invoices, contracts, strings — so **default to immutable**, and often model change as a **sequence of
events producing new immutable objects** (an ongoing call becomes a *new* finished call). Immutability
buys you a lot: you stop worrying about the passage of time, and about the consequences of handing the
object out (no defensive copies, no aliasing bugs, safe as a hash key, naturally thread-safe). When an
entity genuinely changes, model the change deliberately: avoid setters, keep changes **atomic and
valid** (H3), let the **owner** control mutation, hand out copies or immutable views rather than
mutable internals, and protect identity, equality, and hashing. (See
[11 — H5](11-h5-immutable-objects.md).)

### H6 — Don't break encapsulation

Every earlier heuristic quietly relied on this one. **Encapsulation is assigning responsibilities to
objects correctly** — not merely hiding fields. *Information hiding* (the access-control mechanism) is
just the part that remains once you take the responsibilities away. Think about it through what breaks
when you violate it: you **create coupling** (callers depend on internal structure — worse in
statically typed languages), and you **strip responsibility from the right object**, leaking its logic
out into callers as **repeated code**. The cure is **Tell, Don't Ask**: add a message for each thing a
collaborator needs to do (`card.isExpiredOn(date)`, `card.isOwnedBy(person)`) instead of exposing data
to decide outside, and *don't* add getters/setters indiscriminately. When you must return an internal,
prefer immutable objects, copies, or wrappers — though none of these removes the coupling. Languages
help or hinder (per-object privacy like Smalltalk/Ruby helps; per-class privacy and weak modifiers
hinder), but in the end encapsulation is **a discipline the object's user must respect**. (See
[12 — H6](12-h6-encapsulation.md).)

---

## How it all fits together

Read top to bottom, the guide is one argument. Software is a **computable model of reality** (01),
and that model **is the source code** (02), judged on the implementation, descriptive, and
**functional** axes (03), refined through **iterative learning** with a short feedback loop (04). Its
unit is the **object**, defined by the **messages** it answers (05), and all the design advice is
**heuristics** to apply with judgment (06).

The heuristics then keep the *functional* axis honest over the life of the system: represent each
entity **faithfully and 1:1** (H1), bring objects into existence **complete** (H2) and **valid** (H3),
refuse the great representational lie of **null** (H4), let objects change only as their entities do —
**favoring immutability** (H5) — and protect each object's responsibilities by **not breaking
encapsulation** (H6).

---

## Principles for development

The short checklist (each is a heuristic — apply it in context).

1. **Design from the definition.** Software is a computable model of a problem domain; build the
   model, don't just script behavior.
2. **Treat the source code as the design.** It is the single source of truth; programming is
   designing; testing and debugging are design.
3. **Judge the model on three axes**, and anchor on the **functional** one: aim for a 1:1 domain–model
   correspondence so new cases are *added*, not patched.
4. **Work as a learner.** Iterate, ground decisions in facts, make tacit knowledge explicit, and keep
   the feedback loop short; design so change stays cheap.
5. **Define objects by their messages, not their data.** Capture the essence; remove the incidental.
6. **H1 — one object per entity.** No entity split across fields; no object/primitive overloaded to
   mean many entities; name things for what they are.
7. **H2 — create objects complete.** Require what's needed in the constructor; no temporal coupling;
   split uninitialized-field objects in two; use a Builder for complex assembly.
8. **H3 — only create valid objects.** Make invalid objects impossible; fail fast; validate in the
   domain model via instance-creation methods; exceptions over return codes.
9. **H4 — don't use null.** Model absence as an object (Null Object / Optional); replace null-checks
   with polymorphism; keep absence inside the object.
10. **H5 — favor immutable objects.** Mutable iff the entity is; default to immutable; model change as
    new objects; control mutation carefully when it's real.
11. **H6 — don't break encapsulation.** Assign responsibilities correctly; Tell, Don't Ask; avoid
    indiscriminate getters/setters; respect encapsulation even when the language won't enforce it.
12. **Apply every guideline as a heuristic.** Weigh cost vs. benefit, expect exceptions, think
    critically — never follow by authority.

---

## Sources

- The full treatment of each topic, with its own sources, lives in chapters
  [01](01-what-is-software.md)–[12](12-h6-encapsulation.md) of this guide.
- Jack Reeves, *What Is Software Design?* (1992) — source code as the design.
- Frederick P. Brooks, *No Silver Bullet* (1986) — essential vs. accidental complexity.
- Arthur J. Riel, *Object-Oriented Design Heuristics* (1996) — heuristics as a way to teach design.
- Eric Evans, *Domain-Driven Design* (2003); Rebecca Wirfs-Brock, *Designing Object-Oriented
  Software* — domain models and responsibility-driven design.
- David L. Parnas, *On the Criteria To Be Used in Decomposing Systems into Modules* (1972) —
  information hiding.
- Hernán Wilkinson / 10Pines, *Heurísticas de Diseño de Software con Objetos* — course on
  object-oriented software design heuristics.
