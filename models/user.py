from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.expense import Expense

class User(BaseModel):
    """
    User model.
    Represents a system user who can create and manage expenses.
    """
    __tablename__ = "users"

    # Username used to identify user in CLI
    username = Column(String)

    # One-to-many relationship: one user -> many expenses
    expenses = relationship("Expense", back_populates="user")