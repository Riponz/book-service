from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.books import Book
from schemas.response import ResponseSchema
from exception_handlers import BookNotFoundException


async def db_delete_book(book_id: str, db: AsyncSession):
    result = await db.execute(select(Book).filter(Book.id == book_id))
    book = result.scalars().first()

    if not book:
        raise BookNotFoundException("Book not found")

    await db.delete(book)
    await db.commit()

    return ResponseSchema(
        status_code=200,
        message="Deleted Successfully"
    )
