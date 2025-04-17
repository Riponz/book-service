from sqlalchemy.orm import Mapped, mapped_column
from uuid import uuid4
from models.base import Base




class Book(Base):
    __tablename__ = "books"
    
    id : Mapped[str] = mapped_column(default=lambda: str(uuid4()) , primary_key=True )
    title : Mapped[str] = mapped_column()
    author : Mapped[str] = mapped_column()
    genre : Mapped[str] = mapped_column()
    availability : Mapped[int] = mapped_column()