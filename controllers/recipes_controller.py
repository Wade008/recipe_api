from flask import Blueprint, jsonify, request
from main import db
from models.recipe import Recipe
from schemas.recipe_schema import recipe_schema, recipes_schema
from datetime import date

recipes = Blueprint("recipes", __name__, url_prefix="/recipes")


# all recipe
@recipes.route("/", methods=["GET"])

def get_recipes():

    recipes_list = Recipe.query.all()
    result = recipes_schema.dump(recipes_list)
    return jsonify(result), 200


