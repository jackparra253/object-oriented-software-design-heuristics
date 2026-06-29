# CLAUDE.md

This repository holds foundational design context for building software with objects. The
documents under `docs/` define what software is and how to design it. **Use them as the basis for
every design and implementation decision in this repo.**

## Design context to apply

Read and apply these before designing or writing code. English is primary; the `es/` files are
translations of the same content.

| Topic                                           | Document                              |
| ----------------------------------------------- | ------------------------------------- |
| What Is Software?                               | `docs/en/01-what-is-software.md`      |
| Where Is the Model? (Source Code Is the Design) | `docs/en/02-where-is-the-model.md`    |
| What Makes a Good Model? (Three Axes)           | `docs/en/03-good-model.md`            |
| Software Development as a Learning Process       | `docs/en/04-software-development.md`  |
| What Is an Object?                              | `docs/en/05-what-is-an-object.md`     |
| Why Heuristics, Not Principles or Rules?        | `docs/en/06-why-heuristics.md`        |
| H1 — One Object per Entity                      | `docs/en/07-h1-object-per-entity.md`  |
| H2 — Create Objects Complete                    | `docs/en/08-h2-complete-objects.md`   |
| H3 — Only Create Valid Objects                  | `docs/en/09-h3-valid-objects.md`      |
| H4 — Don't Use Null                             | `docs/en/10-h4-no-null.md`            |
| H5 — Favor Immutable Objects                    | `docs/en/11-h5-immutable-objects.md`  |
| H6 — Don't Break Encapsulation                  | `docs/en/12-h6-encapsulation.md`      |

## Working principles (summary)

These come from the documents above; the documents are the source of truth.

1. **Software is a computable model of a problem domain of reality** — not "a set of
   instructions". Design from this definition.
2. **Good software is a good model.** Judge code first by how faithfully it represents the domain.
3. **Organize code around the domain, not the framework.** When the two conflict, favor the domain.
4. **Model the relevant business domain only** — slice reality on purpose.
5. **A model represents; it is not the thing.** Keep the map distinct from the territory.
6. **Specify the *what* and implement the *how*.** Software must be executable.
7. **Design is the deliberate move from an ambiguous, contextual domain to a formal, executable
   model.**
8. **Source code is the design.** It is the single source of truth for the model; programming is
   designing. Diagrams and docs only visualize it.
9. **The build is free; the design is the cost.** Compilation produces the executable; effort and
   estimates belong on the code. Treat testing and debugging as design (validation and refinement).
10. **The model is dynamic.** It executes and its state changes over time; design accordingly.
11. **Judge a model on three axes:** implementation (how it executes), descriptive (how
    understandable it is — names, domain language, habitability), and functional (how faithfully it
    represents the domain).
12. **Aim for a 1:1 domain–model correspondence.** New domain cases should be added, not patched in;
    one domain change should map to one model change (open–closed).
13. **Development is a learning process.** Work iteratively and incrementally; ground knowledge in
    concrete facts; make tacit domain knowledge explicit in the model.
14. **Change is essential, not accidental.** The domain, your understanding, and your modeling all
    shift over time; design so change is cheap and learning capacity is preserved.
15. **Shorten the feedback loop.** Immediate feedback (fast tests, live console) is the engine of
    learning; apply the scientific method — characterize, hypothesize, predict, experiment.
16. **An object is the essential representation of a domain entity — not "code + data".** Define it
    by the messages it responds to (its protocol), not by its internal data; capture the essence and
    remove the incidental.
17. **All design guidance here is heuristics, not rules.** Apply each in context, expect exceptions,
    weigh cost vs. benefit, and think critically — never follow guidance dogmatically or by
    authority.
18. **H1 — one object per entity (faithful representation).** Keep a 1:1 correspondence: never split
    one entity across many fields, never overload one object/primitive to mean many entities (fix
    Primitive Obsession). Name the entity for what it really is; prefer the right existing type over
    a needless new class.
19. **H2 — create objects complete.** An object must be valid and faithful from the moment it exists;
    require what it needs in its constructor, avoid post-construction setters and temporal coupling.
    Uninitialized fields signal "split into two objects"; use a Builder for complex construction.
20. **H3 — only create valid objects.** Make invalid objects impossible to construct and fail fast on
    bad creation. Put validation in the domain model (one rule serves REST, batch, and UI alike), not
    at the edges; signal errors with exceptions, not return codes. Validate in an instance-creation
    method (ideally a polymorphic class method), not the raw constructor. Choose SOFE vs. collect-all
    errors to fit the consumer (collect-all for UIs).
21. **H4 — don't use null/nil.** `null` breaks H1 by meaning many things at once (uninitialized, "no
    value", "nothing"); model absence as an object instead. Replace `if x.nil?` with polymorphism via
    a Null Object (name it for the domain — `NotProvidedAddress`, not `NullAddress`). In statically
    typed languages make "maybe absent" explicit with Optional/Maybe. Keep absence inside the object
    (Explicit Absent Message over safe-navigation `&.`); don't write defensive null-checks on
    parameters.
22. **H5 — favor immutable objects.** Mutability is a modeling choice, not a technical one: an object
    is mutable iff the entity it represents is. Default to immutable (numbers, dates, invoices,
    strings…); model change as a sequence of events producing new immutable objects when you can.
    Immutables free you from worrying about time and from the consequences of handing out the object.
    For genuinely mutable objects: avoid setters, make changes atomic and valid (H3), let the owner
    control mutation, hand out copies/immutable views, and protect identity, equality, and hashing.
23. **H6 — don't break encapsulation.** Encapsulating is assigning responsibilities correctly, not
    just hiding fields; information hiding is what's left once you remove the responsibilities.
    Breaking it creates coupling and strips logic from the object into callers (repeated code). Apply
    "Tell, Don't Ask": add a message for what you need (`isExpiredOn`, `isOwnedBy`) instead of
    exposing data; don't add getters/setters indiscriminately. When returning internals, prefer
    immutable objects, copies, or wrappers (none removes the coupling). Respect encapsulation even
    when the language (per-class privacy, weak modifiers) lets you break it.

## Conventions

- Documentation lives in `docs/`, split by language: `docs/en` (primary), `docs/es`.
- Each document is self-contained: definitions and principles in the body, sources at the end.
- When adding a topic, create both language versions and update the table in `README.md` and the
  table above.
