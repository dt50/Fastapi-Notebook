import asyncpg
from fastapi import FastAPI
from app.core.config import DATABASE_URL


async def connect_to_db(app: FastAPI) -> None:
    app.state.pool = await asyncpg.create_pool(
        str(DATABASE_URL),
    )


async def close_db_connection(app: FastAPI) -> None:
    await app.state.pool.close()
