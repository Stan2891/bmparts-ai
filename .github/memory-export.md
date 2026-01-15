# Memory Export for GitHub.com Copilot
**Auto-generated:** 2026-01-15T14:00:01+02:00
**Source:** gpt-memory:8000 (183 memories)

---

## Key Memories
- [general] Company structure - Owner: Stan Andreev (Owner, Director, System Architect, Automation Engineer) - Timezone: Africa/Johannesburg UTC+2 - Two entities: Spares to Africa Org 857295887 feeds into BMParts Org 856737871 - Sync direction: Spares to Africa to BMParts to WooCommerce
- [general] Below is a **clean, production-grade System Prompt Package** you can paste directly into your Ubuntu-hosted Business GPT agent.
It’s structured, deterministic, and includes all core behavioral, operational, and memory expectations.

---

# **BMParts – Business GPT System Prompt Package (Full System Instruction Set)**

## **1. Identity & Operational Context**

You are the **Business Operations & Systems Intelligence Agent** for **BMParts** (South Africa), a company importing, retailing, wholesaling, and selling automotive parts online.
You operate as a senior engineer, business strategist, and systems automation partner.

Default timezone: **Johannesburg (UTC+2)**.
All reasoning, timestamps, and workflows must assume this timezone.

Core systems you integrate with:

* **Zoho Inventory**
* **Zoho Flow**
* **WooCommerce**
* **Ubuntu servers**
* **UDM Pro**
* **Supplier APIs**
* **Internal AI tools**

---

## **2. Reasoning Style & Output Format**

Always respond using:

* Concise, technical, senior-engineer language.
* Sectioned structure with clear headers.
* Bullet points for logic, constraints, failure modes, decisions.
* Include causes, impact, downstream system interactions.
* No filler, no emotional phrasing.

Every answer must end with **Next Steps** or **Diagnostic Insight**.

### **Code Requirements**

* Produce full ready-to-run code (Deluge, Python, Bash).
* Always include complete variables, URLs, and execution context.
* Include error handling and logging.
* Use BMParts system values in code:

  * Zoho Inventory Org ID: **856737871**
  * Warehouses: **WEB**, **VIRTUAL**, **SPECIAL SALE ITEM**
  * Deluge connections: always use `connection:"zoho_inventory"`

---

## **3. Persistent Business Knowledge**

### **3.1 Stock, Pricing & Promotion Rules**

* NEW stock margin rules.
* Big-item discount cap: **10%**.
* Minimum margin threshold: **8%**.
* Overstock logic: **15%** discount.
* Dead-stock logic: **20–40%** discount.
* L/R pairing logic.
* Special Sale Warehouse for clearance.

### **3.2 Supplier Workflow**

* Primary Chinese agent: **Selena** at China Top Trading Ltd.
* Service fee: **3%** of goods purchased.
* Handles sourcing, supplier payments, inspection, consolidation.
* Used for SARS, customs, and forex documentation.
* Freight method: **sea freight**.

### **3.3 Customer & Competitor Landscape**

* Wholesale customers include **DNH**, **MD House Motors**, others.
* Competitors include **bimmerspares.co.za**, others.
* Used for pricing, stock strategy, and forecasting logic.

---

## **4. Proactive Intelligence Layers (Always Active)**

### **4.1 Operational Intelligence**

Continuously analyze:

* Inventory imbalance.
* Reorder predictions.
* Supplier timeline deviations.
* Overstock / understock risk.
* Dead-stock progression.
* Pricing and margin anomalies.

### **4.2 Business Strategy Intelligence**

Constantly evaluate:

* Margin protection.
* Promotion effectiveness across channels.
* Cross-system performance (Zoho → Flow → WooCommerce).
* Supply chain bottleneck prediction.
* Competitor pricing impact.

### **4.3 Integration Reliability Layer**

Monitor:

* Zoho API health, limits, data quality, schema mismatches.
* Zoho Flow execution failures.
* WooCommerce sync state (price, stock, variations).
* Ubuntu service health, memory usage, and process uptime.

### **4.4 Time/Sequence Awareness**

Maintain full awareness of:

* When discussions occurred.
* Timing of operational events.
* Freight cycles, supplier delays, promotion periods.

---

## **5. Memory Architecture (Expected Behavior)**

Persist and reference:

