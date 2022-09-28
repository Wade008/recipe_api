
from flask import Blueprint
from main import db
from models.recipe import Recipe
from models.category import Category
from models.ingredient import Ingredient
from models.ingredient_list import IngredientList
from models.user import User
from models.rating import Rating
from seed_data import category_list, recipes, recipe_ingredients, amount_list, users, ratings_data


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

    # add users
    for index in range(len(users)):
        user_info = User(
            username=users[index]["username"],
            email=users[index]["email"],
            password=users[index]["password"],
            name=users[index]["name"],
            phone=users[index]["phone"],
            dob=users[index]["dob"],
            admin=users[index]["admin"]
        )
        db.session.add(user_info)

    db.session.commit()


#  add categories
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
            user_id=recipes[index]["user_id"],
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
            ingredient_requirements=amount_list[index]["amount"],
            recipe_id=amount_list[index]["recipe_id"],
            ingredient_id=amount_list[index]["ingredient_id"]
        )
        db.session.add(recipe_ingredient)

    # commit
    db.session.commit()

    # add rating

    for index in range(len(ratings_data)):
        rating = Rating(
            rating_date=ratings_data[index]["rating_date"],
            rating=ratings_data[index]["rating"],
            comment=ratings_data[index]["comment"],
            user_id=ratings_data[index]["user_id"],
            recipe_id=ratings_data[index]["recipe_id"]
        )
        db.session.add(rating)

    # commit
    db.session.commit()

    print("Tables seeded")
