# from uuid import uuid4

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from uuid import uuid4
from ... import Base


class SetBlock(Base):
    __tablename__ = "set_blocks"
    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
    index = Column(Integer, nullable=False)
    rest_interval = Column(Integer, nullable=False)
    description = Column(String)

    sets = relationship("Set", secondary="set_blocks_sets", back_populates="set_blocks")
    workouts = relationship(
        "Workout", secondary="workouts_set_blocks", back_populates="set_blocks"
    )
