from main import db


class Recipe(db.Model):
    __tablename__ = "recipes"
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(), nullable=False)
    serves = db.Column(db.Integer(), nullable=False)
    instructions = db.Column(db.String(), nullable=False)
    time_required = db.Column(db.Float(), nullable=False)
    private = db.Column(db.Boolean(), nullable=False)
    date_added = db.Column(db.Date(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.user_id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(
        "categories.category_id"), nullable=True)
    ingredient_list = db.relationship(
        "IngredientList",
        backref="recipe",
        cascade="all, delete"
    )
    ratings = db.relationship(
        "Rating",
        backref="recipe",
        cascade="all, delete"
    )
