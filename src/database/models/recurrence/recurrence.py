from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from ... import Base


class Recurrence(Base):
    __tablename__ = 'recurrences'
    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
    name = Column(String(255))

    # workouts = relationship('Workout', back_populates='recurrence')