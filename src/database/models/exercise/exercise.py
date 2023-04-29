from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from ... import Base

class Exercise(Base):
    __tablename__ = 'exercises'
    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
    name = Column(String(255))
    description = Column(String, nullable=True)
    media = Column(String, nullable=True) 

    muscles = relationship('Muscle', secondary='exercises_muscles', back_populates='exercises')
    # sets = relationship('ExerciseSet', back_populates='exercise')