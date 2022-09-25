from main import ma
from marshmallow import fields
from schemas.category_schema import CategorySchema
from schemas.ingredient_list_schema import IngredientListSchema
from schemas.user_schema import UserSchema


class RecipeSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["owner", "recipe_id", "recipe_name", "serves",
                  "instructions", "time_required", "private", "date_added", "category_id", "recipe_category", "ingredient_list"]
        load_only = ["category_id"]

    # Schemas imported above
    owner = fields.Pluck(UserSchema, "name", many=False)
    recipe_category = fields.Pluck(CategorySchema, "category", many=False)
    ingredient_list = fields.List(fields.Nested(IngredientListSchema, only=["ingredient","ingredient_requirements"]))

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
