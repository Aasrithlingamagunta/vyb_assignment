import pandas as pd
from rapidfuzz import process

class DishClassifier:
    def __init__(self, category_file_path):
        self.categories = pd.read_excel(category_file_path, sheet_name='Food categories')
        self.category_names = self.categories['Food category name'].dropna().tolist()
        self.standard_weights = {}

        for _, row in self.categories.iterrows():
            food_category = row['Food category name']
            weight_raw = str(row['Weight Cat']).strip().lower()

            if 'g' in weight_raw:
                weight_value = int(weight_raw.replace('g', '').replace(')', '').strip())
            elif 'ml' in weight_raw:
                weight_value = int(weight_raw.replace('ml', '').replace(')', '').strip())
            else:
                weight_value = 150

            self.standard_weights[food_category] = weight_value

    def classify_dish(self, dish_name, score_cutoff=75):
        matches = process.extract(dish_name, self.category_names, limit=1, score_cutoff=score_cutoff)
        if matches:
            best_match = matches[0][0]
            return best_match
        return None

    def get_standard_serving_weight(self, category_name):
        return self.standard_weights.get(category_name, 150)
