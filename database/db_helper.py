from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL подключения к базе данных SQLite (локально)
DATABASE_URL = "sqlite:///./wallets.db"

# экземпляр SQLAlchemy Engine для подключения к базе данных
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# фабрика сессий SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# класс для описания моделей базы данных
Base = declarative_base()
