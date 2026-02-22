# Server Migration State
**Last updated:** 2026-02-22 19:40 SAST

## Servers
| | Old (to wipe) | New (production) |
|---|---|---|
| **IP** | 192.168.80.10 | 192.168.80.2 |
| **Hostname** | stan-S600 | ai.partner.lan |
| **Role** | Disabled, pending wipe | Active production |

## Completed Tasks
- [x] All crons DISABLED on 80.10 (backup: ~/crontab_backup_80.10.txt)
- [x] stock_compare.py copied to 80.2 with LOG_DIR="/home/stan/Desktop/logs"
- [x] Cron on 80.2 updated: logs to ~/Desktop/logs/stock_compare_cron.log
- [x] Tested stock_compare.py on 80.2 — works correctly

## Pending Tasks
- [ ] Enable gpt-app + gpt-realtime on 80.2: `sudo systemctl enable --now gpt-app.service gpt-realtime.service`
- [ ] Fix GDrive token (invalid_grant error on both servers)
- [ ] Merge/reconcile memory databases (both servers run memory-mcp with separate data)
- [ ] Stop duplicate services on 80.10 (docker, nginx, MCP servers all still running)
- [ ] Wipe 80.10 after confirming 80.2 is fully operational

## Services Comparison
| Service | 80.10 (old) | 80.2 (new) |
|---|---|---|
| docker | running | running |
| gpt-memory | running | running |
| mem0 | running | running |
| memory-mcp | running | running |
| nginx | running | running |
| ngrok-mcp | running | running |
| zoho-mcp-node | running | running |
| **gpt-app** | running | **not enabled** |
| **gpt-realtime** | running | **not enabled** |

## Docker Containers (same on both)
- compintel-postgres (port 5433)
- sqlserver-bmparts (port 1433)
- open-webui
- qdrant (port 6333)

## Crons on 80.2 (active)
```
*/5 * * * * /home/stan/.copilot-memory/auto-save.sh
*/10 * * * * /home/stan/.copilot-memory/save-full-chat.sh
0 * * * * /usr/bin/python3 /opt/aipartner/scripts/stock_compare.py >> /home/stan/Desktop/logs/stock_compare_cron.log 2>&1
0 6 * * 1 /home/stan/competitor-price-scraper/weekly_price_check.sh
0 * * * * cd /home/stan/competitor-intel && python3 scripts/price_alert.py
0 */6 * * * cd /home/stan/competitor-intel && .venv/bin/python scripts/run_monitor.py --no-cache
```

## Crons on 80.10 (all disabled)
All commented out with "# DISABLED (old server):" prefix.

## Known Issues
- Two memory-mcp instances (80.10 + 80.2) have separate/conflicting data — needs merge
- GDrive OAuth token expired on both servers
- gpt-app and gpt-realtime service files exist on 80.2 but need sudo to enable

## Other Session Work (2026-02-22)
- Zoho Commerce (www.partsza.co.za): Fixed category image sizing CSS (120px desktop, 90px mobile)
- Removed category-section-replacer.js script
- Fixed header code (unclosed style tag, missing containers for .zs-category-hover-effect)
- Zoho Deluge: Fixed invoice time extraction — split on "T" instead of hardcoded subString(11,16)
