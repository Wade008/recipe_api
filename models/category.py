from main import db


class Category(db.Model):
    __tablename__ = "categories"
    category_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(), unique=True, nullable=False)
    recipes = db.relationship(
        "Recipe",
        backref="category"

    )
