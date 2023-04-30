from fastapi import APIRouter, FastAPI

from .exercise import exercise_router
from .muscle import router as muscle_router
from .recurrence import router as recurrence_router
from .sets import sets_router, set_blocks_router

app = FastAPI()
router = APIRouter(prefix="/v1")

router.include_router(recurrence_router)
router.include_router(muscle_router)
router.include_router(exercise_router)
router.include_router(sets_router)
router.include_router(set_blocks_router)
app.include_router(router)
