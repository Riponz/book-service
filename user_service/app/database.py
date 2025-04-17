import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from models.base import Base


USER_DB_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./users.db")

engine = create_async_engine(USER_DB_URL,
                             connect_args={"check_same_thread": False})


db_session = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def get_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    db = db_session()
    try:
        yield db
    finally:
        await db.close()