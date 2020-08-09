from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies.database import get_repository
from app.models.schemas.notes import NoteIn, NoteOut, NotesList, NoteUpdate, NoteDelete
from app.models.schemas.users import UserIn
from app.db.repositories.notes import NotesRepository
from app.db.repositories.users import UsersRepository
from app.db.errors import EntityDoesNotExist
router = APIRouter()


@router.post("/create-user-note/", response_model=NoteOut, name="notes:create-user-note")
async def create_user_note(
        user: UserIn,
        note: NoteIn,
        notes_repo: NotesRepository = Depends(get_repository(NotesRepository)),
        users_repo: UsersRepository = Depends(get_repository(UsersRepository))
) -> NoteOut:
    try:
        user_id = await users_repo.get_user_id(
            login=user.login,
            password=user.password
        )
    except EntityDoesNotExist as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc))

    note = await notes_repo.create_user_note(
        id_user=user_id.id,
        title=note.title,
        description=note.description
    )
    return note


@router.post("/get-user-notes/", response_model=NotesList, name="notes:get-user-notes")
async def get_user_notes(
        user: UserIn,
        notes_repo: NotesRepository = Depends(get_repository(NotesRepository))
) -> NotesList:
    notes_list = await notes_repo.get_all_notes(
        login=user.login,
        password=user.password
    )
    return notes_list


@router.put("/update-user-note/", response_model=NoteOut, name="notes:update-user-note")
async def update_user_note(
        user: UserIn,
        note: NoteUpdate,
        notes_repo: NotesRepository = Depends(get_repository(NotesRepository))
) -> NoteOut:
    try:
        note = await notes_repo.update_user_note(
            login=user.login,
            password=user.password,
            id=note.id,
            title=note.title,
            description=note.description
        )
    except EntityDoesNotExist as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    return note


@router.delete("/delete-user-note/", name="notes:delete-user-note")
async def delete_user_note(
        user: UserIn,
        note: NoteDelete,
        notes_repo: NotesRepository = Depends(get_repository(NotesRepository))
):
    await notes_repo.delete_user_note(
        id=note.id,
        login=user.login,
        password=user.password
    )
    return "deleted"
