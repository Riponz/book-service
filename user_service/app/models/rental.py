from sqlalchemy import ForeignKey
from uuid import uuid4
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base



class Rental(Base):
    __tablename__ = "rentals"

    id : Mapped[str] = mapped_column(default=lambda: str(uuid4()), primary_key=True)
    user_id : Mapped[str] = mapped_column(ForeignKey("users.id"))
    book_id : Mapped[str] = mapped_column()
    returned : Mapped[bool] = mapped_column(default=False)