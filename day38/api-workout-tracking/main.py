from nutritionix import NutritionIX
from sheety import Sheety

user_query = input("What exercises did you do today? ")
data_manager = NutritionIX(user_query)
sheety_manager = Sheety(data_manager.exercise_data['exercises'])
sheety_manager.post_to_sheets()
