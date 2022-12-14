from main import ma
from marshmallow import fields
from marshmallow.validate import Length


class IngredientSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["ingredient_id", "ingredient"]

    # add validation here
    ingredient = ma.String(required=True, allow_none=False, validate=Length(min=2))


# single
ingredient_schema = IngredientSchema()
# multiple
ingredients_schema = IngredientSchema(many=True)
