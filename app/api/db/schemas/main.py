from fastapi import FastAPI, HTTPException, status

from app.models import models
from app.api.db.crud import notes
from app.api.db.crud import users
from app.api.db.migrations import migration

import uvicorn

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await migration.startup()


@app.post('/create-user/', status_code=status.HTTP_201_CREATED, tags=['Creating'])
async def create_user(payload: models.UserCreate):
    if payload.usr_password1 != payload.usr_password2:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Password dont much!')
    user_info = await users.create_user(payload)

    if not user_info:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Users with this login already exists')
    return {'user': payload.usr_login}


@app.post('/create-user-note/', status_code=status.HTTP_201_CREATED, tags=['Creating'])
async def create_user_note(payload: models.NoteSchema):
    create_note = await notes.create_note(payload)
    if not create_note:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=create_note)
    return {'title': payload.title, 'description': payload.description}


@app.get('/get-user-notes/', tags=['Get notes'])
async def get_user_notes(usr_login: str, usr_password: str):
    notes_list = await notes.get_user_notes(usr_login, usr_password)
    if not notes_list:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No notes find')
    return {'notes': notes_list}


@app.put('/change-note/{id}', tags=['Change note'])
async def change_note(payload: models.ChangeNoteSchema):
    response = await notes.change_user_note(payload)
    if not response:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Note or User doesnt match in system!')
    return {'note_id': payload.id, 'note_title':payload.title, 'note_description': payload.description}


@app.delete('/delete-note/{id}', tags=['Delete note'])
async def delete_note(id: int, usr_login: str, usr_password: str):
    response = await notes.delete_user_note(id, usr_login, usr_password)
    if not response:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Note or User doesnt match in system!')
    return {'response': response}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
