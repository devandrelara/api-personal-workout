# from uuid import uuid4

# from sqlalchemy import Column, String
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.orm import relationship

# from ... import Base


# class Day(Base):
#     __tablename__ = "days"
#     id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
#     name = Column(String(255))

#     exercises = relationship("WorkoutDay", back_populates="day")
