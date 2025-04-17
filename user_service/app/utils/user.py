from sqlalchemy import select
from user_service.app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from user_service.app.utils.password import verify_password


async def get_user(username: str, db : AsyncSession):
    result = await db.execute(select(User).filter(User.username == str(username)))
    user = result.scalars().first()
    return user

async def authenticate_user(db, username: str, password: str):
    user = await get_user(username, db)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user