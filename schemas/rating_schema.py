from main import ma
from marshmallow import fields
from marshmallow.validate import Range
from schemas.user_schema import UserSchema

class RatingSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["rated_by", "rating_id", "rating_date", "rating",
                  "comment", "user_id", "recipe_id"]

    
    # Schemas imported above

    rated_by = fields.Pluck(UserSchema, "name", many=False)
    
    
    # add validation here
    rating = ma.Integer(required=True, allow_none=False, validate=Range(
        min=1, max=5, min_inclusive=True, max_inclusive=True))
    comment = ma.String(required=False)


# single
rating_schema = RatingSchema()
# multiple
ratings_schema = RatingSchema(many=True)