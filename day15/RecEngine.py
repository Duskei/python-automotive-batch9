import json
import csv

class RecEngine:
    def __init__(self):
        self.products = []
        self.user_history = {}

    def validate_product(self, product):
        """Validates product records: ID > 0, Price > 0, strings non-empty."""
        try:
            p_id = product.get('id')
            price = product.get('price')
            title = product.get('title')
            category = product.get('category')

            if (isinstance(p_id, int) and p_id > 0 and 
                isinstance(price, (int, float)) and price > 0 and
                title and category):
                return True
        except (AttributeError, TypeError):
            return False
        return False

    def load_products(self, products_list):
        """Processes and stores only valid product records."""
        self.products = [p for p in products_list if self.validate_product(p)]
        return len(self.products)

    def track_user_activity(self, user_id, product_id):
        """Collects user activity data."""
        if user_id not in self.user_history:
            self.user_history[user_id] = []
        self.user_history[user_id].append(product_id)

    def get_content_recommendations(self, user_id):
        """
        Simple content-based filtering algorithm:
        Recommends products in the same categories the user has previously viewed.
        """
        if user_id not in self.user_history or not self.products:
            return []

        # Find categories user has interacted with
        interacted_ids = set(self.user_history[user_id])
        user_categories = {p['category'] for p in self.products if p['id'] in interacted_ids}

        # Recommend products in those categories that the user hasn't seen yet
        recommendations = [
            p for p in self.products 
            if p['category'] in user_categories and p['id'] not in interacted_ids
        ]
        return recommendations

    def save_valid_data(self, filename="valid_products.json"):
        """Stores data locally in JSON format."""
        with open(filename, 'w') as f:
            json.dump(self.products, f, indent=4)