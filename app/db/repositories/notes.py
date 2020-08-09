from typing import Optional
from app.db.repositories.base import BaseRepository
from app.db.queries.queries import queries
from app.models.schemas.notes import NoteIn, NoteOut, NotesList
from app.db.errors import EntityDoesNotExist


class NotesRepository(BaseRepository):
    async def create_user_note(
            self,
            *,
            id_user: int,
            title: str,
            description: str
    ) -> NoteOut:
        async with self.connection.transaction():
            user_row = await queries.create_user_note(
                self.connection,
                id_user=id_user,
                title=title,
                description=description
            )
        return NoteOut(**user_row)

    async def get_note_by_id(
            self,
            login: str,
            password: str,
            id: int
    ) -> NoteIn:
        note_row = await queries.get_user_note(
            self.connection,
            login=login,
            password=password,
            id=id
        )

        if note_row:
            return NoteIn(**note_row)

        raise EntityDoesNotExist(
            "note with id={0} for user with login={1} does not exist".format(id, login),
        )

    async def get_all_notes(
            self, *, login: str, password: str
    ) -> NotesList:
        notes_list = await queries.get_all_user_notes(
            self.connection,
            login=login,
            password=password
        )
        return NotesList(notes=[dict(record) for record in notes_list])

    async def update_user_note(
            self,
            *,
            login: str,
            password: str,
            id: int,
            title: Optional[str] = None,
            description: Optional[str] = None
    ):
        note_in_db = await self.get_note_by_id(login=login, password=password, id=id)

        async with self.connection.transaction():
            note = await queries.update_user_note(
                self.connection,
                login=login,
                password=password,
                id=id,
                title=title or note_in_db.title,
                description=description or note_in_db.description
            )

        return NoteOut(**note)

    async def delete_user_note(
            self,
            login: str,
            password: str,
            id: int
    ) -> None:
        async with self.connection.transaction():
            await queries.delete_user_note(
                self.connection,
                id=id,
                login=login,
                password=password
            )
