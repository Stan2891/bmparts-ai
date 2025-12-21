# GitHub Issues Sync Export
Updated: 2025-12-21 02:06 UTC

## Open Issues
- #7: 🔄 Sync Test #7
- #6: 🔄 Copilot Sync Channel
- #5: Add write operation confirmations
- #4: Replace ngrok with stable public tunnel
- #3: Implement sync_woo_zoho and compare_woo_zoho tools
- #2: Voice: Upgrade to Hybrid mode (tools + memory)
- #1: Port 9091 conflict: MCP server vs master_qty_sync

## Sync Channel (Last 5 Comments)
**Stan2891** (2025-12-20T18:32:40Z):
# Copilot Sync Protocol

## Capabilities by Platform

| Action | VS Code Copilot | GitHub.com Copilot | Mobile App |
|--------|-----------------|-------------------|------------|
| Read issues | ✅ | ✅ | ✅ |
| Read comments | ✅ | ✅ | ✅ |
| Write comments | ✅ (via script) | ❌ | ✅ |
| Create issues | ✅ (via gh cli) | ✅ | ✅ |
| Close issues | ✅ (via gh cli) | ✅ | ✅ |

## How to Sync

**VS Code Copilot (Vandamchik):**
```bash
./scripts/copilot-sync.sh "Your message here"
```

**GitHub.com Copilot:**
- Read: `gh issue view 6 --comments`
- Create issue: Use built-in tool
- Write comment: Ask VS Code Copilot to post

**Mobile:**
- Open GitHub app → bmparts-ai → Issues → #6
- Comment directly

## Auto-Sync
- GitHub Action runs every 6 hours
- Updates `.github/issues-sync.md`
- Triggers on new comments to Issue #6

---
*Protocol documented by Vandamchik*

**Stan2891** (2025-12-20T18:33:25Z):
**[2025-12-20 20:33:24]** GitHub.com Copilot (Vandamchik) sync check-in.  Context loaded: Memory API auth done, pending port 9091 conflict + voice hybrid mode.  Ready for tasks.

**Stan2891** (2025-12-20T18:34:09Z):
**[2025-12-20 20:34:08]** GitHub.com Copilot (Vandamchik) sync check-in.  Context loaded: Memory API auth done, pending port 9091 conflict + voice hybrid mode.  Ready for tasks.

**Stan2891** (2025-12-20T18:36:13Z):
**[2025-12-20 20:36:11]** MEMORY: Stan asked to remember 'number 7' - this is a sync test. Issue #7 created.

**Stan2891** (2025-12-20T18:36:37Z):
**[2025-12-20 20:36:36]** MEMORY SYNC: Stan asked to remember 'number 7' - saved to memory ID 1007. Issue #7 also created for testing.

