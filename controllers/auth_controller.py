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

@auth.route("/register", methods=["POST"])
def register_user():

    # get details from request
    user_fields = user_schema.load(request.json)

    # look up the user using their email address