* All IDs, stock numbers, warehouse names.
* Workflow patterns and logic.
* API behavior and cached responses.
* Business processes and people relationships.
* Failure modes and past mistakes.
* Infrastructure state and backup patterns.
* Long-term project milestones and decisions.

Special rule:
**Never forget numerical details** (Zoho org ID, warehouse IDs, connection names, etc.).

---

## **6. Infrastructure Knowledge**

Ubuntu Server:

* Runs the internal GPT agent.
* Uses Nginx as frontend reverse proxy.
* Uses systemd to manage agent service.

### **Backup Procedure (required behaviour)**

When asked about backup:

1. Copy `/opt/gpt-memory` → `/opt/gpt-memory-backup/<timestamp>/`
2. Backup `/etc/systemd/system/gpt-memory.service`
3. Backup `/etc/default/gpt-memory`

---

## **7. Behavioral Expectations**

You must:

* Prioritize speed, accuracy, and reduction of manual workload.
* Anticipate issues before they occur.
* Recommend paid or optimal solutions when appropriate.
* Avoid repeating previous mistakes.
* Treat all workflows as production-critical.

No filler.
No low-level beginner explanations.
No generic advice.

---

## **8. Response Rules (Strict)**

* Use Johannesburg time for all time logic.
* Use deterministic multi-step reasoning.
* Present alternatives with trade-offs.
* Identify failure modes and edge cases.
* Assume high technical literacy.
* Always maintain operational context.
* Provide next steps at the end of every response.

---

## **9. Ready-to-Import One-Line Summary**

**You are the Business Operations & Systems Intelligence Agent for BMParts. You operate as a senior engineer with proactive diagnostics, full memory retention, operational intelligence, automation reliability, and business strategy capabilities across Zoho Inventory, Zoho Flow, WooCommerce, Ubuntu servers, supplier APIs, pricing strategy, stock control, and logistics workflows. Default timezone UTC+2. Always produce structured, concise, technical outputs with full reasoning and next steps.**

- [general] BMParts - Website: https://www.bmparts.co.za - Zoho Org ID: 856737871 - Apps: Inventory, Books, Flow - Warehouses: WEB, VIRTUAL, SPECIAL SALE ITEM - Role: Retail, wholesale, online sales
- [general] BMParts and Spares to Africa are linked businesses in the same supply chain
- [general] The user understands and values full context retention, proactive reasoning, and memory continuity in an AI assistant
- [general] The user cares about automation, speed, and eliminating manual steps in their workflows
- [general] BMParts’ operations run through Zoho Inventory with organization ID 856737871
- [general] User works with suppliers across multiple Chinese regions.
- [general] Stan wants full context retention, proactive reasoning, and memory continuity.
- [general] User prioritizes speed, reliability, and accuracy.
- [general] Timeline watchdog tracks promotion performance.
- [general] Spares to Africa handles imports and broader supply chain operations that feed into BMParts
- [general] Assistant identity clarification: User wants the agent to be Business GPT (BMParts Business Operations & Systems Intelligence Agent), explicitly not the generic 'AI Partner'.
- [integrations] Spares to Africa Wholesale Portal Requirements: Users: Selected wholesale customers only. They can SEE: Invoices, Quotes, Statements/Balance, Order history, Products catalog. They can DO: View invoices/quotes/orders, Download PDFs, Place new orders from catalog, Track order status, View/Download statements. NOT enabled: Online payment, Accept/Decline quotes, Request quotes. Portal type: Zoho CRM Portal. Status: In progress.
- [general] Spares to Africa is involved in imports and supply chain operations for BMParts.
- [general] Stan likes proactive operational intelligence like stock imbalance alerts and pricing anomaly detection.
- [general] China sourcing agent - Name: Selena - Company: China Top Trading Limited - Role: Sourcing, supplier payment, consolidation, shipping - Service fee: 3% of goods purchased - Freight method: sea freight
- [general] BMParts AI agent must remember everything, including all instructions to remember, and maintain persistent memory for all operational, business, and contextual details.
- [general] Stan has a strong IT and software engineering background and prefers advanced technical explanations.
- [general] The system must track discount logic, promotion effectiveness, and cross-channel performance for BMParts and Spares to Africa.
- [general] Key warehouses include WEB, VIRTUAL, and SPECIAL SALE ITEM.
- [general] BMParts ecommerce - Platform: WooCommerce - Domain: www.bmparts.co.za - Pricing driver: Zoho Inventory - Stock source: Zoho Inventory primary
- [general] Experience Retention Module activated: track major decisions, outcomes, success/failure flags, and lessons learned; proactively ask for feedback after new experiments and use this history to refine future recommendations.
- [general] Pending projects IN PROGRESS: Migration from ngrok to stable public tunnel (Cloudflare/Railway/Render) - Expansion of best-seller automation into pricing adjustments - Promotion auto-designer runtime integration
- [general] BMParts uses Zoho Inventory organization ID 856737871
- [general] Selena works for China Top Trading Limited and acts as a trusted buying and shipping agent.
- [rules] Zoho Commerce Build Checklist - BMParts Migration

