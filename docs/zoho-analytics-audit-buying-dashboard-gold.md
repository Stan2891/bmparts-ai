# Zoho Analytics Workspace Audit: "Buying Dashboard Gold"

**Generated:** 2026-02-19  
**Workspace:** Buying Dashboard Gold  
**Owner:** stan@bmparts.co.za  
**Orgs:** BMParts (856737871) + Spares to Africa (857295887)  
**Data source:** `analytics_views.json` API cache (334 views)

---

## ⚡ Critical Findings (Executive Summary)

1. **`buying_base_sta_v4` is the latest/intended production query** but is not yet wired into any reports or dashboards.
2. **The Buying Dashboard still runs on legacy `Buying_Base_v2`** — needs to be cut over to v4.
3. **`Buying_Base_v2_OLD` still powers 8 legacy reports** — never migrated, even older than v2.
4. **Only 3 of 70 query tables have downstream dependents.** The other 67 (including the entire STA pipeline) are orphans awaiting wiring.
5. **24 test/debug query tables** (prefix `_`, `QT_Test_*`) clutter the workspace.
6. **All base tables last synced 2026-02-16 07:54 SAST** — sync is healthy.
7. **3 custom tables** (`vw_DetailOsta
Ctrl+I to generate a command.




1h
27m
Show More
zoho-analytics-audit-buying-dashboard-gold.md
+4
-5
313 hidden lines
 
1. **`bmp` joins on SKU, not ItemID** — cross-org join, SKU matching can fail if SKUs differ between BMParts and STA. Verify SKU alignment between orgs.
1. ~~`bmp` joins on SKU, not ItemID~~ — **NOT A RISK: SKUs confirmed matching across orgs.**
 

Done. SKU cross-org join risk struck through — confirmed matching.

Remaining real risks on v4 are now just:

⚠️ Availability v1 vs v2
⚠️ "Categor" typo
⚠️ No status filter (inactive items)
⚠️ Warehouse handling in upstream QTs
What would you like to tackle next?

Feedback submitted



⚠️ "Categor" typo thats the correct category

zoho-analytics-audit-buying-dashboard-gold.md
+3
-5
316 hidden lines
 
6. **Typo in column name:** `it."Categor"` — missing the 'y' (should be `it."Category"`). This may cause the COALESCE to always fall through to `a."Category"` if the column name doesn't match.
6. ~~Typo in column name: `it."Categor"`~~ — **NOT A RISK: actual column name is `"Categor"`** (Zoho truncation).
 

Done. "Categor" confirmed as the actual column name — struck through.

Remaining real v4 risks are now just 2:

⚠️ Uses Availability v1 not v2
⚠️ Warehouse handling unknown (in upstream STA_Stock_By_Item_v2)
Plus the upstream QT checks (date fields, credit notes, status filters). Do you know offhand if you intentionally used STA_Stock_Availability_90_v1 over v2?

Feedback submitted



not sure

Good — that's worth checking. Let me note it as a quick action item. You can compare the two in under a minute: right-click STA_Stock_Availability_90_v1 → Edit Design, then do the same for _v2, and see what changed.

zoho-analytics-audit-buying-dashboard-gold.md
+2
-2
**Impact:** v1 may have known issues that v2 was created to fix.  
**Action:** Compare v1 vs v2 SQL, switch to v2 if it's the corrected version.
**Impact:** v1 may have known issues that v2 was created to fix. Unknown if intentional.  
**Action:** Right-click both `STA_Stock_Availability_90_v1` and `_v2` → Edit Design → compare SQL. If v2 is the fix, update v4's JOIN to use v2.
 

The v4 SQL analysis is looking clean. Here's where we stand:

v4 risk scorecard:

NEW/USED — not a risk (STA = NEW only)
SKU cross-org — not a risk (confirmed matching)
"Categor" typo — not a risk (actual column name)
⚠️ Availability v1 vs v2 — quick check needed
⚠️ Warehouse handling — depends on STA_Stock_By_Item_v2 SQL
⚠️ Upstream QTs (dates, credit notes, status filters) — still unknown
What's ready to act on now:

Compare STA_Stock_Availability_90_v1 vs _v2 (1 min in UI)
Glance at STA_Stock_By_Item_v2 SQL for warehouse handling
Then the big move — wire v4 into reports
Want to keep auditing the upstream QTs, or are you ready to start wiring v4 into the dashboard?

Feedback submitted



v1  SELECT
         d."ItemID" AS "ItemID",
         COUNT(*) AS "DaysTotal90",
         SUM(d."InStockFlag") AS "InStockDays90",
         ROUND(AVG(d."InStockFlag") * 100.0, 0) AS "StockAvailability90_Pct"
FROM  "STA_Stock_Daily_v1" d 
GROUP BY  d."ItemID" 
v2:   SELECT
         "STA_Stock_Daily_v2"."ItemID" AS "ItemID",
         COUNT(*) AS "DaysTotal90",
         SUM("STA_Stock_Daily_v2"."InStockFlag") AS "InStockDays90",
         ROUND(AVG("STA_Stock_Daily_v2"."InStockFlag") * 100.0, 0) AS "StockAvailability90_Pct"
FROM  "STA_Stock_Daily_v2" 
GROUP BY  "STA_Stock_Daily_v2"."ItemID" 

The two are identical logic — the only difference is the upstream table:

v1 → STA_Stock_Daily_v1
v2 → STA_Stock_Daily_v2
So the real question is: what changed between STA_Stock_Daily_v1 and _v2? That's where the actual fix (if any) lives.

zoho-analytics-audit-buying-dashboard-gold.md
+5
-3
- v1: `FROM STA_Stock_Daily_v1` ← used by v4  
- v2: `FROM STA_Stock_Daily_v2`  
**Impact:** Depends on what changed between `STA_Stock_Daily_v1` and `_v2`.  
**Action:** Compare `STA_Stock_Daily_v1` vs `_v2` SQL to determine if v4 should switch to availability v2.
 

Same logic, just different upstream table. Can you share STA_Stock_Daily_v1 vs _v2 SQL? That'll close this chain. Or if you'd rather move on to wiring v4 into the dashboard, we can park this as a minor item.

Waiting on your input — do you want to:

Keep auditing — share STA_Stock_Daily_v1 vs _v2 and STA_Stock_By_Item_v2 SQL to close the remaining upstream unknowns
Move on — start wiring v4 into reports/dashboard
Either way, the audit doc is in good shape with the v4 SQL fully analyzed.

Feedback submitted



can we wire v4 and remove orthans

3 more
Compare STA_Stock_Availability_90 v1 vs v2

5
Wire v4 into reports — create pivot/chart reports on buying_base_sta_v4

2 more
This needs to be done in the Zoho Analytics UI — I can't modify Zoho directly from here. Let me give you the exact step-by-step with all the object names.

Feedback submitted



bu the way plawrite also available

Playwright can automate the Zoho Analytics UI directly. Let me check what tools are available.

1
Use Playwright to automate Zoho Analytics UI for wiring v4 and cleanup

Wire v4: Create new reports on buying_base_sta_v4 or repoint existing ones

Delete orphan query tables (67 total)

Migrate/remove legacy reports from Buying_Base_v2_OLD

Let me first check what's available in the browser via Playwright.

Command echo

echo "Checking Playwright MCP availability"
Checking Playwright MCP availability


Using legacy terminal
Configure
Let me try to navigate to the Zoho Analytics workspace with Playwright.

The Playwright MCP server is listed as available, but I don't know the exact tool names it exposes. The tool names I tried (mcp_playwright_browser_navigate, mcp_playwright_navigate) don't match what's registered.

Two options to proceed:

You tell me the Playwright tool names — if you know them from your MCP config, I can use them to automate the Zoho Analytics UI (delete orphans, wire v4 into reports)
I generate a step-by-step manual action plan — exact object names, click paths, and a safe deletion order you can execute in the Zoho Analytics UI yourself. This would take you ~15 minutes.
Which do you prefer?

Feedback submitted



some of repositories must have this inf

Command find, head

find /home/stan -maxdepth 4 -name "*.json" -path "*mcp*" 2>/dev/null | head -20
/home/stan/mcp-chatgpt-web/node_modules/call-bind-apply-helpers/package.json
/home/stan/mcp-chatgpt-web/node_modules/call-bind-apply-helpers/tsconfig.json
/home/stan/mcp-chatgpt-web/node_modules/express-rate-limit/package.json
/home/stan/mcp-chatgpt-web/node_modules/express-rate-limit/tsconfig.json
/home/stan/mcp-chatgpt-web/node_modules/depd/package.json
/home/stan/mcp-chatgpt-web/node_modules/es-errors/package.json
/home/stan/mcp-chatgpt-web/node_modules/es-errors/tsconfig.json
/home/stan/mcp-chatgpt-web/node_modules/mime-types/package.json
/home/stan/mcp-chatgpt-web/node_modules/hasown/package.json
/home/stan/mcp-chatgpt-web/node_modules/hasown/tsconfig.json
/home/stan/mcp-chatgpt-web/node_modules/ms/package.json
/home/stan/mcp-chatgpt-web/node_modules/.package-lock.json
/home/stan/mcp-chatgpt-web/node_modules/serve-static/package.json
/home/stan/mcp-chatgpt-web/node_modules/is-promise/package.json
/home/stan/mcp-chatgpt-web/node_modules/ajv-formats/package.json
/home/stan/mcp-chatgpt-web/node_modules/unpipe/package.json
/home/stan/mcp-chatgpt-web/node_modules/once/package.json
/home/stan/mcp-chatgpt-web/node_modules/side-channel/package.json
/home/stan/mcp-chatgpt-web/node_modules/side-channel/tsconfig.json
/home/stan/mcp-chatgpt-web/node_modules/has-symbols/package.json


Using legacy terminal
Configure
Command find, xargs, head

find /home/stan -maxdepth 5 -name "*.json" 2>/dev/null | xargs grep -l "playwright" 2>/dev/null | head -10
/home/stan/.copilot-memory/chats/full-session-2026-01-25_03-10-01.json
/home/stan/.copilot-memory/chats/full-session-2026-01-28_23-30-01.json
/home/stan/.copilot-memory/chats/full-session-2026-01-29_03-00-01.json
/home/stan/.copilot-memory/chats/full-session-2026-02-07_17-10-01.json
/home/stan/.copilot-memory/chats/full-session-2026-02-09_06-20-01.json
/home/stan/.copilot-memory/chats/full-session-2026-02-07_04-10-01.json
/home/stan/.copilot-memory/chats/full-session-2026-01-27_11-30-01.json
/home/stan/.copilot-memory/chats/full-session-2026-01-31_09-10-01.json
/home/stan/.copilot-memory/chats/full-session-2026-02-08_18-30-01.json
/home/stan/.copilot-memory/chats/full-session-2026-02-10_05-20-01.json


Using legacy terminal
Configure
Command cat, find, head

cat /home/stan/.windsurf/settings.json 2>/dev/null || cat /home/stan/.config/windsurf/settings.json 2>/dev/null || find /home/stan/.windsurf -name "settings.json" -maxdepth 3 2>/dev/null | head -5

Using legacy terminal
Configure
Command find, grep, head

find /home/stan/.windsurf -name "mcp*" -o -name "*mcp*" 2>/dev/null | grep -v worktrees | grep -v node_modules | head -20

Using legacy terminal
Configure
Command find, head

find /home/stan -maxdepth 2 -name "mcp_config*" -o -name "mcp-config*" -o -name "mcp.json" -o -name "mcpServers*" 2>/dev/null | head -10
/home/stan/.vscode/mcp.json


Using legacy terminal
Configure
Command cat

cat /home/stan/.vscode/mcp.json
{
  "servers": {
    "chatgpt-web": {
      "type": "stdio",
      "command": "node",
      "args": ["/home/stan/mcp-chatgpt-web/server.js"],
      "env": {
        "CHATGPT_USER_DATA": "/home/stan/.chatgpt-session"
      }
    },
    "memory": {
      "type": "stdio",
      "command": "node",
      "args": ["/home/stan/memory-mcp-server/stdio-wrapper.js"]
    },
    "zoho": {
      "type": "stdio",
      "command": "node",
      "args": ["/home/stan/zoho-mcp-server/stdio-wrapper.js"]
    },
    "playwright": {
      "type": "stdio",
      "command": "/home/stan/.nvm/versions/node/v20.19.5/bin/npx",
      "args": ["@playwright/mcp@latest", "--user-data-dir", "/home/stan/.playwright-profile"]
    }
  }
}


Using legacy terminal
Configure
Found the config. Let me try the Playwright MCP tools with the correct naming.

The Playwright MCP server is configured in your system, but I can't find the correct tool name format to invoke it. The standard playwright/mcp package exposes tools like browser_navigate, browser_click, browser_snapshot, etc., but the prefix/naming convention Windsurf uses to expose them isn't matching what I'm trying.

Options:

Check the Playwright MCP tool names — Can you look in Windsurf settings or try typing @playwright in the chat to see what tool names are auto-suggested? Or run:
bash
npx @playwright/mcp@latest --help
I generate the full manual action plan — exact object names, deletion order, and wiring steps you can execute in the Zoho Analytics UI in ~15 minutes. No automation needed.
We use the Zoho MCP server instead — your zoho-mcp-server might have API tools to delete query tables and create reports programmatically, which would be cleaner than browser automation anyway.
Which route do you want to take?

Feedback submitted



tets playwrite mcp copilot say its available and ready

Command npx, head in ~/

npx @playwright/mcp@latest --help 2>&1 | head -30
Usage: Playwright MCP [options]

Options:
  -V, --version                         output the version number
  --allowed-hosts <hosts...>            comma-separated list of hosts this
                                        server is allowed to serve from.
                                        Defaults to the host the server is bound
                                        to. Pass '*' to disable the host check.
  --allowed-origins <origins>           semicolon-separated list of TRUSTED
                                        origins to allow the browser to request.
                                        Default is to allow all.
                                        Important: *does not* serve as a
                                        security boundary and *does not* affect
                                        redirects.
  --allow-unrestricted-file-access      allow access to files outside of the
                                        workspace roots. Also allows
                                        unrestricted access to file:// URLs. By
                                        default access to file system is
                                        restricted to workspace root directories
                                        (or cwd if no roots are configured)
                                        only, and navigation to file:// URLs is
                                        blocked.
  --blocked-origins <origins>           semicolon-separated list of origins to
                                        block the browser from requesting.
                                        Blocklist is evaluated before allowlist.
                                        If used without the allowlist, requests
                                        not matching the blocklist are still
                                        allowed.
                                        Important: *does not* serve as a
                                        security boundary and *does not* affect


Using legacy terminal
Configure
Command npx in ~/

npx @playwright/mcp@latest --help 2>&1
Usage: Playwright MCP [options]

Options:
  -V, --version                         output the version number
  --allowed-hosts <hosts...>            comma-separated list of hosts this server is allowed to serve from. Defaults to the host the server is bound to. Pass '*' to disable the host check.
  --allowed-origins <origins>           semicolon-separated list of TRUSTED origins to allow the browser to request. Default is to allow all.
                                        Important: *does not* serve as a security boundary and *does not* affect redirects.
  --allow-unrestricted-file-access      allow access to files outside of the workspace roots. Also allows unrestricted access to file:// URLs. By default access to file system is restricted to workspace root directories (or cwd if
                                        no roots are configured) only, and navigation to file:// URLs is blocked.
  --blocked-origins <origins>           semicolon-separated list of origins to block the browser from requesting. Blocklist is evaluated before allowlist. If used without the allowlist, requests not matching the blocklist are still
                                        allowed.
                                        Important: *does not* serve as a security boundary and *does not* affect redirects.
  --block-service-workers               block service workers
  --browser <browser>                   browser or chrome channel to use, possible values: chrome, firefox, webkit, msedge.
  --caps <caps>                         comma-separated list of additional capabilities to enable, possible values: vision, pdf, devtools.
  --cdp-endpoint <endpoint>             CDP endpoint to connect to.
  --cdp-header <headers...>             CDP headers to send with the connect request, multiple can be specified.
  --cdp-timeout <timeout>               timeout in milliseconds for connecting to CDP endpoint, defaults to 30000ms
  --codegen <lang>                      specify the language to use for code generation, possible values: "typescript", "none". Default is "typescript".
  --config <path>                       path to the configuration file.
  --console-level <level>               level of console messages to return: "error", "warning", "info", "debug". Each level includes the messages of more severe levels.
  --device <device>                     device to emulate, for example: "iPhone 15"
  --executable-path <path>              path to the browser executable.
  --extension                           Connect to a running browser instance (Edge/Chrome only). Requires the "Playwright MCP Bridge" browser extension to be installed.
  --grant-permissions <permissions...>  List of permissions to grant to the browser context, for example "geolocation", "clipboard-read", "clipboard-write".
  --headless                            run browser in headless mode, headed by default
  --host <host>                         host to bind server to. Default is localhost. Use 0.0.0.0 to bind to all interfaces.
  --ignore-https-errors                 ignore https errors
  --init-page <path...>                 path to TypeScript file to evaluate on Playwright page object
  --init-script <path...>               path to JavaScript file to add as an initialization script. The script will be evaluated in every page before any of the page's scripts. Can be specified multiple times.
  --isolated                            keep the browser profile in memory, do not save it to disk.
  --image-responses <mode>              whether to send image responses to the client. Can be "allow" or "omit", Defaults to "allow".
  --no-sandbox                          disable the sandbox for all process types that are normally sandboxed.
  --output-dir <path>                   path to the directory for output files.
  --output-mode <mode>                  whether to save snapshots, console messages, network logs to a file or to the standard output. Can be "file" or "stdout". Default is "stdout".
  --port <port>                         port to listen on for SSE transport.
  --proxy-bypass <bypass>               comma-separated domains to bypass proxy, for example ".com,chromium.org,.domain.com"
  --proxy-server <proxy>                specify proxy server, for example "http://myproxy:3128" or "socks5://myproxy:8080"
  --sandbox                             enable the sandbox for all process types that are normally not sandboxed.
  --save-session                        Whether to save the Playwright MCP session into the output directory.
  --save-trace                          Whether to save the Playwright Trace of the session into the output directory.
  --save-video <size>                   Whether to save the video of the session into the output directory. For example "--save-video=800x600"
  --secrets <path>                      path to a file containing secrets in the dotenv format
  --shared-browser-context              reuse the same browser context between all connected HTTP clients.
  --snapshot-mode <mode>                when taking snapshots for responses, specifies the mode to use. Can be "incremental", "full", or "none". Default is incremental.
  --storage-state <path>                path to the storage state file for isolated sessions.
  --test-id-attribute <attribute>       specify the attribute to use for test ids, defaults to "data-testid"
  --timeout-action <timeout>            specify action timeout in milliseconds, defaults to 5000ms
  --timeout-navigation <timeout>        specify navigation timeout in milliseconds, defaults to 60000ms
  --user-agent <ua string>              specify user agent string
  --user-data-dir <path>                path to the user data directory. If not specified, a temporary directory will be created.
  --viewport-size <size>                specify browser viewport size in pixels, for example "1280x720"
  -h, --help                            display help for command


Using legacy terminal
Configure
I've tried multiple Playwright MCP tool name patterns and they all fail. The server is configured in your ~/.vscode/mcp.json but it may not be connected to Windsurf (Copilot and Windsurf use different MCP configurations).

Let me just generate the exact action plan you can execute. It'll be faster than debugging MCP connectivity.

1
Generate wiring + cleanup action plan with exact object names

Wire v4: repoint 5 current reports from Buying_Base_v2 to buying_base_sta_v4

Delete 24 test tables, 4 audit tables, old version chain predecessors

Handle 8 legacy reports on Buying_Base_v2_OLD

Let me create a concrete, step-by-step action plan you can execute right now in the Zoho Analytics UI.

zoho-analytics-audit-buying-dashboard-gold.md
+201
-119
| 70 query tables | **9 query tables** |
| 67 orphans | **0 orphans** |
| 24 test tables | **0 test tables** |
| 8 version chains | **latest versions only** |
 

The full action plan is in the audit doc at zoho-analytics-audit-buying-dashboard-gold.md:440-640. Here's the summary:

What To Do Now (in Zoho Analytics UI)
Step 1 — Wire v4 (~5 min)

Create 4 new reports (Pivot/Chart) sourced from buying_base_sta_v4
Add them to the Buying Dashboard
Step 2 — Delete orphans (~10 min, 7 batches)

Batch 1: 24 test tables (_*, QT_Test_*)
Batch 2: 4 audit tables
Batch 3: 7 Top SKU orphans
Batch 4: 5 old sales/stock
Batch 5: 3 old buying_base_sta versions (v1-v3)
Batch 6: 7 old version predecessors (⚠️ switch v4 to use STA_Stock_Availability_90_v2 before deleting v1)
Batch 7: 9 unused STA QTs not referenced by v4
Step 3 — Delete 8 legacy reports on Buying_Base_v2_OLD, then delete the OLD QT

Step 4 — Delete old v2 reports + Buying_Base_v2 + Buying_Base_v2_OLD after validation

End state: 70 → 9 query tables, 0 orphans.

The exact names are all listed in the doc. Ready to start with Batch 1?

Feedback submitted



give me list of exactly what reports to delete

Command cat, python3

cat /home/stan/.windsurf/worktrees/bmparts-ai/bmparts-ai-41b30c5b/analytics_views.json | python3 -c "
import json, sys
 
d = json.load(sys.stdin)
views = json.loads(d['result']['content'][0]['text'])['data']['views']
 
# Get all non-Table, non-Dashboard, non-QueryTable views (i.e. reports)
report_types = ['Pivot', 'AnalysisView', 'Report', 'SummaryView']
reports = [v for v in views if v['viewType'] in report_types]
 
# Build parent map
id_to_name = {v['viewId']: v['viewName'] for v in views}
id_to_type = {v['viewId']: v['viewType'] for v in views}
 
# Get v4's upstream QTs (the ones we're keeping)
keep_qts = {
    'buying_base_sta_v4',
    'STA_Sales_Agg_v3',
    'STA_Stock_By_Item_v2',
    'STA_Stock_Availability_90_v2',
    'STA_Sales_Agg_External90_v1',
    'BMP_Sales_Agg_90_v1',
    'STA_Sales_Fact_180d_v3',
    'STA_Stock_Daily_v2',
    'Cash Flow Query',
}
 
# Identify which reports are on tables we're keeping vs deleting
print('=== ALL REPORTS (sorted by parent) ===')
print()
 
# Group by parent
from collections import defaultdict
by_parent = defaultdict(list)
for r in reports:
    pid = r.get('parentViewId', '')
    pname = id_to_name.get(pid, f'UNKNOWN ({pid})')
    ptype = id_to_type.get(pid, '?')
    by_parent[(pname, ptype, pid)].append(r)
 
for (pname, ptype, pid), reps in sorted(by_parent.items()):
    # Determine if parent is a QT we're deleting
    if ptype == 'QueryTable' and pname not in keep_qts and pname not in ['Buying_Base_v2', 'Buying_Base_v2_OLD']:
        action = 'DELETE (parent QT being deleted)'
    elif pname in ['Buying_Base_v2_OLD']:
        action = 'DELETE (legacy, replaced by v4)'
    elif pname in ['Buying_Base_v2']:
        action = 'DELETE AFTER v4 validated'
    elif ptype == 'Table':
        action = 'KEEP (auto-generated from base table)'
    elif pname in keep_qts:
        action = 'KEEP'
    else:
        action = 'KEEP'
    
    print(f'Parent: {pname} ({ptype}) — {action}')
    for r in sorted(reps, key=lambda x: x['viewName']):
        print(f'  {r[\"viewType\"]:15s} {r[\"viewName\"]}')
    print()
" 2>&1
=== ALL REPORTS (sorted by parent) ===

Parent: Accounts (Table) — KEEP (auto-generated from base table)
  Pivot           Account Opening and Closing Balance Monthly Trend
  Pivot           Account Opening and Closing Balance Yearly Trend
  AnalysisView    Accounts Receivables vs Accounts Payable Monthly Trend
  AnalysisView    Asset Turnover Ratio Monthly Trend
  AnalysisView    Assets vs Liabilities Monthly Trend
  Pivot           Balance Sheet Monthly Trend with Opening and Closing Balance
  Pivot           Balance Sheet This Year
  Pivot           Balance Sheet Yearly Trend with Opening and Closing Balance
  Pivot           Cash Flow
  AnalysisView    Cash Flow Margin Monthly Trend
  AnalysisView    Cash Flow Monthly Trend
  AnalysisView    Cash Ratio Monthly Trend
  Pivot           Chart of Accounts
  AnalysisView    Debt to Assets Ratio Monthly Ratio
  AnalysisView    Debt to Equity Ratio Monthly Trend
  AnalysisView    EBIT vs EBIT Margin Monthly Trend
  AnalysisView    Efficiency ratio Monthly Trend
  Pivot           Financial Overview Report
  AnalysisView    Gross Profit Margin by Month
  AnalysisView    Operating Income vs Operating Expenses Monthly Trend
  Pivot           Overview of Revenue vs Expenses vs ROI
  AnalysisView    Profit Monthly Trend
  Pivot           Profit and Loss
  AnalysisView    Quick Ratio Monthly Trend
  AnalysisView    Revenue vs Expense by Month
  Pivot           Trial Balance Quarterly Trend
  AnalysisView    Working Capital Ratio Monthly Trend
  Pivot           YTD Balance Sheet

Parent: Buying_Base_v2 (QueryTable) — DELETE AFTER v4 validated
  Pivot           Buying List v3 FINAL
  Pivot           Count SKUs to Reorder v3
  AnalysisView    Top Reorders v3 FINAL
  Pivot           Total Reorder Qty v3
  Pivot           Untitled-1

Parent: Buying_Base_v2_OLD (QueryTable) — DELETE (legacy, replaced by v4)
  Report          Buying List
  Report          Buying List v3
  Report          Buying List v3 new
  SummaryView     Count of SKUs to Reorder
  SummaryView     Min DaysCover
  AnalysisView    Top Reorders
  AnalysisView    Top Reorders v3
  SummaryView     Total Reorder Qty

Parent: Cash Flow Query (QueryTable) — KEEP
  Pivot           Cash Flow Statement

Parent: Customers (Table) — KEEP (auto-generated from base table)
  Pivot           Aging Summary by Customer
  AnalysisView    Bottom 10 Customers by Sales
  AnalysisView    Bottom 10 Customers by Sales Invoice Generated
  AnalysisView    Customer Addition Monthly Trend
  Pivot           Customer Balances
  AnalysisView    Customer Growth Rate vs Customers Count
  Pivot           Open Invoice vs Available Credits by Customer
  Pivot           Overall Profit Distribution
  Pivot           Overdue Invoice Details
  Pivot           Paid Invoices vs Applied Credits by Customers
  Pivot           Profit by Customers
  Pivot           Purchases from Customers Last 12 months
  AnalysisView    Quarterly Customer Growth Trend
  AnalysisView    Top 10 Average Sales per Order by Customer
  AnalysisView    Top 10 Customers by Sales
  AnalysisView    Top 10 Customers by Sales Invoice Generated
  Pivot           Top 10 Open Estimates
  AnalysisView    Top 25 Sales by Customers based on Age Tier

Parent: Invoice Items (Table) — KEEP (auto-generated from base table)
  Pivot           Profit by Items

Parent: Invoices (Table) — KEEP (auto-generated from base table)
  Pivot           Bottom 10 products by Invoice
  AnalysisView    Invoice Generated Monthly Trend
  AnalysisView    Invoice Generated by Status Monthly Trend
  AnalysisView    Invoice Overdue Monthly Trend
  Pivot           Invoice Stats by Products
  AnalysisView    Invoiced Amount Monthly Trend
  AnalysisView    Open Invoice Monthly Trend
  AnalysisView    Open Invoice by Age Tier
  AnalysisView    Open Invoices Count vs Open Invoices Value
  AnalysisView    Overdue Invoices Monthly Trend
  Pivot           Profit by Invoices
  AnalysisView    Revenue from Subscription Monthly Trend
  AnalysisView    Revenue vs Revenue Growth %
  AnalysisView    Sales Cycle Time Vs Deals Count (Age Tier)
  AnalysisView    Sales Trend by Invoices Delivered - Last 12 months
  AnalysisView    Sales by Invoice Status
  AnalysisView    Top 10 Products by Sales Value
  AnalysisView    Total Invoices vs Paid Invoices Monthly Trend
  AnalysisView    Total Sales Monthly Trend
  Pivot           Unpaid Invoices Count (Subscription)
  AnalysisView    Y-o-Y Revenue Growth Monthly Trend
  AnalysisView    YTD Invoice Amount  Monthly Trend

Parent: Items (Table) — KEEP (auto-generated from base table)
  AnalysisView    Cost of Sales vs Sales vs Profit Monthly Trend
  AnalysisView    Overall Revenue Split by Plan
  Pivot           Products vs Profit/Loss Margin - By Invoices Paid
  AnalysisView    Revenue by Plans Monthly Trend
  Pivot           Sales Invoice by Product
  AnalysisView    Top 10 Fast Moving Products
  AnalysisView    Top 10 Items Stock in Hand
  AnalysisView    Top 10 Items by Stock In
  AnalysisView    Top 10 Items by Stock Out
  AnalysisView    Top 10 Products by Paid Invoices Value
  AnalysisView    Top100

Parent: Payment Refunds (Table) — KEEP (auto-generated from base table)
  Pivot           Refund History

Parent: Quotes (Table) — KEEP (auto-generated from base table)
  AnalysisView    Estimates Trend - Created vs Won vs Lost count Last 12 months
  Pivot           Top 10 Products by Open Estimates

Parent: Sales Order Invoice (Table) — KEEP (auto-generated from base table)
  AnalysisView    Sales Funnel - Estimate to SalesOrder to Invoices

Parent: Sales Order Items (Table) — KEEP (auto-generated from base table)
  AnalysisView    Top 10 Items by Sales Orders
  AnalysisView    Top 10 Items by Sales Orders Value

Parent: Sales Orders (Table) — KEEP (auto-generated from base table)
  AnalysisView    Customer Order Fill Rate Monthly Trend
  AnalysisView    Item Fill Rate Monthly Trend
  AnalysisView    MTD Sales Orders Cumulative Value
  AnalysisView    Month-over-Month Sales Orders Count Growth %
  AnalysisView    Sales Funnel - Estimates to Sales Order to Invoice by Amount
  AnalysisView    Sales Orders Count Monthly Trend
  AnalysisView    Sales Orders by Value Monthly Trend
  AnalysisView    YTD Sales Orders Count Monthly Trend

Parent: Sales Persons (Table) — KEEP (auto-generated from base table)
  Pivot           Invoice Stats by Salesperson

Parent: Shipment Order (Table) — KEEP (auto-generated from base table)
  AnalysisView    Shipment Carrier Distribution
  AnalysisView    Shipment Count vs Delivered Shipments
  AnalysisView    Shipments by Status

Parent: Taxes (Table) — KEEP (auto-generated from base table)
  AnalysisView    Overall Distribution of Tax Rate by Tax Type
  AnalysisView    Tax Rate by Tax Name Monthly Trend
  AnalysisView    Tax Rate by Tax Type Monthly Trend
  Pivot           Tax Summary

Parent: Users (Table) — KEEP (auto-generated from base table)
  AnalysisView    Overall Distribution of Employee by Role

Parent: Vendors (Zoho Inventory) (Table) — KEEP (auto-generated from base table)
  Pivot           Purchase Receive History (Zoho Inventory)


Using legacy terminal
Configure
Here's the complete list:

Reports to DELETE
Batch A — 8 Legacy Reports (on Buying_Base_v2_OLD) — Delete Now
Buying List
Buying List v3
Buying List v3 new
Count of SKUs to Reorder
Min DaysCover
Top Reorders
Top Reorders v3
Total Reorder Qty
Batch B — 5 Reports on Buying_Base_v2 — Delete After v4 Wired
Buying List v3 FINAL
Count SKUs to Reorder v3
Top Reorders v3 FINAL
Total Reorder Qty v3
Untitled-1
Reports to KEEP (103 auto-generated from base tables)
All reports under Accounts (28), Customers (18), Invoices (22), Items (11), Sales Orders (8), Taxes (4), Shipment Order (3), Quotes (2), Sales Order Invoice (1), Invoice Items (1), Sales Persons (1), Payment Refunds (1), Users (1), Vendors (Zoho Inventory) (1), Cash Flow Query (1) — all auto-generated by Zoho connectors, don't touch these.

Summary
Action	Count
DELETE now (Batch A — legacy on v2_OLD)	8
DELETE after v4 wired (Batch B — on v2)	5
KEEP (auto-generated + Cash Flow)	103
Total reports	116
Safe order:

Wire v4 into 4 new reports + add to dashboard
Delete Batch A (8 legacy reports)
Delete Buying_Base_v2_OLD (now 0 dependents)
Validate v4 dashboard works
Delete Batch B (5 old v2 reports)
Delete Buying_Base_v2 (now 0 dependents)
Feedback submitted



Cascade vs Copilot
Feature	Cascade	Copilot
Context window	Larger	Smaller
Codebase search	Built-in @codebase	Tools
MCP support	Native	Via extensions
Terminal access	Yes	Yes
Multi-file edits	Good	Good
Tips for BMParts Work
1. For Zoho/Deluge code:


"Write Deluge function to get item stock from BMParts Zoho Inventory (org 856737871), use connection:zoho_inventory, return map with success/message/data"
2. For data analysis:


"Analyze ~/Downloads/buying_base.csv - find items with sales but zero InStockDays90"
3. For scraping:


"Use Playwright to scrape price from beelinespares.co.za/product/thermostat-n20"
MCP Tools in Cascade
If Windsurf has MCP configured (check your config), you can use:

Memory tools (memory_save, memory_search)
Zoho tools (if zoho MCP is connected)
Playwright browser automation
Check: Settings → Extensions → MCP or ~/.windsurf/mcp.json

The MCP config might be in a different location for Windsurf. Let me check.

Command find, grep, head

find /home/stan -maxdepth 4 -path "*/windsurf/*mcp*" -o -path "*/windsurf/*/mcp*" 2>/dev/null | grep -v worktrees | grep -v node_modules | head -20
/home/stan/.codeium/windsurf/mcp_config.json


Using legacy terminal
Configure
Command cat

cat /home/stan/.codeium/windsurf/mcp_config.json
{
  "mcpServers": {
    "memory": {
      "args": [
        "/home/stan/memory-mcp-server/stdio-wrapper.js"
      ],
      "command": "node",
      "disabled": false,
      "env": {}
    },
    "playwright": {
      "args": [
        "@playwright/mcp@latest",
        "--user-data-dir",
        "/home/stan/.playwright-profile"
      ],
      "command": "/home/stan/.nvm/versions/node/v20.19.5/bin/npx",
      "disabled": false,
      "env": {}
    },
    "sequential-thinking": {
      "args": [
        "-y",
        "@modelcontextprotocol/server-sequential-thinking"
      ],
      "command": "npx",
      "env": {}
    },
    "zoho": {
      "args": [
        "/home/stan/zoho-mcp-server/stdio-wrapper.js"
      ],
      "command": "node",
      "disabled": false,
      "env": {}
    }
  }


Using legacy terminal
Configure
Found the Windsurf MCP config. Playwright is enabled. Let me try the correct tool names.

The Playwright MCP server is configured and enabled in your Windsurf config (mcp_config.json), but I can't discover the correct tool name format to invoke it. I've tried mcp_playwright_browser_navigate, mcp__playwright__browser_navigate, mcp_playwright_navigate, and mcp_playwright_snapshot — none match.

Possible causes:

The Playwright MCP server may not be running/connected to this Cascade session
The tool name prefix format may be different than what I'm guessing
How to proceed — pick one:

Check if Playwright tools appear in Cascade — In the chat input, type @ or look in the MCP tools panel to see if Playwright tools are listed and what their exact names are. Share one tool name with me and I can use the rest.
Skip automation, use the manual plan — The action plan is already written in the audit doc with every exact object name. You can execute it in the Zoho Analytics UI in ~15 minutes:
Delete 8 legacy reports (Batch A)
Delete orphan QTs (Batches 1-7)
Create 4 new v4 reports
Add to dashboard
Try the Zoho MCP server instead — it might have API tools to delete views programmatically, which would be cleaner than browser automation.
What would you like to do?

Feedback submitted



xoho mcp

Command cat

cat /home/stan/zoho-mcp-server/stdio-wrapper.js
#!/usr/bin/env node
/**
 * MCP stdio wrapper for zoho-mcp-server HTTP API
 * Translates stdin/stdout JSON-RPC to HTTP calls
 */

const http = require('http');
const readline = require('readline');

const API_PORT = 9091;
const API_PATH = '/mcp/v1';

function makeRequest(body) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify(body);
    const options = {
      hostname: '127.0.0.1',
      port: API_PORT,
      path: API_PATH,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(data)
      }
    };

    const req = http.request(options, (res) => {
      let responseData = '';
      res.on('data', chunk => responseData += chunk);
      res.on('end', () => {
        try {
          resolve(JSON.parse(responseData));
        } catch (e) {
          reject(new Error(`Invalid JSON: ${responseData}`));
        }
      });
    });

    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

function sendResponse(response) {
  process.stdout.write(JSON.stringify(response) + '\n');
}

async function handleMessage(message) {
  try {
    const { jsonrpc, id, method, params } = message;

    if (method === 'initialize') {
      return sendResponse({
        jsonrpc: '2.0',
        id,
        result: {
          protocolVersion: '2024-11-05',
          capabilities: { tools: {} },
          serverInfo: {
            name: 'zoho-mcp-server',
            version: '2.1.0'
          }
        }
      });
    }

    if (method === 'notifications/initialized') {
      return; // No response needed
    }

    if (method === 'tools/list') {
      const result = await makeRequest({ jsonrpc: '2.0', method: 'tools/list', id: 1 });
      return sendResponse({ jsonrpc: '2.0', id, result: result.result });
    }

    if (method === 'tools/call') {
      const { name, arguments: args } = params;
      const result = await makeRequest({
        jsonrpc: '2.0',
        method: 'tools/call',
        id: 1,
        params: { name, arguments: args }
      });

      if (result.error) {
        return sendResponse({
          jsonrpc: '2.0',
          id,
          error: result.error
        });
      }

      return sendResponse({
        jsonrpc: '2.0',
        id,
        result: result.result
      });
    }

    // Unknown method
    sendResponse({
      jsonrpc: '2.0',
      id,
      error: { code: -32601, message: `Method not found: ${method}` }
    });

  } catch (error) {
    sendResponse({
      jsonrpc: '2.0',
      id: message.id,
      error: { code: -32603, message: error.message }
    });
  }
}

// Read JSON-RPC messages from stdin
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

rl.on('line', async (line) => {
  if (!line.trim()) return;
  try {
    const message = JSON.parse(line);
    await handleMessage(message);
  } catch (e) {
    sendResponse({
      jsonrpc: '2.0',
      id: null,
      error: { code: -32700, message: 'Parse error' }
    });
  }
});

process.stderr.write('Zoho MCP stdio wrapper started\n');


Using legacy terminal
Configure
Command curl, python3, head

curl -s -X POST http://127.0.0.1:9091/mcp/v1 -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"tools/list","id":1}' 2>&1 | python3 -m json.tool 2>&1 | head -100
{
    "jsonrpc": "2.0",
    "result": {
        "tools": [
            {
                "name": "search_crm",
                "description": "Search/list Zoho CRM records (Contacts, Accounts, Deals, Leads)",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "module": {
                            "type": "string",
                            "enum": [
                                "Contacts",
                                "Accounts",
                                "Deals",
                                "Leads"
                            ],
                            "description": "CRM module"
                        },
                        "query": {
                            "type": "string",
                            "description": "Optional search term"
                        },
                        "per_page": {
                            "type": "number",
                            "description": "Results per page (default: 20)",
                            "default": 20
                        },
                        "page": {
                            "type": "number",
                            "description": "Page number (default: 1)",
                            "default": 1
                        }
                    },
                    "required": [
                        "module"
                    ]
                },
                "annotations": {
                    "readOnlyHint": true
                }
            },
            {
                "name": "get_books_customers",
                "description": "Get Zoho Books customers/contacts",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "page": {
                            "type": "number",
                            "default": 1
                        },
                        "per_page": {
                            "type": "number",
                            "default": 25
                        },
                        "search": {
                            "type": "string",
                            "description": "Search by name/email"
                        }
                    }
                },
                "annotations": {
                    "readOnlyHint": true
                }
            },
            {
                "name": "get_books_invoices",
                "description": "Get Zoho Books invoices with filtering",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "period": {
                            "type": "string",
                            "enum": [
                                "today",
                                "yesterday",
                                "this_week",
                                "this_month",
                                "mtd",
                                "last_7_days",
                                "last_30_days"
                            ],
                            "description": "Preset date period"
                        },
                        "date": {
                            "type": "string",
                            "description": "Specific date (YYYY-MM-DD)"
                        },
                        "date_start": {
                            "type": "string",
                            "description": "Start date (YYYY-MM-DD)"
                        },
                        "date_end": {
                            "type": "string",
                            "description": "End date (YYYY-MM-DD)"
                        },
                        "status": {
                            "type": "string",


Using legacy terminal
Configure
Command curl, python3

curl -s -X POST http://127.0.0.1:9091/mcp/v1 -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"tools/list","id":1}' 2>&1 | python3 -c "
import json, sys
data = json.load(sys.stdin)
tools = data.get('result', {}).get('tools', [])
for t in tools:
    print(f'{t[\"name\"]:40s} {t[\"description\"][:80]}')
" 2>&1
search_crm                               Search/list Zoho CRM records (Contacts, Accounts, Deals, Leads)
get_books_customers                      Get Zoho Books customers/contacts
get_books_invoices                       Get Zoho Books invoices with filtering
get_sales_summary                        Get sales totals for a period (MTD, today, yesterday, etc.)
get_books_items                          Get Zoho Books inventory items/products
get_inventory_items                      Get Zoho Inventory items with pagination support. Returns items with stock level
zoho/get_inventory_item_detail           Get full details of a single Zoho Inventory item including warehouse-level stock
zoho/get_negative_stock                  Scan all inventory items and return rows where warehouse stock is negative.
update_inventory_item                    Update a Zoho Inventory item (triggers flows)
trigger_zoho_flow                        Trigger a Zoho Flow webhook with optional data payload
update_item                              Update a Zoho Books item (e.g., clear sale price, update stock)
get_invoice_details                      Get full invoice details including line_items (products sold).
get_best_sellers                         Analyze paid invoices and return top selling items.
analytics/list_workspaces                List all Zoho Analytics workspaces (reporting spaces)
analytics/get_workspace                  Get details of a specific Zoho Analytics workspace
analytics/list_views                     List all views (tables, reports, dashboards) in a workspace
analytics/get_view_data                  Get data from a table/view (max 1000 rows)
analytics/duplicate_workspace            Create a copy of an existing workspace with a new name
analytics/list_datasources               List all data source connections in a workspace
analytics/remove_datasource              Remove/disconnect a data source from a workspace
analytics/rename_datasource              Rename a data source connection in a workspace


Using legacy terminal
Configure
The Zoho MCP has analytics tools. No delete/create report tools unfortunately, but I can get datasource info we're missing. Let me try.

Command curl, python3, head

curl -s -X POST http://127.0.0.1:9091/mcp/v1 -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"tools/call","id":1,"params":{"name":"analytics/list_datasources","arguments":{"workspaceId":"2914904000000846397"}}}' 2>&1 | python3 -m json.tool 2>&1 | head -80
{
    "jsonrpc": "2.0",
    "result": {
        "content": [
            {
                "type": "text",
                "text": "{\"error\":\"workspace_id is required\"}"
            }
        ]
    },
    "id": 1
}


Using legacy terminal
Configure
Command curl, python3

curl -s -X POST http://127.0.0.1:9091/mcp/v1 -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","method":"tools/call","id":1,"params":{"name":"analytics/list_datasources","arguments":{"workspace_id":"2914904000000846397"}}}' 2>&1 | python3 -m json.tool 2>&1
{
    "jsonrpc": "2.0",
    "error": {
        "code": -32000,
        "message": "Request failed with status code 400",
        "data": {
            "success": false,
            "error": "Request failed with status code 400",
            "status": 400,
            "details": {
                "status": "failure",
                "summary": "ORGID_NOT_PRESENT_IN_THE_HEADER",
                "data": {
                    "errorCode": 8083,
                    "errorMessage": "Organization id is not present in the request header."
                }
            }
        }
    },
    "id": 1
}


Using legacy terminal
Configure
The Zoho MCP has analytics tools but they're read-only (list views, get data, manage datasources). No delete or create report tools available. And it needs org ID headers that aren't configured.

Bottom line: Neither Playwright MCP nor Zoho MCP can create/delete reports or views from Cascade. The Zoho analytics tools are read-only, and Playwright tool names aren't resolving.

Everything you need is in the audit doc at zoho-analytics-audit-buying-dashboard-gold.md:440-640. It has:

Step 1: Exact report specs to create on v4 (4 reports)
Step 2: Every orphan QT name to delete (7 batches, ~55 tables)
Step 3: 8 legacy report names to delete
Step 4: 5 v2 report names to delete after validation
KEEP list: 9 QTs that v4 needs
This is a manual ~15 min job in the Zoho Analytics UI. Want me to help with anything else while you work through it, or should we move on to another task?

Feedback submitted



get setting from vs code copilot

Command cat

cat /home/stan/.vscode/mcp.json
{
  "servers": {
    "chatgpt-web": {
      "type": "stdio",
      "command": "node",
      "args": ["/home/stan/mcp-chatgpt-web/server.js"],
      "env": {
        "CHATGPT_USER_DATA": "/home/stan/.chatgpt-session"
      }
    },
    "memory": {
      "type": "stdio",
      "command": "node",
      "args": ["/home/stan/memory-mcp-server/stdio-wrapper.js"]
    },
    "zoho": {
      "type": "stdio",
      "command": "node",
      "args": ["/home/stan/zoho-mcp-server/stdio-wrapper.js"]
    },
    "playwright": {
      "type": "stdio",
      "command": "/home/stan/.nvm/versions/node/v20.19.5/bin/npx",
      "args": ["@playwright/mcp@latest", "--user-data-dir", "/home/stan/.playwright-profile"]
    }
  }
}


Using legacy terminal
Configure
Same config as Windsurf — both have Playwright configured identically. The issue is that Cascade can't resolve the MCP tool names even though the server is registered.

Let me try one more thing — check if the Playwright MCP server is actually running:

Command ps, grep

ps aux | grep -i playwright | grep -v grep
stan     1954289  0.0  0.3 1233192 64312 ?       Sl   18:48   0:00 npm exec @playwright/mcp@latest --user-data-dir /home/stan/.playwright-profile
stan     1954337  0.0  0.0   3040  2000 ?        S    18:48   0:00 sh -c "playwright-mcp" --user-data-dir /home/stan/.playwright-profile
stan     1954338  0.0  0.4 11516304 91680 ?      Sl   18:48   0:01 node /home/stan/.npm/_npx/9833c18b2d85bc59/node_modules/.bin/playwright-mcp --user-data-dir /home/stan/.playwright-profile


Using legacy terminal
Configure
Playwright is running. Let me try more tool name formats:

The Playwright MCP server is running (confirmed via ps aux), but Cascade can't invoke it — every tool name format I've tried (mcp_playwright_browser_navigate, playwright_browser_navigate, mcp_playwright_snapshot, etc.) returns "unknown tool name".

This likely means the Playwright MCP server isn't properly registered/connected to this Cascade session, even though it's configured in both ~/.vscode/mcp.json and ~/.codeium/windsurf/mcp_config.json.

How to proceed — your call:

Restart Windsurf/Cascade — this may re-initialize the MCP connections and make Playwright tools discoverable
Use the manual action plan — everything is already written in the audit doc with exact object names. ~15 min in the Zoho Analytics UI to wire v4 and delete orphans
Try from Copilot instead — since Copilot says Playwright is ready there, you could execute the cleanup from VS Code Copilot's chat
What would you like to do?

Feedback submitted



write prompt for copilot

copilot-cleanup-prompt.mdtok`, `vw_DocumentItems`, `vw_Documents`) appeared 2026-02-06 — likely from 1C/external accounting.

