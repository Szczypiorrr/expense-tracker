from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from base_model import BaseModel
from models.expense import Expense

class Category(BaseModel):
    __tablename__ = "categories"

    name = Column(String)
    expenses = relationship("Expense", back_populates="category")