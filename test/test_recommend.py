import pandas as pd
import pytest

from recommendation_engine import (
    df,
    user_item_matrix,
    recommend_products,
    recommend_similar_products,
    hybrid_recommendation
)

# -------------------------------------------------
# Test 1: Data Availability
# -------------------------------------------------
#asssertion -> true/false checkpoints
def test_data_not_empty():
    assert not df.empty

# -------------------------------------------------
# Test 2: User-Item Matrix Creation
# -------------------------------------------------

def test_user_item_matrix_exists():
    assert user_item_matrix.shape[0] > 0
    assert user_item_matrix.shape[1] > 0

# -------------------------------------------------
# Test 3: Collaborative Recommendation (Valid User)
# -------------------------------------------------

def test_recommend_products_valid_user():
    result = recommend_products(1)
    assert isinstance(result, pd.Series) #checks if the expected output is of type pd.Series
    assert len(result) <= 3

# -------------------------------------------------
# Test 4: Collaborative Recommendation (Invalid User)
# -------------------------------------------------
#Ask for a user that doesn't exist in the database.
def test_recommend_products_invalid_user():
    result = recommend_products(999)
    assert isinstance(result, str) # Expecting a string message for invalid user

# -------------------------------------------------
# Test 5: Content-Based Recommendation
# -------------------------------------------------

def test_content_based_recommendation():
    result = recommend_similar_products(101)
    assert isinstance(result, list) # Expecting a list of recommended products
    assert len(result) > 0

# -------------------------------------------------
# Test 6: Content-Based Recommendation (Invalid Product)
# -------------------------------------------------

def test_content_based_invalid_product():
    result = recommend_similar_products(9999) # Non-existent product_id
    assert result == [] # Expecting an empty list for invalid product

# -------------------------------------------------
# Test 7: Hybrid Recommendation (Existing User)
# hybrid -> combines both collaborative and content-based filtering
# -------------------------------------------------

def test_hybrid_existing_user():
    result = hybrid_recommendation(3) # Existing user_id
    assert isinstance(result, list) # Expecting a list of recommended products 

# -------------------------------------------------
# Test 8: Hybrid Recommendation (New User)
# -------------------------------------------------

def test_hybrid_new_user():
    result = hybrid_recommendation(999) # New user_id
    assert isinstance(result, str) # Expecting a string message for new user