from database.db import Base, engine

from models.category import Category
from models.expense import Expense
from models.user import User

def init_database():
    """
    Initializes database tables.
    Creates all tables defined in ORM models if they do not exist yet.
    """

    Base.metadata.create_all(engine)