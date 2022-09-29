from flask import Blueprint, jsonify, request
from main import db
from models.recipe import Recipe
from models.category import Category
from models.ingredient_list import IngredientList
from models.ingredient import Ingredient
from models.user import User
from models.rating import Rating
from schemas.recipe_schema import recipe_schema, recipes_schema
from schemas.ingredient_list_schema import ingredient_list_schema, ingredients_list_schema
from schemas.rating_schema import rating_schema, ratings_schema
from datetime import date
from marshmallow.exceptions import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity

recipes = Blueprint("recipes", __name__, url_prefix="/recipes")

# all recipe... add search criteria later
# anyone can view all recipes that are not private
@recipes.route("/", methods=["GET"])
def get_recipes():



    # only show recipes that are not private
    recipes_list = Recipe.query.filter_by(private=False).all()
    result = recipes_schema.dump(recipes_list)
    return jsonify(result), 200

# get one recipe
# anyone can view a recipe that is not private

@recipes.route("/<int:id>", methods=["GET"])
def get_recipe(id):
    # get recipe based on id
    recipe = Recipe.query.get(id)
    # check if found
    if not recipe:
        return {"error": "Recipe id not found."}, 404

    # check if private
    if recipe.private == True:
        return {"error": "Private. Only the owner can view this recipe."}, 401

    result = recipe_schema.dump(recipe)
    return jsonify(result), 200


# show recipes for the logged in user

@recipes.route("/myrecipes", methods=["GET"])
@jwt_required()
def user_recipes():

    user_id = get_jwt_identity()

    # check if the user is admin
    if user_id == "admin":
        recipes = Recipe.query.all()

    else: 
        # get all recipes for the user
        recipes = Recipe.query.filter_by(user_id=user_id).all()

    if not recipes:
        return {"message": "You have not entered any recipes yet."}

    result = recipes_schema.dump(recipes)
    return jsonify(result), 200


# add a new recipe


@recipes.route("/", methods=["POST"])
@jwt_required()
def new_recipe():

    # get user_id from jwt
    user_id = get_jwt_identity()

    # check if admin 
    if user_id == "admin":
        user = User.query.filter_by(admin=True).first()
    else:
        # get user details from the db
        user = User.query.get(user_id)

    # add general error handling here
    recipe_fields = recipe_schema.load(request.json)

    # to update category first lookup category in the category table

    cat_search = recipe_fields["recipe_category"]["category"]

    # check if the category exists in the database
    cat_result = db.session.query(Category).filter(
        db.func.lower(Category.category) == db.func.lower(cat_search)).first()

    if not cat_result:
        return {"error": f"{cat_search} not found, enter a different category."}, 404

    recipe = Recipe(
        recipe_name=recipe_fields["recipe_name"],
        serves=recipe_fields["serves"],
        instructions=recipe_fields["instructions"],
        time_required=recipe_fields["time_required"],
        private=recipe_fields["private"],
        date_added=date.today(),
        user_id=user.user_id,
        category_id=cat_result.category_id
    )

    db.session.add(recipe)
    db.session.commit()

    # ingredients can be viewed/added/removed/updated for a particular recipe in the routes below

    return jsonify(recipe_schema.dump(recipe)), 201

# update a recipe


@recipes.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_recipe(id):

    # check if the user owners this recipe
    # get user_id from jwt
    user_id = get_jwt_identity()

    # check if admin 
    if user_id == "admin":
        user = User.query.filter_by(admin=True).first()
    else:
        # get user details from the db
        user = User.query.get(user_id)

    # seach for recipe
    recipe = Recipe.query.get(id)
    
    # check if it exists

    if not recipe:
        return {"error": "Recipe id not found."}, 404
    
    # check if recipe belongs to user
    if recipe.user_id != user.user_id and user_id != "admin":
        return {"error": "You do not have permission to update this recipe."}, 401

    # get recipe details from the frontend request

    recipe_fields = recipe_schema.load(request.json)

    # to update category first lookup category in the category table

    cat_search = recipe_fields["recipe_category"]["category"]

    # check if the category exists in the database
    cat_result = db.session.query(Category).filter(
        db.func.lower(Category.category) == db.func.lower(cat_search)).first()

    if not cat_result:
        return {"error": f"{cat_search} not found, enter a different category."}, 404

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
@jwt_required()
def delete_recipe(id):

     # get user_id from jwt
    user_id = get_jwt_identity()

    # check if admin 
    if user_id == "admin":
        user = User.query.filter_by(admin=True).first()
    else:
        # get user details from the db
        user = User.query.get(user_id)
    # search for recipe by id
    recipe = Recipe.query.get(id)

    # if no recipe is found return message
    if not recipe:
        return {"error": "Recipe id not found."}, 404

    # check if recipe belongs to user
    if recipe.user_id != user.user_id and user_id != "admin":
        return {"error": "You do not have permission to delete this recipe."}, 401    

    # delete the recipe from the database
    db.session.delete(recipe)

    # save changes
    db.session.commit()

    return {"message": "Recipe successfully deleted from database."}, 200


