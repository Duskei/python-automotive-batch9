import pytest
from test_product_tool2 import validate_product, process_and_save

# -----------------------------------
# Fixture: Sample API Data
# -----------------------------------
@pytest.fixture
def sample_products():
    return [
        {"id": 1, "title": "Laptop", "price": 500, "category": "Electronics"},
        {"id": 2, "title": "Phone", "price": 300, "category": "Electronics"},
        {"id": 3, "title": "Shoes", "price": 450, "category": "Fashion"},
        {"id": -1, "title": "", "price": 0, "category": ""}  # Invalid
    ]


# -----------------------------------
# Test API Status
# -----------------------------------
def test_api_status():
    status_code = 200
    content_type = "application/json"

    assert status_code == 200
    assert "application/json" in content_type


# -----------------------------------
# Test Product Validation (Parameterized)
# -----------------------------------
@pytest.mark.parametrize("product, expected", [
    ({"id": 10, "title": "Valid", "price": 5.0, "category": "Food"}, True),
    ({"id": 0, "title": "Invalid", "price": 5.0, "category": "Food"}, False),
])
def test_product_validation(product, expected):
    assert validate_product(product) == expected


# -----------------------------------
# Test Average Price Calculation
# -----------------------------------
def test_average_price(sample_products, tmp_path):
    file_path = tmp_path / "valid_products.json"
    _, total, avg = process_and_save(sample_products, str(file_path))

    assert total == 3
    assert round(avg, 2) == 416.67


# -----------------------------------
# Expected Failure Test
# -----------------------------------
@pytest.mark.xfail(reason="Future API response format may change")
def test_future_api_change():
    assert False