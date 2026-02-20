# Copilot Playwright Prompt: Zoho Analytics Cleanup

Paste this into VS Code Copilot chat. It uses Playwright MCP to automate the Zoho Analytics UI.

---

## PROMPT (copy everything below this line)

```
Use Playwright to automate cleanup of my Zoho Analytics workspace "Buying Dashboard Gold".

The workspace URL is: https://analytics.zoho.com
I'm already logged in via the Playwright profile at ~/.playwright-profile.

Execute these tasks IN ORDER. Wait for each page to fully load before clicking. Use browser_snapshot between actions to verify state.

---

### TASK 1: Delete 24 Test/Temp Query Tables

Navigate to the workspace. For EACH of these query tables, find it in the left sidebar, right-click → Delete → Confirm:

1. _buying_sta_sample
2. _buying_sta_v2_sample_test
3. _direct_xenon_test2
4. _join_test_v3
5. _spares_compare_test
6. _spares_items_sample
7. _spares_items_xenon
8. _spares_stock_sample
9. _spares_stock_xenon_vanos
10. _spares_xenon_bulb
11. _sta_items_xenon_test
12. _temp_avail_check_v1
13. _temp_xenon_stock
14. _verify_stock_v2_sum
15. _verify_stock_v2_xenon
16. _verify_xenon_sum
17. _verify_xenon_v2_final
18. _verify_xenon_v3
19. _verify_xenon_v3b
20. QT_Test_DateFilter2
21. QT_Test_FromTable
22. QT_Test_Join
23. QT_Test_Minimal
24. test query

After each deletion, take a snapshot to confirm it's gone before moving to the next.

---

### TASK 2: Delete 4 Audit/Debug Tables

Same process — right-click → Delete → Confirm:

1. AvBuilderAudit
2. B audit
3. MIssmatchFinderA
4. Missing Row

---

### TASK 3: Delete 7 Top SKU Orphan Query Tables

1. Top 10 Items by Category - 6 Months
2. Top 10 NEW Items by Category - 6 Months
3. Top 10 SKUs - Filterable by Period
4. Top 10 SKUs by Category - NEW - 6 Months
5. Top 10 SKUs by Category with Stock - NEW
6. Top 10 SKUs with Stock Model Engine - NEW
7. Top SKUs by Category - Dynamic Filter

---

### TASK 4: Delete 5 Old Sales/Stock Orphans

1. Sales_Agg_NEW
2. Sales_Fact_NEW_180d
3. Stock_By_Item
4. Stock_By_Item_v2
5. Buying_Base

---

### TASK 5: Delete 3 Old buying_base_sta Versions (v4 is the keeper)

1. buying_base_sta
2. buying_base_sta_v2
3. buying_base_sta_v3

---

### TASK 6: Delete Old Version Chain Predecessors

1. STA_Sales_Fact_180d
2. STA_Sales_Fact_180d_v2
3. STA_Sales_Agg
4. STA_Sales_Agg_v2
5. STA_Stock_By_Item
6. STA_Stock_Daily_v1

⚠️ DO NOT delete STA_Stock_Availability_90_v1 yet — v4 still references it.

---

### TASK 7: Delete 8 Legacy Reports (on Buying_Base_v2_OLD)

1. Buying List
2. Buying List v3
3. Buying List v3 new
4. Count of SKUs to Reorder
5. Min DaysCover
6. Top Reorders
7. Top Reorders v3
8. Total Reorder Qty

---

### TASK 8: Delete Unused STA Query Tables

1. STA_Items
2. STA_Invoices
3. STA_Invoice_Items
4. STA_Invoice_Lines_v1
5. STA_Warehouses
6. STA_Item_Stock_By_Warehouse
7. STA_AsOf_TxnDate_v1
8. STA_Latest_Txn_By_Day_v1
9. STA_Sales_Agg_90_v1

---

### DO NOT DELETE — These must stay:

- buying_base_sta_v4 (production query)
- STA_Sales_Agg_v3 (used by v4)
- STA_Stock_By_Item_v2 (used by v4)
- STA_Stock_Availability_90_v1 (used by v4 — will switch to v2 later)
- STA_Stock_Availability_90_v2 (future target)
- STA_Sales_Agg_External90_v1 (used by v4)
- BMP_Sales_Agg_90_v1 (used by v4)
- STA_Sales_Fact_180d_v3 (upstream of STA_Sales_Agg_v3)
- STA_Stock_Daily_v2 (upstream of avail v2)
- Cash Flow Query (powers Cash Flow Statement)
- Buying_Base_v2 (still has 5 active reports — delete later)
- Buying_Base_v2_OLD (0 dependents after Task 7 — can delete after confirming)
- ALL base tables (imported data — never delete)
- ALL 103 auto-generated reports on base tables

After all deletions, take a final snapshot and tell me how many objects remain.
```
