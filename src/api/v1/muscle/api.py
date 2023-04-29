from fastapi_crudrouter import SQLAlchemyCRUDRouter

from src.database.db import get_db
from src.database.models.muscle import Muscle as MuscleModel
from src.schemas.muscle import CreateMuscle, Muscle

router = SQLAlchemyCRUDRouter(
    schema=Muscle,
    create_schema=CreateMuscle,
    db_model=MuscleModel,
    db=get_db,
    prefix="muscle",
)
