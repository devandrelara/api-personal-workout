import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models.exercise import Exercise
from .models.muscle import Muscle
from .models.recurrence import Recurrence
from .models.relations import ExerciseMuscle

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://myuser:mypassword@db:5432/mydb")
engine = create_engine(
    DATABASE_URL,
    pool_size=20,
    max_overflow=0,
    echo=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()

