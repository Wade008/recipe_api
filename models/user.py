from main import db


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=True)
    dob = db.Column(db.Date(), nullable=True)
    admin = db.Column(db.Boolean(), nullable=False, default=False)
    recipes = db.relationship(
        "Recipe",
        backref="owner",
        cascade="all, delete"
    )
    ratings = db.relationship(
        "Rating",
        backref="rated_by",
        cascade="all, delete"
    )
