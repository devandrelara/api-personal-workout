# from uuid import uuid4

# from sqlalchemy import Column
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.orm import relationship

# from ... import Base


# class ExerciseGroup(Base):
#     __tablename__ = "exercise_groups"
#     id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
#     sets = relationship("ExerciseGroupExercise", back_populates="exercise_group")
