from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from book_service.app.models.books import Book
from book_service.app.schemas.book import BookSchema, BookUpdateSchema
from book_service.app.schemas.response import ResponseSchema
from book_service.app.exception_handlers import BookNotFoundException
from book_service.app.exception_handlers import NegetiveCountException


async def db_update_book(book_details: BookUpdateSchema, book_id: str, db: AsyncSession):
    result = await db.execute(select(Book).filter(Book.id == book_id))
    book = result.scalars().first()

    if not book:
        raise BookNotFoundException("Book not found")

    for key, value in book_details.model_dump().items():
        if value is not None:
            if key == 'availability' and value < 0:
                raise NegetiveCountException('Count Cannot Negetive')
            setattr(book, key, value)

    await db.commit()

    await db.refresh(book)

    return ResponseSchema(
        status_code=200,
        message="success",
        data=BookSchema.model_validate(book)
    )
