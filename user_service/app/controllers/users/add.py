from sqlalchemy.ext.asyncio import AsyncSession
from user_service.app.schemas.response import ResponseSchema
from user_service.app.schemas.user import UserSchema, UserCreateSchema
from user_service.app.models.user import User
from user_service.app.utils.password import get_password_hash
from user_service.app.utils.user import get_user
from user_service.app.exception_handlers import DuplicateUserException



async def add_user(user_details: UserCreateSchema, db: AsyncSession):
    db_user = await get_user(user_details.username, db)

    if db_user:
        raise DuplicateUserException("User Already Exists")


    hash = get_password_hash(user_details.password)
    new_user = User(
        name=user_details.name,
        username=user_details.username,
        email=user_details.email,
        password=hash
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return ResponseSchema(
        status_code=201,
        message="success",
        data= UserSchema.model_validate(new_user)
    )