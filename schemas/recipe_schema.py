from main import ma
from marshmallow import fields
from schemas.category_schema import CategorySchema
from schemas.ingredient_list_schema import IngredientListSchema
from schemas.user_schema import UserSchema
from schemas.rating_schema import RatingSchema

class RecipeSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["owner", "recipe_id", "recipe_name", "serves",
                  "instructions", "time_required", "private", "date_added", "category_id", "recipe_category", "ingredient_list", "ratings"]
        load_only = ["category_id"]

    # Schemas imported above
    owner = fields.Pluck(UserSchema, "name", many=False)
    recipe_category = fields.Pluck(CategorySchema, "category", many=False)
    ingredient_list = fields.List(fields.Nested(IngredientListSchema, only=[
                                  "ingredient", "ingredient_requirements"]))
    ratings = fields.List(fields.Nested(RatingSchema, only=["rated_by","rating", "comment"]))

    # add validation here
    recipe_name = ma.String(required=True, allow_none=False)
    serves = ma.Integer(required=True, allow_none=False)
    instructions = ma.String(required=True, allow_none=False)
    time_required = ma.Float(required=True, allow_none=False)
    private = ma.Boolean(required=True, allow_none=False,
                         truthy=set([True]), falsy=set([False]))


# single recipe schema
recipe_schema = RecipeSchema()
# multiple recipes
recipes_schema = RecipeSchema(many=True)
