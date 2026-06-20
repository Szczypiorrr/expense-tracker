from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from datetime import datetime

class Expense(BaseModel):
    """
    Expense model.
    Represents a single expense entry created by a user.
    """

    __tablename__ = "expenses"

    # Amount of expense (e.g. 25.50)
    amount = Column(Float)

    # Short description of expense (e.g. "Lunch")
    description = Column(String)
    
    # Date when expense was created
    date = Column(DateTime, default=datetime.now)

    # Foreign key to user who created expense
    user_id = Column(Integer, ForeignKey("users.id"))

    # Foreign key to category of expense
    category_id = Column(Integer, ForeignKey("categories.id"))

    # Relationship to User model
    user = relationship("User", back_populates="expenses")

    # Relationship to Category model
    category = relationship("Category", back_populates="expenses")