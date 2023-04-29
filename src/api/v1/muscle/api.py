from ....database.db import get_db

from fastapi_crudrouter import SQLAlchemyCRUDRouter
from ....schemas.muscle import Muscle, CreateMuscle
from ....database.models.muscle import Muscle as MuscleModel

router = SQLAlchemyCRUDRouter(
    schema=Muscle,
    create_schema=CreateMuscle,
    db_model=MuscleModel,
    db=get_db,
    prefix='muscle',
)