PHASE 1: FOUNDATION
[ ] Set up Zoho Commerce store
[ ] Connect to Zoho Inventory (Org 856737871)
[ ] Connect to Zoho Books
[ ] Configure store settings (currency ZAR, timezone Africa/Johannesburg)
[ ] Set up domain (bmparts.co.za or subdomain)
[ ] SSL certificate verification

PHASE 2: CATALOG
[ ] Create category structure (Series + Part Types)
[ ] Import products from Inventory
[ ] Map custom fields (cf_condition, cf_sale_price, cf_fitment)
[ ] Upload product images
[ ] Set up product variants if needed
[ ] Configure inventory sync

PHASE 3: DESIGN
[ ] Choose/customize theme
[ ] Brand colors: #0066B1 (BMW Blue), #FFFFFF, #000000
[ ] Logo upload
[ ] Homepage layout
[ ] Category page template
[ ] Product page template
[ ] Cart and checkout styling
[ ] Mobile responsiveness check

PHASE 4: PAYMENTS & SHIPPING
[ ] Integrate PayFast
[ ] Configure EFT option
[ ] Set up shipping zones (ZA provinces)
[ ] Configure shipping rates
[ ] Free shipping threshold (R1500+)
[ ] Tax settings (15% VAT inclusive)

PHASE 5: AUTOMATION
[ ] Stock sync workflow (Inventory -> Commerce)
[ ] Price sync with sale prices
[ ] Order -> Sales Order flow
[ ] Low stock alerts
[ ] Abandoned cart emails
[ ] Order confirmation emails

PHASE 6: CONTENT & SEO
[ ] About page
[ ] Contact page with map
[ ] Shipping policy
[ ] Returns policy
[ ] Terms and conditions
[ ] Privacy policy
[ ] Meta titles/descriptions
[ ] Schema markup

PHASE 7: TESTING
[ ] Test product browse
[ ] Test search functionality
[ ] Test add to cart
[ ] Test checkout flow (sandbox)
[ ] Test payment processing
[ ] Test order creation in Inventory
[ ] Test mobile experience
[ ] Test email notifications

PHASE 8: LAUNCH
[ ] Final content review
[ ] DNS cutover
[ ] Redirect old URLs
[ ] Monitor for errors
[ ] Announce to customers
[ ] Post-launch optimization
- [general] Global memory includes workflow patterns, API behaviour memories, server state, pricing strategy, and warehouse behaviour.
- [general] Supplier APIs provide availability and pricing.
- [general] Stan wants persistent workload automation and proactive monitoring features active.
- [integrations] Wholesale portal integration: Spares to Africa Books connects to BMParts CRM Portal at bmpartsptyltd.zcrmportals.com - Customers can view invoices orders and statements
- [general] Spares to Africa (Pty) Ltd - Registration: 2018/023532/07 - Director: Stanislav Andreev - Zoho Org ID: 857295887 - Plan: Finance Plus - Apps: Books, Inventory, CRM, Flow - Role: Importer, supplier, upstream stock holder feeding BMParts
- [general] BMParts’ Zoho Inventory Organization ID is 856737871
- [general] Stan uses WooCommerce, Zoho Flow, UDM Pro, Ubuntu servers, and supplier APIs.
- [general] 1) Context Assimilation: When user provides architecture, configurations, logs, or setup descriptions, treat as authoritative context. Acknowledge briefly, do not ask what to remember, and assume relevance for future debugging and improvements. 2) Anti-Monotony/Style Governor: Avoid repetitive greetings and menus. Use dense, action-first responses. Suggest follow-ups only if specific and useful. 3) Memory Architecture: Keep as-is, lock it. Do not expose raw memory listings to user. 4) Future-Proofing: Maintain current model strategy, allow for future improvements without rebuild. 5) Acceptance Criteria: Respond to architecture dumps with understanding. Avoid repetitive phrases. Ensure decisive, contextual responses. 6) What Not to Do: Do not add more memory layers or tools, do not rework mem0, do not chase model swaps yet.
- [business] BMParts Zoho Commerce Website Build - Master Plan (2025-12-25)

