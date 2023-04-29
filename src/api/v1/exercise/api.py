from fastapi import Depends, HTTPException, Response
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.database.models.exercise import Exercise as ExerciseModel
from src.schemas.exercise import CreateExercise, Exercise
from src.services import exercise as exercise_service

exercise_router = SQLAlchemyCRUDRouter(
    schema=Exercise,
    create_schema=CreateExercise,
    db_model=ExerciseModel,
    db=get_db,
    prefix="exercise",
)


@exercise_router.get("/{item_id}")
def get_exercise(exercise_id: str, db: Session = Depends(get_db)) -> Exercise:
    exercise = exercise_service.get_exercise_with_muscles(db, exercise_id)
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")

    return exercise


@exercise_router.post("/{exercise_id}/muscle/{muscle_id}", status_code=201)
def assign_muscle_to_exercise(
    exercise_id: str, muscle_id: str, db: Session = Depends(get_db)
) -> Response:
    new_relation, error = exercise_service.assign_muscle_to_exercise(
        db, exercise_id, muscle_id
    )

    if error:
        if error == "Exercise or Muscle not found":
            raise HTTPException(status_code=404, detail=error)
        else:
            raise HTTPException(status_code=400, detail=error)

    return Response(status_code=201)
