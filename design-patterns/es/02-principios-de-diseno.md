# Principios de diseño de software

> **Propósito de este documento.** Enunciar los principios de diseño universales que motivan los
> patrones: tres principios fundamentales y los cinco principios SOLID. Léelos como heurísticas —
> guían, no ordenan. Los patrones del catálogo son en gran medida aplicaciones concretas de estas
> ideas.

---

## Definición operativa

> **Los principios de diseño son guías universales para hacer el software flexible, estable y fácil de
> entender.** Describen *cómo se ve el buen diseño*; los patrones son *formas reutilizables de
> lograrlo*.

El buen diseño suele caracterizarse por tres cualidades:

- **Reutilización de código** — reutilizar recorta costo y tiempo, pero suele elevar el acoplamiento;
  los patrones ayudan a reutilizar sin acoplar en exceso.
- **Extensibilidad** — el cambio es la única constante; diseña de modo que los nuevos requisitos se
  *añadan*, no se *parcheen*.
- **Bajo acoplamiento** — cuanto menos sabe cada parte de las demás, más fácil es cambiar el sistema.

---

## Tres principios fundamentales

### 1. Encapsular lo que varía

> Identifica los aspectos de tu programa que varían y sepáralos de lo que permanece igual.

El objetivo es aislar las partes que cambian para que un cambio afecte a menos código. Puedes
encapsular la variación **a nivel de método** (extrae la lógica cambiante a su propio método) o **a
nivel de clase** (extráela a su propia clase). Esto minimiza el "radio de impacto" de un cambio y
mantiene estable el resto del sistema.

*Ejemplo.* Sacar el cálculo de impuestos de una clase `Order` hacia un objeto dedicado hace que
cambiar las reglas de impuestos nunca toque `Order`.

### 2. Programar hacia una interfaz, no hacia una implementación

> Depende de abstracciones, no de clases concretas.

Tu código es más flexible cuando colabora a través de interfaces (tipos abstractos) en lugar de clases
concretas. Entonces cualquier objeto que satisfaga la interfaz es intercambiable, y puedes añadir
nuevas implementaciones sin tocar al cliente. Esta es la columna vertebral de la mayoría de los
patrones.

### 3. Favorecer la composición sobre la herencia

> Construye comportamiento combinando objetos en lugar de extender clases.

La herencia es la forma más obvia de reutilizar código, pero tiene costos: una subclase no puede
reducir la interfaz de la superclase, los métodos redefinidos deben seguir siendo compatibles, la
herencia rompe el encapsulamiento, y las jerarquías profundas se vuelven rígidas. La **composición** —
que un objeto contenga referencias a otros y les delegue trabajo — suele ser más flexible: puedes
intercambiar colaboradores en tiempo de ejecución y cambiar comportamiento sin recablear una jerarquía
de clases.

---

## Principios SOLID

Cinco principios introducidos por Robert C. Martin para hacer los diseños más comprensibles,
flexibles y mantenibles. Trátalos como heurísticas, no como leyes — perseguidos dogmáticamente pueden
producir complejidad innecesaria.

### S — Responsabilidad Única

> Una clase debe tener una sola razón para cambiar.

Mantén cada clase enfocada en una sola responsabilidad. Cuando una clase hace varias cosas, un cambio
en una preocupación arriesga romper las otras.

### O — Abierto/Cerrado

> Las clases deben estar abiertas a la extensión pero cerradas a la modificación.

Deberías poder añadir nuevo comportamiento (extender) sin alterar el código existente que ya funciona
(modificar). Esto se corresponde directamente con el ideal de modelado de *añadir* un nuevo caso del
dominio en lugar de parchear. El patrón Strategy es una forma clásica de lograrlo.

### L — Sustitución de Liskov

> Los subtipos deben poder sustituir a sus tipos base.

Una subclase debe poder usarse en cualquier lugar donde se espere su padre, sin romper al cliente.
Requisitos: los tipos de parámetros no más estrictos, los tipos de retorno no más amplios, ninguna
excepción nueva que el padre no lance, y las precondiciones no reforzadas / postcondiciones no
debilitadas.

### I — Segregación de Interfaces

> Los clientes no deben verse forzados a depender de métodos que no usan.

Divide interfaces anchas y "gordas" en otras más estrechas y específicas, para que una clase
implemente solo los métodos que tienen sentido para ella.

### D — Inversión de Dependencias

> Las clases de alto nivel no deben depender de las de bajo nivel. Ambas deben depender de
> abstracciones.

Depende de abstracciones en lugar de implementaciones concretas, para que la lógica de negocio (alto
nivel) no quede atada a los detalles (bajo nivel). Combinado con "programar hacia una interfaz",
mantiene estables las partes importantes del sistema mientras los detalles cambian.

---

## Principios para el desarrollo

1. **Aísla lo que cambia.** Antes de elegir un patrón, pregúntate *¿qué varía aquí?* y encapsúlalo.
2. **Depende de abstracciones.** Programa hacia interfaces para que los colaboradores sean
   intercambiables.
3. **Prefiere la composición** para reutilizar con flexibilidad; usa herencia para relaciones "es-un"
   genuinas.
4. **Aplica SOLID como guía,** no como una lista que cumplir mecánicamente.
5. **Estos principios sirven al modelo.** Existen para mantenerlo fiel, habitable y barato de cambiar —
   no por sí mismos.

---

## Glosario

- **Encapsular lo que varía** — separar las partes cambiantes de las estables.
- **Programar hacia una interfaz** — depender de un tipo abstracto, no de una clase concreta.
- **Composición** — construir comportamiento conteniendo y delegando a otros objetos.
- **SOLID** — Responsabilidad Única, Abierto/Cerrado, Sustitución de Liskov, Segregación de
  Interfaces, Inversión de Dependencias.
- **Acoplamiento** — el grado en que una parte depende de otra; el bajo acoplamiento es el objetivo.

---

## Fuentes

- Alexander Shvets, *Dive Into Design Patterns*, Refactoring.Guru, 2022 — "Features of Good Design",
  "Design Principles" y "SOLID Principles".
- Robert C. Martin, *Agile Software Development, Principles, Patterns, and Practices*, Prentice Hall,
  2002.
