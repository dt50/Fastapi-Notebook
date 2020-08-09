from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies.database import get_repository
from app.models.schemas.users import UserIn, UserOut
from app.db.repositories.users import UsersRepository
from app.db.errors import SimplePassword, EntityAlreadyExist
router = APIRouter()


@router.post("/create-user/", response_model=UserOut, name="users:create-user")
async def create_user(
        user: UserIn,
        users_repo: UsersRepository = Depends(get_repository(UsersRepository))
):
    try:
        users_row = await users_repo.create_user(
            login=user.login,
            password=user.password
        )
    except (SimplePassword, EntityAlreadyExist) as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

    return users_row
