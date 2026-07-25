# Patrones estructurales

> **Propósito de este documento.** Definir los siete patrones estructurales orientándolos al marco
> H1–H6: cómo componer objetos sin perder fidelidad del dominio, encapsulamiento ni claridad del
> modelo.

---

## Definición operativa

> **Los patrones estructurales gobiernan la forma de conectar objetos** para que la estructura resultante
> sea expresiva para el dominio y barata de cambiar.

La pregunta central no es "cómo pego clases", sino: **qué dependencias permito**, **qué escondo** y
**dónde vive cada responsabilidad**.

Los siete: **Adapter**, **Bridge**, **Composite**, **Decorator**, **Facade**, **Flyweight**,
**Proxy**.

---

## Adapter

**Intención.** Convertir una interfaz existente en otra que el modelo necesita, sin contaminar el
núcleo del dominio con detalles externos.

**Presión de diseño.** Un servicio/librería externa no habla el lenguaje de tu dominio.

**Señales de uso.**

- Clases de dominio conocen tipos de SDK/framework.
- Mapeos repetidos repartidos en múltiples llamadas.
- Cambiar proveedor externo obliga cambios en reglas de negocio.

**Relación con heurísticas.**

- **H1:** protege la representación de entidades del dominio frente a formatos técnicos externos.
- **H6:** encapsula traducción y evita que clientes manipulen detalles de integración.

**Riesgo típico.** Usarlo para ocultar un mal modelo interno en lugar de corregirlo.

---

## Bridge

**Intención.** Separar dos ejes de variación que cambian de manera independiente.

**Presión de diseño.** Una jerarquía combina dimensiones distintas (p. ej. tipo de documento × canal de
entrega) y crece explosivamente.

**Señales de uso.**

- Multiplicación de subclases por combinatoria.
- Cambiar una dimensión rompe la otra.
- Mucho código duplicado con pequeñas variaciones.

**Relación con heurísticas.**

- **H1:** evita objetos que representan "dos entidades mezcladas" en una sola clase gigante.
- **H6:** mantiene responsabilidades separadas y colaboración explícita por composición.

**Riesgo típico.** Introducir Bridge sin dos ejes reales de variación.

---

## Composite

**Intención.** Modelar jerarquías parte–todo permitiendo tratar hoja y compuesto por un protocolo común.

**Presión de diseño.** El dominio tiene estructuras recursivas (carrito, árbol de menús, paquetes,
organigramas).

**Señales de uso.**

- Condicionales por tipo (si es hoja / si es contenedor) en muchos lugares.
- Lógica de agregación duplicada para casos simples y compuestos.
- Dificultad para agregar nuevos nodos sin tocar clientes.

**Relación con heurísticas.**

- **H1:** expresa explícitamente la entidad "compuesto" y la entidad "elemento", sin codificarla con
  primitivas o banderas.
- **H6:** clientes envían mensajes al nodo; no inspeccionan estructura interna del árbol.

**Riesgo típico.** Forzar una interfaz única cuando hojas y compuestos no comparten semántica real.

---

## Decorator

**Intención.** Añadir responsabilidades de forma incremental y componible, sin alterar la identidad del
objeto decorado.

**Presión de diseño.** Necesitas combinaciones dinámicas de comportamiento (validación, trazas,
cacheado, formato) sin explosión de subclases.

**Señales de uso.**

- Herencia con combinaciones (`ConLogYCacheYRetry...`).
- Responsabilidades transversales mezcladas con lógica de dominio.
- Necesidad de habilitar/deshabilitar comportamiento en runtime.

**Relación con heurísticas.**

- **H6:** conserva encapsulamiento: el cliente sigue hablando al mismo protocolo.
- **H1:** evita meter múltiples entidades técnicas en la misma clase de dominio.

**Riesgo típico.** Cadenas de decoradores opacas que dificultan trazabilidad y depuración.

---

## Facade

**Intención.** Exponer una entrada de alto nivel a un subsistema complejo, alineada con casos de uso
reales.

**Presión de diseño.** El cliente necesita resolver una tarea de negocio y hoy debe orquestar muchos
pasos técnicos.

**Señales de uso.**

- Clientes conocen demasiadas clases internas del subsistema.
- Secuencias de llamadas repetidas para la misma operación.
- Cambios internos propagan rupturas externas.

**Relación con heurísticas.**

- **H6:** concentra responsabilidades de orquestación y reduce acoplamiento estructural.
- **H1:** la fachada puede expresar operaciones de dominio en vez de pasos técnicos sueltos.

**Riesgo típico.** Transformarla en "objeto dios" con toda la lógica del sistema.

---

## Flyweight

**Intención.** Compartir estado invariante entre muchas instancias para reducir costo de memoria.

**Presión de diseño.** Gran volumen de objetos similares donde la mayoría del estado se repite.

**Señales de uso.**

- Perfil de memoria dominado por objetos repetitivos.
- Campos idénticos en miles/millones de instancias.
- La presión de GC/memoria afecta rendimiento.

**Relación con heurísticas.**

- **H5:** el estado compartido debe ser inmutable para no contaminar otras instancias.
- **H1:** separar estado intrínseco/extrínseco debe mantener una entidad clara por objeto.

**Riesgo típico.** Optimizar prematuramente y complicar el modelo sin evidencia de problema.

---

## Proxy

**Intención.** Interponer un representante con el mismo protocolo para controlar acceso al objeto real.

**Presión de diseño.** Necesitas políticas alrededor del acceso (lazy load, control de permisos,
telemetría, caché, remoto) sin modificar cliente ni objeto real.

**Señales de uso.**

- Inicialización costosa que no siempre se usa.
- Reglas de acceso repetidas en múltiples clientes.
- Integraciones remotas que deben parecer locales para el cliente.

**Relación con heurísticas.**

- **H6:** encapsula políticas de acceso sin exponer internals del objeto real.
- **H1:** evita que el cliente confunda "objeto real" con "mecanismo de acceso"; ambos tienen roles
  distintos.

**Riesgo típico.** Acumular demasiadas responsabilidades en el proxy y convertirlo en cuello de botella.

---

## Principios para el desarrollo

1. **Primero modela entidades y responsabilidades (H1/H6); luego elige estructura.**
2. **No confundas wrappers:** Adapter traduce, Decorator amplía, Proxy controla.
3. **Compón para desacoplar, no para esconder deuda.**
4. **Cualquier optimización estructural (Flyweight/Proxy) requiere evidencia operativa previa.**
5. **La estructura correcta reduce condicionales y preserva lenguaje de dominio en el código.**

---

## Glosario

- **Eje de variación** — dimensión de cambio independiente en el diseño.
- **Parte–todo** — relación jerárquica donde un compuesto contiene elementos del mismo protocolo.
- **Wrapper** — objeto que envuelve otro manteniendo/interponiendo el protocolo.
- **Estado intrínseco/extrínseco** — estado compartible vs. estado contextual por instancia.
- **Orquestación** — coordinación de varios colaboradores para ejecutar un caso de uso.

---

## Fuentes

- Alexander Shvets, *Dive Into Design Patterns*, Refactoring.Guru, 2022 — "Structural Design
  Patterns".
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable
  Object-Oriented Software*, Addison-Wesley, 1994.
- Documentos de heurísticas del repositorio: H1–H6 (`docs/es/07...12`).
