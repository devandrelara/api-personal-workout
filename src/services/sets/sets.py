from sqlalchemy.orm import Session

from src.schemas.exercise import CreateSet, CreateSetBlock

from ...database.operations import exercise as exercise_operations


def create_set_of_exercises(db: Session, set_data: CreateSet):
    with db.begin():
        new_set = exercise_operations.create_set(
            db, set_data.reps, set_data.description
        )

        for exercise_id in set_data.exercises:
            exercise_operations.create_set_exercise_relation(
                db, new_set.id, exercise_id
            )

    return new_set


def create_block_of_sets(db: Session, set_data: CreateSetBlock):
    with db.begin():
        new_set_block = exercise_operations.create_set_block(
            db,
            index=set_data.index,
            rest_interval=set_data.rest_interval,
            description=set_data.description,
        )

        for set_index, set_id in enumerate(set_data.sets):
            exercise_operations.update_set_index(
                db=db, set_id=set_id, new_index=set_index
            )
            exercise_operations.create_set_block_set_relation(
                db, new_set_block.id, set_id
            )

    return new_set_block