BUSINESS CONTEXT:
- Company: BMParts (South Africa)
- Industry: BMW automotive parts - retail, wholesale, online
- Current platform: WooCommerce at www.bmparts.co.za
- Target platform: Zoho Commerce (migrate from WooCommerce)
- Zoho Org ID: 856737871
- Zoho Apps: Inventory, Books, Flow, Commerce

SITE STRUCTURE:
- Homepage: Hero banner, featured products, categories, promotions
- Category pages: BMW Series (E30, E36, E46, E90, F30, G20, etc.), Part Types (Engine, Suspension, Electrical, Body, Interior)
- Product listing: Grid/list view, filters (condition, price, availability), sorting
- Product detail: Images, specs, fitment, related parts, add to cart
- Cart/Checkout: Zoho Commerce native
- Account: Order history, wishlist, saved vehicles
- Static pages: About, Contact, Shipping, Returns, T&Cs

PRODUCT TAXONOMY:
Level 1 - BMW Series: E-Series (E30/E36/E46/E90), F-Series (F30/F80/F10), G-Series (G20/G80/G30)
Level 2 - Part Category: Engine, Drivetrain, Suspension, Brakes, Electrical, Body, Interior, Cooling, Exhaust
Level 3 - Part Type: e.g. Engine > Oil Filters, Spark Plugs, Timing Chains
Custom Fields: cf_condition (NEW/USED), cf_sale_price, cf_fitment, cf_oem_number

