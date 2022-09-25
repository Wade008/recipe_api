from main import db


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    phone = db.Column(db.Integer(), nullable=False)
    dob = db.Column(db.Date(), nullable=False)
    admin = db.Column(db.Boolean(), nullable=False)
    recipes = db.relationship(
        "Recipe",
        backref="user",
        cascade="all, delete"
    )
    ratings = db.relationship(
        "Rating",
        backref="recipe",
        cascade="all, delete"
    )
