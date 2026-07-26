# CLAUDE.md

This repository holds foundational design context for building software with objects: what software
is, what makes a model good, and six heuristics (H1–H6) for designing with objects — plus a companion
catalog of the 23 classic (GoF) design patterns.

**Use this guidance as the basis for every design and implementation decision in this repo**, and for
any code you write or review here. When the domain and the framework disagree, favor the domain.

## The guidance lives in skills — invoke them

The full material is packaged as skills in `.claude/skills/`, one per document. **Invoke the skill
rather than reading `docs/` or `design-patterns/` directly**: each skill is a short operative summary
that points to its full documents when you need the detail.

Start with **`designing-with-objects`** — it routes to the right heuristic, practice or pattern.

## The frame (always on)

The six heuristics have their own skills, and those descriptions are already loaded — invoke the one
that matches what you are doing. What follows is only the framing, which has no natural trigger:

- **Software is a computable model of a problem domain of reality** — not "a set of instructions".
  Good software is a good model, and **the source code is the design**: programming is designing, and
  testing and debugging are design too.
- **Judge a model on three axes** — implementation (how it executes), descriptive (how understandable
  it is), functional (how faithfully it represents the domain) — anchored on the **functional**. Aim
  for a 1:1 domain–model correspondence, so a new domain case is *added*, not patched in.
- **Development is a learning process.** Change is essential, not accidental; work iteratively and
  keep the feedback loop short.
- **All of this is heuristics, not rules.** Apply each in context, expect exceptions, weigh cost vs.
  benefit, and think critically — never follow guidance by authority. The same holds for patterns:
  never introduce one where its problem does not exist.

## Layout

| Content                                                       | Location                              |
| ------------------------------------------------------------- | ------------------------------------- |
| The guide — what software is, H1–H6, TDD, naming              | `docs/en`, `docs/es`                  |
| Design patterns — the 23 GoF patterns and the principles behind them | `design-patterns/en`, `design-patterns/es` |
| Skill catalog — one skill per document                        | `.claude/skills/`                     |

English is primary; the `es/` files are translations of the same content. Full navigation tables, with
links to every document in both languages, are in `README.md`.

## Conventions

- Each document is self-contained: definitions and principles in the body, sources at the end.
- Documents and skills are **1:1**. A skill is a short operative summary plus a pointer to its
  documents — keep it that way; never let a skill grow into a copy of the document it summarizes.
- When adding a topic: create both language versions, add the matching skill in `.claude/skills/`, and
  update the tables in `README.md`.
