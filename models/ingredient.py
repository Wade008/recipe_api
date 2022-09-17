from main import db

class Ingredient(db.Model):
    __tablename__ = "ingredients"
    ingredient_id = db.Column(db.Integer, primary_key=True)
    ingredient = db.Column(db.String(), unique=True, nullable=False)
    ingredient_list = db.relationship(
        "IngredientList",
        backref="ingredient",
        cascade="all, delete"
    )

