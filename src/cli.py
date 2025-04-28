import argparse
import json
from src.ingredient_mapper import IngredientMapper
from src.quantity_converter import QuantityConverter
from src.nutrition_calculator import NutritionCalculator
from src.dish_classifier import DishClassifier

class NutritionEstimatorCLI:
    def __init__(self, data_file_path):
        self.mapper = IngredientMapper(data_file_path)
        self.converter = QuantityConverter(data_file_path)
        self.calculator = NutritionCalculator()
        self.classifier = DishClassifier(data_file_path)

    def estimate_nutrition(self, dish_name, ingredients_list):
        processed_ingredients = []

        for ingredient in ingredients_list:
            matched = self.mapper.find_best_match(ingredient['ingredient'])
            nutrition_info = self.mapper.get_nutrition_info(matched) if matched else None
            quantity_in_grams = self.converter.standardize_quantity(ingredient['quantity'])
            if nutrition_info and quantity_in_grams:
                processed_ingredients.append({
                    'nutrition': nutrition_info,
                    'quantity_in_grams': quantity_in_grams
                })

        total_nutrition = self.calculator.calculate_total_nutrition(processed_ingredients)
        category = self.classifier.classify_dish(dish_name)
        serving_weight = self.classifier.get_standard_serving_weight(category)

        factor = serving_weight / sum(item['quantity_in_grams'] for item in processed_ingredients) if processed_ingredients else 1
        estimated_per_serving = {k: round(v * factor, 2) for k, v in total_nutrition.items()}

        output = {
    'estimated_nutrition_per_standard_serving': {k: float(v) for k, v in estimated_per_serving.items()},
    'dish_type': category if category else "Wet Sabzi",
    'ingredients_used': ingredients_list
}


        return output

def main():
    parser = argparse.ArgumentParser(description='Estimate nutrition for a dish.')
    parser.add_argument('--dish', type=str, required=True, help='Dish name')
    parser.add_argument('--ingredients', type=str, required=True, help='Path to ingredients JSON file')
    args = parser.parse_args()

    with open(args.ingredients, 'r') as f:
        ingredients_list = json.load(f)

    estimator = NutritionEstimatorCLI('data/Assignment Inputs.xlsx')
    result = estimator.estimate_nutrition(args.dish, ingredients_list)
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
