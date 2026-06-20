from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.expense import Expense

class Category(BaseModel):
    """
    Category model.
    Represents expense category like Food, Transport, etc.
    """

    __tablename__ = "categories"

    # Category name (e.g. "Food")
    name = Column(String)
    expenses = relationship("Expense", back_populates="category")