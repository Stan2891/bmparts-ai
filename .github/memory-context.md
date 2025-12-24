# 🧠 BMParts Memory Context
> Auto-synced: 2025-12-24 18:38 | Total: 145 memories

---

## Business Context
- Stan owns BMParts, an automotive parts import, retail, wholesale, and ecommerce business.
- Stan uses Zoho Inventory Org ID 856737871.
- Stan runs BMParts’ website on https://www.bmparts.co.za.
- Stan uses WooCommerce, Zoho Flow, UDM Pro, Ubuntu servers, and supplier APIs.
- Spares to Africa is involved in imports and supply chain operations for BMParts.
- Stan wants to maintain automation reliability across Zoho, WooCommerce, API integrations, and stock rules.
- The system must track discount logic, promotion effectiveness, and cross-channel performance for BMParts and Spares to Africa.
- BMParts uses AI systems for operational decisions.
- WooCommerce reflects live stock for online buyers.
- Zoho Inventory warehouses sync to WooCommerce stock.
- BMParts uses real-world margin protection rules.
- BMParts uses system logs for debugging automations.
- Spares to Africa (Pty) Ltd - Registration: 2018/023532/07 - Director: Stanislav Andreev - Zoho Org ID: 857295887 - Plan: Finance Plus - Apps: Books, Inventory, CRM, Flow - Role: Importer, supplier, upstream stock holder feeding BMParts
- Spares to Africa Zoho IDs - COGS Account ID: 5368452000000034003 - Head Office Location ID: 5368452000000239023 - Default Warehouse: Head Office
- BMParts - Website: https://www.bmparts.co.za - Zoho Org ID: 856737871 - Apps: Inventory, Books, Flow - Warehouses: WEB, VIRTUAL, SPECIAL SALE ITEM - Role: Retail, wholesale, online sales

---

## Infrastructure
- Low priority: Old ngrok URL was abc123.ngrok.io - deprecated
- NETWORK TOPOLOGY REFERENCE - UDM Pro gateway. VLANs: br3=192.168.10.x (main home WiFi), br4=192.168.80.x (server VLAN), br7=192.168.6.x (Quarantine VLAN created during incident). Server stan-S600 at 192.168.80.2. Shop network uses 192.168.220.x with MikroTik wireless bridge. WireGuard VPN clients get 192.168.4.x IPs.
- Voice Conversation Setup (2025-12-15): Deployed OpenAI Realtime API for voice chat. Components: 1) realtime-proxy at /opt/gpt-app/realtime-proxy/server.js (port 9002), 2) gpt-realtime.service systemd unit, 3) voice-enabled frontend at /var/www/gpt/index.html, 4) backup at index-text-only.html. Architecture: Browser WebSocket to nginx:80/realtime to gpt-realtime:9002 to OpenAI Realtime API. Cost ~$0.06/min. Current limitation: voice mode has no access to memory/WooCommerce/Zoho tools - uses standalone OpenAI. Pending upgrade: Hybrid mode (Whisper STT + gpt-app backend + OpenAI TTS) for full tool access. Testing issue: WAN timeout, likely router port forwarding problem (port 80 to 192.168.80.2).
- Dec 21 2025 Session: Restored GitHub Copilot MCP setup after port hardening. Key fixes: 1) nginx gateway changed from 127.0.0.1:8888 to 0.0.0.0:8888, 2) copilot-mcp.json updated to http://gpt-api.sparestoafrica.co.za/mcp, 3) copilot-instructions.md restored to Dec 20 version with MCP endpoint and service table. GitHub.com Copilot does NOT support MCP - only VS Code Copilot does. Memory MCP server on port 9092 working.
- Memory MCP server deployed on port 9092 for GitHub Copilot integration - Dec 20, 2025
- Memory MCP Server deployed on port 9092 (Dec 20, 2025). Enables GitHub Copilot to search and save memories via MCP protocol. Endpoints: /mcp (JSON-RPC), /mcp/tools, /mcp/health. External URL: http://gpt-api.sparestoafrica.co.za/mcp. Tools: memory_search, memory_save, memory_stats. Syncs Vandamchik (VS Code) with GitHub Copilot.
- GitHub Copilot on github.com now connected to shared memory via Memory MCP Server (port 9092). Same memory as Vandamchik in VS Code.
- MCP Configuration Updated 2025-12-22: Zoho MCP at https://sparestoafrica.ngrok.app/mcp/v1 (paid stable domain), Memory MCP at http://localhost:9092/mcp. ngrok runs as systemd service ngrok-mcp on port 9091.

---

## Rules & Preferences
- Stan prefers concise, technical, high-impact answers with engineering logic.
- Stan prefers production-ready code with explicit variables and parameters.
- Stan wants full context retention, proactive reasoning, and memory continuity.
- Stan wants all explanations to use section headers, bullet points, and end with next steps.
- Stan prefers answers optimized for real-world operational behaviour, not theory.
- Stan wants tasks and long-term projects tracked persistently via memory.
- ChatGPT must remember key numbers, IDs, warehouse names, and configuration details accurately.
- Stan wants to maintain automation reliability across Zoho, WooCommerce, API integrations, and stock rules.
- Stan wants persistent workload automation and proactive monitoring features active.
- Stan prefers answers with early root cause detection and minimal troubleshooting loops.
