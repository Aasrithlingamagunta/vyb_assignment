from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from src.cli import NutritionEstimatorCLI

app = FastAPI()
estimator = NutritionEstimatorCLI('data/Assignment Inputs.xlsx')

class IngredientInput(BaseModel):
    ingredient: str
    quantity: str

class DishRequest(BaseModel):
    dish_name: str
    ingredients: List[IngredientInput]

@app.post("/estimate_nutrition")
def estimate_nutrition(request: DishRequest):
    try:
        ingredients_list = [{'ingredient': item.ingredient, 'quantity': item.quantity} for item in request.ingredients]
        result = estimator.estimate_nutrition(request.dish_name, ingredients_list)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
