from database.db import Session
from models.category import Category

def create_category(name):
    session = Session()

    category = Category(name = name)

    session.add(category)
    session.commit()

    session.close()

    return category

def get_category(name):
    session = Session()

    category = session.query(Category).where(name == name).first()

    session.close()

    return category

def get_all_categories():
    session = Session()

    categories = session.query(Category).all()

    session.close()

    return categories