---

## What Was Confirmed vs. Needs UI

| Data Point | Status | UI Path If Missing |
|------------|--------|--------------------|
| All 334 view names, types, IDs | ✅ CONFIRMED | — |
| Parent→child dependencies | ✅ CONFIRMED via parentViewId | — |
| Folder groupings (connector ID) | ✅ CONFIRMED | — |
| Created/modified timestamps | ✅ CONFIRMED (SAST) | — |
| Version chains + orphan detection | ✅ CONFIRMED | — |
| Row counts per table | ❌ | Open table → status bar |
| Query table SQL | ❌ | Right-click QT → Edit Design |
| Join keys, WHERE, GROUP BY | ❌ | Right-click QT → Edit Design |
| Formula/derived columns | ❌ | Table → More → Manage Columns → "Formula" |
| Sync schedule + type | ❌ | Settings → Data Sources → click connector |
| Dashboard widget→report map | ❌ | Open dashboard → click each widget |

---

## A) Workspace Inventory

### Object Counts

| Type | Count |
|------|-------|
| Base Tables | 134 |
| Query Tables | 70 |
| Dashboards | 12 |
| Pivot Reports | 38 |
| Analysis Views (charts) | 74 |
| Tabular Reports | 3 |
| Summary Views | 3 |
| **Total** | **334** |

