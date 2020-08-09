from fastapi import APIRouter
from app.api.routes.users import router as users_router
from app.api.routes.notes import router as notes_router
router = APIRouter()

router.include_router(users_router, tags=['User'], prefix='/users')
router.include_router(notes_router, tags=['Note'], prefix='/notes')