import asyncpg
import app.models.models as models
from app.api.db.crud.users import get_user_id


async def create_note(payload: models.NoteSchema):
    user_id = await get_user_id(payload.usr_login, payload.usr_password)
    if not user_id:
        return False

    async with await asyncpg.create_pool(host='db', port='5432',
                                         database='note', user='fastapi_note', password='fastapi') as pool:
        async with pool.acquire() as conn:
            await conn.execute(
                '''INSERT INTO Notes (id_users, title, description) VALUES ($1, $2, $3)''',
                user_id[0].get('id'), payload.title, payload.description
            )
    return True


async def get_user_notes(usr_login, usr_password):
    user_id = await get_user_id(usr_login, usr_password)
    if not user_id:
        return False
    async with await asyncpg.create_pool(host='db', port='5432',
                                         database='note', user='fastapi_note', password='fastapi') as pool:
        async with pool.acquire() as conn:
            res = await conn.fetch(
                '''SELECT * FROM Notes WHERE id_users = $1''',
                user_id[0].get('id')
            )
    return res


async def change_user_note(payload: models.ChangeNoteSchema):
    user_id = await get_user_id(payload.usr_login, payload.usr_password)
    if not user_id:
        return False
    notes = await get_user_notes(payload.usr_login, payload.usr_password)
    for item in notes:
        if payload.id == item.get('id'):
            async with await asyncpg.create_pool(host='db', port='5432',
                                         database='note', user='fastapi_note', password='fastapi') as pool:
                async with pool.acquire() as conn:
                    await conn.execute(
                        '''UPDATE Notes SET (title, description) = ($1, $2)
                        WHERE id = $3 AND id_users = $4 ''',
                        payload.title, payload.description, payload.id, user_id[0].get('id')
                    )
            return True
    return False


async def delete_user_note(id, usr_login, usr_password):
    user_id = await get_user_id(usr_login, usr_password)
    if not user_id:
        return False
    notes = await get_user_notes(usr_login, usr_password)
    for item in notes:
        if id == item.get('id'):
            async with await asyncpg.create_pool(host='db', port='5432',
                                         database='note', user='fastapi_note', password='fastapi') as pool:
                async with pool.acquire() as conn:
                    await conn.execute(
                        '''DELETE FROM Notes WHERE id = $1 AND id_users = $2''',
                        id, user_id[0].get('id')
                    )
            return True
    return False
