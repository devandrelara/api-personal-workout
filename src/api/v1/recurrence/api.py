from ....database.db import get_db

from fastapi_crudrouter import SQLAlchemyCRUDRouter
from ....schemas.recurrence import CreateRecurrence, Recurrence
from ....database.models.recurrence import Recurrence as RecurrenceModel
router = SQLAlchemyCRUDRouter(
    schema=Recurrence,
    create_schema=CreateRecurrence,
    db_model=RecurrenceModel,
    db=get_db,
    prefix='recurrence',
)