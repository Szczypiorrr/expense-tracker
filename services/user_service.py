from database.db import Session
from models.user import User


def create_user(name):
    """
    Creates a new user and saves it to database.
    """

    session = Session()

    user = User(username = name)

    session.add(user)
    session.commit()
    session.close()

    return user

def get_user(name):
    """
    Returns user by username.
    If user does not exist, returns None.
    """

    session = Session()

    user = session.query(User).where(User.username == name).first()

    session.close()

    return user