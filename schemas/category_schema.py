from main import ma
from marshmallow import fields
from marshmallow.validate import Length
# from schemas.recipe_schema import RecipeSchema


class CategorySchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["category_id", "category", "recipes"]

    recipes = fields.List(fields.Nested('RecipeSchema', only=["recipe_name", "serves", "time_required","date_added"]))

    # add validation here
    category = ma.String(required=True, allow_none=False, validate=Length(min=3))

# single
category_schema = CategorySchema()
# multiple
categories_schema = CategorySchema(many=True)




