from typing import Optional
from uuid import UUID
from sqlalchemy.orm import Session

from ...models.exercise import Set, SetBlock
from ...models.relations import SetBlockSet


def create_set(db: Session, reps: str, description: Optional[str]):
    new_set = Set(reps=reps, description=description)
    db.add(new_set)
    db.flush()
    return new_set


def create_set_block(
    db: Session, index: int, rest_interval: int, description: Optional[str]
):
    new_set = SetBlock(
        index=index, rest_interval=rest_interval, description=description
    )
    db.add(new_set)
    db.flush()
    return new_set


def create_set_block_set_relation(db: Session, set_block_id: UUID, set_id: UUID):
    new_relation = SetBlockSet(set_block_id=set_block_id, set_id=set_id)
    db.add(new_relation)
    db.flush()
    return new_relation


def update_set_index(db: Session, set_id: UUID, new_index: int) -> Optional[Set]:
    set_to_update = db.query(Set).filter(Set.id == set_id).first()
    if not set_to_update:
        return None

    set_to_update.index = new_index
    db.add(set_to_update)
    db.flush()
    db.refresh(set_to_update)

    return set_to_update
