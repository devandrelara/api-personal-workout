# from uuid import uuid4

# from sqlalchemy import Column, String
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.orm import relationship

# from ... import Base


# class Set(Base):
#     __tablename__ = "sets"
#     id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
#     repetitions = Column(
#         String
#     )  # or duration, depending on the application requirements

#     exercises = relationship("ExerciseSet", back_populates="set")
