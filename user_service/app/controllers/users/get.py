from sqlalchemy.ext.asyncio import AsyncSession
from user_service.app.schemas.response import ResponseSchema
from user_service.app.schemas.user import UserSchema
from sqlalchemy import select
from user_service.app.models.user import User



async def all_users(db: AsyncSession):
    result = await db.execute(select(User))
    users = result.scalars().all()

    return ResponseSchema(
        status_code=200,
        message="success",
        data= [UserSchema.model_validate(user) for user in users]
    )