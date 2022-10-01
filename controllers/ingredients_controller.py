from flask import Blueprint, jsonify, request
from main import db
from models.ingredient import Ingredient
from schemas.ingredient_schema import ingredients_schema
from marshmallow.exceptions import ValidationError
from flask_jwt_extended import jwt_required


ingredients = Blueprint("ingredients", __name__, url_prefix="/ingredients")


# get all available ingredients. Only available to logged in users


@ingredients.route("/", methods=["GET"])
@jwt_required()
def get_ingredients():
    # get all ingredients

     # can use a query_sting to search for ingredients
    if request.query_string:

        if request.args.get("ingredient"):

            ing = request.args.get("ingredient").lower()

            if ing == "all":
                filtered_ingredients= Ingredient.query.all()
            else:
                filtered_ingredients = db.session.query(Ingredient).filter(db.func.lower(Ingredient.ingredient).like(f"%{ing}%")).all()

            if filtered_ingredients == []:
                return {"message": "No ingredients found"}, 404

            result = ingredients_schema.dump(filtered_ingredients)
            return jsonify(result), 200
        else:
            return {"message": "Nothing found."}, 404



    categories_list = Ingredient.query.all()
    result = ingredients_schema.dump(categories_list)
    return jsonify(result), 200



# catch validation errors

@ingredients.errorhandler(ValidationError)
def register_validation_error(err):
    return err.messages, 400
