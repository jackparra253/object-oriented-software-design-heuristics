# Patrones creacionales

> **Propósito de este documento.** Definir los cinco patrones creacionales con foco en *decisiones de
> modelado* y su relación con las heurísticas H1–H6. Para cada patrón: intención, presión de diseño,
> señales de uso, riesgos y vínculo explícito con el modelo fiel.

---

## Definición operativa

> **Los patrones creacionales controlan cómo nace un objeto del modelo** para que su creación no
> degrade la fidelidad del dominio ni el encapsulamiento.

No son solo "formas de instanciar": son mecanismos para decidir **quién crea**, **con qué invariantes**
y **con qué acoplamiento** se crea.

Los cinco: **Factory Method**, **Abstract Factory**, **Builder**, **Prototype**, **Singleton**.

---

## Factory Method

**Intención.** Delegar la decisión del tipo concreto a subclases, manteniendo al cliente acoplado a
una abstracción de producto.

**Presión de diseño.** El cliente conoce *qué necesita* (capacidad/protocolo) pero no debería conocer
*qué clase exacta* lo implementa.

**Señales de uso.**

- Hay `new` repetidos en lógica de negocio para escoger variantes.
- Cada variante cambia en momentos distintos, forzando cambios transversales.
- Quieres extender familias de productos sin tocar el flujo principal.

**Relación con heurísticas.**

- **H1 (objeto por ente):** ayuda a crear el objeto correcto para la entidad correcta, evitando
  primitivas "marcadoras" para diferenciar variantes.
- **H3 (solo objetos válidos):** la fábrica puede centralizar validación e impedir construcciones
  inválidas.
- **H6 (encapsulamiento):** encapsula la política de creación; el cliente "pide", no "pregunta y
  construye".

**Riesgo típico.** Convertir cada creación trivial en fábrica, añadiendo capas sin presión real.

---

## Abstract Factory

**Intención.** Crear *familias coherentes* de objetos relacionados que deben evolucionar juntas.

**Presión de diseño.** Existen variantes de un mismo sistema (tema/UI, proveedor, entorno, país,
reglas de negocio) y mezclar productos de familias distintas rompe consistencia.

**Señales de uso.**

- El sistema produce varios objetos que colaboran y deben ser compatibles entre sí.
- Hay condicionales de variante repetidos para cada objeto de la familia.
- Un cambio de "familia" debería ser una decisión de composición, no un refactor transversal.

**Relación con heurísticas.**

- **H1:** mantiene correspondencia clara entre entidad de dominio y tipo concreto por contexto.
- **H2/H3:** fuerza creación completa y válida por familia; evita ensamblajes mixtos inválidos.
- **H6:** evita que clientes inspeccionen variantes internas para decidir manualmente.

**Riesgo típico.** Sobre-modelar: muchas interfaces/fábricas para un dominio que aún no tiene
variantes reales.

---

## Builder

**Intención.** Construir objetos complejos paso a paso sin exponer estados intermedios inválidos al
cliente.

**Presión de diseño.** Un agregado requiere múltiples piezas, orden de construcción, validaciones y
opcionalidad controlada.

**Señales de uso.**

- Constructor telescópico o explosión de constructores sobrecargados.
- Objetos que hoy "nacen a medias" y luego se completan con setters.
- Reglas de validez que dependen de combinaciones de campos.

**Relación con heurísticas.**

- **H2 (objetos completos):** Builder evita objetos incompletos visibles.
- **H3 (objetos válidos):** `build()` es la frontera para verificar invariantes y fallar rápido.
- **H5 (inmutabilidad):** favorece crear una instancia final inmutable en lugar de mutarla paso a
  paso.

**Riesgo típico.** Usar Builder para objetos simples y terminar con API más verbosa que el problema.

---

## Prototype

**Intención.** Crear nuevos objetos a partir de copias de prototipos existentes, ocultando la clase
concreta y el detalle de clonación.

**Presión de diseño.** Inicializar ciertos objetos es costoso o complejo; copiar una plantilla válida
es más seguro que recrear manualmente.

**Señales de uso.**

- Configuraciones base que se repiten con pequeñas variaciones.
- Construcción cara (cálculos, carga de metadatos, armado de estructuras).
- Necesidad de duplicar preservando reglas internas sin exponer estado privado.

**Relación con heurísticas.**

- **H1:** cada clon sigue representando una entidad concreta (no "copias ambiguas").
- **H3:** una clonación correcta debe preservar invariantes del objeto origen.
- **H6:** la copia la decide el propio objeto/prototipo; el cliente no manipula internals.

**Riesgo típico.** Clonado superficial accidental compartiendo referencias mutables y rompiendo validez.

---

## Singleton

**Intención.** Garantizar una única instancia de un colaborador cuando esa unicidad es requisito del
dominio o de infraestructura.

**Presión de diseño.** Debe existir exactamente un punto coordinador/servicio y su identidad única es
semánticamente relevante.

**Señales de uso (pocas y fuertes).**

- La unicidad es una regla explícita del sistema, no una conveniencia técnica.
- Hay coordinación global real que no puede resolverse por composición del grafo de objetos.

**Relación con heurísticas.**

- **H1:** fácil violarlo si Singleton pasa a representar "muchas cosas" del dominio.
- **H6:** puede romper encapsulamiento al convertirse en dependencia implícita global.
- **H5:** en la práctica se vuelve estado mutable compartido, aumentando acoplamiento temporal.

**Riesgo típico (alto).** Variable global disfrazada, difícil de testear, acoplamiento oculto,
contención en concurrencia. **Preferir inyección de dependencias** y composición explícita salvo
necesidad estricta.

---

## Principios para el desarrollo

1. **Diseña la creación como parte del modelo, no como detalle técnico.**
2. **Si la creación permite estados inválidos, prioriza Builder/fábricas con validación centralizada**
   (H2/H3).
3. **No uses patrones para ocultar un modelo pobre.** Primero corrige la representación de entidades
   (H1), luego elige mecanismo de creación.
4. **Evita estado global mutable.** Singleton solo con justificación de dominio/infraestructura fuerte.
5. **En cualquier patrón creacional, el cliente debe pedir capacidades, no ensamblar internals** (H6).

---

## Glosario

- **Presión de diseño** — fuerza recurrente que justifica un patrón.
- **Política de creación** — reglas de qué se crea, cuándo y con qué invariantes.
- **Constructor telescópico** — constructor con demasiados parámetros opcionales o ambiguos.
- **Clonado superficial/profundo** — copia de referencias vs. copia independiente de estructura.
- **Dependencia implícita global** — colaboración no declarada en la interfaz pública.

---

## Fuentes

- Alexander Shvets, *Dive Into Design Patterns*, Refactoring.Guru, 2022 — "Creational Design
  Patterns".
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable
  Object-Oriented Software*, Addison-Wesley, 1994.
- Documentos de heurísticas del repositorio: H1–H6 (`docs/es/07...12`).
