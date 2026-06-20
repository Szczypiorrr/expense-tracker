from sqlalchemy import Integer, Column
from database.db import Base

class BaseModel(Base):
    """
    Base model for all database entities.
    Provides common fields like primary key ID.
    """
    
    __abstract__ = True

    # Primary key used in all tables
    id = Column(Integer, primary_key=True)