# get ingredients for a recipe

@recipes.route("/<int:id>/ingredients", methods=["GET"])
@jwt_required()
def get_ingredients(id):

    # seach for recipe
    recipe = Recipe.query.get(id)
    # check if it exists
    if not recipe:
        return {"error": "Recipe id not found"}, 404

    ingredients = IngredientList.query.filter_by(recipe_id=id).all()

    result = ingredients_list_schema.dump(ingredients)
    return jsonify(result), 200

# get one ingredient for a recipe


@recipes.route("/<int:recipe_id>/ingredients/<int:list_id>", methods=["GET"])
@jwt_required()
def get_one_ingredient(recipe_id, list_id):
    # seach for recipe
    recipe = Recipe.query.get(recipe_id)
    # check if it exists
    if not recipe:
        return {"error": "Recipe id not found"}, 404
    # check if ingredient is in the ingredient_list table
    ingredient = IngredientList.query.filter_by(
        recipe_id=recipe_id, list_id=list_id).first()

    if not ingredient:
        return {"error": "Ingredient id not found for the recipe."}, 404

    result = ingredient_list_schema.dump(ingredient)
    return jsonify(result), 200


# add ingredient/s to a recipe

@recipes.route("/<int:id>/ingredients", methods=["POST"])
@jwt_required()
def add_ingredients(id):

    # get user_id from jwt
    user_id = get_jwt_identity()

    # check if admin 
    if user_id == "admin":
        user = User.query.filter_by(admin=True).first()
    else:
        # get user details from the db
        user = User.query.get(user_id)


    # seach for recipe
    recipe = Recipe.query.get(id)
    # check if it exists
    if not recipe:
        return {"error": "Recipe id not found."}, 404

    # check if recipe belongs to user
    if recipe.user_id != user.user_id and user_id != "admin":
        return {"error": "You do not have permission to update this recipe."}, 401   

    # note: ingredients must be added inside a list, even for just one ingredient. List_id not required in post.
    ingredients_fields = ingredients_list_schema.load(request.json)

    # needs to be in a loop as ingredients_fields is a list

    for element in ingredients_fields:

        # check and add details to ingredient_list

        ingredient_search = element["ingredient"]["ingredient"]

        # check if the ingredient exists in the ingredient table
        ingredient_result = db.session.query(Ingredient).filter(
            db.func.lower(Ingredient.ingredient) == db.func.lower(ingredient_search)).first()

        if not ingredient_result:
            return {"error": f"{ingredient_search} not found, enter a different ingredient."}, 404

        # now check if the ingredient_id has already be added to the ingredient_list for the given recipe_id. This is done to prevent duplicate ingredients being added for a given recipe.

        result = IngredientList.query.filter_by(
            recipe_id=id, ingredient_id=ingredient_result.ingredient_id).first()

        if result:
            return {"error": f"{ingredient_result.ingredient} has already been added to the recipe, add a different ingredient."}, 400

        ingredient = IngredientList(
            ingredient_requirements=element["ingredient_requirements"],
            recipe_id=id,
            ingredient_id=ingredient_result.ingredient_id

        )

        db.session.add(ingredient)

    # only commit to the db once all new ingredients have been checked for errors

    db.session.commit()

    return {"message": "Ingredients added to recipe successfully."}

# update an ingredient in a recipe


@recipes.route("/<int:recipe_id>/ingredients/<int:list_id>", methods=["PUT"])
@jwt_required()
def update_ingredient(recipe_id, list_id):
    
    # get user_id from jwt
    user_id = get_jwt_identity()

    # check if admin 
    if user_id == "admin":
        user = User.query.filter_by(admin=True).first()
    else:
        # get user details from the db
        user = User.query.get(user_id)

    # seach for recipe
    recipe = Recipe.query.get(recipe_id)
    # check if it exists in the recipe table

    if not recipe:
        return {"error": "Recipe id not found."}, 404

    # check if recipe belongs to user
    if recipe.user_id != user.user_id and user_id != "admin":
        return {"error": "You do not have permission to update this recipe."}, 401    

    # check if ingredient is in the ingredient_list table
    ingredient = IngredientList.query.filter_by(
        recipe_id=recipe_id, list_id=list_id).first()

    if not ingredient:
        return {"error": "Ingredient id not found for recipe."}, 404

    # if the ingredient changes, need to fist check if the ingredient is available in the ingredients table.. similar to post method above

    # note: ingredients must be added as JSON. List_id is included in the URL.

    ingredient_fields = ingredient_list_schema.load(request.json)

    new_ingredient = ingredient_fields["ingredient"]["ingredient"]
    print(new_ingredient)

    #  check if the ingredient exists in the ingredient table
    ingredient_result = db.session.query(Ingredient).filter(
        db.func.lower(Ingredient.ingredient) == db.func.lower(new_ingredient)).first()

    if not ingredient_result:
        return {"error": f"{new_ingredient} not found, enter a different ingredient."}, 404

    # now check if the new ingredient has already been added to the recipe
    result = db.session.query(IngredientList).filter(
        IngredientList.recipe_id == recipe_id, IngredientList.ingredient_id == ingredient_result.ingredient_id, IngredientList.list_id != list_id).first()

    if result:
        return {"error": f"{ingredient_result.ingredient} has already been added to the recipe, add a different ingredient."}, 400

    # update information in the ingredients_list table

    ingredient.ingredient_requirements = ingredient_fields["ingredient_requirements"]
    ingredient.ingredient_id = ingredient_result.ingredient_id

    db.session.commit()

    return jsonify(ingredient_list_schema.dump(ingredient)), 201


