from fastapi_crudrouter import SQLAlchemyCRUDRouter

from ....database.db import get_db
from ....database.models.muscle import Muscle as MuscleModel
from ....schemas.muscle import CreateMuscle, Muscle

router = SQLAlchemyCRUDRouter(
    schema=Muscle,
    create_schema=CreateMuscle,
    db_model=MuscleModel,
    db=get_db,
    prefix='muscle',
)

