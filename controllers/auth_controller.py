from datetime import timedelta
from flask import Blueprint, jsonify, request
from main import db
from main import bcrypt
from main import jwt
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required 
from models.user import User
from schemas.user_schema import user_schema
from marshmallow.exceptions import ValidationError

auth = Blueprint("auth", __name__, url_prefix="/auth")

# register a new user


@auth.route("/register", methods=["POST"])
def register_user():

    # get details from request
    user_fields = user_schema.load(request.json)

    # Check if username already exists in the databse
    user = User.query.filter_by(username=user_fields["username"]).first()

    if user:
        return {"error": "Username has already been taken"}
  
    # check the user's email address to make sure they are not already registered

    user = User.query.filter_by(email=user_fields["email"]).first()

    if user:
        return {"error": "Email already exists in the database"}

    # create the user object
    user = User(
        username=user_fields["username"],
        email=user_fields["email"],
        password=bcrypt.generate_password_hash(
            user_fields["password"]).decode("utf-8"),
        name=user_fields["name"],
        phone=user_fields["phone"],
        dob=user_fields["dob"]
    )

    # add the user to the database
    db.session.add(user)

    # commit
    db.session.commit()

    token = create_access_token(identity=str(
        user.user_id), expires_delta=timedelta(hours=1))

    return {"user": user.username, "token": token}

# login in existing user


@auth.route("/user/login", methods=["POST"])
def login_user():

    # fields required to login include username and password
    user_fields = user_schema.load(request.json)

    # check if provided username  is valid

    user = User.query.filter_by(username=user_fields["username"]).first()
    
    # check if the username/email is valid

    if not user:
        return {"error": "Invalid username"}

    # check if the password is correct
    if not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return {"error": "Incorrect password"}

    # check if user has admin privileges

    if user.admin:
        id_1 = "admin"
        id_2 = id_1
    else:
        id_1 = str(user.user_id)
        id_2 = str(user.username)

   
    token = create_access_token(identity=id_1, expires_delta=timedelta(hours=1))

    print(f"id_1: {id_1}")
    print(f"id_2: {id_2}")
 
    return {"username": id_2, "token": token}

# get user dtails
@auth.route("/user/view", methods=["GET"])
@jwt_required()
def get_user():
    
    # get the user_id from the currently logged in user

    user_id = get_jwt_identity()

    # check if user is admin
    if user_id == "admin":
        user = User.query.filter_by(admin=True).first()
    else:
        # get user details from the db
        user = User.query.get(user_id)

    result = user_schema.dump(user)
    return jsonify(result), 200


# update existing user

@auth.route("/user/view", methods=["PUT"])
@jwt_required()
def update_user():

    # get username and password and other details to be updated
    user_fields = user_schema.load(request.json)

    # to update a user profile the user must submit their username and password along with all other fields listed in the get request above.
     
    # get the user_id from the currently logged in user

    user_id = get_jwt_identity()

    # check if user is admin
    if user_id == "admin":
        user = User.query.filter_by(admin=True).first()
    else:
        # get user details from the db
        user = User.query.get(user_id)

    # check if the submitted email and username are unique
      
    # Check if new username already exists in the databse
    check_user = db.session.query(User).filter(User.username==user_fields["username"], User.user_id != user.user_id).first()

    if check_user:
        return {"error": "Username has already been taken"}
  
    # check the user's email address to make sure if it is unique

    check_user = db.session.query(User).filter(User.email==user_fields["email"], User.user_id != user.user_id).first()

    if check_user:
        return {"error": "Email already exists in the database"}

    
    # check if username is different for admin. This is not allowed

    if user_id == "admin" and user.username != user_fields["username"]:
        return {"error": "Cannot change username for admin user"}


    # update the values for the user

    user.username = user_fields["username"]
    user.email = user_fields["email"]
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")
    user.name = user_fields["name"]
    user.phone = user_fields["phone"]
    user.dob= user_fields["dob"]

    # save changes
    db.session.commit()

    return jsonify(user_schema.dump(user)), 201


# delete a user
@auth.route("/user/delete", methods=["DELETE"])
@jwt_required()
def delete_user():
    
    # seach for the user in databse
    user_id = get_jwt_identity()

    if user_id == "admin":
        return {"error": "Cannot delete admin user"}

    # get user from databse
    user = User.query.get(user_id)
    # delete the user
    db.session.delete(user)
    # commit changes in the db
    db.session.commit()

    return {"success": "User deleted successfully"}

# catch validation errors
@auth.errorhandler(ValidationError)
def register_validation_error(err):

    return err.messages, 400
