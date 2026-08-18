# Arquitectura Angular v22 — Aplicar las heurísticas con TDD (material adicional)

> **Propósito de este documento.** Es **material adicional**, no una heurística. H1–H6 son
> independientes de la tecnología; este documento es *una aplicación concreta* de ellas a un stack
> puntual —Angular v22— junto con el ciclo de TDD de [13 — TDD](13-tdd.md). Usalo cuando el framework y
> el dominio tiran para lados distintos, que en Angular es la norma. Cuando no coinciden, **gana el
> dominio**.

---

## La premisa: Angular es un adaptador de entrega, no el modelo

Una aplicación Angular es **un modelo computable de un dominio de problema** que se entrega a través de
un browser ([01 — ¿Qué es el software?](01-que-es-software.md)). El trabajo del framework es la
entrega: ruteo, renderizado, HTTP, formularios. No es tarea del framework sostener tu dominio, y no lo
hace bien: sus idiomas empujan en dirección contraria a las heurísticas.

| El framework hace esto | Y empuja en contra de |
| ---------------------- | --------------------- |
| Instancia componentes vacíos y llena los `input` después | H2 — crear objetos completos |
| Te entrega DTOs: registros anémicos que espejan el formato de red | H1 — un objeto por ente |
| Devuelve `undefined` mientras carga un recurso, y `null` desde los validadores | H4 — no usar null |
| Te da señales: celdas mutables, mutadas en el lugar | H5 — objetos inmutables |
| Fomenta templates que leen campos y deciden | H6 — no romper el encapsulamiento |

La arquitectura de abajo no pelea contra esto: lo **contiene**. Un núcleo de dominio donde H1–H6 valen
al 100%, y una zona de adaptadores donde las excepciones son pocas, están nombradas y se pagan a
conciencia ([06 — Por qué heurísticas](06-por-que-heuristica.md)).

### Qué prescribe realmente la documentación de Angular

