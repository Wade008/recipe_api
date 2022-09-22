from flask import Blueprint, jsonify, request
from main import db
from models.recipe import Recipe
from schemas.recipe_schema import recipe_schema, recipes_schema
from datetime import date

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

    recipe_fields = recipe_schema.load(request.json)
    recipe = Recipe(
        recipe_name=recipe_fields["recipe_name"],
        serves=recipe_fields["serves"],
        instructions=recipe_fields["instructions"],
        time_required=recipe_fields["time_required"],
        private=recipe_fields["private"],
        category_id=recipe_fields["category_id"]
    )

    db.session.add(recipe)
    db.session.commit()
    return jsonify(recipe_schema.dump(recipe)), 201

# update a recipe


@recipes.route("/<int:id>", methods=["PUT"])
def update_recipe(id):

    # seach for recipe
    recipe = Recipe.query.get(id)
    # check if it exists
    if not recipe:
        return {"error": "recipe id not found"}
    # get recipe details from the frontend request
    recipe_fields = recipe_schema.load(request.json)
    # update the values for the recipe
    recipe.recipe_name = recipe_fields["recipe_name"]
    recipe.serves = recipe_fields["serves"]
    recipe.instructions = recipe_fields["instructions"]
    recipe.time_required = recipe_fields["time_required"]
    recipe.private = recipe_fields["private"]

    # save changes
    db.session.commit()

    return jsonify(recipe_schema.dump(recipe)), 201

# update a recipe category


# delete a recipe


@recipes.route("/<int:id>", methods=["DELETE"])
def delete_recipe(id):
    # search for recipe by id
    recipe = Recipe.query.get(id)

    # if no recipe is found return message
    if not recipe:
        return {"error": "recipe id not found"}

    # delete the recipe from the database
    db.session.delete(recipe)

    # save changes
    db.session.commit()

    return {"message": "Recipe successfully deleted from database"}


# get ingredients for a recipe
