import asyncpg

async def startup():
    async with await asyncpg.create_pool(host='db', port='5432',
                                         database='note', user='fastapi_note', password='fastapi') as pool:
        async with pool.acquire() as conn:
            await conn.execute('''
            CREATE EXTENSION IF NOT EXISTS pgcrypto;
            
            CREATE TABLE IF NOT EXISTS Users(
                id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
                login VARCHAR(40) NOT NULL UNIQUE,
                password TEXT NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS Notes(
                id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
                id_users int,
                title VARCHAR(50),
                description TEXT,
                created_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
            );''')