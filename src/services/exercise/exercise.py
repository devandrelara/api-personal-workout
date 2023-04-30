from sqlalchemy.orm import Session

from src.schemas.exercise import CreateSet

from ...database.operations import exercise as exercise_operations
from ...database.operations import muscle as muscle_operations


def assign_muscle_to_exercise(db: Session, exercise_id: str, muscle_id: str):
    exercise = exercise_operations.get_exercise_by_id(db, exercise_id)
    muscle = muscle_operations.get_muscle_by_id(db, muscle_id)

    if not exercise or not muscle:
        return None, "Exercise or Muscle not found"

    existing_relation = exercise_operations.get_exercise_muscle_relation(
        db, exercise_id, muscle_id
    )
    if existing_relation:
        return None, "The relationship already exists"

    new_relation = exercise_operations.create_exercise_muscle_relation(
        db, exercise_id, muscle_id
    )
    return new_relation, None


def get_exercise_with_muscles(db: Session, exercise_id: str):
    return exercise_operations.get_exercise_by_id(db, exercise_id)


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


def get_exercises_set(db: Session, set_id: str):
    return exercise_operations.get_set_by_id_with_exercises(db, set_id)
