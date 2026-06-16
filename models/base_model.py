from sqlalchemy import Integer, Column
from database.db import Base

class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)