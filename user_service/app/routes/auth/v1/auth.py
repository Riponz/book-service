from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user import UserCreateSchema, UserSchema
from schemas.token import Token
from models.user import User
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db
from utils.token import create_access_token
from utils.authentication import get_current_user
from utils.password import get_password_hash
from utils.user import get_user, authenticate_user

router = APIRouter()


@router.post("/register", response_model=Token)
async def register_user(user: UserCreateSchema, db: AsyncSession = Depends(get_db)):
    db_user = await get_user(user.username, db)

    if db_user:
        raise HTTPException(400, detail="user already exists")

    hash_pass = get_password_hash(user.password)

    new_user = User(
        name=user.name,
        email=user.email,
        username=user.username,
        password=hash_pass
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=UserSchema)
def read_users_me(current_user: UserSchema = Depends(get_current_user)):
    return current_user