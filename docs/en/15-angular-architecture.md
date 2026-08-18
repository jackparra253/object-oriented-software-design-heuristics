# Angular v22 Architecture — Applying the Heuristics with TDD (additional material)

> **Purpose of this document.** This is **additional material**, not a heuristic. H1–H6 are
> technology-independent; this document is *one worked application* of them to a concrete stack —
> Angular v22 — together with the TDD loop from [13 — TDD](13-tdd.md). Use it when the framework and
> the domain pull in different directions, which in Angular they routinely do. When they disagree,
> **favor the domain**.

---

## The premise: Angular is a delivery adapter, not the model

An Angular application is a **computable model of a problem domain** that happens to be delivered
through a browser ([01 — What Is Software?](01-what-is-software.md)). The framework's job is delivery:
routing, rendering, HTTP, forms. It is not the job of the framework to hold your domain, and it is not
good at it — Angular's idioms push in the opposite direction from the heuristics:

| The framework does this | Which pushes against |
| ------------------------- | -------------------- |
| Instantiates components empty and fills `input`s afterwards | H2 — create objects complete |
| Hands you DTOs: anemic records that mirror the wire format | H1 — one object per entity |
| Returns `undefined` while a resource loads, and `null` from validators | H4 — don't use null |
| Gives you signals: mutable cells, mutated in place | H5 — favor immutable objects |
| Encourages templates that read fields and decide | H6 — don't break encapsulation |

The architecture below does not fight this. It **contains** it: a domain core where H1–H6 hold at 100%,
and an adapter zone where the exceptions are few, named, and paid for on purpose
([06 — Why Heuristics](06-why-heuristics.md)).

### What Angular's documentation actually prescribes

