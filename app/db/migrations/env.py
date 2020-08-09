import asyncpg
from os import path
from app.core.config import DATABASE_URL

VERSIONS = './db/migrations/versions/'


async def run_migration() -> None:
    with open(path.join(VERSIONS, 'first_migrate.sql'), 'r') as file:
        row_sql = file.read()

    async with await asyncpg.create_pool(str(DATABASE_URL)) as pool:
        async with pool.acquire() as conn:
            await conn.execute(row_sql)
