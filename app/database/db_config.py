from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os



# Data base url
URL = os.getenv("DATABSE_URL")
# create an engine
engine = create_engine(DATABASE_URL, pool_pre_ping=True, future=True)

# sesson to reuse anywhere
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()