from typing import Optional, List
from schemas.base import Base

class BookSchema(Base):
    id: str
    title: str
    author: str
    genre: str
    availability: int

    class Config:
        from_attributes = True

class BookCreateSchema(Base):
    title: str
    author: str
    genre: str
    availability: int


class BookUpdateSchema(Base):
    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[str] = None
    availability: Optional[int] = None

class BookIdsSchema(Base):
    books : List[str]