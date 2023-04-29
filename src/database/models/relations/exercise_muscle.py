from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from ... import Base


class ExerciseMuscle(Base):
    __tablename__ = 'exercises_muscles'
    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
    exercise_id = Column(UUID(as_uuid=True), ForeignKey('exercises.id'))
    muscle_id = Column(UUID(as_uuid=True), ForeignKey('muscles.id'))

    exercise = relationship('Exercise', backref='exercise_muscles')
    muscle = relationship('Muscle', backref='trained_by')