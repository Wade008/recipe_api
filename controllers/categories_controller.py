from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from main import db
from models.category import Category
from schemas.category_schema import category_schema, categories_schema
from marshmallow.exceptions import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity


categories = Blueprint("categories", __name__, url_prefix="/categories")

# get all available categories. Only available to logged in users.


@categories.route("/", methods=["GET"])
@jwt_required()
def get_categories():

    # can use a query_sting to search for a category
    if request.query_string:

        if request.args.get("category"):

            cat = request.args.get("category").lower()

            if cat == "all":
                filtered_categories= Category.query.all()
            else:
                filtered_categories = db.session.query(Category).filter(db.func.lower(Category.category).like(f"%{cat}%")).all()

            if filtered_categories == []:
                return {"message": "No categories found"}, 404

            result = categories_schema.dump(filtered_categories)
            return jsonify(result), 200
        else:
            return {"message": "Nothing found"}, 404

    # get all categories

    categories_list = Category.query.all()
    result = categories_schema.dump(categories_list)
    return jsonify(result), 200


#  get one category. Only available to logged in users.


@categories.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_category(id):
    # search for the category
    category = Category.query.get(id)

    # check if the category exists
    if not category:
        return {"error": "Category id not found"}, 404

    # serialise
    result = category_schema.dump(category)
    return jsonify(result), 200

# post a category. Only an admin can post a category


@categories.route("/", methods=["POST"])
@jwt_required()
def add_category():

    user_id= get_jwt_identity()

    # check if the user is an admin
    if user_id != "admin":
        return {"error": "Only users with admin rights can add a category"}, 403 

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

# update a category. Only an admin can post a category


@categories.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_category(id):

    user_id= get_jwt_identity()

    # check if the user is an admin
    if user_id != "admin":
        return {"error": "Only users with admin rights can update a category"}, 403 

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

# delete a category. Only an admin can delete a category

@categories.route("/<int:id>", methods=["DELETE"])

@jwt_required()
def delete_category(id):

    user_id= get_jwt_identity()

    # check if the user is an admin
    if user_id != "admin":
        return {"error": "Only users with admin rights can update a category"}, 403 

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
