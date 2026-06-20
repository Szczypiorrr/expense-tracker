from database.db import Session
from models.category import Category

def create_category(name):
    """
    Creates new category and saves it to database.
    """

    session = Session()

    category = Category(name = name)

    session.add(category)
    session.commit()

    session.close()

    return category

def get_category(name):
    """
    Returns category by name.
    If category does not exist, returns None.
    """

    session = Session()

    category = session.query(Category).where(name == name).first()

    session.close()

    return category