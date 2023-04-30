from uuid import uuid4

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from ... import Base


class WorkoutSetBlock(Base):
    __tablename__ = "workouts_set_blocks"
    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
    set_block_id = Column(UUID(as_uuid=True), ForeignKey("set_blocks.id"))
    workout_id = Column(UUID(as_uuid=True), ForeignKey("sets.id"))

    set_block = relationship("SetBlock", backref="parent_workout")
    workout = relationship("Workout", backref="assigned_set_blocks")
