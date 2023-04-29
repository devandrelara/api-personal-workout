from fastapi_crudrouter import SQLAlchemyCRUDRouter

from src.database.db import get_db
from src.database.models.recurrence import Recurrence as RecurrenceModel
from src.schemas.recurrence import CreateRecurrence, Recurrence

router = SQLAlchemyCRUDRouter(
    schema=Recurrence,
    create_schema=CreateRecurrence,
    db_model=RecurrenceModel,
    db=get_db,
    prefix="recurrence",
)
