from flask import Blueprint, jsonify, request 
from main import db
from models.category import Category
from schemas.category_schema import category_schema,categories_schema

categories = Blueprint("categories", __name__, url_prefix="/categories")

@categories.route("/", methods=["GET"])
def get_categories():
    # get all categories and associated recipes

    categories_list = Category.query.all()
    result = categories_schema.dump(categories_list)
    return jsonify(result), 200


