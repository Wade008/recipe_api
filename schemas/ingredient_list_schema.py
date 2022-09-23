from main import ma
from marshmallow import fields
from schemas.ingredient_schema import IngredientSchema


class IngredientListSchema(ma.Schema):
    class Meta:
        ordered=True
        fields=["list_id", "ingredient_requirements", "ingredient"]

    ingredient = fields.Pluck(IngredientSchema, "ingredient", many=False)

# single ingredient
ingredient_list_schema = IngredientListSchema()

# multiple ingredients
ingredients_list_schema = IngredientListSchema(many=True)

