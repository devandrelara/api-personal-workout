from fastapi import APIRouter, Depends, HTTPException
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from sqlalchemy.orm import Session

from ....database.db import get_db
from ....database.models.exercise import Exercise as ExerciseModel
from ....schemas.exercise import CreateExercise, Exercise
from ....services import exercise as exercise_service

router = SQLAlchemyCRUDRouter(
    schema=Exercise,
    create_schema=CreateExercise,
    db_model=ExerciseModel,
    db=get_db,
    prefix='exercise',
)

@router.get('/{item_id}')
def get_exercise(
    exercise_id: str,
    db: Session = Depends(get_db)
):
    exercise = exercise_service.get_exercise_with_muscles(db, exercise_id)
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")

    return exercise

@router.post("/{exercise_id}/muscle/{muscle_id}")
def assign_muscle_to_exercise(
    exercise_id: str,
    muscle_id: str,
    db: Session = Depends(get_db)
):
    new_relation, error = exercise_service.assign_muscle_to_exercise(db, exercise_id, muscle_id)

    if error:
        if error == "Exercise or Muscle not found":
            raise HTTPException(status_code=404, detail=error)
        else:
            raise HTTPException(status_code=400, detail=error)

    return {"message": "Muscle assigned to exercise successfully"}