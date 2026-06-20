from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQL database url (local file)
db_url = "sqlite:///database.db"

# Engine used to connect SQLAlchemy with database
engine = create_engine(db_url)

# Session creator used to create DB sessions in services
Session = sessionmaker(bind=engine)

# Base class for all ORM models
Base = declarative_base()