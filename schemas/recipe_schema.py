from main import ma
from marshmallow import fields
from schemas.category_schema import CategorySchema


class RecipeSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["recipe_id", "recipe_name", "serves",
                  "instructions", "time_required", "private", "date_added", "category_id", "recipe_category"]
        load_only = ["category_id"]

    # Schema is imported above
    recipe_category = fields.Nested(CategorySchema, only=["category"])

    # add validation here
    recipe_name = ma.String(required=True)
    serves = ma.Integer(required=True)
    instructions = ma.String(required=True)
    time_required = ma.Float(required=True)
    private = ma.Boolean(required=True, truthy=set([True]), falsy=set([False]))


# single recipe schema
recipe_schema = RecipeSchema()
# multiple recipes
recipes_schema = RecipeSchema(many=True)
