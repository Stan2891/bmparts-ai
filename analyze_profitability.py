import requests
import json
from datetime import datetime, timedelta
from collections import defaultdict
import time

# Configuration
SPARES_ORG_ID = "857295887"
BMPARTS_ORG_ID = "856744527"
BMPARTS_CONTACT_ID = "5368452000000244001" # Customer ID in Spares to Africa
ANALYTICS_WORKSPACE_ID = "2914904000000846397"
ANALYTICS_VIEW_ID = "2914904000000846511" # Invoice Items view
MCP_URL = "http://localhost:9091/mcp/v1"

def call_mcp(method, params, request_id=1):
    headers = {"Content-Type": "application/json"}
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": request_id
    }
    response = requests.post(MCP_URL, headers=headers, json=payload)
    return response.json()

def get_date_range(months=3):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=months*30)
    return start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")

def fetch_purchases(start_date, end_date):
    print(f"Fetching purchases from Spares to Africa ({start_date} to {end_date})...")
    purchased_items = defaultdict(lambda: {'qty': 0, 'total_cost': 0.0, 'names': set()})
    
    page = 1
    has_more = True
    invoice_ids = []

    # 1. Get Invoices
    while has_more:
        res = call_mcp("tools/call", {
            "name": "get_books_invoices",
            "arguments": {
                "organization_id": SPARES_ORG_ID,
                "customer_id": BMPARTS_CONTACT_ID,
                "date_start": start_date,
                "date_end": end_date,
                "status": "paid",
                "per_page": 200,
                "page": page
            }
        })
        
        try:
            content = json.loads(res['result']['content'][0]['text'])
            invoices = content.get('invoices', [])
            invoice_ids.extend([inv['invoice_id'] for inv in invoices])
            
            has_more = content.get('page_context', {}).get('has_more_page', False)
            print(f"  Page {page}: Found {len(invoices)} invoices.")
            page += 1
            if not invoices: has_more = False
        except Exception as e:
            print(f"  Error fetching invoices: {e}")
            has_more = False

    print(f"  Total Invoices to process: {len(invoice_ids)}")

    # 2. Get Line Items for each invoice
    for i, inv_id in enumerate(invoice_ids):
        if i % 10 == 0: print(f"  Processing invoice {i+1}/{len(invoice_ids)}...")
        
        res = call_mcp("tools/call", {
            "name": "get_invoice_details",
            "arguments": {
                "organization_id": SPARES_ORG_ID,
                "invoice_id": inv_id
            }
        })
        
        try:
            content = json.loads(res['result']['content'][0]['text'])
            line_items = content.get('invoice', {}).get('line_items', [])
            
            for item in line_items:
                # Use Name as key since SKU might differ or be missing, but ideally SKU
                # Spares to Africa might not use SKUs consistently? Let's check item keys
                key = item.get('name') 
                if not key: continue
                
                qty = item.get('quantity', 0)
                rate = item.get('rate', 0)
                total = item.get('item_total', 0) # or rate * qty
                
                purchased_items[key]['qty'] += qty
                purchased_items[key]['total_cost'] += total
                purchased_items[key]['names'].add(item.get('name'))
                
        except Exception as e:
            print(f"  Error fetching invoice details for {inv_id}: {e}")
        
        # Rate limit kindness
        # time.sleep(0.1) 

    return purchased_items

