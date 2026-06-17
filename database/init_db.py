from database.db import Base, engine

from models.category import Category
from models.expense import Expense
from models.user import User

def init_database():
    Base.metadata.create_all(engine)