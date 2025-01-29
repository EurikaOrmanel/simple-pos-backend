import contextlib
from typing import Any, AsyncIterator

from core.env_settings import EnvironmentSettings
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DatabaseSessionManager:
    def __init__(self, host: str, engine_kwargs: dict[str, Any] = {}):
        self._engine = create_async_engine(
            host,
            **engine_kwargs,
            pool_size=10,
            max_overflow=20,
            pool_timeout=60,
        )
        self._sessionmaker = async_sessionmaker(
            class_=AsyncSession,
            autocommit=False,
            bind=self._engine,
            expire_on_commit=False,
        )

    async def close(self):
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")
        await self._engine.dispose()

        self._engine = None
        self._sessionmaker = None

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self._sessionmaker is None:
            raise Exception("DatabaseSessionManager is not initialized")

        session = self._sessionmaker()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


# Print both the environment variables and the connection string for debugging


string_connection = f"postgresql+asyncpg://{EnvironmentSettings.SQL_DB_USERNAME}:{EnvironmentSettings.SQL_DB_PASSWORD}@{EnvironmentSettings.SQL_DB_HOST}:{EnvironmentSettings.SQL_DB_PORT}/{EnvironmentSettings.SQL_DB_NAME}"
sessionmanager = DatabaseSessionManager(string_connection)


async def get_db_session():
    async with sessionmanager.session() as session:
        yield session
