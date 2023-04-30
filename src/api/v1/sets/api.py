from fastapi import Depends
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from sqlalchemy.orm import Session
from src.database.db import get_db
from src.database.models.exercise import Set as SetModel, SetBlock as SetBlockModel
from src.schemas.exercise import Set, CreateSet, SetBlock, CreateSetBlock
from src.services import sets as sets_service

sets_router = SQLAlchemyCRUDRouter(
    schema=Set, db_model=SetModel, db=get_db, prefix="sets", create_route=False
)


@sets_router.post("/", status_code=201, response_model=Set)
def create_exercise_set(set_data: CreateSet, db: Session = Depends(get_db)) -> Set:
    return sets_service.create_set_of_exercises(db, set_data)


set_blocks_router = SQLAlchemyCRUDRouter(
    schema=SetBlock,
    db_model=SetBlockModel,
    db=get_db,
    prefix="set_blocks",
    create_route=False,
)


@set_blocks_router.post("/", status_code=201, response_model=SetBlock)
def create_set_block(
    set_data: CreateSetBlock, db: Session = Depends(get_db)
) -> SetBlock:
    return sets_service.create_block_of_sets(db, set_data)
