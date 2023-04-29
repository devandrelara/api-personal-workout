from sqlalchemy.orm import Session, joinedload

from ...models.exercise import Exercise as ExerciseModel
from ...models.muscle import Muscle as MuscleModel
from ...models.relations import ExerciseMuscle


def get_exercise_by_id(db: Session, exercise_id: str):
    return db.query(ExerciseModel).options(joinedload(ExerciseModel.muscles)).filter(ExerciseModel.id == exercise_id).first()


def get_exercise_muscle_relation(db: Session, exercise_id: str, muscle_id: str):
    return db.query(ExerciseMuscle).filter(
        ExerciseMuscle.exercise_id == exercise_id,
        ExerciseMuscle.muscle_id == muscle_id
    ).first()

def create_exercise_muscle_relation(db: Session, exercise_id: str, muscle_id: str):
    new_relation = ExerciseMuscle(exercise_id=exercise_id, muscle_id=muscle_id)
    db.add(new_relation)
    db.commit()
    db.refresh(new_relation)
    return new_relation

def get_exercise_muscle_relations(db: Session, exercise_id: str):
    return db.query(ExerciseMuscle).filter(ExerciseMuscle.exercise_id == exercise_id).all()


def get_exercise_with_muscles(db: Session, exercise_id: str):
    return db.query(ExerciseModel).options(
        db.joinedload(ExerciseModel.muscles)
    ).filter(ExerciseModel.id == exercise_id).first()
