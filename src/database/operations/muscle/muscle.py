from sqlalchemy.orm import Session

from ...models.muscle import Muscle as MuscleModel


def get_muscle_by_id(db: Session, muscle_id: str):
    return db.query(MuscleModel).filter(MuscleModel.id == muscle_id).first()

