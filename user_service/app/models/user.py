from uuid import uuid4
from sqlalchemy.orm import Mapped, mapped_column
from user_service.app.models.base import Base


class User(Base):
    __tablename__ = "users"


    id : Mapped[str] = mapped_column(default=lambda: str(uuid4()), primary_key=True)
    name : Mapped[str] = mapped_column()
    username : Mapped[str] = mapped_column()
    email : Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()