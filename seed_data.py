from datetime import date


# seed data

# set recipe categories

category_list = [
    "Breakfast", "Brunch", "Lunch", "Dinner", "Pancakes", "Appetisers", "Soups", "Salads", "Sides", "Vegetarian", "Snacks", "Burgers", "Pizza", "Pies", "Mince", "Lamb", "Chicken", "Seafood", "Rice", "Noodles", "Pasta", "Sausages", "Beef", "Stir Fry", "Pork", "Turkey", "Duck", "Condiments and Spreads", "Sauces", "Bread", "Slices", "Muffins, Scones and Scrolls", "Biscuits and Cookies", "Treats", "Baking", "Desserts", "Ice Cream", "Drinks", "Poultry", "Meat"
]

# add recipe
recipes = [
    {"recipe_name": "Bacon and Eggs",
     "serves": 2,
     "instructions": "Poach eggs in saucepan on medium heat for 6 min. Cook bacon in pan for 10 min on medium heat. Place tomato in pan after bacon has cooked for 8 min",
     "time_required": 30.0,
     "private": False,
     "date_added": date.today(),
     "category_id": 1},
    {"recipe_name": "Toasted sandwiches",
     "serves": 2,
     "instructions": "Butter both sides of two slices of bread...",
     "time_required": 15.0,
     "private": False,
     "date_added": date.today(),
     "category_id": 3},
    {"recipe_name": "Fettuccine Alfredo",
     "serves": 2,
     "instructions": "In a large pot of boiling salted water, cook pasta according to package instructions...",
     "time_required": 40.0,
     "private": True,
     "date_added": date.today(),
     "category_id": 21
     }
]

# add ingredient
recipe_ingredients = [
    "Eggs",
    "Bacon",
    "Tomataos",
    "Bread",
    "Ham",
    "Cheese",
    "Butter",
    "Fettuccine pasta",
    "Salt",
    "Black pepper",
    "Shallots",
    "Parmesan",
    "Cream"
]

amount_list = [
    {"amount": "2 eggs",
     "recipe_id": 1,
     "ingredient_id": 1},
    {"amount": "2 bacon rashers",
     "recipe_id": 1,
     "ingredient_id": 2},
    {"amount": "1 tomato",
     "recipe_id": 1,
     "ingredient_id": 3},
    {"amount": "2 slices",
     "recipe_id": 1,
     "ingredient_id": 4},
    {"amount": "2 slices",
     "recipe_id": 2,
     "ingredient_id": 4},
    {"amount": "2 slices of ham",
     "recipe_id": 2,
     "ingredient_id": 5},
    {"amount": "2 slices of cheese",
     "recipe_id": 2,
     "ingredient_id": 6},
    {"amount": "1/4 of a tablespoon",
     "recipe_id": 2,
     "ingredient_id": 7},
    {"amount": "250g of pasta",
     "recipe_id": 3,
     "ingredient_id": 8},
    {"amount": "1/4 tablespoon of salt",
     "recipe_id": 3,
     "ingredient_id": 9},
    {"amount": "small amount of black pepper",
     "recipe_id": 3,
     "ingredient_id": 10},
    {"amount": "1 small shallot",
     "recipe_id": 3,
     "ingredient_id": 11},
    {"amount": "3/4 parmesan",
     "recipe_id": 3,
     "ingredient_id": 12},
    {"amount": "1/2 cup of heavy cream",
     "recipe_id": 3,
     "ingredient_id": 13}
]
