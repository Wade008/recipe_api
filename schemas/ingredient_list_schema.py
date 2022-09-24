from main import ma
from marshmallow import fields
from schemas.ingredient_schema import IngredientSchema
# from schemas.recipe_schema import RecipeSchema

class IngredientListSchema(ma.Schema):
    class Meta:
        ordered=True
        fields=["list_id", "recipe", "ingredient_requirements", "ingredient"]

    ingredient = fields.Pluck(IngredientSchema, "ingredient", many=False)
    recipe = fields.Pluck('RecipeSchema', "recipe_name")

# single ingredient
ingredient_list_schema = IngredientListSchema()

# multiple ingredients
ingredients_list_schema = IngredientListSchema(many=True)