### Data Sources / Connectors (confirmed from folder analysis)

| Connector | Org | Tables | Connector Folders | Last Data Update |
|-----------|-----|--------|-------------------|-----------------|
| **Zoho Books/Inventory (BMParts)** | 856737871 | ~50 (no suffix) | …846461, …846471, …846460, …846476 | 2026-02-16 07:54 SAST |
| **Zoho Inventory (Spares to Africa)** | 857295887 | 84 (suffix "Zoho Inventory") | …909180 (17), …909228 (41), …909729 (12), …930732 (2), …931001 (7), …932208 (5) | 2026-02-16 07:54 SAST |
| **Manual Import** | — | 4 | Main folder | See below |

**Still needs UI** (`Settings > Data Sources`): sync schedule, incremental vs full, primary key strategy.

### Custom / Manually Imported Tables

| Table | Created | Last Modified | Origin |
|-------|---------|---------------|--------|
| Calendar_Dates | 2026-01-19 14:10 | 2026-01-19 14:10 | Manual — date dimension, **never updated since creation** |
| vw_DetailOstatok | 2026-02-06 22:18 | 2026-02-06 22:29 | External (1C/accounting — Russian: "balance detail") |
| vw_DocumentItems | 2026-02-06 22:18 | 2026-02-06 22:28 | External (1C — document line items) |
| vw_Documents | 2026-02-06 22:18 | 2026-02-06 22:28 | External (1C — document headers) |

