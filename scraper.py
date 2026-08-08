import requests

def check_target_stock(tcin_id, store_zip):
    # This URL pings Target's internal system directly for inventory
    url = f"https://redsky.target.com/redsky_aggregations/v1/web/product_summary_with_fulfillment_v1?tcins={tcin_id}&zip={store_zip}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        # We drill down into the data to find the exact store status
        status = data['data']['product_summaries'][0]['item']['fulfillment']['store_status']
        
        # EXACT string matching for "IN_STOCK"
        if status == "IN_STOCK":
            return True
        else:
            return False
            
    except Exception as e:
        print("Error checking Target:", e)
        return False