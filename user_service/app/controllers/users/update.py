from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from user_service.app.models.user import User
from user_service.app.schemas.user import UserSchema, UserUpdateSchema
from user_service.app.schemas.response import ResponseSchema




async def update_user(update_details : UserUpdateSchema, user_id:str, db : AsyncSession):

    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalars().first()

    if not user:
        raise HTTPException(404, detail="User Not Found")

    upd = update_details.model_dump()

    for key, value in upd.items():
        if value is not None:
            setattr(user,key, value)

    await db.commit()
    await db.refresh(user)

    return ResponseSchema(
        status_code=200,
        message="success",
        data=UserSchema.model_validate(user)
    )