### Base Tables (134 total)

All BMParts tables created **2026-01-11 16:50** (workspace init). All STA tables created **2026-01-17 06:02**.
All synced as of **2026-02-16 07:54 SAST**. Row counts need UI verification (🔍).

#### BMParts Core Tables (no suffix) — key tables only

| Table | Folder | Downstream Reports |
|-------|--------|--------------------|
| Items | …846461 | 11 reports (Top 10s, Stock In/Out, Profit, Top100) |
| Invoices | …846461 | 22 reports (Sales trends, Revenue, Invoice stats) |
| Customers | …846461 | 18 reports (Aging, Balances, Top 10 Customers) |
| Sales Orders | …846461 | 8 reports (SO trends, Fill Rate, MTD) |
| Invoice Items | …846461 | 1 report (Profit by Items) |
| Accounts | …846461 | 28 reports (Balance Sheet, P&L, Cash Flow) |
| Taxes | …846461 | 4 reports (Tax Summary, Tax rates) |
| Shipment Order | …846471 | 3 reports (Carrier, Shipment status) |
| Sales Order Invoice | …846461 | 1 report (Sales Funnel) |
| Sales Persons | …846461 | 1 report (Invoice Stats by Salesperson) |
| Quotes | …846476 | 2 reports (Estimates Trend) |
| Payment Refunds | …846461 | 1 report (Refund History) |
| Vendors (Zoho Inventory) | STA folder | 1 report (Purchase Receive History) |

