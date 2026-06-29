# CLAUDE.md

This repository holds foundational design context for building software with objects. The
documents under `docs/` define what software is and how to design it. **Use them as the basis for
every design and implementation decision in this repo.**

## Design context to apply

Read and apply these before designing or writing code. English is primary; the `es/` files are
translations of the same content.

| Topic              | Document                              |
| ------------------ | ------------------------------------- |
| What Is Software?  | `docs/en/01-what-is-software.md`      |

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

## Conventions

- Documentation lives in `docs/`, split by language: `docs/en` (primary), `docs/es`.
- Each document is self-contained: definitions and principles in the body, sources at the end.
- When adding a topic, create both language versions and update the table in `README.md` and the
  table above.
