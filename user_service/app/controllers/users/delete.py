from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from user_service.app.models.user import User
from user_service.app.schemas.response import ResponseSchema
from user_service.app.exception_handlers import UserNotFoundException

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