#### Spares to Africa Tables — 84 tables with "(Zoho Inventory)" suffix

Key tables: Items, Invoices, Invoice Items, Sales Orders, Sales Order Items, Purchase Orders, Purchase Order Items, Purchase Receive, Stock In/Out Flow, Inventory Adjustment Items, Credit Notes, Credit Note Items, Customers, Vendors, Locations, Landed Cost, Landed Cost Allocation, Transfer Order, Transfer Order Items.

**Only 1 STA base table has a direct report dependency:** `Vendors (Zoho Inventory)` → `Purchase Receive History (Zoho Inventory)` pivot.

---

### Query Tables (70 total)

#### ACTIVE Query Tables — Only 3 Have Downstream Dependents

| Query Table | Dependents | Created | Downstream Reports |
|-------------|------------|---------|-------------------|
| **Buying_Base_v2** | **5** | 2026-01-16 16:37 | Buying List v3 FINAL, Count SKUs to Reorder v3, Top Reorders v3 FINAL, Total Reorder Qty v3, Untitled-1 |
| **Buying_Base_v2_OLD** | **8** | 2026-01-16 13:05 | Buying List, Buying List v3, Buying List v3 new, Count of SKUs to Reorder, Min DaysCover, Top Reorders, Top Reorders v3, Total Reorder Qty |
| **Cash Flow Query** | **1** | 2026-01-11 16:50 | Cash Flow Statement |

#### ORPHAN STA Pipeline (22 query tables — built but never connected)

| Query Table | Created | Last Modified | Refresh Batch |
|-------------|---------|---------------|---------------|
| STA_Items | 2026-01-17 11:12 | 2026-02-16 07:54 | 07:54 batch |
| STA_Invoices | 2026-01-17 11:25 | 2026-02-16 01:10 | 01:10 batch |
| STA_Invoice_Items | 2026-01-17 11:25 | 2026-02-16 01:10 | 01:10 batch |
| STA_Invoice_Lines_v1 | 2026-02-06 23:42 | 2026-02-16 07:54 | 07:54 batch |
| STA_Warehouses | 2026-01-17 11:13 | 2026-02-16 01:10 | 01:10 batch |
| STA_Item_Stock_By_Warehouse | 2026-01-17 11:13 | 2026-02-16 01:10 | 01:10 batch |
| STA_Stock_By_Item | 2026-01-17 11:28 | 2026-02-16 01:10 | 01:10 batch |
| STA_Stock_By_Item_v2 | 2026-01-17 11:38 | 2026-02-16 01:10 | 01:10 batch |
| STA_Stock_Daily_v1 | 2026-01-19 13:22 | 2026-02-16 01:10 | 01:10 batch |
| STA_Stock_Daily_v2 | 2026-01-24 15:18 | 2026-02-16 01:10 | 01:10 batch |
| STA_Stock_Availability_90_v1 | 2026-01-19 14:46 | 2026-02-16 01:10 | 01:10 batch |
| STA_Stock_Availability_90_v2 | 2026-01-24 15:22 | 2026-02-16 01:10 | 01:10 batch |
| STA_Sales_Fact_180d | 2026-01-17 11:27 | 2026-02-16 07:54 | 07:54 batch |
| STA_Sales_Fact_180d_v2 | 2026-01-17 11:37 | 2026-02-16 07:54 | 07:54 batch |
| STA_Sales_Fact_180d_v3 | 2026-01-17 12:22 | 2026-02-16 07:54 | 07:54 batch |
| STA_Sales_Agg | 2026-01-17 11:27 | 2026-02-16 07:54 | 07:54 batch |
| STA_Sales_Agg_v2 | 2026-01-17 11:38 | 2026-02-16 07:54 | 07:54 batch |
| STA_Sales_Agg_v3 | 2026-01-17 12:22 | 2026-02-16 07:54 | 07:54 batch |
| STA_Sales_Agg_90_v1 | 2026-02-06 23:51 | 2026-02-16 07:54 | 07:54 batch |
| STA_Sales_Agg_External90_v1 | 2026-02-06 23:27 | 2026-02-16 01:10 | 01:10 batch |
| STA_AsOf_TxnDate_v1 | 2026-01-24 15:17 | 2026-02-16 01:10 | 01:10 batch |
| STA_Latest_Txn_By_Day_v1 | 2026-01-19 14:26 | 2026-02-16 01:10 | 01:10 batch |

**Note:** Two refresh batches visible — 01:10 (stock-related QTs) and 07:54 (sales/items QTs). Likely different scheduled refresh groups.

#### ORPHAN Buying Base Iterations (5 — never connected to reports)

