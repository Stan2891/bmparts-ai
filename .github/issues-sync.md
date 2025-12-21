# GitHub Issues Sync Export
Updated: 2025-12-21 14:25 UTC

## Open Issues
- #7: 🔄 Sync Test #7
- #6: 🔄 Copilot Sync Channel
- #5: Add write operation confirmations
- #4: Replace ngrok with stable public tunnel
- #3: Implement sync_woo_zoho and compare_woo_zoho tools
- #2: Voice: Upgrade to Hybrid mode (tools + memory)
- #1: Port 9091 conflict: MCP server vs master_qty_sync

## Sync Channel (Last 5 Comments)
**Stan2891** (2025-12-20T18:33:25Z):
**[2025-12-20 20:33:24]** GitHub.com Copilot (Vandamchik) sync check-in.  Context loaded: Memory API auth done, pending port 9091 conflict + voice hybrid mode.  Ready for tasks.

**Stan2891** (2025-12-20T18:34:09Z):
**[2025-12-20 20:34:08]** GitHub.com Copilot (Vandamchik) sync check-in.  Context loaded: Memory API auth done, pending port 9091 conflict + voice hybrid mode.  Ready for tasks.

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

