from sqlalchemy import create_engine, text, sess
from sqlalchemy.orm import sessionmaker

# Data base url
DATABASE_URL = "postgresql://postgres:rahul5600@localhost:5432/supplychain"

# create an engine
engine = create_engine(DATABASE_URL, pool_pre_ping=True, future=True)

# sesson to reuse anywhere
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


