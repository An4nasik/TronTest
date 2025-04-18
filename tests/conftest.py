import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.database import Base

TEST_DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5433/test_tron_service"

engine_test = create_async_engine(TEST_DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)

@pytest.fixture(scope="session")
async def db_engine():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine_test
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture(scope="function")
async def db_session(db_engine):
    async with AsyncSessionLocal() as session:
        yield session
        await session.rollback()
