# from uuid import uuid4

# from sqlalchemy import Column, ForeignKey, Integer
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.orm import relationship

# from ... import Base


# class ExerciseBlockSet(Base):
#     __tablename__ = "exercise_block_sets"
#     id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
#     order = Column(Integer)

#     set_id = Column(UUID(as_uuid=True), ForeignKey("sets.id"))
#     set = relationship("Set", back_populates="exercise_blocks")

#     exercise_block_id = Column(UUID(as_uuid=True), ForeignKey("exercise_blocks.id"))
#     exercise_block = relationship("ExerciseBlock", back_populates="sets")
