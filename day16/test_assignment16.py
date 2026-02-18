from unittest.mock import patch, MagicMock

# --- Components to be Tested ---

def fetch_product_from_api(product_id):
    #Simulates Component 1: API Client
    import requests
    print(f"\n[STEP 1] Requesting data for Product ID: {product_id}...")
    response = requests.get(f"https://api.example.com/products/{product_id}")
    
    data = response.json()
    print(f"[STEP 1] Received: {data['title']} - ${data['price']}")
    return data

def save_to_db(product_data):
    #Simulates Component 2: Database Service
    print(f"[STEP 2] Validating data for: {product_data.get('title')}...")
    
    # Check for required interface fields
    if not product_data.get("id") or not product_data.get("price"):
        print("[STEP 2] ERROR: Interface validation failed. Missing fields.")
        raise ValueError("Invalid Data Mapping")
    
    print(f"[STEP 2] Success: Writing Product {product_data['id']} to database.")
    return True

# --- Integration Test ---

def test_api_to_db_integration():
    #Validates interactions between the API module and Database module.
    print("\n--- STARTING INTEGRATION TEST ---")
    
    # Setup Mock Data
    mock_api_response = {
        "id": 101,
        "title": "Integration Test Phone",
        "price": 599.99,
        "category": "electronics"
    }

    # Use patch to simulate the external dependency (requests)
    with patch('requests.get') as mock_get:
        # Mocking the response object
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_api_response
        mock_get.return_value = mock_response

        # Execution Phase
        try:
            # 1. Component Interaction: Fetch
            product = fetch_product_from_api(101)
            
            # 2. Component Interaction: Save
            db_status = save_to_db(product)

            # 3. Final Verification (Assertions)
            print("[STEP 3] Running final assertions...")
            assert db_status is True
            assert product['price'] == 599.99
            print("--- INTEGRATION TEST PASSED SUCCESSFULLY ---")

        except Exception as e:
            print(f"--- TEST FAILED: {e} ---")
            raise e 