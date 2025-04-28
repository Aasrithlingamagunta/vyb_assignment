import pandas as pd
from rapidfuzz import process

class IngredientMapper:
    def __init__(self, nutrition_file_path):
        self.nutrition_data = pd.read_excel(nutrition_file_path, sheet_name='Nutrition source')
        self.food_names = self.nutrition_data['food_name'].dropna().tolist()

    def find_best_match(self, ingredient_name, score_cutoff=75):
        matches = process.extract(ingredient_name, self.food_names, limit=1, score_cutoff=score_cutoff)
        if matches:
            return matches[0][0]
        return None

    def get_nutrition_info(self, matched_ingredient):
        record = self.nutrition_data[self.nutrition_data['food_name'] == matched_ingredient]
        if not record.empty:
            return {
                'calories': record.iloc[0]['energy_kcal'],
                'protein': record.iloc[0]['protein_g'],
                'carbs': record.iloc[0]['carb_g'],
                'fat': record.iloc[0]['fat_g'],
                'fiber': record.iloc[0]['fibre_g']
            }
        return None