**La documentación de Angular no define una arquitectura de aplicación.** Define la anatomía del
*framework* —componentes, inyección de dependencias, ruteo, formularios— y te deja enteramente a vos las
capas, las fronteras de dominio y la pregunta de dónde viven las reglas de negocio. Dos frases del
[style guide](https://angular.dev/style-guide) son la excepción, y las dos respaldan lo que sigue:

- *"Organizá tu proyecto en subdirectorios basados en las features de tu aplicación"* — y
  explícitamente **"evitá crear subdirectorios basados en el tipo de código."**
- *"El código dentro de tus componentes y directivas debería en general relacionarse con la UI que se
  muestra en la página. Para el código que tiene sentido por sí solo, desacoplado de la UI, preferí
  refactorizarlo a otros archivos"* — y nombra como ejemplos las reglas de validación de formularios y
  las transformaciones de datos.

Entonces: la estructura de abajo es **feature-first**, porque esa es la única regla estructural que
Angular sí impone. El núcleo de dominio *dentro* de cada feature no sale de la documentación: es H1–H6
aplicadas. Este documento es una arquitectura de autor, y lo dice de frente.

---

## Qué cambia v22, y por qué le importa al diseño

- **Zoneless es el default** (desde v21) y **OnPush es la estrategia de detección de cambios por
  defecto** — la reactividad ahora es explícita y guiada por señales. Tener objetos de dominio
  inmutables dentro de señales dejó de ser una elección purista: es para lo que el framework está
  optimizado. `ChangeDetectionStrategy.Default` quedó deprecado y lo reemplaza `Eager`, que `ng update`
  le escribe a los componentes existentes para preservar su comportamiento — tratá cada `Eager` que te
  deje como una migración pendiente, no como un destino.
- **Signal Forms es estable** (`@angular/forms/signals`) — la validación es una función común que
  escribís vos, así que puede *delegar en el dominio* en vez de duplicar reglas en un array de
  `Validators`.
- **`resource()` / `httpResource()` son estables** — las lecturas remotas son señales con
  `isLoading()`, `error()`, `hasValue()`, `value()`, y un `status()` de seis valores (`idle`,
  `loading`, `reloading`, `error`, `resolved`, `local`). Eso es una máquina de estados que el framework
  deja sin tipar; H4 dice que le pongas objetos.
- **La navegación segura ahora devuelve `undefined`, no `null`.** En v22 `user?.profile?.name` en un
  template sigue la semántica real de JavaScript; `$null(...)` restaura el comportamiento viejo. Un
  `null` menos viniendo del framework — pero el caso ausente sigue sin modelarse, así que H4 aplica
  igual que antes. Solo cambió cómo se escribe.
- **`@Service()` reemplaza los casos comunes de `@Injectable()`** y auto-provee en root por defecto.
  Cómodo, y una trampa cuando la clase además se ata a un puerto a mano — ver más abajo.
- **Vitest es el runner por defecto** (se fueron Karma/Jasmine) — un test unitario de una clase de
  dominio, sin `TestBed`, corre en milisegundos. Recién ahora el ciclo de TDD es lo bastante rápido
  como para ser un ciclo.
- **`strictTemplates`**, `HttpClient` sobre `fetch` (`FetchBackend` es ahora el default y deprecó
  `withFetch()`) y TypeScript 6 son la base.

---

## La arquitectura: features afuera, capas adentro

**Primero la feature, después la capa**, y **una sola regla de dependencia: todo apunta hacia
adentro**. `domain/` no importa nada — y mucho menos `@angular/*`.

```
src/app/orders/          ← una feature (un contexto acotado), no un rol técnico
  domain/                entes, value objects, puertos (interfaces)   ← cero imports de @angular/*
  application/           casos de uso: orquestan entes a través de puertos
  data-access/           adaptadores HTTP/storage + mapeadores de DTO — implementan los puertos
  feat-order-list/       páginas ruteadas
  ui-order-card/         componentes presentacionales
src/app/shared/          depende solo de shared, así no se pueden formar ciclos
```

En un monorepo cada uno de esos directorios pasa a ser una librería y su nombre pasa a ser un tag.

Los nombres `data-access`, `feat-*` y `ui-*` son [la taxonomía convencional de Nx](https://nx.dev/blog/architecting-angular-applications);
`domain/` y `application/` **no**. Nx mete a los dos dentro de `data-access`, que define como
"comunicación con la API y gestión de estado" — una taxonomía sin ningún casillero para los entes, que
es exactamente el mecanismo por el cual el DTO termina siendo el tipo de dominio. Agregar esas dos
capas es el desacuerdo deliberado de este documento, y la razón por la que existe.

### Hacelo cumplir mecánicamente

Una regla de fronteras que rompe el build vale más que un párrafo en una wiki. Dos herramientas, la
misma idea: **Sheriff** para una app sola, **module boundaries de Nx** para un monorepo. Con Nx,
etiquetá cada librería dos veces —por scope y por tipo— y la regla de dependencia se vuelve una regla
de lint:

| Tag | Puede depender de |
| --- | ----------------- |
| `type:domain` | **nada** |
| `type:application` | `type:domain` |
| `type:data-access` | `type:application`, `type:domain` |
| `type:feature` | cualquier tipo, dentro de su propio scope |
| `type:ui` | `type:ui`, `type:domain` |
| `scope:shared` | solo `scope:shared` |

Que `type:domain` no dependa de nada es la regla que sostiene toda la arquitectura. El resto es
higiene.

### El dominio: entes completos y válidos (H1, H2, H3)

```ts
// orders/domain/Order.ts
export class Order {
  static placedBy(customer: Customer, lines: readonly OrderLine[]): Order {
    if (lines.length === 0) throw new OrderWithoutLines(customer);   // H3: fallar rápido
    return new Order(customer, lines);
  }

  private constructor(                                               // H2: no hay otra puerta de entrada
    private readonly customer: Customer,                             // H5: readonly
    private readonly lines: readonly OrderLine[],
  ) {}

  total(): Money {
    return this.lines.reduce((sum, line) => sum.plus(line.total()), Money.zeroIn(this.customer.currency()));
  }

  canBeCancelledBy(person: Person): boolean {                        // H6: tell, don't ask
    return this.customer.is(person) && this.isPending();
  }

  without(line: OrderLine): Order {                                  // H5: cambiar = objeto nuevo
    return new Order(this.customer, this.lines.filter((each) => each !== line));
  }
}
```

El **puerto** es una interfaz nombrada por el rol de dominio que cumple, no por su implementación
([14 — Nombramiento](14-nombramiento.md)):

```ts
// orders/domain/Orders.ts — clase abstracta, no interfaz: también hace de token de DI
export abstract class Orders {
  abstract placedBy(customer: Customer): Promise<readonly Order[]>;
  abstract add(order: Order): Promise<void>;
}
```

### La frontera: el DTO muere en el mapeador (H1)

Un solo lugar en toda la aplicación sabe cómo es el JSON:

```ts
// orders/data-access/HttpOrders.ts
@Service({ autoProvided: false })     // ← ver la nota de abajo; a este lo proveemos a mano
export class HttpOrders implements Orders {
  readonly #http = inject(HttpClient);

  async placedBy(customer: Customer): Promise<readonly Order[]> {
    const dtos = await firstValueFrom(
      this.#http.get<OrderDto[]>('/api/orders', { params: { customer: customer.id() } }),
    );
    return dtos.map(orderFrom);      // ← el DTO termina acá; nadie más arriba ve OrderDto
  }
}
```

El puerto se conecta con el adaptador una sola vez, en la raíz:
`{ provide: Orders, useClass: HttpOrders }` — los casos de uso dependen de `Orders`, nunca de
`HttpOrders`.

Dos detalles de v22 que muerden acá:

- **`@Service()` auto-provee en root.** Un adaptador que además atás a un puerto quedaría registrado dos
  veces: una como sí mismo y otra como `Orders`. Poné `@Service({ autoProvided: false })` (o un
  `@Injectable()` pelado) en todo lo que proveas a mano.
- Una `interface` de TypeScript desaparece en runtime y no puede ser token de DI; por eso el puerto es
  una clase abstracta. Un `InjectionToken<Orders>` también sirve, al costo de un segundo nombre para la
  misma idea.

### El estado remoto como objetos, no como `undefined` (H4)

`httpResource` expone una máquina de seis estados vía `status()`, más `isLoading()`, `error()`,
`hasValue()` y `value()`. Leerlos en el template desparrama esa máquina por tu HTML; modelá los estados
en su lugar:

```ts
// orders/application/RemoteOrders.ts — un objeto por estado, todos con el mismo protocolo
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

`hasValue()` es un type predicate, así que dentro de esa última rama `value()` se angosta a
`OrderDto[]` y el código compila con `strict`. Saltearlo —`resource.value().map(...)` justo después de
los chequeos de carga y error— no compila, y además reventaría en el estado `idle`, donde no está
cargando, no falló nada, y no hay valor. **`undefined` existe en exactamente una línea, dentro del
conversor, y nunca cruza hacia `application/` ni `domain/`.**

### Formularios: validar preguntándole al dominio (H3)

Los validadores de Signal Forms son funciones comunes —devuelven `null` si es válido y
`{ kind, message }` si no—, así que pueden delegar en vez de duplicar la regla:

```ts
// orders/feat-checkout/EmailField.ts
import { form, validate, FormField } from '@angular/forms/signals';

emailForm = form(this.model, (path) => {
  validate(path.email, ({ value }) =>
    EmailAddress.isValid(value()) ? null : { kind: 'email', message: 'No es una dirección válida' },
  );
});
```

La única fuente de verdad sobre qué es un email válido queda en `EmailAddress`. El formulario
pregunta; no vuelve a decidir. Y esa misma regla vale entonces para el payload REST, la importación de
CSV y el proceso batch — que es todo el punto de H3.

**Sobre `validateStandardSchema()`.** v22 te deja validar un campo contra un schema de Zod o Valibot.
Eso es un buen chequeo **de frontera** —forma, tipos, qué llegó por la red— y un mal lugar para las
reglas de dominio. Si el schema decide qué es una orden válida, ya tenés dos fuentes de verdad y H3 se
perdió. Schema en el borde, ente para la regla.

### Templates: hacer una pregunta, no cinco (H6)

```html
<!-- Mal: la regla de "esto se puede cancelar" ahora vive en HTML, en cada template que la necesite -->
@if (order().status === 'PENDING' && order().customerId === currentUser().id) { … }

<!-- Bien: -->
@if (cancellable()) { <button (click)="cancel()">Cancelar</button> }
```

```ts
readonly cancellable = computed(() => this.order().canBeCancelledBy(this.currentUser()));
```

El `computed` no es decoración: con OnPush se reevalúa solo cuando cambian `order` o `currentUser`, y
además le pone nombre a la pregunta.

---

## TDD con Vitest, alineado a las capas

El primer lugar donde el layering se paga solo es la suite de tests. Cada capa tiene un costo distinto
y una razón de ser distinta:

| Capa | Cómo se testea | Costo |
| ---- | -------------- | ----- |
| `domain/` | Vitest pelado. Sin `TestBed`, sin DOM, sin HTTP. **Acá vive la mayoría de tus tests.** | ~1 ms |
| `application/` | Casos de uso contra **fakes en memoria** de los puertos (`InMemoryOrders`). Tampoco hay `TestBed`. | ~ms |
| `data-access/` | El mapeador, directo. Un test por forma de DTO que realmente recibís. | ~ms |
| `feat-*/`, `ui-*/` | `TestBed` + harnesses, sobre comportamiento observable. **Pocos, y solo por lo que el componente agrega.** | ~100 ms |
| end-to-end | Una suite aparte, un puñado de recorridos críticos. | segundos |

**El ciclo.** Corré Vitest en modo watch. Rojo: el test más chico para el próximo comportamiento, y
tiene que fallar *por la razón correcta*. Verde: el código mínimo honesto. **Refactor: acá nace el ente
y acá se lo nombra**; saltearlo te deja una aplicación que funciona y no modela nada
([13 — TDD](13-tdd.md), [14 — Nombramiento](14-nombramiento.md)).

**Fakes, no mocks.** Un `InMemoryOrders` que realmente guarda órdenes te deja afirmar *qué pasó*; un
mock afirma *cómo lo llamaste* y suelda el test a la implementación. Tell, don't ask también aplica a
los tests.

**Zoneless cambia los tests de componentes.** Con zoneless por defecto, preferí
`await fixture.whenStable()` antes que los trucos de flush de zonas; las lecturas de señales son
sincrónicas después de `fixture.detectChanges()`. `fakeAsync` sigue funcionando con el patch de zone.js
para Vitest, pero necesitarlo suele ser señal de que esa lógica pertenece a una capa que no tiene
fixture.

**No testees:** el cableado de señales, la detección de cambios de Angular, los getters, ni que un
`computed` recalcule. Testeá la regla de dominio, y que el componente la muestre.

---

## Las excepciones, nombradas y contenidas

Cuatro lugares donde gana el framework. Cada uno está permitido *solo* en su capa, y eso es lo que
evita que se propague:

1. **Los componentes nacen vacíos (H2).** Inevitable: Angular es dueño de su ciclo de vida. Se contiene
   no dándoles reglas de dominio propias, declarando los inputs como `input.required<T>()`, y creando
   todo objeto de dominio completo en una factoría o un mapeador.
2. **Los DTOs son anémicos (H1).** Inevitable: son un formato de red, no un ente. Se contiene con el
   sufijo `Dto` y con vivir únicamente dentro de `data-access/`.
3. **`undefined` y `null` vienen de la API (H4).** `resource.value()` antes de cargar, `viewChild`,
   parámetros de ruta opcionales, la navegación segura en templates (ahora `undefined` en v22), y
   validadores que deben devolver `null` para decir "válido". Se contiene convirtiendo en la frontera,
   en un solo lugar por caso.
4. **Las señales son celdas mutables (H5).** Es a propósito: una señal modela "qué es lo actual", que
   genuinamente cambia. Se contiene guardando adentro **objetos de dominio inmutables**: hacé `set` de
   un objeto nuevo, nunca mutes el que está adentro.

Cualquier otra cosa que rompa una heurística no es una excepción: es una decisión de diseño que todavía
no tomaste.

---

## Checklist de olores

| Olor | Heurística | Qué suele significar |
| ---- | ---------- | -------------------- |
| `interface Order { id: string; total: number }` usada como tipo de dominio | H1 | El DTO se escapó del mapeador |
| Directorios de primer nivel `components/`, `services/`, `models/` | — | Cortaste por rol técnico; la feature no tiene casa |
| Reglas de negocio dentro de un `@if` en el template | H6 | Al ente le falta un mensaje |
| Un schema de Zod que decide qué es una orden válida | H3 | Un chequeo de frontera ascendido a regla de dominio |
| `Validators.required` duplicando una regla que el ente ya tiene | H3 | Dos fuentes de verdad sobre la validez |
| `value() ?? []`, cadenas de `?.` sobre datos remotos | H4 | Nunca se modeló el estado de carga |
| Un servicio con `#state = signal<Order \| null>(null)` y setters | H2/H4/H5 | Máquina de estados modelada como campo mutable nullable |
| `TestBed` en la mayoría de tus archivos de test | — | La lógica de dominio está viviendo en los componentes |
| `domain/` importando `@angular/core` | todas | El núcleo dejó de ser independiente |
| `ChangeDetectionStrategy.Eager` dejado por `ng update` | — | Una migración sin terminar, no una decisión |

---

## Principios para el desarrollo

1. **Cortá por feature primero y por capa adentro** — nunca directorios de primer nivel nombrados por
   rol técnico.
2. **Mantené `domain/` libre de `@angular/*`,** y hacelo cumplir con lint, no con disciplina.
3. **Que toda dependencia apunte hacia adentro:** feature/ui → application → domain; `data-access`
   implementa los puertos del dominio. Convertilo en una regla de tags que rompa el CI.
4. **Matá el DTO en el mapeador.** Un solo lugar conoce el formato de red.
5. **Nombrá los puertos por su rol de dominio** (`Orders`), no por su implementación (`OrderService`).
6. **Modelá los estados remotos como objetos,** para que `undefined` no cruce la frontera.
7. **Delegá la validación del formulario en el ente;** el formulario pregunta, no vuelve a decidir. Los
   schemas cuidan el borde, no la regla.
8. **Guardá objetos de dominio inmutables en las señales;** reemplazá, nunca mutes.
9. **Que el template haga una pregunta con nombre** (un `computed`), no cinco lecturas de campos.
10. **Poné la mayoría de los tests en `domain/`, sin `TestBed`,** y usá fakes en memoria para los puertos.
11. **Nunca te saltees el refactor** — es donde aparece el ente y donde se lo nombra.
12. **Sopesá el costo.** En una app chica, colapsar `application/` en un store de señales por feature es
    un trade-off legítimo; dejar que los entes se vuelvan registros anémicos, no.

---

## Fuera de alcance

Este documento cubre únicamente los lugares donde **el framework y el dominio no coinciden**. Todo lo
demás que una aplicación Angular también necesita, pero que no mueve la aguja de H1–H6 en ninguna
dirección, está ausente a propósito: NgRx Signal Store, SSR e hidratación incremental, micro frontends y
Native Federation, internacionalización, autenticación y autorización (OAuth 2 / OIDC), tooling de build
de monorepo más allá de las reglas de fronteras, y análisis forense de un código existente. El *Modern
Angular* de Steyer cubre todos esos temas; tomalo como volumen complementario, no como competencia.

Dos de ellos sí tocan el diseño, y vale nombrarlos:

- **SSR** exige que tu dominio nunca asuma que hay un browser. La regla de `domain/` —sin `@angular/*`,
  sin `window`, sin `document`— ya te lo da gratis. Si SSR se rompe por tu código de dominio, la
  frontera ya estaba filtrando.
- **Los micro frontends** no son una alternativa a esta estructura: son en lo que se convierte cuando
  una feature gana su propio equipo y su propio deploy. Cortar por feature primero es la precondición,
  que es la misma razón por la que es el principio #1.

---

## Glosario

| Término | Definición |
| ------- | ---------- |
| **Feature** | Un contexto acotado del dominio, y la unidad más externa de la estructura (`orders/`). |
| **Puerto** | Interfaz en `domain/` que nombra una colaboración que el dominio necesita (`Orders`). |
| **Adaptador** | Clase en `data-access/` que implementa un puerto con una tecnología real (`HttpOrders`). |
| **Mapeador** | La única función que convierte un DTO en un ente; la frontera del modelo. |
| **DTO** | Data Transfer Object: el formato de red. Anémico a propósito, confinado a `data-access/`. |
| **Tag** | Etiqueta sobre una librería (`scope:orders`, `type:domain`) que vuelve lint la regla de dependencia. |
| **Señal (signal)** | Celda reactiva mutable. Guarda "qué es lo actual"; su contenido debe ser inmutable. |
| **`httpResource`** | API estable en v22 que expone una lectura HTTP como señales `status()`/`isLoading()`/`error()`/`value()`. |
| **Signal Forms** | API de formularios estable en v22 (`@angular/forms/signals`); los validadores son funciones comunes. |
| **Zoneless** | Detección de cambios sin zone.js; default desde v21. La reactividad es explícita. |
| **Fake** | Implementación en memoria y funcional de un puerto, usada en tests en lugar de un mock. |
| **Harness** | API de Angular para manejar un componente en tests a través de su comportamiento público. |

---

## Fuentes

- Documentación de Angular — style guide (lo único oficial sobre estructura de proyecto)
  https://angular.dev/style-guide ; `httpResource` https://angular.dev/guide/http/http-resource ;
  validación de Signal Forms https://angular.dev/guide/forms/signals/validation
- Equipo de Angular, *Angular skills for AI agents* — https://github.com/angular/skills
- ANGULARarchitects, *Angular 22: The Most Important New Features at a Glance* —
  https://www.angulararchitects.io/en/blog/angular-22-the-most-important-new-features-at-a-glance/
- Nx, *Architecting Angular Applications* — https://nx.dev/blog/architecting-angular-applications
  (corte feature-first, la taxonomía `feat`/`ui`/`data-access`, doble etiquetado)
- Manfred Steyer, *Modern Angular: Architecture, Concepts, Implementation* (2026) — vertical slicing,
  modulith, hacer cumplir las fronteras con Sheriff.
- Ninja Squad, *What's new in Angular 22.0* — https://blog.ninja-squad.com/2026/06/03/what-is-new-angular-22.0
- Alistair Cockburn, *Hexagonal Architecture (Ports and Adapters)* (2005).
- Steve Freeman & Nat Pryce, *Growing Object-Oriented Software, Guided by Tests* (2009) — fakes en vez
  de mocks, TDD outside-in.
- Esta guía: [07 — H1](07-h1-objeto-por-ente.md) … [12 — H6](12-h6-encapsulamiento.md),
  [13 — TDD](13-tdd.md), [14 — Nombramiento](14-nombramiento.md).
