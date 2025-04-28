class NutritionCalculator:
    def __init__(self):
        self.nutrition_fields = ['calories', 'protein', 'carbs', 'fat', 'fiber']

    def calculate_total_nutrition(self, ingredient_nutrition_list):
        totals = {field: 0 for field in self.nutrition_fields}

        for item in ingredient_nutrition_list:
            nutrition = item['nutrition']
            quantity_in_grams = item['quantity_in_grams']
            if nutrition:
                for field in self.nutrition_fields:
                    if nutrition.get(field) is not None:
                        totals[field] += (nutrition[field] / 100) * quantity_in_grams

        return {field: round(totals[field], 2) for field in self.nutrition_fields}
