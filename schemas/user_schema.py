from main import ma
from marshmallow import fields

class UserSchema(ma.Schema):
    class Meta:
        ordered=True
        fields=["user_id", "email", "password", "name", "phone","dob","admin"]