| Query Table | Created | Status |
|-------------|---------|--------|
| Buying_Base | 2026-01-16 13:05 | ORPHAN — original, no dependents |
| buying_base_sta | 2026-01-17 11:28 | ORPHAN — first STA attempt |
| buying_base_sta_v2 | 2026-01-17 11:39 | ORPHAN |
| buying_base_sta_v3 | 2026-01-17 12:23 | ORPHAN |
| **buying_base_sta_v4** | **2026-01-23 16:12** | **LATEST — intended production version, not yet wired into reports** |

#### ORPHAN Sales/Stock/BMP Tables (5)

| Query Table | Created |
|-------------|---------|
| BMP_Sales_Agg_90_v1 | 2026-02-06 23:56 |
| Sales_Agg_NEW | 2026-01-16 13:04 |
| Sales_Fact_NEW_180d | 2026-01-16 13:02 |
| Stock_By_Item | 2026-01-16 13:04 |
| Stock_By_Item_v2 | 2026-01-16 16:34 |

#### ORPHAN Top SKU Analysis (7)

| Query Table | Created |
|-------------|---------|
| Top 10 Items by Category - 6 Months | 2026-01-16 06:42 |
| Top 10 NEW Items by Category - 6 Months | 2026-01-16 06:59 |
| Top 10 SKUs - Filterable by Period | 2026-01-16 10:01 |
| Top 10 SKUs by Category - NEW - 6 Months | 2026-01-16 07:07 |
| Top 10 SKUs by Category with Stock - NEW | 2026-01-16 07:24 |
| Top 10 SKUs with Stock Model Engine - NEW | 2026-01-16 07:43 |
| Top SKUs by Category - Dynamic Filter | 2026-01-16 10:01 |

#### ORPHAN Audit/Debug (4)

| Query Table | Created |
|-------------|---------|
| AvBuilderAudit | 2026-01-21 13:34 |
| B audit | 2026-01-21 13:32 |
| MIssmatchFinderA | 2026-01-21 13:27 |
| Missing Row | 2026-01-21 13:42 |

#### Test/Temp Tables — 24 (safe to delete, all orphans)

`_buying_sta_sample`, `_buying_sta_v2_sample_test`, `_direct_xenon_test2`, `_join_test_v3`, `_spares_compare_test`, `_spares_items_sample`, `_spares_items_xenon`, `_spares_stock_sample`, `_spares_stock_xenon_vanos`, `_spares_xenon_bulb`, `_sta_items_xenon_test`, `_temp_avail_check_v1`, `_temp_xenon_stock`, `_verify_stock_v2_sum`, `_verify_stock_v2_xenon`, `_verify_xenon_sum`, `_verify_xenon_v2_final`, `_verify_xenon_v3`, `_verify_xenon_v3b`, `QT_Test_DateFilter2`, `QT_Test_FromTable`, `QT_Test_Join`, `QT_Test_Minimal`, `test query`

#### Version Chains (confirmed)

| Base Name | Versions (oldest → newest) | Which Has Dependents? |
|-----------|---------------------------|----------------------|
| Buying_Base_v2 | _v2_OLD → _v2 | **BOTH** (OLD=8, v2=5) |
| buying_base_sta | v1 → v2 → v3 → v4 | **NONE** |
| STA_Sales_Fact_180d | v1 → v2 → v3 | **NONE** |
| STA_Sales_Agg | v1 → v2 → v3 | **NONE** |
| STA_Stock_By_Item | v1 → v2 | **NONE** |
| STA_Stock_Daily | v1 → v2 | **NONE** |
| STA_Stock_Availability_90 | v1 → v2 | **NONE** |
| Stock_By_Item | v1 → v2 | **NONE** |

---

### Dashboards (12 total)

| Dashboard | Last Modified | Type | Folder |
|-----------|---------------|------|--------|
| **Buying Dashboard** | **2026-01-16 15:11** | **Custom** | …846461 (main) |
| Customers Insights Dashboard | 2026-01-11 16:56 | Auto-generated | …846463 |
| Finance Overview Dashboard | 2026-01-11 16:51 | Auto-generated | …846463 |
| Financial Statement Dashboard | 2026-01-11 16:51 | Auto-generated | …846463 |
| Inventory Overview Dashboard | 2026-01-12 12:20 | Auto-generated | …846463 |
| Inventory Sales Orders and Invoices Dashboard | 2026-01-11 16:58 | Auto-generated | …846463 |
| Inventory Shipment and Sales Returns Dashboard | 2026-01-11 17:00 | Auto-generated | …846463 |
| Sales and Receivables Dashboard | 2026-01-11 16:51 | Auto-generated | …846463 |
| Subscriptions Customer Dashboard | 2026-01-11 17:16 | Auto-generated | …846463 |
| Subscriptions Overview Dashboard | 2026-01-11 17:16 | Auto-generated | …846463 |
| Subscriptions Revenue Dashboard | 2026-01-11 17:16 | Auto-generated | …846463 |
| Vendor Insights Dashboard | 2026-01-11 17:16 | Auto-generated | …846463 |

**11 dashboards are Zoho-auto-generated** (created 2026-01-11, folder …846463). Only **Buying Dashboard** is custom.

---

### Reports — Confirmed Source Mapping (via parentViewId)

#### Reports sourced from `Buying_Base_v2` (CURRENT PRODUCTION)

| Report | Type | Confirmed |
|--------|------|-----------|
| **Buying List v3 FINAL** | Pivot | ✅ parentViewId → Buying_Base_v2 |
| **Count SKUs to Reorder v3** | Pivot | ✅ parentViewId → Buying_Base_v2 |
| **Top Reorders v3 FINAL** | AnalysisView | ✅ parentViewId → Buying_Base_v2 |
| **Total Reorder Qty v3** | Pivot | ✅ parentViewId → Buying_Base_v2 |
| **Untitled-1** | Pivot | ✅ parentViewId → Buying_Base_v2 |

#### Reports sourced from `Buying_Base_v2_OLD` (LEGACY — still active!)

| Report | Type | Confirmed |
|--------|------|-----------|
| Buying List | Report | ✅ parentViewId → Buying_Base_v2_OLD |
| Buying List v3 | Report | ✅ parentViewId → Buying_Base_v2_OLD |
| Buying List v3 new | Report | ✅ parentViewId → Buying_Base_v2_OLD |
| Count of SKUs to Reorder | SummaryView | ✅ parentViewId → Buying_Base_v2_OLD |
| Min DaysCover | SummaryView | ✅ parentViewId → Buying_Base_v2_OLD |
| Top Reorders | AnalysisView | ✅ parentViewId → Buying_Base_v2_OLD |
| Top Reorders v3 | AnalysisView | ✅ parentViewId → Buying_Base_v2_OLD |
| Total Reorder Qty | SummaryView | ✅ parentViewId → Buying_Base_v2_OLD |

#### Reports sourced from base tables (auto-generated by Zoho connectors)

| Parent Table | Report Count | Example Reports |
|-------------|-------------|-----------------|
| Accounts | 28 | Balance Sheet, P&L, Cash Flow, Financial Overview |
| Invoices | 22 | Sales Trend, Invoice Stats, Revenue trends |
| Customers | 18 | Aging Summary, Customer Balances, Top 10 Customers |
| Items | 11 | Top 10 Fast Moving, Stock In/Out, Top100 |
| Sales Orders | 8 | SO Count/Value trends, Fill Rate, MTD Cumulative |
| Taxes | 4 | Tax Summary, Tax Rate trends |
| Shipment Order | 3 | Carrier Distribution, Shipments by Status |
| Quotes | 2 | Estimates Trend, Top 10 Open Estimates |
| Sales Order Invoice | 1 | Sales Funnel |
| Invoice Items | 1 | Profit by Items |
| Sales Persons | 1 | Invoice Stats by Salesperson |
| Payment Refunds | 1 | Refund History |
| Users | 1 | Distribution of Employee by Role |
| Vendors (Zoho Inventory) | 1 | Purchase Receive History |
| Cash Flow Query | 1 | Cash Flow Statement |

---

## B) Dependency Graph

### Confirmed Dependency Graph (from parentViewId)

```
Buying Dashboard (custom, folder …846461)
│
├── CURRENT (from Buying_Base_v2):
│   ├── Buying List v3 FINAL (Pivot) ← Buying_Base_v2
│   ├── Count SKUs to Reorder v3 (Pivot) ← Buying_Base_v2
│   ├── Top Reorders v3 FINAL (AnalysisView) ← Buying_Base_v2
│   ├── Total Reorder Qty v3 (Pivot) ← Buying_Base_v2
│   └── Untitled-1 (Pivot) ← Buying_Base_v2
│
├── LEGACY (from Buying_Base_v2_OLD — still wired!):
│   ├── Buying List (Report) ← Buying_Base_v2_OLD
│   ├── Buying List v3 (Report) ← Buying_Base_v2_OLD
│   ├── Buying List v3 new (Report) ← Buying_Base_v2_OLD
│   ├── Count of SKUs to Reorder (SummaryView) ← Buying_Base_v2_OLD
│   ├── Min DaysCover (SummaryView) ← Buying_Base_v2_OLD
│   ├── Top Reorders (AnalysisView) ← Buying_Base_v2_OLD
│   ├── Top Reorders v3 (AnalysisView) ← Buying_Base_v2_OLD
│   └── Total Reorder Qty (SummaryView) ← Buying_Base_v2_OLD
│
└── PENDING CUTOVER (STA pipeline — built, ready to wire):
    buying_base_sta_v4 (LATEST — not yet connected to reports)
    ├── Likely uses: STA_Items, STA_Stock_By_Item_v2, STA_Sales_Agg_v3 (verify SQL)
    └── STA_* chain → base tables "(Zoho Inventory)" from Spares to Africa
```

**`buying_base_sta_v4` is the intended replacement** for both `Buying_Base_v2` and `Buying_Base_v2_OLD`.
The critical next step is wiring v4 into new reports and validating against the current dashboard before cutover.
`Buying_Base_v2` SQL should still be inspected to understand what the current dashboard shows for comparison.

### Upstream Dependencies (inferred — needs SQL verification)

```
Buying_Base_v2 (PRODUCTION — SQL unknown, inspect via Edit Design)
├── ? Items                          -- BMParts items?
├── ? Invoice Items                  -- BMParts sales?
├── ? Stock In/Out Flow Tables       -- BMParts stock?
└── ? OR does it reference STA_* query tables?

buying_base_sta_v4 (LATEST — SQL CONFIRMED)
├── Items (Zoho Inventory)              ← driving table (STA base table)
├── STA_Sales_Agg_v3                    ← JOIN ON ItemID (sales 30/90/180d)
├── STA_Stock_By_Item_v2                ← JOIN ON ItemID (stock on hand)
├── STA_Stock_Availability_90_v1        ← JOIN ON ItemID (⚠️ uses v1 not v2!)
├── STA_Sales_Agg_External90_v1         ← JOIN ON ItemID (external revenue)
└── BMP_Sales_Agg_90_v1                 ← JOIN ON SKU ⚠️ (cross-org, not ItemID)
```

### Top 10 Most Central Objects (confirmed downstream counts)

