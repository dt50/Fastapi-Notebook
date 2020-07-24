import asyncpg
import app.models.models as models

async def create_user(payload: models.UserCreate):
    async with await asyncpg.create_pool(host='db', port='5432',
                                         database='note', user='fastapi_note', password='fastapi') as pool:
        async with pool.acquire() as conn:
            try:
                await conn.execute(
                    '''INSERT INTO Users (login, password) VALUES ($1, crypt($2, gen_salt('bf', 8)))''',
                    payload.usr_login, payload.usr_password1
                )
            except asyncpg.exceptions.UniqueViolationError:
                return False
    return True


async def get_user_id(user_login, user_password):
    async with await asyncpg.create_pool(host='db', port='5432',
                                         database='note', user='fastapi_note', password='fastapi') as pool:
        async with pool.acquire() as conn:
            res = await conn.fetch(
                '''SELECT id FROM Users WHERE login = $1 and password = crypt($2, password)''',
                user_login, user_password
            )
            if not res:
                return False
    return res



