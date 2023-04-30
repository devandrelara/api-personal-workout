from fastapi_crudrouter import SQLAlchemyCRUDRouter

from src.database.db import get_db
from src.database.models.workout import Workout as WorkoutModel
from src.schemas.workout import CreateWorkout, Workout

workout_router = SQLAlchemyCRUDRouter(
    schema=Workout,
    create_schema=CreateWorkout,
    db_model=WorkoutModel,
    db=get_db,
    prefix="workout",
)
