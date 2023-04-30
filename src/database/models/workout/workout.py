from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ... import Base


class Workout(Base):
    __tablename__ = "workouts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
    name = Column(String(255), nullable=False)
    rest_interval = Column(Integer, nullable=False)

    recurrence_id = Column(UUID(as_uuid=True), ForeignKey("recurrences.id"))
    recurrence = relationship("Recurrence", back_populates="workouts")

    set_blocks = relationship(
        "SetBlock", secondary="workouts_set_blocks", back_populates="workouts"
    )
