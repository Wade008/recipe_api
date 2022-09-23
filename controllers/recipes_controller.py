from flask import Blueprint, jsonify, request
from main import db
from models.recipe import Recipe
from models.category import Category
from models.ingredient_list import IngredientList
from schemas.recipe_schema import recipe_schema, recipes_schema
from schemas.ingredient_list_schema import ingredient_list_schema, ingredients_list_schema
from datetime import date
from marshmallow.exceptions import ValidationError

recipes = Blueprint("recipes", __name__, url_prefix="/recipes")


# all recipe... add search criteria later
@recipes.route("/", methods=["GET"])
def get_recipes():

    recipes_list = Recipe.query.all()
    result = recipes_schema.dump(recipes_list)
    return jsonify(result), 200

# get one recipe


@recipes.route("/<int:id>", methods=["GET"])
def get_recipe(id):
    # get recipe based on id
    recipe = Recipe.query.get(id)
    # check if found
    if not recipe:
        return {"error": "recipe id not found"}

    result = recipe_schema.dump(recipe)
    return jsonify(result), 200

#  add a new recipe


@recipes.route("/", methods=["POST"])
def new_recipe():

    # add general error handling here
    recipe_fields = recipe_schema.load(request.json)

    # to update category first lookup category in the category table

    cat_search = recipe_fields["recipe_category"]["category"]

    # check if the category exists in the database
    cat_result = db.session.query(Category).filter(
        db.func.lower(Category.category) == db.func.lower(cat_search)).first()

    if not cat_result:
        return {"error": "category not found, enter a different category"}, 404

    recipe = Recipe(
        recipe_name=recipe_fields["recipe_name"],
        serves=recipe_fields["serves"],
        instructions=recipe_fields["instructions"],
        time_required=recipe_fields["time_required"],
        private=recipe_fields["private"],
        date_added=date.today(),
        category_id=cat_result.category_id
    )
    print(recipe_fields["ingredient_list"])
    db.session.add(recipe)
    db.session.commit()

    # now add data to the ingredient_list table, skip if ingredient_list is empty

    print(recipe.recipe_id)

    return jsonify(recipe_schema.dump(recipe)), 201

# update a recipe


@recipes.route("/<int:id>", methods=["PUT"])
def update_recipe(id):

    # seach for recipe
    recipe = Recipe.query.get(id)
    # check if it exists
    if not recipe:
        return {"error": "recipe id not found"}, 404
    # get recipe details from the frontend request
    recipe_fields = recipe_schema.load(request.json)

    # to update category first lookup category in the category table

    cat_search = recipe_fields["recipe_category"]

    # check if the category exists in the database
    cat_result = db.session.query(Category).filter(
        db.func.lower(Category.category) == db.func.lower(cat_search)).first()

    if not cat_result:
        return {"error": "category not found, enter a different category"}, 404

    # Then update the id in the recipe table
    recipe.category_id = cat_result.category_id

    # update the values for the recipe
    recipe.recipe_name = recipe_fields["recipe_name"]
    recipe.serves = recipe_fields["serves"]
    recipe.instructions = recipe_fields["instructions"]
    recipe.time_required = recipe_fields["time_required"]
    recipe.private = recipe_fields["private"]

    # save changes
    db.session.commit()

    return jsonify(recipe_schema.dump(recipe)), 201

# delete a recipe


@recipes.route("/<int:id>", methods=["DELETE"])
def delete_recipe(id):
    # search for recipe by id
    recipe = Recipe.query.get(id)

    # if no recipe is found return message
    if not recipe:
        return {"error": "recipe id not found"}, 404

    # delete the recipe from the database
    db.session.delete(recipe)

    # save changes
    db.session.commit()

    return {"message": "Recipe successfully deleted from database"}, 200


# get ingredients for a recipe

@recipes.route("/<int:id>/ingredients", methods=["GET"])
def get_ingredients(id):
    # seach for recipe
    recipe = Recipe.query.get(id)
    # check if it exists
    if not recipe:
        return {"error": "recipe id not found"}, 404

    ingredients = IngredientList.query.filter_by(recipe_id=id).all()

    result = ingredients_list_schema.dump(ingredients)
    return jsonify(result), 200


# catch validation errors
@recipes.errorhandler(ValidationError)
def register_validation_error(err):

    return err.messages, 400
