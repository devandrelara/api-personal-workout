# from uuid import uuid4

# from sqlalchemy import Column, ForeignKey
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.orm import relationship

# from ... import Base


# class WorkoutMuscle(Base):
#     __tablename__ = "workout_muscles"
#     id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
#     workout_id = Column(UUID(as_uuid=True), ForeignKey("workouts.id"))
#     workout = relationship("Workout", back_populates="muscles")
#     muscle_id = Column(UUID(as_uuid=True), ForeignKey("muscles.id"))
#     muscle = relationship("Muscle", back_populates="workouts")
