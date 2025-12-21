# 🧠 BMParts Memory Context
> Auto-synced: 2025-12-21 20:44 | Total: 144 memories

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
- BMParts ecommerce - Platform: WooCommerce - Domain: www.bmparts.co.za - Pricing driver: Zoho Inventory - Stock source: Zoho Inventory primary
- Company structure - Owner: Stan Andreev (Owner, Director, System Architect, Automation Engineer) - Timezone: Africa/Johannesburg UTC+2 - Two entities: Spares to Africa Org 857295887 feeds into BMParts Org 856737871 - Sync direction: Spares to Africa to BMParts to WooCommerce
- Best seller inventory filters - Condition: NEW - Status: Active - Sale price required: true - In stock only: true - Qty sold greater than zero: true
- Competitors and wholesale customers - Competitors: bimmerspares.co.za - Wholesale customers: DNH, MD House Motors
- Webhook endpoints - GET /webhook/inventory with filters: sku, condition, limit, in_stock_only - POST /webhook/best-sellers with filters: period, limit, condition, in_stock_only, has_sale_price - POST /webhook/update-item with fields: cf_sale_price, rate, name - GET /health for status check

---

## Infrastructure & Services
- Stan owns BMParts, an automotive parts import, retail, wholesale, and ecommerce business.
- Stan imports via sea freight with a 14-day consolidation cycle handled by Selena.
- Stan uses WooCommerce, Zoho Flow, UDM Pro, Ubuntu servers, and supplier APIs.
- Stan wants full context retention, proactive reasoning, and memory continuity.
- Spares to Africa is involved in imports and supply chain operations for BMParts.
- Stan wants tasks and long-term projects tracked persistently via memory.
- Stan uses a local GPT Memory Server located in /opt/gpt-memory.
- Memory server backups: copy /opt/gpt-memory to /opt/gpt-memory-backup + backup systemd service and environment file.
- Stan wants to maintain automation reliability across Zoho, WooCommerce, API integrations, and stock rules.
- Global memory includes workflow patterns, API behaviour memories, server state, pricing strategy, and warehouse behaviour.
- Supplier APIs provide availability and pricing.
- API failures trigger fallback safety modes.
- Import documentation always lists China Top Trading.
- Spares to Africa (Pty) Ltd - Registration: 2018/023532/07 - Director: Stanislav Andreev - Zoho Org ID: 857295887 - Plan: Finance Plus - Apps: Books, Inventory, CRM, Flow - Role: Importer, supplier, upstream stock holder feeding BMParts
- Infrastructure - Memory server path: /opt/gpt-memory - Backup path: /opt/gpt-memory-backup - Service file: /etc/systemd/system/gpt-memory.service - Env file: /etc/default/gpt-memory - Backup method: timestamped full directory copy

---

## People & Contacts
- User name is Stan.
- Stan owns BMParts, an automotive parts import, retail, wholesale, and ecommerce business.
- Stan focuses on automation, speed, accuracy, and eliminating manual steps.
- Stan prefers concise, technical, high-impact answers with engineering logic.
- Stan uses Zoho Inventory Org ID 856737871.
- Stan runs BMParts’ website on https://www.bmparts.co.za.
- Stan imports via sea freight with a 14-day consolidation cycle handled by Selena.
- Selena works for China Top Trading Limited and acts as a trusted buying and shipping agent.
- Selena charges a 3% service fee on total goods purchased.
- Stan transfers funds to Selena via FNB Forex or cash when in China.

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

---

## Recent Sessions
- Test memory from Copilot session
- MALWARE EVIDENCE - libCert file found in Nedbank Money banking app folder on iPhone. SQLite database with SHA-256 obfuscated table and column names (deliberate anti-forensics). File: 90112 bytes, dated Nov 26 2025. SHA256: 1d2dcc69b89dcf6324d0f2b19563184ac315198a767844d1ec5375123f6125fd. MD5: 214c114401f294aa89363618fa4dcabd. Contains encrypted BLOBs - credential/session storage for exfiltration. VirusTotal: 0/63 detections. File preserved at /tmp/libcert_analysis/libCert and /home/stan/Downloads/thunderbird.tmp/dnd_file/libCert.zip
- DELETED MALWARE FILES from iCloud - 1) dss211e: unknown executable, 2) Fake Unifi backup file: disguised malware, 3) rootCA.pem: Root CA certificate for MITM attacks allowing decryption of all HTTPS traffic including banking. Also deleted Mat Network WiFi profile from iPhone - installed by China hotel WiFi containing root CA. Apple ID password changed to kill all sessions.
- TENCENT INVESTIGATION DEC 2025 - iPhone 12 Pro (MAC fa:ec:43:d0:ff:eb, IP 192.168.10.218) identified as source of suspicious Tencent Cloud connections. Connected to ins-3tmwbr4q.ias.tencent-cloud.net (43.154.254.56, 43.159.234.88) - specific VM instance in Hong Kong. Connections: Dec 18 16:12 to VM, Dec 19 00:06 to two more Tencent HK IPs. Phone removed from iCloud. Geo-blocking active CN/HK/SG/MY/KP/KR. Sep 2025 device 3e:55:41:5c:f7:3c queried res.wx.qq.com (WeChat). UDM Pro support bundle analyzed.
- Security Investigation 2025 - THREE suspicious iPhones with China/Tencent traffic. Device 1: iPhone 12 Pro (fa:ec:43:d0:ff:eb, 192.168.10.218) REMOVED from iCloud, connected to ins-3tmwbr4q Tencent VM. Device 2: UNKNOWN iPhone (52:3a:29:3e:c5:cd, 192.168.10.55) ACTIVE Oct-Dec 2025, 42 Tencent connections to HK/SG. Device 3: UNKNOWN iPhone (3e:55:41:5c:f7:3c, 192.168.7.240) active Sept 2-20 only, WeChat DNS queries. Suspicious VM: ins-3tmwbr4q.ias.tencent-cloud.net (43.154.254.56, AS132203 HK). WeChat Pay detected. Geo-blocking enabled but traffic bypassed via TLS/QUIC. ACTION: Identify who owns 192.168.10.55 and who was on network Sept 2-20.
