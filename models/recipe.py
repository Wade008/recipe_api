from main import db


class Recipe(db.Model):
    __tablename__ = "recipes"
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String())
    serves = db.Column(db.Integer())
    instructions = db.Column(db.String())
    time_required = db.Column(db.Float())
    private = db.Column(db.Boolean())
    date_added = db.Column(db.Date())
    category_id = db.Column(db.Integer, db.ForeignKey("categories.category_id"))
    ingredient_list = db.relationship(
        "IngredientList",
        backref="recipe",
        cascade="all, delete"
    )