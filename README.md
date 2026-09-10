# Simple Agent Practice

A basic hands-on exercise demonstrating core agent-building concepts:
- **Tool** (ADK pattern): a simple function that performs an action
- **State & Nodes** (LangGraph pattern): a dictionary passed through step-by-step functions

## What it does
Checks inventory stock for an item (e.g., "laptop") based on a simulated user query, and returns the result.

## How to run
\`\`\`bash
uv venv
uv run agent.py
\`\`\`

## Project structure
- `agent.py` — the main script containing the tool and node functions