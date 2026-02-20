import json

def find_view_id():
    try:
        with open('analytics_views.json', 'r') as f:
            data = json.load(f)
        
        # content is a string containing JSON, need to parse it
        content_str = data['result']['content'][0]['text']
        content = json.loads(content_str)
        
        views = content.get('data', {}).get('views', [])
        
        for view in views:
            if view['viewName'] == 'Invoice Items':
                print(f"Found 'Invoice Items' View ID: {view['viewId']}")
                return view['viewId']
        
        print("View 'Invoice Items' not found.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_view_id()
