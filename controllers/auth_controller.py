from datetime import timedelta
from flask import Blueprint, jsonify, request
from main import db
from main import bcrypt
from main import jwt
from flask_jwt_extended import create_access_token
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




# catch validation errors
@ auth.errorhandler(ValidationError)
def register_validation_error(err):

    return err.messages, 400
