from pydantic import EmailStr
from typing import Optional
from user_service.app.schemas.base import Base


class UserCreateSchema(Base):
    name: str
    email: EmailStr
    username : str
    password: Optional[str]

class UserSchema(Base):
    id: str
    name: str
    username : str
    email: EmailStr

    class Config:
        from_attributes = True

class UserUpdateSchema(Base):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