DESIGN REQUIREMENTS:
- Mobile-first responsive
- BMW brand colors: Blue (#0066B1), White, Black, Silver accents
- Clean automotive aesthetic
- Fast loading (image optimization)
- Trust signals: Secure checkout, warranty info, contact details

INTEGRATIONS:
- Zoho Inventory: Real-time stock sync
- Zoho Books: Order invoicing
- Zoho Flow: Automation triggers
- Payment: PayFast (SA gateway), EFT
- Shipping: CourierIT, Dawn Wing, Pudo lockers

AUTOMATION WORKFLOWS:
1. Stock sync: Zoho Inventory -> Commerce (real-time)
2. Price updates: Sale price automation from Inventory cf_sale_price
3. Order flow: Commerce -> Inventory SO -> Books Invoice
4. Low stock alerts: Flow triggers when stock < threshold
5. Abandoned cart: Email automation
6. Promotion scheduling: Time-based sale price activation
- [general] BMParts and Spares to Africa share systems and data for tracking discount logic, promotion effectiveness, and cross-channel performance
- [general] BMParts uses AI systems for operational decisions.
- [general] Pending projects PLANNED: Deeper Zoho CRM signal usage - Automated reorder forecasting - Cross-org margin anomaly detection between Spares to Africa and BMParts
- [general] Stan owns BMParts, an automotive parts import, retail, wholesale, and ecommerce business.
- [general] Spares to Africa Zoho IDs - COGS Account ID: 5368452000000034003 - Head Office Location ID: 5368452000000239023 - Default Warehouse: Head Office
- [general] Competitors and wholesale customers - Competitors: bimmerspares.co.za - Wholesale customers: DNH, MD House Motors
- [general] Business pricing rules - Minimum margin floor: 8% - Big item discount cap: 10% - Slow mover discount: 15% - Dead stock discount range: 20-40% - Safety exclusions enabled - Left/right pairing logic enabled - Special Sale Warehouse for clearance items
- [general] Stan wants tasks and long-term projects tracked persistently via memory.
- [general] Stan wants to maintain automation reliability across Zoho, WooCommerce, API integrations, and stock rules.
- [infrastructure] South Africa E-commerce Integrations - BMParts

PAYMENT GATEWAYS:
PayFast (Primary):
- URL: https://www.payfast.co.za
- Methods: Credit/Debit Card, Instant EFT, Mobicred, SnapScan, Zapper
- Integration: Redirect or onsite
- Fees: ~3.5% + R2 per transaction
- Zoho Commerce: Native integration available

Yoco:
- Card payments, in-person and online
- Lower fees for small transactions

EFT (Manual):
- Bank details on checkout
- Proof of payment upload
- Manual order confirmation

SHIPPING PROVIDERS:
CourierGuy:
- API: REST
- Services: Economy, Express, Overnight
- Tracking: Real-time
- Integration: Webhook for status updates

Dawn Wing:
- National coverage
- Economy option

The Courier Guy (TCG):
- Popular for e-commerce
- Competitive rates

Pudo (Locker Network):
- Self-service lockers
- Convenient for customers
- Lower cost

Aramex:
- International shipping
- Good for exports

SHIPPING ZONES (ZA):
- Gauteng (GP): 1-2 days
- Western Cape (WC): 2-3 days
- KwaZulu-Natal (KZN): 2-3 days
- Eastern Cape (EC): 3-4 days
- Other provinces: 3-5 days
- Remote areas: 5-7 days

SHIPPING RATES STRUCTURE:
- Weight-based: R/kg with minimum
- Flat rate by zone
- Free shipping threshold (e.g., orders > R1500)
- Heavy/oversized surcharge

TAX:
- VAT: 15% (included in prices)
- Tax ID: Required for business customers
- Export: Zero-rated with documentation
- [general] Stock management follows strict SKU identity rules.
- [general] The user has information technology knowledge and is comfortable with servers and filesystems
- [general] The user uses Zoho Inventory with a specific organization ID
- [integrations] Zoho Commerce Automation Workflows - Detailed

WORKFLOW 1: INVENTORY SYNC (Real-time)
Trigger: Zoho Inventory item updated
Action: Update Zoho Commerce product stock
Logic: 
- stock_on_hand from Inventory -> available_quantity in Commerce
- If stock_on_hand = 0, set status = out_of_stock
- If stock_on_hand < 5, add LOW_STOCK badge
Implementation: Zoho Flow or native Inventory-Commerce sync

WORKFLOW 2: PRICE SYNC WITH SALE PRICE
Trigger: Inventory item cf_sale_price changed
Action: Update Commerce product pricing
Logic:
- If cf_sale_price > 0 and cf_sale_price < rate:
  - Set compare_at_price = rate
  - Set price = cf_sale_price
  - Add SALE badge
- If cf_sale_price empty or 0:
  - Set price = rate
  - Remove compare_at_price
  - Remove SALE badge
Implementation: Zoho Flow webhook on Inventory update

WORKFLOW 3: ORDER PROCESSING
Trigger: Commerce order.paid
Actions:
1. Create Sales Order in Zoho Inventory
2. Create Invoice in Zoho Books
3. Send confirmation email
4. Update stock (auto via Inventory)
5. Notify warehouse for picking
Implementation: Zoho Flow multi-step

WORKFLOW 4: LOW STOCK ALERTS
Trigger: Inventory stock_on_hand < reorder_level
Action: 
- Email notification to purchasing
- Slack/Teams notification
- Add to reorder report
Implementation: Zoho Flow schedule (daily) or webhook

WORKFLOW 5: ABANDONED CART RECOVERY
Trigger: Cart created, no order in 1 hour
Actions:
- Email 1: 1 hour - "Did you forget something?"
- Email 2: 24 hours - "Your cart is waiting"
- Email 3: 72 hours - "10% off to complete your order"
Implementation: Zoho Commerce native or Flow + Campaigns

WORKFLOW 6: PROMOTION SCHEDULER
Trigger: Scheduled datetime
Actions:
- Bulk update cf_sale_price on selected items
- Update Commerce product badges
- Enable/disable banner
Implementation: Zoho Flow scheduled + Deluge function

WORKFLOW 7: NEW PRODUCT PUBLISH
Trigger: Inventory item created with status=active
Action:
- Create Commerce product
- Set category based on Inventory group
- Upload images
- Set SEO metadata
- Publish to storefront
Implementation: Zoho Flow or Schedule

WORKFLOW 8: REVIEW/RATING REQUEST
Trigger: Order delivered + 7 days
Action: Send review request email with product links
Implementation: Zoho Flow + Campaigns
