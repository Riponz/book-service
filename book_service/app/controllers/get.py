from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.books import Book
from schemas.book import BookSchema, BookIdsSchema
from schemas.response import ResponseSchema
from exception_handlers import BookNotFoundException




async def db_get_all(db : AsyncSession):

    result = await db.execute(select(Book))
    books = result.scalars().all()
    return ResponseSchema(
        status_code=200,
        message="success",
        data=[BookSchema.model_validate(book) for book in books]
    )

async def db_get_book_by_id(book_id: str, db: AsyncSession):
    result = await db.execute(select(Book).filter(Book.id == book_id))
    book = result.scalars().first()

    if not book:
        raise BookNotFoundException("Book Not found")

    print(result.__dict__)

    return ResponseSchema(
        status_code=200,
        message="success",
        data=BookSchema.model_validate(book)
    )


async def db_get_books_by_ids(book_ids: BookIdsSchema, db: AsyncSession):
    book_list = book_ids.books

    print("%%%%")
    print(book_list)

    result = await db.execute(select(Book).where(Book.id.in_(book_list)))
    books = result.scalars().all()

    if not books:
        raise BookNotFoundException("No books found")

    print(books)

    return ResponseSchema(
        status_code=200,
        message="success",
        data=[BookSchema.model_validate(book) for book in books]
    )