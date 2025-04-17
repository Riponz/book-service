import pytest
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from user_service.app.database import get_db
from user_service.app.models.base import Base
from user_service.app.models.user import User
from user_service.app.schemas.user import UserCreateSchema
from user_service.app.main import app

DATABASE_URL = "sqlite+aiosqlite:///:memory:"

engine = create_async_engine(DATABASE_URL,
                       connect_args={
                           "check_same_thread":False,
                       },
                       poolclass=StaticPool)

TestSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def override_get_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    database = TestSessionLocal()
    try:
        yield database
    finally:
        await database.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.mark.asyncio(scope='function')
@pytest.fixture()
async def test_env():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    db_session = TestSessionLocal()
    user = UserCreateSchema(name="Diganta", email="dig@gmail.com", username="dig", password="12345")
    new_user = User(**user.model_dump())
    db_session.add(new_user)
    await db_session.commit()
    await db_session.refresh(new_user)

    yield new_user, db_session

    await db_session.close()

@pytest.mark.asyncio(scope='function')
@pytest.fixture()
async def db_test_env():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    db_session = TestSessionLocal()
    user = UserCreateSchema(name="Diganta", email="dig@gmail.com", username="dig", password="12345")
    new_user = User(**user.model_dump())
    db_session.add(new_user)
    await db_session.commit()
    await db_session.refresh(new_user)

    yield new_user, db_session

    await db_session.close()

# @pytest.fixture()
# async def test_env_zero_aval():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     db_session = TestSessionLocal()
#     user = UserCreateSchema(name="Diganta", email="dig@gmail.com", username="dig", password="12345")
#     new_user = User(**user.model_dump())
#     db_session.add(new_user)
#     await db_session.commit()
#     await db_session.refresh(new_user)
#
#     yield new_user, db_session
#
#     await db_session.close()

@pytest.fixture()
def client():
    return TestClient(app)