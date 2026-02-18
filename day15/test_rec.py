import pytest
from RecEngine import RecEngine

@pytest.fixture
def engine():
    """Fixture to initialize the engine with sample data."""
    re = RecEngine()
    sample_data = [
        {"id": 1, "title": "Smartphone", "price": 699, "category": "Electronics"},
        {"id": 2, "title": "Laptop", "price": 1200, "category": "Electronics"},
        {"id": 3, "title": "Blender", "price": 50, "category": "Home App"},
        {"id": 4, "title": "Invalid", "price": -10, "category": "Error"}, # Invalid
    ]
    re.load_products(sample_data)
    return re

def test_data_validation(engine):
    """Verifies that only 3 valid products are loaded."""
    assert len(engine.products) == 3

@pytest.mark.parametrize("user_id, viewed_id, expected_recommendation_id", [
    (101, 1, 2),  # Viewed Smartphone (Electronics), should recommend Laptop (Electronics)
    (102, 3, None) # Viewed Blender, no other 'Home App' products exist
])
def test_recommendation_logic(engine, user_id, viewed_id, expected_recommendation_id):
    """Verifies content-based filtering accuracy."""
    engine.track_user_activity(user_id, viewed_id)
    recs = engine.get_content_recommendations(user_id)
    
    if expected_recommendation_id:
        assert any(p['id'] == expected_recommendation_id for p in recs)
    else:
        assert len(recs) == 0

@pytest.mark.xfail(reason="Engine currently doesn't handle non-list inputs gracefully")
def test_invalid_input_type(engine):
    """Example of an expected failure (xfail)."""
    engine.load_products(None)

@pytest.mark.skip(reason="Scaling tests require distributed environment")
def test_millions_of_users():
    """Skipped test for future scaling implementation."""
    pass