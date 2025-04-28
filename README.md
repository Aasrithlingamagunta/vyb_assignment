# VYB Assignment: Nutrition Estimator for Indian Dishes
!!!DONT MISS TO CHECK FUTURE ENHANCEMENTS IN THE LAST!!!
## Objective

The objective of this project is to develop a system that estimates the nutritional values of a home-cooked Indian dish based on its ingredients. The system must handle real-world messy inputs, make intelligent assumptions, and work reliably both via a Command Line Interface (CLI) and a Local API.

---

## Methodology

I   followed a modular and step-by-step approach:

1. Ingredient Fetching: Simulated a realistic list of ingredients per dish.
2. Ingredient Mapping: Used fuzzy matching against a Nutrition Database to map ingredients accurately.
3. Quantity Standardization: Converted common household units (cup, teaspoon, tablespoon) into standardized gram measurements.
4. Nutrition Calculation: Calculated total nutrition by sum-product of quantity and per-100g nutritional values.
5. Dish Classification: Mapped dishes into categories like Wet Sabzi, Dal, etc., using fuzzy string matching.
6. Error Handling: Applied smart fallbacks to handle missing ingredients, missing categories, and inconsistent quantities.
7. Exposure: Built both a Command Line Interface and a FastAPI-powered Local API for interaction.

---

## Technologies Used

- Python 3.10
- Pandas
- RapidFuzz
- FastAPI
- Uvicorn
- Openpyxl

---

## How the Solution Was Built

- Modular code organized inside the `src/` directory.
- IngredientMapper, QuantityConverter, NutritionCalculator, and DishClassifier classes were created to isolate responsibilities.
- CLI (`main.py`) allows users to input dish name and ingredients manually.
- API (`app.py`) offers a `/estimate_nutrition` endpoint to send JSON requests and receive nutrition estimates.
- Exception handling and fallback defaults ensure the program never crashes on bad inputs.
- Swagger UI automatically generated for easy API testing.

---

## Results

- Successfully estimated nutrition for standard servings across multiple test dishes.
- Correct handling of ambiguous or missing data points without program crashes.
- Robust fuzzy matching and quantity standardization.
- Working CLI and Local API verified through manual and automated tests.

---

## Project Structure
nutrition_estimator/ ├── data/ │ └── Assignment Inputs.xlsx ├── src/ │ ├── init.py │ ├── cli.py │ ├── dish_classifier.py │ ├── ingredient_mapper.py │ ├── nutrition_calculator.py │ └── quantity_converter.py ├── main.py ├── app.py ├── README.md


---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Aasrithlingamagunta/vyb_assignment.git
cd vyb_assignment

2. Install dependencies

pip install pandas fastapi uvicorn rapidfuzz openpyxl

3. Run the CLI

python main.py

    Enter the dish name when prompted.

    Enter ingredients and their quantities one by one.

4. Run the API Server

python -m uvicorn app:app --reload

    Open http://127.0.0.1:8000/docs to test the API using Swagger UI.


Example API Input

{
  "dish_name": "Paneer Butter Masala",
  "ingredients": [
    { "ingredient": "paneer cubes", "quantity": "0.75 cup cubes" },
    { "ingredient": "butter", "quantity": "2 teaspoons" },
    { "ingredient": "tomato puree", "quantity": "0.5 cup" },
    { "ingredient": "onion chopped", "quantity": "0.5 cup" },
    { "ingredient": "cream", "quantity": "1 tablespoon" }
  ]
}


```
Check the test_outputs folder to see the outputs we have checked!!

## Future Enhancements

Although the current version fulfills the basic requirements, several improvements can be made in future iterations:

1. **Ingredient Synonym Dictionary:**  
   Build a custom dictionary to better handle common ingredient name variations (e.g., "paneer cubes" vs "paneer").

2. **Quantity Interpretation Improvements:**  
   Handle complex quantity phrases like "half a glass", "a handful of spinach", or "two large onions" more intelligently.

3. **Recipe Scraper Integration:**  
   Automatically fetch generic recipes online based on dish name using APIs instead of manual ingredient entry.

4. **Dynamic Dish Classification:**  
   Implement lightweight ML models to classify dish types (Wet Sabzi, Dal, Non-Veg Curry) instead of relying only on fuzzy string matching.

5. **Deployment of API:**  
   Host the FastAPI app publicly using services like Render, Railway, or AWS to allow easy access without local setup

