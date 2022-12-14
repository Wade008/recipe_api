from datetime import date
import pandas as pd
from main import bcrypt

# seed data


# set user data

users = [

    {"username": "doolanw",
     "email": "wadedoolan@email.com",
     "password": bcrypt.generate_password_hash("123456789").decode("utf-8"),
     "name": "Wade Doolan",
     "phone": "0123456789",
     "dob": "1980-02-12",
     "admin": True
     },
    {"username": "mayerj",
     "email": "jmayer@email.com",
     "password": bcrypt.generate_password_hash("123456789").decode("utf-8"),
     "name": "John Mayer",
     "phone": "0124566789",
     "dob": "1978-01-23",
     "admin": False
     }
]


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
     "user_id": 1,
     "category_id": 1},
    {"recipe_name": "Toasted sandwiches",
     "serves": 2,
     "instructions": "Butter both sides of two slices of bread...",
     "time_required": 15.0,
     "private": False,
     "date_added": date.today(),
     "user_id": 2,
     "category_id": 3},
    {"recipe_name": "Fettuccine Alfredo",
     "serves": 2,
     "instructions": "In a large pot of boiling salted water, cook pasta according to package instructions...",
     "time_required": 40.0,
     "private": True,
     "date_added": date.today(),
     "user_id": 2,
     "category_id": 21
     }
]

food = pd.read_csv("generic-food.csv", usecols=[0])

recipe_ingredients = food["FOOD NAME"].tolist()

# add ingredient
# recipe_ingredients = [
#     "Eggs",
#     "Bacon",
#     "Tomataos",
#     "Bread",
#     "Ham",
#     "Cheese",
#     "Butter",
#     "Fettuccine pasta",
#     "Salt",
#     "Black pepper",
#     "Shallots",
#     "Parmesan",
#     "Cream"
# ]

amount_list = [
    {"amount": "2 eggs",
     "recipe_id": 1,
     "ingredient_id": 632},
    {"amount": "2 bacon rashers",
     "recipe_id": 1,
     "ingredient_id": 548},
    {"amount": "1 tomato",
     "recipe_id": 1,
     "ingredient_id": 171},
    {"amount": "2 slices",
     "recipe_id": 1,
     "ingredient_id": 822},
    {"amount": "2 slices",
     "recipe_id": 2,
     "ingredient_id": 822},
    {"amount": "2 slices of ham",
     "recipe_id": 2,
     "ingredient_id": 548},
    {"amount": "2 slices of cheese",
     "recipe_id": 2,
     "ingredient_id": 630},
    {"amount": "1/4 of a tablespoon",
     "recipe_id": 2,
     "ingredient_id": 661},
    {"amount": "250g of pasta",
     "recipe_id": 3,
     "ingredient_id": 273},
    {"amount": "1/4 tablespoon of salt",
     "recipe_id": 3,
     "ingredient_id": 660},
    {"amount": "small amount of black pepper",
     "recipe_id": 3,
     "ingredient_id": 139},
    {"amount": "1 small shallot",
     "recipe_id": 3,
     "ingredient_id": 243},
    {"amount": "3/4 parmesan",
     "recipe_id": 3,
     "ingredient_id": 725},
    {"amount": "1/2 cup of heavy cream",
     "recipe_id": 3,
     "ingredient_id": 663}
]

# rating data

ratings_data = [
    {
        "rating_date": date.today(),
        "rating": 4,
        "comment": "Lovely food",
        "user_id": 1,
        "recipe_id": 1
    },
    {
        "rating_date": date.today(),
        "rating": 5,
        "comment": "Wow food",
        "user_id": 2,
        "recipe_id": 1
    }

]
