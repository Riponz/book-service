from sqlalchemy.ext.asyncio import AsyncSession
from schemas.response import ResponseSchema
from models.user import User
from schemas.user import UserSchema
from sqlalchemy import select



async def all_users(db: AsyncSession):
    result = await db.execute(select(User))
    users = result.scalars().all()

    return ResponseSchema(
        status_code=200,
        message="success",
        data= [UserSchema.model_validate(user) for user in users]
    )