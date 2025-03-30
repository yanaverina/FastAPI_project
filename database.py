import asyncpg
from fastapi import HTTPException
import os

async def get_connection():
    database_url = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/app_db")
    try:
        conn = await asyncpg.connect(database_url)
        return conn
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database connection error: {str(e)}"
        )