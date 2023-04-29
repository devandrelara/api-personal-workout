from fastapi import APIRouter, FastAPI

from .exercise import router as exercise_router
from .muscle import router as muscle_router
from .recurrence import router as recurrence_router

app = FastAPI()
router = APIRouter(prefix="/v1")

router.include_router(recurrence_router)
router.include_router(muscle_router)
router.include_router(exercise_router)
app.include_router(router)
