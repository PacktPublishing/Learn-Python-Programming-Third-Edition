# api_code/api/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import Settings

settings = Settings()


DB_URL = "sqlite:///train.db"


engine = create_engine(
    DB_URL,
    connect_args={"check_same_thread": False},
    echo=settings.debug,  # when debug is True, queries are logged
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = declarative_base()
