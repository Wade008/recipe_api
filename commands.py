from dis import Instruction
from flask import Blueprint
from main import db
from models.recipe import Recipe
from models.category import Category
from models.ingredient import Ingredient
from models.ingredient_list import IngredientList
from seed_data import category_list, recipes, recipe_ingredients, amount_list
from datetime import date


db_commands = Blueprint("db", __name__)


# Create recipe database and tables
@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created successfully")


# Drop recipe database
@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")

# seed database
@db_commands.cli.command("seed")
def seed_db():
    
    
    for item in category_list:
        cat_item = Category(
            category=item
        )
        db.session.add(cat_item)

    db.session.commit()

# add recipes
    for index in range(len(recipes)):

        recipe_data = Recipe(
            recipe_name=recipes[index]["recipe_name"],
            serves=recipes[index]["serves"],
            instructions=recipes[index]["instructions"],
            time_required=recipes[index]["time_required"],
            private=recipes[index]["private"],
            date_added=recipes[index]["date_added"],
            category_id=recipes[index]["category_id"]
        )
        db.session.add(recipe_data)


    # add ingredient

    for ingredient in recipe_ingredients:
        required_ingredient = Ingredient(
            ingredient=ingredient
        )
        db.session.add(required_ingredient)


    # commit
    db.session.commit()

    # add ingredients and amounts for recipe1 to ingredient_list

    for index in range(len(amount_list)):
        recipe_ingredient = IngredientList(
            amount=amount_list[index]["amount"],
            recipe_id=amount_list[index]["recipe_id"],
            ingredient_id=amount_list[index]["ingredient_id"]
        )
        db.session.add(recipe_ingredient)

    # commit
    db.session.commit()

    print("Tables seeded")