# remove an ingredient from a recipe

@recipes.route("/<int:recipe_id>/ingredients/<int:list_id>", methods=["DELETE"])
@jwt_required()
def delete_ingredient(recipe_id, list_id):
    
    # get user_id from jwt
    user_id = get_jwt_identity()

    # check if admin 
    if user_id == "admin":
        user = User.query.filter_by(admin=True).first()
    else:
        # get user details from the db
        user = User.query.get(user_id)

    # seach for recipe
    recipe = Recipe.query.get(recipe_id)
    # check if it exists
    if not recipe:
        return {"error": "Recipe id not found."}, 404

    # check if ingredient is in the ingredient_list table
    ingredient = IngredientList.query.filter_by(
        recipe_id=recipe_id, list_id=list_id).first()

    if not ingredient:
        return {"error": "Ingredient id not found for recipe."}, 404

     # check if recipe belongs to user
    if recipe.user_id != user.user_id and user_id != "admin":
        return {"error": "You do not have permission to update this recipe."}, 401    

    # delete the recipe from the database
    db.session.delete(ingredient)

    # save changes
    db.session.commit()

    return {"message": "Ingredient successfully removed from the recipe."}, 200

# add a rating to a recipe. Note any user can rate a recipe

@recipes.route("/<int:recipe_id>/rating", methods=["POST"])
@jwt_required()
def add_rating(recipe_id):

    # only need to add rating between 1 and 5. Comment is optional
    rating_fields = rating_schema.load(request.json)

    # get user_id from jwt
    user_id = get_jwt_identity()

    # check if admin 
    if user_id == "admin":
        user = User.query.filter_by(admin=True).first()
    else:
        # get user details from the db
        user = User.query.get(user_id)

    # seach for recipe
    recipe = Recipe.query.get(recipe_id)
    # check if it exists
    if not recipe:
        return {"error": "Recipe id not found."}, 404
    
    # check if recipe is private
    if recipe.private:
        return {"error": "This recipe is private. You do not have permission to update this recipe."}, 401

    # create a new rating object

    rating = Rating(
        rating_date=date.today(),
        rating=rating_fields["rating"],
        comment=rating_fields["comment"],
        recipe_id=recipe.recipe_id,
        user_id=user.user_id
    )
    # save
    db.session.add(rating)
    # commit
    db.session.commit()

    # return the recipe with the new rating
    return jsonify(recipe_schema.dump(recipe))

#  Delete a rating. Only the user who posted the rating can delete the rating

@recipes.route("/<int:recipe_id>/rating/<int:rating_id>", methods=["DELETE"])
@jwt_required()
def delete_rating(recipe_id, rating_id):

     # get user_id from jwt
    user_id = get_jwt_identity()

    # check if admin 
    if user_id == "admin":
        user = User.query.filter_by(admin=True).first()
    else:
        # get user details from the db
        user = User.query.get(user_id)

    # seach for recipe
    recipe = Recipe.query.get(recipe_id)
    # check if it exists
    if not recipe:
        return {"error": "Recipe id not found."}, 404

    # check if rating is associated with the recipe
    rating = Rating.query.filter_by(
        recipe_id=recipe_id, rating_id=rating_id).first()

    if not rating:
        return {"error": "Rating id not found for recipe."}, 404

     # check if rating belongs to user
    if rating.user_id != user.user_id and user_id != "admin":
        return {"error": "You do not have permission delete this rating."}, 401    

    # delete the recipe from the database
    db.session.delete(rating)

    # save changes
    db.session.commit()

    return {"message": "Rating successfully removed from the recipe."}, 200

# catch validation errors
@recipes.errorhandler(ValidationError)
def register_validation_error(err):

    return err.messages, 400
