from main import db


class Rating(db.Model):
     __tablename__ = "ratings"
     rating_id = db.Column(db.Integer, primary_key=True)
     rating_date = db.Column(db.Date(), nullable=False)
     rating = db.Column(db.Integer, nullable=False)
     comment = db.Column(db.String(), nullable=True)
     user_id = db.Column(db.Integer, db.ForeignKey(
        "users.user_id"), nullable=False)
     recipe_id = db.Column(db.Integer, db.ForeignKey(
        "recipes.recipe_id"), nullable=False)

  