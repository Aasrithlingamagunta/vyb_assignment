from src.cli import NutritionEstimatorCLI

if __name__ == '__main__':
    estimator = NutritionEstimatorCLI('data/Assignment Inputs.xlsx')
    print("Welcome to the Nutrition Estimator!")
    print("Enter a dish name:")

    dish_name = input("> ").strip()
    print("Now enter ingredients one by one. Type 'done' when finished.")

    ingredients = []
    while True:
        ingredient_name = input("Ingredient name: ").strip()
        if ingredient_name.lower() == 'done':
            break
        quantity = input("Quantity (e.g., '0.5 cup'): ").strip()
        ingredients.append({
            'ingredient': ingredient_name,
            'quantity': quantity
        })

    result = estimator.estimate_nutrition(dish_name, ingredients)
    print("\nEstimated Nutrition Output:\n")
    for key, value in result.items():
        print(f"{key}: {value}")
