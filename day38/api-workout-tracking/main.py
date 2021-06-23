from nutritionix import NutritionIX

user_query = input("What exercises did you do today? ")
data_manager = NutritionIX(user_query)
print(data_manager.exercise_data)
