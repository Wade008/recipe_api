from flask import Blueprint, jsonify, request
from main import db
from models.category import Category
from schemas.category_schema import category_schema, categories_schema
from marshmallow.exceptions import ValidationError

categories = Blueprint("categories", __name__, url_prefix="/categories")

# get all categories


@categories.route("/", methods=["GET"])
def get_categories():
    # get all categories and associated recipes

    categories_list = Category.query.all()
    result = categories_schema.dump(categories_list)
    return jsonify(result), 200


#  get one category

@categories.route("/<int:id>", methods=["GET"])
def get_category(id):
    # search for the category
    category = Category.query.get(id)

    # check if the category exists
    if not category:
        return {"error": "Category id not found"}, 404

    # serialise
    result = category_schema.dump(category)
    return jsonify(result), 200

# post a category


@categories.route("/", methods=["POST"])
def add_category():

    # get values from front end
    category_fields = category_schema.load(request.json)

    # check if the category exists
    exists = db.session.query(Category).filter(
        db.func.lower(Category.category) == db.func.lower(category_fields["category"])).first()

    if exists:
        return {"error": "Category already exists"}, 403

    category = Category(
        category=category_fields["category"]
    )

    db.session.add(category)
    db.session.commit()

    return jsonify(category_schema.dump(category)), 201

# update a category


@categories.route("/<int:id>", methods=["PUT"])
def update_category(id):

    # search for a category
    category = Category.query.get(id)

    # check if the category exists
    if not category:
        return {"error": "Category not found"}, 404

    # get new values from front end
    category_fields = category_schema.load(request.json)

    # check if the category exists against the new value
    exists = db.session.query(Category).filter(
        db.func.lower(Category.category) == db.func.lower(category_fields["category"])).first()

    if exists:
        return {"error": "Category already exists"}, 403

    category.category = category_fields["category"]

    # save changes
    db.session.commit()

    return jsonify(category_schema.dump(category)), 201

# delete a category
@categories.route("/<int:id>", methods=["DELETE"])
def delete_category(id):
    # search for a category
    category = Category.query.get(id)

    # check if the category exists
    if not category:
        return {"error": "Category not found"}, 404

    # delete the category
    db.session.delete(category)
    # commit changes
    db.session.commit()

    return {"message": "Category removed successfully"}, 200


# catch validation errors

@categories.errorhandler(ValidationError)
def register_validation_error(err):
    return err.messages, 400