def fetch_sales(start_date):
    print(f"Fetching sales from BMParts Analytics (since {start_date})...")
    
    # Analytics Criteria: "Created Time" >= 'YYYY-MM-DD 00:00:00'
    # Note: Column name in sample was "Created Time"
    criteria = f"\"Created Time\" >= '{start_date} 00:00:00'"
    
    all_rows = []
    limit = 2000 # Max for Analytics usually 100 or higher? Tool default 100.
    # We'll rely on the tool's limit logic or pagination if implemented. 
    # The tool 'get_view_data' supports 'limit'. Let's try a large limit.
    
    # Since tool doesn't support offset/pagination explicitly in the schema shown earlier (it just has limit),
    # we might be limited to the top N rows. Let's hope 5000 is enough or implement loop if tool supported it.
    # The tool wrapper actually only exposes 'limit'. 
    # Wait, the tool definition says "limit: Max rows (1-1000)". 
    # I might need to fetch multiple times if I could, but without offset, I can't paginate Analytics via this tool easily.
    # However, I can try to use 'limit': 2000 and see if it works or truncates.
    
    res = call_mcp("tools/call", {
        "name": "analytics/get_view_data",
        "arguments": {
            "workspace_id": ANALYTICS_WORKSPACE_ID,
            "view_id": ANALYTICS_VIEW_ID,
            "org_id": BMPARTS_ORG_ID,
            "criteria": criteria,
            "limit": 5000
        }
    })
    
    sales_items = defaultdict(lambda: {'qty': 0, 'revenue': 0.0})
    
    try:
        content = json.loads(res['result']['content'][0]['text'])
        # CSV or JSON? The sample looked like CSV text inside JSON...
        # Wait, the sample file output was: "Item ID,Invoice ID,..."
        # So 'get_view_data' returns CSV format in the 'text' field if it's raw data?
        # Let's check the tool implementation in mcp-sse-server-fixed.js
        # It calls `resp.data`. Zoho Analytics API usually returns JSON if requested or CSV.
        # The sample I read earlier started with `"Item ID,Invoice ID...`.
        # It seems the tool returns CSV string.
        
        # We need to parse CSV.
        import csv
        import io
        
        csv_data = content
        if isinstance(content, dict):
             # Maybe it returned JSON object?
             # If `resp.data` was an object, `JSON.stringify` would make it a json string.
             # If `resp.data` was a string (CSV), it would be a string.
             pass
             
        # If content is a string and looks like CSV
        if isinstance(content, str):
            f = io.StringIO(content)
            reader = csv.DictReader(f)
            for row in reader:
                # Columns: "Item Name", "Quantity", "Sub Total (BCY)" or "Total (BCY)"
                name = row.get('Item Name')
                if not name: continue
                
                try:
                    qty = float(row.get('Quantity', 0))
                    # Total (BCY) might be formatted "1,750.00"
                    total_str = row.get('Total (BCY)', '0').replace(',', '')
                    revenue = float(total_str)
                    
                    sales_items[name]['qty'] += qty
                    sales_items[name]['revenue'] += revenue
                except ValueError:
                    continue
        else:
            print("Unexpected format from Analytics tool.")
            print(str(content)[:500])
            
    except Exception as e:
        print(f"Error fetching/parsing sales data: {e}")

    return sales_items

def analyze(purchases, sales):
    print("\nAnalyzing Data...")
    
    # We only care about items that were purchased from Spares to Africa in this period
    # and then look at how they performed in sales.
    
    report_data = []
    
    for name, p_data in purchases.items():
        p_qty = p_data['qty']
        p_cost = p_data['total_cost']
        avg_cost = p_cost / p_qty if p_qty > 0 else 0
        
        # Find corresponding sales
        # Exact name match
        s_data = sales.get(name, {'qty': 0, 'revenue': 0.0})
        s_qty = s_data['qty']
        s_rev = s_data['revenue']
        avg_price = s_rev / s_qty if s_qty > 0 else 0
        
        # Profitability on SOLD items
        # We assume the sold items came from this stock (simplified assumption)
        # Profit = (Avg Selling Price - Avg Cost Price) * Quantity Sold
        
        unit_margin = avg_price - avg_cost
        total_profit = unit_margin * s_qty
        
        # ROI %
        roi = (unit_margin / avg_cost * 100) if avg_cost > 0 else 0
        
        if s_qty > 0: # Only report if sold
            report_data.append({
                'name': name,
                'purchased_qty': p_qty,
                'avg_cost': avg_cost,
                'sold_qty': s_qty,
                'avg_price': avg_price,
                'total_revenue': s_rev,
                'total_profit': total_profit,
                'roi': roi
            })
            
    # Sort by Total Profit
    report_data.sort(key=lambda x: x['total_profit'], reverse=True)
    
    print("\n=== PROFITABILITY REPORT (Last 3 Months) ===")
    print(f"{'Product Name':<40} | {'Sold':<5} | {'Cost/Unit':<10} | {'Price/Unit':<10} | {'Profit':<10} | {'ROI %':<8}")
    print("-" * 100)
    
    total_period_profit = 0
    
    for item in report_data:
        total_period_profit += item['total_profit']
        print(f"{item['name'][:38]:<40} | {int(item['sold_qty']):<5} | R{item['avg_cost']:<9.2f} | R{item['avg_price']:<9.2f} | R{item['total_profit']:<9.2f} | {item['roi']:<7.1f}%")
        
    print("-" * 100)
    print(f"Total Profit from Spares to Africa items: R{total_period_profit:,.2f}")
    
    # Top Sellers by Quantity
    print("\n=== TOP SELLERS (By Quantity) ===")
    report_data.sort(key=lambda x: x['sold_qty'], reverse=True)
    for item in report_data[:10]:
        print(f"{item['name'][:40]:<40} : {int(item['sold_qty'])} sold (Profit: R{item['total_profit']:.2f})")

if __name__ == "__main__":
    start_str, end_str = get_date_range(3)
    purchases = fetch_purchases(start_str, end_str)
    
    if not purchases:
        print("No purchases found from Spares to Africa in the last 3 months.")
    else:
        print(f"Found {len(purchases)} unique items purchased.")
        sales = fetch_sales(start_str)
        analyze(purchases, sales)
