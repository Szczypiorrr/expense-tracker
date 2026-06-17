from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.expense import Expense

class User(BaseModel):
    __tablename__ = "users"

    username = Column(String)
    expenses = relationship("Expense", back_populates="user")