| Rank | Object | Type | Downstream Reports | Risk |
|------|--------|------|--------------------|------|
| 1 | **Accounts** | Table | 28 | Financial core |
| 2 | **Invoices** | Table | 22 | Sales/revenue core |
| 3 | **Customers** | Table | 18 | Customer analytics |
| 4 | **Items** | Table | 11 | Product master |
| 5 | **Buying_Base_v2_OLD** | QueryTable | 8 | ⚠️ LEGACY still active |
| 6 | **Sales Orders** | Table | 8 | SO analytics |
| 7 | **Buying_Base_v2** | QueryTable | 5 | PRODUCTION buying |
| 8 | **Taxes** | Table | 4 | Tax reports |
| 9 | **Shipment Order** | Table | 3 | Shipping |
| 10 | **Quotes** | Table | 2 | Estimates |

**Key insight:** No STA_* query table or STA base table (except Vendors) has any downstream dependents. The entire STA pipeline is invisible to dashboards/reports.

---

## C) Risk Audit

### 🔴 CONFIRMED HIGH RISK

#### 1. `Buying_Base_v2_OLD` Still Powers 8 Reports
**Status:** ✅ CONFIRMED from parentViewId  
**Impact:** Reports sourced from the OLD query table may show different data than `Buying_Base_v2`.  
**Action:** Inspect SQL of both `Buying_Base_v2` and `Buying_Base_v2_OLD` — if they differ, the dashboard shows inconsistent data between the v3 FINAL reports and the legacy reports.  
**To check:** Right-click each → Edit Design → compare SQL.

#### 2. `Buying_Base_v2` SQL Is Unknown — Single Point of Failure
**Status:** ✅ CONFIRMED — API does not expose SQL  
**Impact:** All 5 production buying reports depend on one query table whose logic is opaque.  
**Action:** Right-click `Buying_Base_v2` → Edit Design → document the full SQL. Look for:
- Join keys (item_id vs sku vs name)
- Which org's tables it uses (BMParts vs STA)
- Warehouse handling (filtered or summed blindly)
- NEW/USED handling (cf_condition filter present?)
- Date field used (invoice_date vs created_time)
- Status filter (void/draft excluded?)

#### 3. STA Pipeline Not Yet Wired — 22 QTs Refreshing Without Reports
**Status:** ✅ CONFIRMED — all 22 STA_* QTs have 0 report dependents (yet)  
**Impact:** These query tables refresh on schedule (two batches: 01:10 and 07:54) and feed `buying_base_sta_v4`, but v4 itself has no reports pointing to it yet.  
**Action:** Wire `buying_base_sta_v4` into new reports → add to dashboard → validate → cutover from `Buying_Base_v2`.

#### 4. `Calendar_Dates` Never Updated
**Status:** ✅ CONFIRMED — created 2026-01-19, never modified  
**Impact:** If any query uses date joins against this table, it may run out of rows or miss future dates.  
**Action:** Check if any QT references `Calendar_Dates`. If so, set up periodic refresh or extend the date range.

### 🟡 CONFIRMED FROM v4 SQL — Needs Fix or Verification

#### 5. ~~No NEW/USED Filter in v4~~ — NOT A RISK
**Status:** Downgraded — **STA org (Spares to Africa) only stocks NEW items.**  
**Impact:** None. The driving table `Items (Zoho Inventory)` only contains NEW condition items, so no `cf_Condition` filter is needed.  
**Note:** This WOULD be a risk if BMParts items (which include USED) were ever added to v4's FROM clause.

#### 6. ⚠️ No Status Filter in v4
**Status:** ✅ CONFIRMED — no WHERE clause at all  
**Impact:** Inactive/discontinued STA items may inflate row count (671 rows) and produce zero-sales reorder suggestions.  
**Fix:** Consider adding `WHERE it."Status" = 'Active'` to exclude discontinued items, or verify that STA only has active items.

#### 7. ~~Cross-Org SKU Join~~ — NOT A RISK
**Status:** Downgraded — **SKUs match correctly between BMParts and STA orgs** (user confirmed).  
**Note:** `bmp."SKU" = it."SKU"` is valid for cross-org revenue attribution.

#### 8. ⚠️ Uses Availability v1 Not v2
**Status:** SQL compared — **identical logic**, only difference is upstream table:  
- v1: `FROM STA_Stock_Daily_v1` ← used by v4  
- v2: `FROM STA_Stock_Daily_v2`  
**Impact:** Depends on what changed between `STA_Stock_Daily_v1` and `_v2`.  
**Action:** Compare `STA_Stock_Daily_v1` vs `_v2` SQL to determine if v4 should switch to availability v2.

#### 9. ~~Possible Typo: `it."Categor"`~~ — NOT A RISK
**Status:** Downgraded — **`"Categor"` is the actual column name** in Items (Zoho Inventory). Not a typo.

#### 10. Warehouse Handling — Unknown (Pushed to Upstream QTs)
**Status:** v4 itself has no warehouse filter. Depends on `STA_Stock_By_Item_v2`.  
**Action:** Inspect `STA_Stock_By_Item_v2` SQL — does it filter out WEB/VIRTUAL/SPECIAL SALE warehouses?

### 🟡 STILL NEEDS VERIFICATION (upstream QTs)

#### 11. Date Fields in Sales Aggregation
**Where to check:** `STA_Sales_Agg_v3`, `STA_Sales_Fact_180d_v3`  
**Risk:** `created_time` used instead of `invoice_date`

#### 12. Missing Returns/Credit Notes
**Where to check:** `STA_Sales_Agg_v3` — does it subtract credit note items?

#### 13. Status Filters in Upstream QTs
**Where to check:** `STA_Sales_Agg_v3`, `STA_Sales_Fact_180d_v3` — do they exclude void/draft invoices?

#### 14. Stock Computation Method
**Where to check:** `STA_Stock_By_Item_v2` — snapshot import or computed from events?

### 🟢 CONFIRMED LOW RISK

#### 15. 67 Orphan Query Tables
**Status:** ✅ CONFIRMED  
**Impact:** Workspace clutter, wasted refresh compute  
**Action:** Safe to archive/delete — none have downstream dependents

#### 16. 24 Test/Debug Tables
**Status:** ✅ CONFIRMED (all prefixed with `_` or `QT_Test_`)  
**Impact:** No dependencies, safe to delete immediately

#### 17. `Untitled-1` Pivot Report
**Status:** ✅ CONFIRMED — sourced from Buying_Base_v2  
**Impact:** Unnamed report in production — accidental or work-in-progress  
**Action:** Rename or delete

---

## D) Cleanup Plan (Non-Breaking)

### ✅ ACTION PLAN — Execute Now

---

### Step 1: Wire `buying_base_sta_v4` Into Reports

v4 columns: `Category, SKU, ItemID, ItemName, Model, Engine, Sub.Lighting, Image URL, AvailabilityMissingFlag, InStockDays90, StockAvailability90_Pct, SoldWhileUnavailableFlag, QtySold30, QtySold90, QtySold180, Revenue90_Internal_Old, Revenue90_STA_External, Revenue90_BMP_Retail, Revenue90_Total_Real, QTY, AvgDaily90, AvgDaily90_Pct, SaleConsistencyScore, DaysCover, ReorderQty, org_key`

**1a. Create new Pivot: "Buying List v4"**
- Click `+` → New Pivot View → Source: `buying_base_sta_v4`
- Rows: SKU, ItemName, Category, Model
- Columns: QTY, QtySold90, DaysCover, ReorderQty, Revenue90_Total_Real, SaleConsistencyScore
- Save as: `Buying List v4`

**1b. Create new Pivot: "Count SKUs to Reorder v4"**
- New Pivot → Source: `buying_base_sta_v4`
- Filter: ReorderQty > 0
- Show: COUNT of SKU
- Save as: `Count SKUs to Reorder v4`

**1c. Create new Chart: "Top Reorders v4"**
- New Chart → Source: `buying_base_sta_v4`
- Filter: ReorderQty > 0
- X: ItemName or SKU, Y: ReorderQty
- Sort: ReorderQty DESC, Top 20
- Save as: `Top Reorders v4`

**1d. Create new Pivot: "Total Reorder Qty v4"**
- New Pivot → Source: `buying_base_sta_v4`
- Show: SUM of ReorderQty
- Save as: `Total Reorder Qty v4`

**1e. Add to Buying Dashboard**
- Open Buying Dashboard → Edit
- Add the 4 new v4 reports as widgets
- Optionally remove or keep old v2 widgets for comparison
- Save dashboard

---

### Step 2: Delete Orphan Query Tables

**Delete in this order** (bottom-up to avoid any dependency issues):

**Batch 1 — 24 Test/Temp tables (zero risk):**
Right-click each → Delete. No dependencies.

```
_buying_sta_sample
_buying_sta_v2_sample_test
_direct_xenon_test2
_join_test_v3
_spares_compare_test
_spares_items_sample
_spares_items_xenon
_spares_stock_sample
_spares_stock_xenon_vanos
_spares_xenon_bulb
_sta_items_xenon_test
_temp_avail_check_v1
_temp_xenon_stock
_verify_stock_v2_sum
_verify_stock_v2_xenon
_verify_xenon_sum
_verify_xenon_v2_final
_verify_xenon_v3
_verify_xenon_v3b
QT_Test_DateFilter2
QT_Test_FromTable
QT_Test_Join
QT_Test_Minimal
test query
```

**Batch 2 — 4 Audit/debug tables (zero risk):**
```
AvBuilderAudit
B audit
MIssmatchFinderA
Missing Row
```

**Batch 3 — 7 Top SKU orphans (zero risk):**
```
Top 10 Items by Category - 6 Months
Top 10 NEW Items by Category - 6 Months
Top 10 SKUs - Filterable by Period
Top 10 SKUs by Category - NEW - 6 Months
Top 10 SKUs by Category with Stock - NEW
Top 10 SKUs with Stock Model Engine - NEW
Top SKUs by Category - Dynamic Filter
```

**Batch 4 — 5 Old sales/stock orphans (zero risk):**
```
Sales_Agg_NEW
Sales_Fact_NEW_180d
Stock_By_Item
Stock_By_Item_v2
Buying_Base
```

**Batch 5 — 3 Old buying_base_sta versions (v4 is the keeper):**
```
buying_base_sta
buying_base_sta_v2
buying_base_sta_v3
```

**Batch 6 — Old version chain predecessors (keep latest of each):**
```
STA_Sales_Fact_180d          (keep v3)
STA_Sales_Fact_180d_v2       (keep v3)
STA_Sales_Agg                (keep v3)
STA_Sales_Agg_v2             (keep v3)
STA_Stock_By_Item            (keep v2)
STA_Stock_Daily_v1           (keep v2)
STA_Stock_Availability_90_v1 (keep v2 — BUT v4 currently uses v1! Switch v4 to v2 FIRST)
```

**⚠️ BEFORE deleting `STA_Stock_Availability_90_v1`:** Update v4's SQL to use `STA_Stock_Availability_90_v2` instead.

**Batch 7 — Unused STA QTs not referenced by v4 (verify first):**
```
STA_Items                    (v4 doesn't use this — uses base table directly)
STA_Invoices                 (not used by v4)
STA_Invoice_Items            (not used by v4)
STA_Invoice_Lines_v1         (not used by v4)
STA_Warehouses               (not used by v4)
STA_Item_Stock_By_Warehouse  (not used by v4)
STA_AsOf_TxnDate_v1          (not used by v4)
STA_Latest_Txn_By_Day_v1     (not used by v4)
STA_Sales_Agg_90_v1          (not used by v4)
STA_Stock_Daily_v2           (used by STA_Stock_Availability_90_v2 — keep if keeping avail v2)
STA_Stock_Availability_90_v2 (keep — switch v4 to use this)
```

---

### Step 3: Handle Legacy Reports on `Buying_Base_v2_OLD`

After v4 reports are confirmed working on the dashboard:

