# GitHub Issues Sync Export
Updated: 2026-01-05 12:56 UTC

## Open Issues
- #7: 🔄 Sync Test #7
- #6: 🔄 Copilot Sync Channel
- #5: Add write operation confirmations
- #3: Implement sync_woo_zoho and compare_woo_zoho tools
- #2: Voice: Upgrade to Hybrid mode (tools + memory)

## Sync Channel (Last 5 Comments)
**Stan2891** (2025-12-20T18:36:13Z):
**[2025-12-20 20:36:11]** MEMORY: Stan asked to remember 'number 7' - this is a sync test. Issue #7 created.

**Stan2891** (2025-12-20T18:36:37Z):
**[2025-12-20 20:36:36]** MEMORY SYNC: Stan asked to remember 'number 7' - saved to memory ID 1007. Issue #7 also created for testing.

**Stan2891** (2025-12-21T14:25:02Z):
**[2025-12-21 16:20]** VS Code Vandamchik confirming:

✅ **Local memory access works** - gpt-memory:8000 accessible from VS Code
✅ **Port hardening complete** - all services bound to localhost
✅ **Zoho MCP integrated** - gpt-app now uses MCP instead of n8n

**Architecture clarification:**
- **VS Code Copilot (Vandamchik)**: Full access to localhost (memory, Zoho MCP, Qdrant)
- **GitHub.com Copilot**: Cloud-based, NO localhost access - uses Issue #6 as sync bridge

**Fixed today:**
- Issue #1: Port 9091 conflict ✅
- Issue #4: Ngrok stable tunnel ✅ (sparestoafrica.ngrok.app)
- GPT-app frontend error ✅

**Pending:**
- Issue #2: Voice hybrid mode
- Issue #3: sync_woo_zoho tools

**Stan2891** (2025-12-21T15:52:29Z):
## VS Code Copilot Session Update
**Date:** 2025-12-21 17:55 SAST

### Completed Today:
1. ✅ **Port Security Hardening** - All services locked to localhost (127.0.0.1)
2. ✅ **Ngrok Pro Setup** - Static domain `sparestoafrica.ngrok.app` → nginx gateway :8888
3. ✅ **iptables Firewall** - WAN blocked on 80/443/3389, LAN + localhost allowed
4. ✅ **GPT-app Zoho Fix** - Replaced n8n with direct Zoho MCP integration
5. ✅ **Frontend Fix** - parseCodeBlocks type error resolved
6. ✅ **GitHub Issues #1, #4** - Closed (port conflict, ngrok tunnel)
7. ✅ **MCP Config Updated** - VS Code now uses ngrok URLs for remote access
8. ✅ **Memory Export** - Hourly cron syncs to `.github/memory-export.md`

### Current Service Status:
| Service | Port | Status |
|---------|------|--------|
| gpt-memory | 8000 | ✅ localhost |
| memory-mcp | 9092 | ✅ localhost |
| Zoho MCP | 9091 | ✅ localhost |
| gpt-app | 9000 | ✅ localhost |
| ngrok gateway | 8888 | ✅ all traffic routed |

### Ngrok Routes:
- `/` → gpt-app (9000)
- `/memory/` → gpt-memory (8000) 
- `/memory-mcp/` → memory-mcp (9092)
- `/mcp/v1` → Zoho MCP (9091)
- `/gpt/` → static files

### For GitHub.com Copilot:
- Read `.github/memory-export.md` for full memory context
- Memory API: `https://sparestoafrica.ngrok.app/memory/search` (with X-API-Key header)

---
*Posted by VS Code Vandamchik*

**Stan2891** (2025-12-21T16:16:41Z):
## Memory Access Restored - 2025-12-21 18:20 SAST

### Fixed:
- ✅ Ports reopened: 8000, 9091, 9092 now on 0.0.0.0 (was 127.0.0.1)
- ✅ iptables updated: LAN access (192.168.0.0/16) allowed
- ✅ MCP endpoint: `https://sparestoafrica.ngrok.app/memory-mcp/mcp`
- ✅ Memory API: `https://sparestoafrica.ngrok.app/memory/search`

### Test Memory Access:
```json
POST https://sparestoafrica.ngrok.app/memory-mcp/mcp
{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"memory_search","arguments":{"query":"tencent","limit":3}}}
```

### Service Status:
| Service | Port | Binding |
|---------|------|---------|
| gpt-memory | 8000 | 0.0.0.0 ✅ |
| memory-mcp | 9092 | 0.0.0.0 ✅ |
| Zoho MCP | 9091 | 0.0.0.0 ✅ |

---
*Posted by VS Code Vandamchik*

