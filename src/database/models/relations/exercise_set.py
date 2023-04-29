# from uuid import uuid4

# from sqlalchemy import Column, ForeignKey
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.orm import relationship

# from ... import Base


# class ExerciseSet(Base):
#     __tablename__ = "exercise_sets"
#     id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
#     exercise_id = Column(UUID(as_uuid=True), ForeignKey("exercises.id"))
#     exercise = relationship("Exercise", back_populates="sets")
#     set_id = Column(UUID(as_uuid=True), ForeignKey("sets.id"))
#     set = relationship("Set", back_populates="exercises")