**Angular's documentation does not define an application architecture.** It defines the anatomy of the
*framework* — components, dependency injection, routing, forms — and leaves layering, domain boundaries
and the question of where business rules live entirely to you. Two statements in the
[style guide](https://angular.dev/style-guide) are the exception, and both support what follows:

- *"Organize your project into subdirectories based on the features of your application"* — and
  explicitly **"avoid creating subdirectories based on the type of code."**
- *"Code inside your components and directives should generally relate to the UI shown on the page. For
  code that makes sense on its own, decoupled from the UI, prefer refactoring to other files"* — naming
  form validation rules and data transformations as the examples.

So the structure below is **feature-first**, because that is the one structural rule Angular does
impose. The domain core *inside* each feature is not from the documentation: it is H1–H6 applied. This
document is an architecture of authorship, and says so.

---

## What v22 changes, and why it matters to the design

- **Zoneless is the default** (since v21) and **OnPush is the default change detection strategy** —
  reactivity is now explicit and signal-driven. Immutable domain objects held in signals are no longer
  a purist's choice; they are what the framework is optimized for. `ChangeDetectionStrategy.Default` is
  deprecated and replaced by `Eager`, which `ng update` writes into existing components to preserve
  their behavior — treat every `Eager` it leaves behind as a migration to-do, not a destination.
- **Signal Forms are stable** (`@angular/forms/signals`) — validation is a plain function you write, so
  it can *delegate to the domain* instead of duplicating rules in a `Validators` array.
- **`resource()` / `httpResource()` are stable** — remote reads are signals with `isLoading()`,
  `error()`, `hasValue()`, `value()`, and a `status()` with six values (`idle`, `loading`, `reloading`,
  `error`, `resolved`, `local`). That is a state machine the framework leaves untyped; H4 says to give
  it objects.
- **Safe navigation now returns `undefined`, not `null`.** In v22 `user?.profile?.name` in a template
  follows real JavaScript semantics; `$null(...)` restores the old behavior. One less `null` coming
  from the framework — but the absent case is still unmodeled, so H4 applies exactly as before. Only
  the spelling changed.
- **`@Service()` replaces the common `@Injectable()` cases** and auto-provides in root by default.
  Convenient, and a trap when a class is bound to a port by hand — see below.
- **Vitest is the default test runner** (Karma/Jasmine are out) — a plain unit test of a domain class,
  with no `TestBed`, runs in milliseconds. The TDD loop is finally fast enough to be a loop.
- **`strictTemplates`**, `HttpClient` on `fetch` (`FetchBackend` is now the default, deprecating
  `withFetch()`), and TypeScript 6 are the baseline.

---

## The architecture: features outside, layers inside

**Feature first, layer second**, and **one dependency rule: everything points inward.** `domain/`
imports nothing — especially not `@angular/*`.

```
src/app/orders/          ← a feature (a bounded context), not a technical role
  domain/                entities, value objects, ports (interfaces)   ← zero @angular/* imports
  application/           use cases: orchestrate entities through ports
  data-access/           HTTP/storage adapters + DTO mappers — they implement the ports
  feat-order-list/       routed pages
  ui-order-card/         presentational components
src/app/shared/          depends only on shared, so cycles cannot form
```

In a monorepo each of those directories becomes a library and its name becomes a tag.

The names `data-access`, `feat-*` and `ui-*` are [Nx's conventional taxonomy](https://nx.dev/blog/architecting-angular-applications);
`domain/` and `application/` are **not**. Nx folds both into `data-access`, which it defines as "API
communication and state management" — a taxonomy with no slot for entities, which is precisely how the
DTO ends up being the domain type. Adding those two layers is the deliberate disagreement of this
document, and the reason it exists.

### Enforce it mechanically

A boundary rule that breaks the build is worth more than a paragraph in a wiki. Two tools, same idea:
**Sheriff** for a single app, **Nx module boundaries** for a monorepo. With Nx, tag every library
twice — by scope and by type — and the dependency rule becomes a lint rule:

| Tag | May depend on |
| --- | ------------- |
| `type:domain` | **nothing** |
| `type:application` | `type:domain` |
| `type:data-access` | `type:application`, `type:domain` |
| `type:feature` | any type, within its own scope |
| `type:ui` | `type:ui`, `type:domain` |
| `scope:shared` | `scope:shared` only |

`type:domain` depending on nothing is the rule that carries the whole architecture. The rest is
hygiene.

### The domain: entities, complete and valid (H1, H2, H3)

```ts
// orders/domain/Order.ts
export class Order {
  static placedBy(customer: Customer, lines: readonly OrderLine[]): Order {
    if (lines.length === 0) throw new OrderWithoutLines(customer);   // H3: fail fast
    return new Order(customer, lines);
  }

  private constructor(                                               // H2: no other way in
    private readonly customer: Customer,                             // H5: readonly
    private readonly lines: readonly OrderLine[],
  ) {}

  total(): Money {
    return this.lines.reduce((sum, line) => sum.plus(line.total()), Money.zeroIn(this.customer.currency()));
  }

  canBeCancelledBy(person: Person): boolean {                        // H6: tell, don't ask
    return this.customer.is(person) && this.isPending();
  }

  without(line: OrderLine): Order {                                  // H5: change = new object
    return new Order(this.customer, this.lines.filter((each) => each !== line));
  }
}
```

The **port** is an interface named after the domain role it plays, not after its implementation
([14 — Naming](14-naming.md)):

```ts
// orders/domain/Orders.ts — an abstract class, not an interface: it also serves as the DI token
export abstract class Orders {
  abstract placedBy(customer: Customer): Promise<readonly Order[]>;
  abstract add(order: Order): Promise<void>;
}
```

### The border: the DTO dies in the mapper (H1)

One place in the whole application knows what the JSON looks like:

```ts
// orders/data-access/HttpOrders.ts
@Service({ autoProvided: false })     // ← see the note below; this one is provided by hand
export class HttpOrders implements Orders {
  readonly #http = inject(HttpClient);

  async placedBy(customer: Customer): Promise<readonly Order[]> {
    const dtos = await firstValueFrom(
      this.#http.get<OrderDto[]>('/api/orders', { params: { customer: customer.id() } }),
    );
    return dtos.map(orderFrom);      // ← the DTO stops here; nothing above sees OrderDto
  }
}
```

Wire the port to the adapter once, at the root: `{ provide: Orders, useClass: HttpOrders }` — the use
cases depend on `Orders`, never on `HttpOrders`.

Two v22 details that bite here:

- **`@Service()` auto-provides in root.** An adapter you also bind to a port would be registered
  twice — once as itself, once as `Orders`. Say `@Service({ autoProvided: false })` (or plain
  `@Injectable()`) on anything you provide by hand.
- A TypeScript `interface` disappears at runtime and cannot be a DI token; that is why the port is an
  abstract class. An `InjectionToken<Orders>` works too, at the cost of a second name for the same
  idea.

### Remote state as objects, not `undefined` (H4)

`httpResource` exposes a six-state machine through `status()`, plus `isLoading()`, `error()`,
`hasValue()` and `value()`. Reading them in the template scatters that machine across your HTML; model
the states instead:

```ts
// orders/application/RemoteOrders.ts — one object per state, all with the same protocol
export abstract class RemoteOrders {
  static from(resource: HttpResourceRef<OrderDto[] | undefined>): RemoteOrders {
    if (resource.status() === 'idle') return new UnrequestedOrders();
    if (resource.isLoading()) return new LoadingOrders();

    const failure = resource.error();
    if (failure) return new FailedOrders(failure);
    if (!resource.hasValue()) return new UnrequestedOrders();

    return new LoadedOrders(resource.value().map(orderFrom));
  }

  abstract summary(): string;
  abstract rows(): readonly Order[];
}
```

`hasValue()` is a type predicate, so inside that last branch `value()` narrows to `OrderDto[]` and the
code compiles under `strict`. Skipping it — `resource.value().map(...)` straight after the loading and
error checks — does not compile, and would also blow up on the `idle` state, where nothing is loading,
nothing failed, and there is no value. **`undefined` exists on exactly one line, inside the converter,
and never crosses into `application/` or `domain/`.**

### Forms: validate by asking the domain (H3)

Signal Forms validators are plain functions — return `null` for valid, `{ kind, message }` for
invalid — so they can delegate instead of duplicating the rule:

```ts
// orders/feat-checkout/EmailField.ts
import { form, validate, FormField } from '@angular/forms/signals';

emailForm = form(this.model, (path) => {
  validate(path.email, ({ value }) =>
    EmailAddress.isValid(value()) ? null : { kind: 'email', message: 'Not a valid email address' },
  );
});
```

The single source of truth for what a valid email *is* stays in `EmailAddress`. The form asks; it does
not re-decide. The same rule then holds for the REST payload, the CSV import and the batch job — which
is the whole point of H3.

**On `validateStandardSchema()`.** v22 lets you validate a field against a Zod or Valibot schema. That
is a fine **boundary** check — shape, types, what arrived over the wire — and a bad place for domain
rules. If the schema decides what a valid order *is*, you now have two sources of truth and H3 is lost.
Schema at the border, entity for the rule.

### Templates: ask one question, not five (H6)

```html
<!-- Don't: the rule for "can this be cancelled" now lives in HTML, in every template that needs it -->
@if (order().status === 'PENDING' && order().customerId === currentUser().id) { … }

<!-- Do: -->
@if (cancellable()) { <button (click)="cancel()">Cancel</button> }
```

```ts
readonly cancellable = computed(() => this.order().canBeCancelledBy(this.currentUser()));
```

The `computed` is not decoration: with OnPush it re-evaluates only when `order` or `currentUser`
change, and it gives the question a name.

---

## TDD with Vitest, aligned to the layers

The layering pays for itself first in the test suite. Each layer has a different cost and a different
reason to exist:

| Layer | How it is tested | Cost |
| ----- | ---------------- | ---- |
| `domain/` | Plain Vitest. No `TestBed`, no DOM, no HTTP. **Most of your tests live here.** | ~1 ms |
| `application/` | Use cases against **in-memory fakes** of the ports (`InMemoryOrders`). Still no `TestBed`. | ~ms |
| `data-access/` | The mapper, directly. One test per DTO shape you actually receive. | ~ms |
| `feat-*/`, `ui-*/` | `TestBed` + component harnesses, over observable behavior. **Few, and only for what the component adds.** | ~100 ms |
| end-to-end | A separate suite, a handful of critical journeys. | seconds |

**The loop.** Run Vitest in watch mode. Red — the smallest test for the next behavior, and it must
fail *for the right reason*. Green — the minimal honest code. **Refactor — this is where the domain
object is born and gets its name**; skipping it leaves you with a working application that models
nothing ([13 — TDD](13-tdd.md), [14 — Naming](14-naming.md)).

**Fakes, not mocks.** An `InMemoryOrders` that really stores orders lets you assert *what happened*;
a mock asserts *how you called it* and welds the test to the implementation. Tell, don't ask applies
to tests too.

**Zoneless changes component tests.** With zoneless the default, prefer `await fixture.whenStable()`
over zone-flushing tricks; signal reads are synchronous after `fixture.detectChanges()`.
`fakeAsync` still works through the zone.js Vitest patch, but needing it is usually a signal that the
logic belongs in a layer that has no fixture.

**Don't test:** signal wiring, Angular's change detection, getters, or that a `computed` recomputes.
Test the domain rule, and test that the component shows it.

---

## The exceptions, named and contained

Four places where the framework wins. Each is allowed *only* in its layer, which is what keeps it from
spreading:

1. **Components are born empty (H2).** Unavoidable — Angular owns their lifecycle. Contained by giving
   components no domain rules of their own, declaring inputs as `input.required<T>()`, and building
   every domain object complete in a factory or mapper.
2. **DTOs are anemic (H1).** Unavoidable — they are a wire format, not an entity. Contained by the
   `Dto` suffix and by living only inside `data-access/`.
3. **`undefined` and `null` come from the API (H4).** `resource.value()` before load, `viewChild`,
   optional route params, safe navigation in templates (now `undefined` in v22), and validators that
   must return `null` to mean "valid". Contained by converting at the boundary, in one place per case.
4. **Signals are mutable cells (H5).** Intended — a signal models "what is current", which genuinely
   changes. Contained by holding **immutable domain objects** inside them: `set` a new object, never
   mutate the one held.

Anything else that breaks a heuristic is not an exception; it is a design decision you have not made
yet.

---

## Smells checklist

| Smell | Heuristic | What it usually means |
| ----- | --------- | --------------------- |
| `interface Order { id: string; total: number }` used as the domain type | H1 | The DTO escaped the mapper |
| Top-level `components/`, `services/`, `models/` directories | — | Sliced by technical role; the feature has no home |
| Business rules inside `@if` in a template | H6 | The entity is missing a message |
| A Zod schema that decides what a valid order is | H3 | Boundary check promoted to domain rule |
| `Validators.required` duplicating a rule the entity already has | H3 | Two sources of truth for validity |
| `value() ?? []`, `?.` chains on remote data | H4 | The loading state was never modeled |
| A service with `#state = signal<Order \| null>(null)` and setters | H2/H4/H5 | State machine modeled as nullable mutable field |
| `TestBed` in most of your test files | — | Domain logic is living in components |
| `domain/` importing `@angular/core` | all | The core is no longer independent |
| `ChangeDetectionStrategy.Eager` left by `ng update` | — | An unfinished migration, not a decision |

---

## Principles for development

1. **Slice by feature first, layer inside** — never top-level directories named after technical roles.
2. **Keep `domain/` free of `@angular/*`,** and enforce it with lint, not discipline.
3. **Point every dependency inward:** feature/ui → application → domain; `data-access` implements the
   domain's ports. Make it a tag rule that fails CI.
4. **Kill the DTO at the mapper.** One place knows the wire format.
5. **Name ports after domain roles** (`Orders`), not after implementations (`OrderService`).
6. **Model remote states as objects,** so `undefined` never crosses the border.
7. **Delegate form validation to the entity;** the form asks, it does not re-decide. Schemas guard the
   border, not the rule.
8. **Hold immutable domain objects in signals;** replace, never mutate.
9. **Ask the template one named question** (a `computed`), not five fields.
10. **Put most tests in `domain/`, with no `TestBed`,** and use in-memory fakes for the ports.
11. **Never skip the refactor step** — it is where the entity appears and gets named.
12. **Weigh the cost.** For a small app, collapsing `application/` into a per-feature signal store is a
    legitimate trade-off; letting entities become anemic records is not.

---

## Out of scope

This document covers only the places where **the framework and the domain disagree**. Everything an
Angular application also needs, but that does not move H1–H6 either way, is deliberately absent: NgRx
Signal Store, SSR and incremental hydration, micro frontends and Native Federation, internationalization,
authentication and authorization (OAuth 2 / OIDC), monorepo build tooling beyond the boundary rules, and
forensic analysis of an existing codebase. Steyer's *Modern Angular* covers all of them; treat it as the
companion volume, not a competitor.

Two of those do touch the design, and are worth naming:

- **SSR** demands that your domain never assume a browser. The `domain/` rule — no `@angular/*`, no
  `window`, no `document` — already gives you that for free. If SSR breaks on your domain code, the
  boundary was already leaking.
- **Micro frontends** are not an alternative to this structure; they are what it becomes when a feature
  gets its own team and its own deploy. Slicing by feature first is the precondition, which is the same
  reason it is principle #1.

---

## Glossary

| Term | Definition |
| ---- | ---------- |
| **Feature** | A bounded context of the domain, and the outermost unit of the structure (`orders/`). |
| **Port** | An interface in `domain/` naming a collaboration the domain needs (`Orders`). |
| **Adapter** | A `data-access/` class implementing a port with a real technology (`HttpOrders`). |
| **Mapper** | The single function that turns a DTO into an entity; the border of the model. |
| **DTO** | Data Transfer Object: the wire format. Anemic on purpose, confined to `data-access/`. |
| **Tag** | A label on a library (`scope:orders`, `type:domain`) that turns the dependency rule into lint. |
| **Signal** | A reactive mutable cell. Holds "what is current"; its contents should be immutable. |
| **`httpResource`** | Stable v22 API exposing an HTTP read as `status()`/`isLoading()`/`error()`/`value()` signals. |
| **Signal Forms** | Stable v22 forms API (`@angular/forms/signals`); validators are plain functions. |
| **Zoneless** | Change detection without zone.js; default since v21. Reactivity is explicit. |
| **Fake** | A working in-memory implementation of a port, used in tests instead of a mock. |
| **Harness** | Angular's component test API for driving a component through its public behavior. |

---

## Sources

- Angular documentation — style guide (the only official statement on project structure)
  https://angular.dev/style-guide ; `httpResource` https://angular.dev/guide/http/http-resource ;
  Signal Forms validation https://angular.dev/guide/forms/signals/validation
- Angular team, *Angular skills for AI agents* — https://github.com/angular/skills
- ANGULARarchitects, *Angular 22: The Most Important New Features at a Glance* —
  https://www.angulararchitects.io/en/blog/angular-22-the-most-important-new-features-at-a-glance/
- Nx, *Architecting Angular Applications* — https://nx.dev/blog/architecting-angular-applications
  (feature-first slicing, the `feat`/`ui`/`data-access` taxonomy, dual tagging)
- Manfred Steyer, *Modern Angular: Architecture, Concepts, Implementation* (2026) — vertical slicing,
  modulith, enforcing boundaries with Sheriff.
- Ninja Squad, *What's new in Angular 22.0* — https://blog.ninja-squad.com/2026/06/03/what-is-new-angular-22.0
- Alistair Cockburn, *Hexagonal Architecture (Ports and Adapters)* (2005).
- Steve Freeman & Nat Pryce, *Growing Object-Oriented Software, Guided by Tests* (2009) — fakes over
  mocks, outside-in TDD.
- This guide: [07 — H1](07-h1-object-per-entity.md) … [12 — H6](12-h6-encapsulation.md),
  [13 — TDD](13-tdd.md), [14 — Naming](14-naming.md).
