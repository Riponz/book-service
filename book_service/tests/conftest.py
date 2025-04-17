import pytest
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from book_service.app.database import get_db
from book_service.app.models.base import Base
from book_service.app.models.books import Book
from book_service.app.schemas.book import BookCreateSchema
from book_service.app.main import app

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
    book = BookCreateSchema(title="Tum Hi Ho", author="Arijit Singh", genre="romantic", availability=100)
    book_item = Book(**book.model_dump())
    db_session.add(book_item)
    await db_session.commit()
    await db_session.refresh(book_item)

    yield book_item, db_session

    await db_session.close()


@pytest.fixture()
async def db_test_env():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    db_session = TestSessionLocal()
    book = BookCreateSchema(title="Tum Hi Ho", author="Arijit Singh", genre="romantic", availability=11)
    book_item = Book(**book.model_dump())
    db_session.add(book_item)
    await db_session.commit()
    await db_session.refresh(book_item)

    yield book_item, db_session

    await db_session.close()

@pytest.fixture()
async def test_env_zero_aval():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    db_session = TestSessionLocal()
    book = BookCreateSchema(title="Tum Hi Ho", author="Arijit Singh", genre="romantic", availability=0)
    book_item = Book(**book.model_dump())
    db_session.add(book_item)
    await db_session.commit()
    await db_session.refresh(book_item)

    yield book_item, db_session

    await db_session.close()

@pytest.fixture()
def client():
    return TestClient(app)