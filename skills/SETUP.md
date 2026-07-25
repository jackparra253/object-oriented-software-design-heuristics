# Puesta en marcha — Arquitectura multi-servidor MCP

Guía para configurar el entorno que ejecuta el pipeline de auto-construcción del grafo de
conocimiento a partir de este repositorio.

---

## 1. Requisitos previos

- **Docker** — para el servidor MCP de GitHub (imagen oficial).
- **uv / uvx** (o Node.js según el servidor de grafos que elijas) — para el servidor de grafos.
- Un **Personal Access Token (PAT)** de GitHub con permiso de lectura del repositorio.
- Un cliente de IA con soporte MCP: **Claude Desktop**, **Cursor** o **VS Code + GitHub Copilot**.

---

## 2. Registrar ambos servidores MCP

Registra los dos servidores **simultáneamente** en el archivo de configuración de tu cliente.

- **Claude Desktop / Cursor:** usa [`mcp/claude_desktop_config.json`](mcp/claude_desktop_config.json).
- **VS Code + Copilot:** usa [`mcp/vscode-mcp.json`](mcp/vscode-mcp.json) (colócalo como
  `.vscode/mcp.json` en tu workspace).

> **Seguridad:** nunca comitees tu token real. Sustituye `REEMPLAZA_CON_TU_TOKEN` por tu PAT en la
> configuración **local**, o usa variables de entorno / un gestor de secretos.

### Servidor de grafos: dos opciones

1. **Estándar (comunidad) — SQLite / Memory:** rápido y sin infraestructura. Es el que traen los
   archivos de ejemplo (`knowledge-graph-memory`).
2. **Empresarial — Neo4j:** sustituye el bloque `knowledge-graph-memory` por el contenedor
   `neo4j-mcp-server` asignando la URI, usuario y contraseña de tu base de datos.

---

## 3. Cargar el skill del agente

Carga el contenido de [`graph-builder/SKILL.md`](graph-builder/SKILL.md) como contexto/sistema del
agente (o pégalo al inicio del chat). Ese skill contiene la **ontología estricta** y el **ciclo de
ejecución autónomo**.

---

## 4. Ejecutar

Da la orden al agente indicando qué archivos procesar, por ejemplo:

> "Ejecuta el plan para `docs/es/10-h4-no-usar-null.md` y `docs/es/11-h5-objetos-inmutables.md`."

El agente:

1. **Lee** cada archivo con `github-extractor → get_file_contents`.
2. **Extrae** entidades según la ontología.
3. **Muta** el grafo con `knowledge-graph-memory → create_nodes` y `create_edges`.
4. **Verifica** que no se dupliquen nodos (reutiliza los existentes).

---

## 5. Verificar y consultar

Usa el skill [`graph-query/SKILL.md`](graph-query/SKILL.md) para hacer preguntas al grafo ya
construido (p. ej. "¿qué problemas previene H4?").

---

## 6. Datos del repositorio de origen

- **owner:** `jackparra253`
- **repo:** `object-oriented-software-design-heuristics`
- **rutas objetivo:** `docs/es/`, `docs/en/`, `design-patterns/es/`, `design-patterns/en/`
