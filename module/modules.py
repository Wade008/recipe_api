from main import db
from models.user import User


 # check if admin
def check_if_admin(user_id):
    if user_id == "admin":
        user = User.query.filter_by(admin=True).first()
    else:
        # get user details from the db
       user = User.query.get(user_id)

    return user