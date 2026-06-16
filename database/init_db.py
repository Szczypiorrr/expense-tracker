from db import Base, engine

def init_database():
    Base.metadata.create_all(engine)