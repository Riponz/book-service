from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User
from schemas.response import ResponseSchema
from exception_handlers import UserNotFoundException

async def delete_user(user_id: str, db: AsyncSession):
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalars().first()

    if not user:
        raise UserNotFoundException("User Not Found")


    await db.delete(user)
    await db.commit()

    return ResponseSchema(
        status_code=204,
        message="deleted success"
    )