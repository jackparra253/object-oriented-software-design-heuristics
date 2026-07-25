# Patrones de comportamiento

> **Propósito de este documento.** Definir los once patrones de comportamiento con foco en el reparto
> de responsabilidades del modelo y su coherencia con H1–H6. Para cada patrón: intención, presión de
> diseño, señales de uso, relación con heurísticas y riesgo de sobreuso.

---

## Definición operativa

> **Los patrones de comportamiento estructuran conversaciones entre objetos** para que las reglas vivan
> en quien corresponde y el cambio no se propague caóticamente.

La pregunta clave es: **quién decide**, **quién ejecuta** y **quién conoce qué**.

Los once: **Chain of Responsibility**, **Command**, **Iterator**, **Mediator**, **Memento**,
**Observer**, **State**, **Strategy**, **Template Method**, **Visitor**.

---

## Chain of Responsibility

**Intención.** Encadenar responsables potenciales de una solicitud, desacoplando emisor y receptor
final.

**Presión de diseño.** La decisión de "quién atiende" varía por contexto (prioridad, reglas,
configuración).

**Señales de uso.**

- `if/else` largos para seleccionar manejador.
- Reglas de encaminamiento que cambian seguido.
- Necesidad de insertar/quitar políticas sin reescribir flujo.

**Relación con heurísticas.**

- **H6:** el emisor no inspecciona internals de cada manejador.
- **H1:** cada handler representa una responsabilidad concreta, no múltiples reglas mezcladas.

**Riesgo típico.** Cadenas opacas sin trazabilidad de quién resolvió la solicitud.

---

## Command

**Intención.** Tratar una acción como objeto de dominio/técnico con identidad, datos y ciclo de vida.

**Presión de diseño.** Necesitas registrar, encolar, reintentar, deshacer o auditar acciones.

**Señales de uso.**

- Operaciones de UI/aplicación acopladas directamente a invocaciones de servicio.
- Lógica de undo/redo dispersa por múltiples clases.
- Requisitos de auditoría o procesamiento asíncrono.

**Relación con heurísticas.**

- **H1:** una acción relevante pasa a ser entidad explícita (no primitives sueltas).
- **H2/H3:** un Command bien diseñado se crea completo y válido antes de ejecutarse.

**Riesgo típico.** Proliferación de comandos triviales sin necesidad de desacople/ciclo de vida.

---

## Iterator

**Intención.** Exponer recorrido sin revelar estructura interna ni reglas de almacenamiento.

**Presión de diseño.** El cliente necesita iterar, pero no debe conocer representación ni invariantes
internos de la colección.

**Señales de uso.**

- Clientes acceden índices/campos internos de colecciones.
- Múltiples algoritmos de recorrido duplicados.
- Cambios de estructura interna rompen consumidores.

**Relación con heurísticas.**

- **H6:** protege encapsulamiento de la colección.
- **H5:** recorridos sobre colecciones inmutables simplifican consistencia temporal.

**Riesgo típico.** Exponer iteradores que filtran internals y permiten modificaciones inválidas.

---

## Mediator

**Intención.** Centralizar protocolos de colaboración para reducir acoplamiento en malla.

**Presión de diseño.** Objetos conversan todos con todos; cada cambio local dispara cambios globales.

**Señales de uso.**

- Componentes UI/proceso con referencias cruzadas múltiples.
- Reutilización casi imposible por dependencias laterales.
- Efectos secundarios inesperados ante cambios pequeños.

**Relación con heurísticas.**

- **H6:** la coordinación vive en el mediador, no en internals compartidos entre colegas.
- **H1:** cada participante conserva su entidad/responsabilidad principal.

**Riesgo típico.** Mediador "objeto dios" que concentra demasiada lógica de negocio.

---

## Memento

**Intención.** Capturar y restaurar estado relevante sin exponer representación interna.

**Presión de diseño.** Necesitas historial, checkpoints o rollback preservando encapsulación.

**Señales de uso.**

- Implementaciones de undo que leen/escriben campos privados desde fuera.
- Lógica de snapshot duplicada en clientes.
- Errores por restauraciones parciales.

**Relación con heurísticas.**

- **H6:** patrón directamente alineado: no se rompen internals para persistir estado.
- **H3:** restaurar debe respetar invariantes del objeto originador.

**Riesgo típico.** Snapshot excesivo (memoria) o snapshot incompleto (inconsistencia).

---

## Observer

**Intención.** Publicar cambios de estado/eventos a suscriptores sin acoplar emisor a consumidores
concretos.

**Presión de diseño.** Una entidad dispara reacciones múltiples y cambiantes.

