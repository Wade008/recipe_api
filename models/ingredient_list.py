from sqlite3 import dbapi2
from main import db

class IngredientList(db.Model):
    __tablename__ = "ingredient_list"

    list_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.String(), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredients.ingredient_id"), nullable=False)
    

