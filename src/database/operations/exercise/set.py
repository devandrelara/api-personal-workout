from typing import Optional

from sqlalchemy.orm import Session, joinedload

from ...models.exercise import Exercise, Set


def create_set(db: Session, reps: str, description: Optional[str]):
    new_set = Set(reps=reps, description=description)
    db.add(new_set)
    db.flush()
    return new_set


def get_set_by_id_with_exercises(db: Session, set_id: str):
    print(f"set id {set_id}")
    return (
        db.query(Set)
        .options(joinedload(Set.exercises).noload(Exercise.muscles))
        .filter(Set.id == set_id)
        .first()
    )
