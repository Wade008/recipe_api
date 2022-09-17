from flask import Blueprint
from main import db
from models.recipe import Recipe
from models.category import Category
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

    # set recipe categories

    category_list = [
        "Breakfast", "Brunch", "Lunch", "Dinner", "Pancakes", "Appetisers", "Soups", "Salads", "Sides", "Vegetarian", "Snacks", "Burgers", "Pizza", "Pies", "Mince", "Lamb", "Chicken", "Seafood", "Rice", "Noodles", "Pasta", "Sausages", "Beef", "Stir Fry", "Pork", "Turkey", "Duck", "Condiments and Spreads", "Sauces", "Bread", "Slices", "Muffins, Scones and Scrolls", "Biscuits and Cookies", "Treats", "Baking", "Desserts", "Ice Cream", "Drinks", "Poultry", "Meat"
    ]

    for item in category_list:

        cat_item = Category(
            category=item
        )
        db.session.add(cat_item)

    db.session.commit()

    # get id for breakfast category
    breakfast = Category.query.filter_by(category = "Breakfast").first()

    recipe1 = Recipe(
        recipe_name="Bacon and Eggs",
        serves=2,
        instructions="Poach eggs in saucepan on medium heat for 6 min. Cook bacon in pan for 10 min on medium heat. Place tomato in pan after bacon has cooked for 8 min",
        time_required=15.0,
        private=False,
        date_added=date.today(),
        category_id=breakfast.category_id

    )

    db.session.add(recipe1)
    db.session.commit()

    print("Tables seeded")
