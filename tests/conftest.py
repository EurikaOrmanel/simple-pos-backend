import pytest
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.db.sql_base import Base
from sqlalchemy.ext.asyncio import AsyncSession

# Use test database URL
TEST_DATABASE_URL = "postgresql+asyncpg://user:password@localhost/test_db"

# Create async test engine
test_engine = create_async_engine(
    TEST_DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

# Create async session factory for testing
TestingSessionLocal = sessionmaker(
    test_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def engine():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield test_engine
    await test_engine.dispose()

@pytest.fixture
async def db_session(engine) -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
