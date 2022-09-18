from main import ma
from marshmallow import fields


class RecipeSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["recipe_id", "recipe_name", "serves",
                  "instructions", "time_required", "private", "date_added"]


# single recipe schema
recipe_schema = RecipeSchema()
# multiple recipes
recipes_schema = RecipeSchema(many=True)
