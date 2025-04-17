from sqlalchemy.ext.asyncio import AsyncSession
from models.books import Book
from schemas.book import BookSchema, BookCreateSchema
from schemas.response import ResponseSchema
from exception_handlers import NegetiveCountException




async def db_add_book(details: BookCreateSchema, db : AsyncSession):
    details = details.model_dump()

    if details['availability'] < 0:
        raise NegetiveCountException('Count Cannot Be Negetive')

    book = Book(**details)

    db.add(book)
    await db.commit()

    await db.refresh(book)

    return ResponseSchema(
        status_code=201,
        message="success",
        data=BookSchema.model_validate(book)
    )