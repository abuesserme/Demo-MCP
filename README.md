# Demo MCP Connector (Mini Example)

This is a lightweight sample MCP connector that demonstrates the same flow we will use for the full Backstop integration. It includes a small FastAPI server, mock CRM data, simple authentication, and two tools: `search_accounts` and `get_account_details`.

The goal is to show how ChatGPT can call a backend service, fetch structured data, and receive a clean, simplified JSON response.

---

## Features

- Simple FastAPI MCP-style server
- Mock CRM data (JSON file)
- Token check (`Authorization: mock-token`)
- Clean, AI-friendly JSON responses
- Two demo tools:
  - `search_accounts`
  - `get_account_details`
- Local MCP manifest for ChatGPT integration

---

Here is the diagram.

                ┌────────────────────────┐
                │      ChatGPT User       │
                └─────────────┬───────────┘
                              │
                              ▼
                  ChatGPT MCP Interface
                              │
                              ▼
                ┌────────────────────────┐
                │   MCP Demo Connector    │
                │ (FastAPI Server)        │
                ├────────────────────────┤
                │ • Token Check           │
                │ • search_accounts       │
                │ • get_account_details   │
                │ • Simplified JSON       │
                └─────────────┬───────────┘
                              │
                              ▼
                ┌────────────────────────┐
                │      Mock CRM Data      │
                │     (JSON File)         │
                └────────────────────────┘
