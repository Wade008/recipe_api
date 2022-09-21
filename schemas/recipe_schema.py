from main import ma
from marshmallow import fields
from schemas.category_schema import CategorySchema

class RecipeSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["recipe_id", "recipe_name", "serves",
                  "instructions", "time_required", "private", "date_added", "category_id", "category"]
        load_only = ["category_id"]

    # Schema is defined as a String, to avoid the circular import error
    category = fields.Nested(CategorySchema, only=["category",])


# single recipe schema
recipe_schema = RecipeSchema()
# multiple recipes
recipes_schema = RecipeSchema(many=True)
