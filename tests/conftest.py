from core.env_settings import EnvironmentSettings
import pytest
import asyncio
import pytest_asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.db.sql_base import SqlBase
from sqlalchemy.ext.asyncio import AsyncSession
from httpx import ASGITransport, AsyncClient
from app.db.database_session import DatabaseSessionManager, get_db_session
from main import app
import asyncpg
import time
from typing import AsyncIterator



@pytest_asyncio.fixture
async def async_client() -> AsyncClient:
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:
        yield client