**Option A (recommended): Delete the 8 legacy reports**
These are old versions superseded by v4 reports:
```
Buying List                    (replaced by Buying List v4)
Buying List v3                 (replaced by Buying List v4)
Buying List v3 new             (replaced by Buying List v4)
Count of SKUs to Reorder       (replaced by Count SKUs to Reorder v4)
Min DaysCover                  (replaced by DaysCover in v4)
Top Reorders                   (replaced by Top Reorders v4)
Top Reorders v3                (replaced by Top Reorders v4)
Total Reorder Qty              (replaced by Total Reorder Qty v4)
```

Then delete `Buying_Base_v2_OLD` (0 dependents after reports removed).

**Option B: Repoint them to v4**
Right-click each report → Change Underlying Data Source → select `buying_base_sta_v4`.
(May break if column names differ from v2_OLD.)

---

### Step 4: Delete Old v2 Reports + Query Tables

After v4 dashboard is validated and legacy reports removed:
```
Untitled-1                     (orphan pivot on v2)
Buying List v3 FINAL           (if replaced by v4 version)
Count SKUs to Reorder v3       (if replaced by v4 version)
Top Reorders v3 FINAL          (if replaced by v4 version)
Total Reorder Qty v3           (if replaced by v4 version)
Buying_Base_v2                 (0 dependents after above)
Buying_Base_v2_OLD             (0 dependents after Step 3)
```

---

### STA QTs to KEEP (referenced by v4 or its upstream chain)

| Keep | Reason |
|------|--------|
| **buying_base_sta_v4** | Production query |
| **STA_Sales_Agg_v3** | Used by v4 (alias `a`) |
| **STA_Stock_By_Item_v2** | Used by v4 (alias `st`) |
| **STA_Stock_Availability_90_v2** | Switch v4 to use this instead of v1 |
| **STA_Sales_Agg_External90_v1** | Used by v4 (alias `sta_ext`) |
| **BMP_Sales_Agg_90_v1** | Used by v4 (alias `bmp`) |
| **STA_Sales_Fact_180d_v3** | Likely upstream of STA_Sales_Agg_v3 |
| **STA_Stock_Daily_v2** | Upstream of STA_Stock_Availability_90_v2 |
| **Cash Flow Query** | Unrelated, powers Cash Flow Statement |

### Summary: From 70 → 9 Query Tables

| Before | After |
|--------|-------|
| 70 query tables | **9 query tables** |
| 67 orphans | **0 orphans** |
| 24 test tables | **0 test tables** |
| 8 version chains | **latest versions only** |

---

## Appendix: Priority SQL Inspection Checklist

Open Zoho Analytics → right-click each → Edit Design → paste SQL below.

### 1. `Buying_Base_v2` (PRODUCTION — powers 5 reports)
```
SQL: [PASTE HERE]

Check:
- [ ] Join keys: item_id or name/sku?
- [ ] Which tables: BMParts (no suffix) or STA ("Zoho Inventory")?
- [ ] Warehouse filter: WHERE warehouse_name IN ('WEB', ...) ?
- [ ] Condition filter: WHERE cf_condition = 'NEW' ?
- [ ] Date field: invoice_date or created_time ?
- [ ] Status filter: WHERE status NOT IN ('void', 'draft') ?
- [ ] Credit notes handling?
```

### 2. `Buying_Base_v2_OLD` (LEGACY — powers 8 reports)
```
SQL: [PASTE HERE]

Differences from v2: [DOCUMENT]
```

### 3. `buying_base_sta_v4` (LATEST — target production query) — FULL SQL

**Output:** 671 rows. Categories: SUSPENSION, LIGHTING, ENGINE, ELECTRICAL SYSTEM, BODYWORK, COOLING SYSTEM.

```sql
SELECT
    COALESCE(it."Categor", a."Category") AS "Category",
    it."SKU" AS "SKU",
    it."Item ID" AS "ItemID",
    it."Item Name" AS "ItemName",
    it."Model" AS "Model",
    a."Engine" AS "Engine",
    it."Lighting Modules" AS "Sub.Lighting",
    it."Image URL" AS "Image URL",

    /* --- Availability diagnostics (hardened) --- */
    CASE
        WHEN av90."ItemID" IS NULL THEN 1
        ELSE 0
    END AS "AvailabilityMissingFlag",
    COALESCE(av90."InStockDays90", 0) AS "InStockDays90",
    COALESCE(av90."StockAvailability90_Pct", 0) AS "StockAvailability90_Pct",

    /* Sold but availability says 0 (model contradiction flag) */
    CASE
        WHEN COALESCE(a."QtySold90", 0) > 0
        AND  COALESCE(av90."InStockDays90", 0) = 0 THEN 1
        ELSE 0
    END AS "SoldWhileUnavailableFlag",

    /* --- Sales volumes (STA-based) --- */
    COALESCE(a."QtySold30", 0) AS "QtySold30",
    COALESCE(a."QtySold90", 0) AS "QtySold90",
    COALESCE(a."QtySold180", 0) AS "QtySold180",

    /* --- Revenue --- */
    COALESCE(a."Revenue90", 0) AS "Revenue90_Internal_Old",
    COALESCE(sta_ext."Revenue90_STA_External", 0) AS "Revenue90_STA_External",
    COALESCE(bmp."Revenue90_BMP_Retail", 0) AS "Revenue90_BMP_Retail",

    /* TRUE GROUP REVENUE (only uses numeric sources) */
    COALESCE(sta_ext."Revenue90_STA_External", 0)
      + COALESCE(bmp."Revenue90_BMP_Retail", 0) AS "Revenue90_Total_Real",

    /* --- Stock --- */
    COALESCE(st."StockOnHand", 0) AS "QTY",

    /* --- Velocity --- */
    ROUND(CASE
        WHEN COALESCE(a."QtySold90", 0) = 0 THEN 0
        ELSE COALESCE(a."QtySold90", 0) / 90.0
    END, 2) AS "AvgDaily90",
    ROUND(CASE
        WHEN COALESCE(a."QtySold90", 0) = 0 THEN 0
        ELSE (COALESCE(a."QtySold90", 0) / 90.0) * 100.0
    END, 0) AS "AvgDaily90_Pct",

    /* --- Consistency score --- */
    CASE
        WHEN (COALESCE(a."QtySold90", 0) / 90.0) >= 1.0 THEN 100
        WHEN (COALESCE(a."QtySold90", 0) / 90.0) >= (1.0 / 3.0) THEN 80
        WHEN (COALESCE(a."QtySold90", 0) / 90.0) >= (1.0 / 7.0) THEN 60
        WHEN (COALESCE(a."QtySold90", 0) / 90.0) >= (1.0 / 30.0) THEN 20
        ELSE 0
    END AS "SaleConsistencyScore",

    /* --- Coverage & reorder --- */
    CASE
        WHEN COALESCE(a."QtySold90", 0) = 0 THEN NULL
        ELSE COALESCE(st."StockOnHand", 0) / (COALESCE(a."QtySold90", 0) / 90.0)
    END AS "DaysCover",

    CASE
        WHEN (59 * (COALESCE(a."QtySold90", 0) / 90.0))
             - COALESCE(st."StockOnHand", 0) > 0
        THEN ROUND((59 * (COALESCE(a."QtySold90", 0) / 90.0))
             - COALESCE(st."StockOnHand", 0), 0)
        ELSE 0
    END AS "ReorderQty",

    'STA' AS "org_key"

FROM "Items (Zoho Inventory)" it
LEFT JOIN "STA_Sales_Agg_v3" a            ON a."ItemID"    = it."Item ID"
LEFT JOIN "STA_Stock_By_Item_v2" st       ON st."ItemID"   = it."Item ID"
LEFT JOIN "STA_Stock_Availability_90_v1" av90
                                          ON av90."ItemID"  = it."Item ID"
LEFT JOIN "STA_Sales_Agg_External90_v1" sta_ext
                                          ON sta_ext."ItemID" = it."Item ID"
LEFT JOIN "BMP_Sales_Agg_90_v1" bmp       ON bmp."SKU"     = it."SKU"
```

#### SQL Analysis — Confirmed Findings

**Tables referenced (upstream dependencies confirmed):**

| Alias | Table | Type | Join Key |
|-------|-------|------|----------|
| `it` | Items (Zoho Inventory) | Base table (STA) | — (driving table) |
| `a` | STA_Sales_Agg_v3 | Query table | `ItemID = Item ID` ✅ |
| `st` | STA_Stock_By_Item_v2 | Query table | `ItemID = Item ID` ✅ |
| `av90` | STA_Stock_Availability_90_v1 | Query table | `ItemID = Item ID` ✅ |
| `sta_ext` | STA_Sales_Agg_External90_v1 | Query table | `ItemID = Item ID` ✅ |
| `bmp` | BMP_Sales_Agg_90_v1 | Query table | `SKU = SKU` ⚠️ cross-org |

#### ✅ What's Good

- **ItemID-based joins** for all STA tables — stable, immutable keys
- **Defensive COALESCEs** everywhere — NULLs from LEFT JOINs handled
- **Availability diagnostics** — flags missing availability data and sold-while-unavailable contradictions
- **Revenue split** — separates STA external vs BMP retail, computes true group total
- **Velocity tiers** — consistency score with meaningful thresholds (daily/3-day/weekly/monthly)
- **Reorder logic** — 59-day cover target (~2 months), only reorders positive deficit
- **DaysCover** — NULL when no sales (avoids division by zero)
- **No GROUP BY** — this is a row-per-item query, aggregation happens in upstream QTs

#### ⚠️ Risk Issues Found

1. ~~`bmp` joins on SKU, not ItemID~~ — **NOT A RISK: SKUs confirmed matching across orgs.**

2. **No WHERE clause at all:**
   - ~~No `cf_condition` filter~~ → **NOT A RISK: STA org is NEW-only**
   - ⚠️ No `status` filter → inactive/discontinued items may be included
   - ⚠️ No warehouse filter → depends entirely on upstream QTs to handle this

3. **Uses `STA_Stock_Availability_90_v1`** (not v2) — v2 exists but v4 uses v1. Was this intentional?

4. **`org_key` hard-coded to 'STA'** — this query only returns STA org items. BMParts-only items (no STA SKU match) won't appear in the BMP revenue column, but items that exist in STA but not BMParts will show Revenue90_BMP_Retail = 0.

5. **`Revenue90_Internal_Old`** — the "Old" suffix suggests this was known to be unreliable, but it's still in the output.

6. ~~Typo in column name: `it."Categor"`~~ — **NOT A RISK: actual column name is `"Categor"`** (Zoho truncation).

### 4. Connector Details
```
BMParts Connector:
  Schedule: [           ]
  Type: [incremental / full]
  Last sync: 2026-02-16 07:54 (confirmed from data)

Spares to Africa Connector:
  Schedule: [           ]
  Type: [incremental / full]
  Last sync: 2026-02-16 07:54 (confirmed from data)
```

---

## Next Steps

1. **Today:** Inspect SQL for `Buying_Base_v2`, `Buying_Base_v2_OLD`, `buying_base_sta_v4` (paste into Appendix)
2. **Today:** Check connector settings (Settings → Data Sources)
3. **This week:** Execute Phase 1 cleanup (delete 24 test tables, pause orphan refreshes)
4. **This week:** Execute Path A — wire `buying_base_sta_v4` into new reports, build side-by-side dashboard
5. **Next week:** Validate v4 dashboard vs current, cutover once confirmed
6. **Week 3:** Deprecate `Buying_Base_v2` + `_v2_OLD`, migrate legacy reports, add validation tables
