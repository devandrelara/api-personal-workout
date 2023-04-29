from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Day(Base):
    __tablename__ = "days"
    id = Column(Integer, primary_key=True, default=lambda: str(uuid4()))
    name = Column(String(255))

    exercises = relationship("WorkoutDay", back_populates="day")
