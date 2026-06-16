from database.db import Session
from models.user import User


def create_user(name):
    session = Session()

    user = User(username = name)

    session.add(user)
    session.commit()
    session.close()

    return user

def get_user(name):
    session = Session()

    user = session.query(User).where(User.username == name).first()

    session.close()

    return user

def get_all_users():
    session = Session()

    users = session.query(User).all()

    session.close()

    return users