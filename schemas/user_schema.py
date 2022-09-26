from main import ma
from marshmallow import fields
from marshmallow.validate import Length, Email, ContainsOnly, And


class UserSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["user_id", "email", "password",
                  "name", "phone", "dob", "admin"]
        load_only = ["admin"]

    # add validation here
    email = ma.Email(required=True, allow_none=False, validate=Email())
    password = ma.String(required=True, allow_non=False, validate=Length(min=8))
    name = ma.String(required=True, allow_none=False, validate=Length(min=1))
    phone = ma.String(required=False, validate=And(ContainsOnly(
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]), Length(equal=10)))
    dob = ma.Date(required = False)
    


# single recipe schema
user_schema = UserSchema()
# multiple recipes
users_schema = UserSchema(many=True)
