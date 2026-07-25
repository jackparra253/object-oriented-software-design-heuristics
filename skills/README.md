# Skills — Auto-Construcción de Grafo Semántico (MCP)

Catálogo de *skills* (habilidades reutilizables) para orquestar un flujo autónomo que lee este
repositorio desde GitHub y construye, en tiempo real, un **grafo de conocimiento** con las
heurísticas y patrones de diseño documentados aquí.

La arquitectura es **multi-servidor MCP** (Model Context Protocol):

- **Cliente de IA** (Claude Desktop, Cursor, VS Code + Copilot) → *cerebro / orquestador*.
- **Servidor MCP de GitHub** → *ojos* (extracción de archivos del repositorio).
- **Servidor MCP de Grafos (Memory / Knowledge Graph)** → *manos* (mutación y almacenamiento
  estructurado del conocimiento).

```
        ┌───────────────────────────┐
        │      Cliente de IA        │  (orquestador)
        │  Claude / Cursor / Copilot│
        └────────┬─────────┬────────┘
                 │         │
     get_file_*  │         │  create_nodes / create_edges
                 ▼         ▼
   ┌──────────────────┐  ┌───────────────────────────┐
   │ github-extractor │  │ knowledge-graph-memory    │
   │  (lee el repo)   │  │  (persiste el grafo)      │
   └──────────────────┘  └───────────────────────────┘
```

## Catálogo de skills

| Skill                          | Propósito                                                   | Archivo                                                      |
| ------------------------------ | ---------------------------------------------------------- | ----------------------------------------------------------- |
| Constructor de grafo semántico | Leer el repo y poblar el grafo de conocimiento (ontología) | [`graph-builder/SKILL.md`](graph-builder/SKILL.md)          |
| Ontología del grafo            | Tipos de nodos y relaciones permitidos                     | [`graph-builder/ontology.md`](graph-builder/ontology.md)    |
| Consultas al grafo             | Preguntas típicas para explotar el grafo ya construido      | [`graph-query/SKILL.md`](graph-query/SKILL.md)              |

## Configuración

- Configuración multi-servidor MCP lista para usar: [`mcp/`](mcp/).
  - [`mcp/claude_desktop_config.json`](mcp/claude_desktop_config.json)
  - [`mcp/vscode-mcp.json`](mcp/vscode-mcp.json)
- Requisitos y puesta en marcha: [`SETUP.md`](SETUP.md).

## Cómo se usa (resumen)

1. Registra ambos servidores MCP en tu cliente (ver [`SETUP.md`](SETUP.md)).
2. Carga el skill `graph-builder` como contexto del agente.
3. Da la orden de ejecución, por ejemplo:
   > "Ejecuta el plan para `docs/es/10-h4-no-usar-null.md` y `docs/es/11-h5-objetos-inmutables.md`".
4. El agente lee vía `github-extractor` y muta el grafo vía `knowledge-graph-memory`, de forma
   autónoma.
5. Consulta el grafo con el skill `graph-query`.

## Alineación con las heurísticas del repositorio

Este catálogo aplica las mismas heurísticas que documenta el repo:

- **H1 — un objeto por ente:** un nodo por entidad; nunca dupliques conceptos.
- **H3 — solo entidades válidas:** no crees nodos/aristas fuera de la ontología.
- **Nombramiento:** nombra las entidades por lo que son en el dominio.
