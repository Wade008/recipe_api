from flask import Blueprint
from main import db
from models.recipe import Recipe
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

    recipe1 = Recipe(
        recipe_name="Bacon and Eggs",
        serves=2,
        instructions="Poach eggs in saucepan on medium heat for 6 min. Cook bacon in pan for 10 min on medium heat. Place tomato in pan after bacon has cooked for 8 min",
        time_required=15.0,
        private=False,
        date_added=date.today()

    )

    db.session.add(recipe1)
    db.session.commit()

    print("Tables seeded")