**Señales de uso.**

- Llamadas directas en cascada a muchos dependientes.
- Nuevos consumidores obligan modificar el emisor.
- Necesidad de suscribir/desuscribir dinámicamente.

**Relación con heurísticas.**

- **H6:** el sujeto anuncia hechos; no conoce detalle interno de observadores.
- **H1:** eventos deben representar hechos de dominio claros, no banderas ambiguas.

**Riesgo típico.** Efectos colaterales difíciles de seguir por orden y concurrencia de notificaciones.

---

## State

**Intención.** Encapsular comportamientos por estado en objetos separados y delegar en el estado actual.

**Presión de diseño.** Un ciclo de vida con transiciones explícitas y reglas distintas por estado.

**Señales de uso.**

- `switch`/`if` extensos por estado en múltiples métodos.
- Transiciones dispersas y difíciles de validar.
- Añadir un estado nuevo obliga tocar muchas clases.

**Relación con heurísticas.**

- **H1:** el estado es una entidad del dominio (p. ej. PedidoPendiente, PedidoPagado), no una cadena.
- **H3:** cada transición valida invariantes y evita estados imposibles.

**Riesgo típico.** Multiplicar clases de estado cuando el ciclo real es simple.

---

## Strategy

**Intención.** Extraer algoritmos intercambiables detrás de un protocolo estable.

**Presión de diseño.** Variantes de cálculo/regla que cambian por contexto sin alterar flujo principal.

**Señales de uso.**

- Condicionales por tipo de algoritmo repartidos en el sistema.
- Nuevas variantes rompen código existente.
- Necesidad de configurar comportamiento por entorno o cliente.

**Relación con heurísticas.**

- **H6:** el contexto delega en la estrategia en lugar de inspeccionar datos para decidir externamente.
- **H1:** cada estrategia representa una política concreta y nombrada del dominio.

**Riesgo típico.** Crear estrategias para diferencias irrelevantes o de una sola línea.

---

## Template Method

**Intención.** Fijar la estructura de un algoritmo y dejar variaciones controladas en puntos de extensión.

**Presión de diseño.** Tienes procesos con esqueleto estable y pasos variables.

**Señales de uso.**

- Duplicación de algoritmos casi idénticos en subclases.
- Cambios de flujo global replicados manualmente.
- Necesidad de imponer orden de pasos y pre/postcondiciones.

**Relación con heurísticas.**

- **H6:** preserva encapsulamiento del flujo global en la superclase.
- **H3:** puntos de extensión pueden reforzar validaciones sin romper contrato general.

**Riesgo típico.** Jerarquías rígidas donde composición (Strategy) sería más flexible.

---

## Visitor

**Intención.** Añadir operaciones sobre una estructura estable de objetos sin modificar esas clases.

**Presión de diseño.** Los tipos de elementos cambian poco, pero las operaciones sobre ellos cambian
mucho.

**Señales de uso.**

- Nuevas operaciones obligan tocar todas las clases de elementos.
- Lógica transversal duplicada por tipo.
- Necesidad de separar reglas analíticas/reporting de entidades núcleo.

**Relación con heurísticas.**

- **H6:** puede preservar encapsulamiento si la interfaz visitable expone solo lo necesario.
- **H1:** evita inflar entidades con responsabilidades ajenas a su esencia.

**Riesgo típico.** Coste alto cuando cambian frecuentemente los tipos de elementos (rompe visitantes).

---

## Principios para el desarrollo

1. **Ubica la decisión donde pertenece el conocimiento del dominio** (H1/H6).
2. **Cuando veas condicionales por variante/estado, evalúa State o Strategy primero.**
3. **Si necesitas historial o reversión, protege invariantes con Memento + validación (H3).**
4. **Mensajes antes que extracción de datos:** favorece "decir" sobre "preguntar".
5. **No introduzcas un patrón de comportamiento sin presión real de cambio o colaboración.**

---

## Glosario

- **Conversación de objetos** — secuencia de mensajes entre colaboradores.
- **Política** — regla intercambiable que define cómo se ejecuta una decisión.
- **Transición de estado** — cambio válido entre estados del ciclo de vida.
- **Punto de extensión** — paso variable dentro de un algoritmo estable.
- **Acoplamiento en malla** — red de dependencias cruzadas difíciles de mantener.

---

## Fuentes

- Alexander Shvets, *Dive Into Design Patterns*, Refactoring.Guru, 2022 — "Behavioral Design
  Patterns".
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable
  Object-Oriented Software*, Addison-Wesley, 1994.
- Documentos de heurísticas del repositorio: H1–H6 (`docs/es/07...12`).
