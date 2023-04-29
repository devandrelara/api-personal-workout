from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class ExerciseBlockSet(Base):
    __tablename__ = "exercise_block_sets"
    id = Column(Integer, primary_key=True, default=lambda: str(uuid4()))
    order = Column(Integer)

    set_id = Column(Integer, ForeignKey("sets.id"))
    set = relationship("Set", back_populates="exercise_blocks")

    exercise_block_id = Column(Integer, ForeignKey("exercise_blocks.id"))
    exercise_block = relationship("ExerciseBlock", back_populates="sets")
