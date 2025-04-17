from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.exceptions import HTTPException
from sqlalchemy import select
from book_service.app.models.books import Book
from book_service.app.schemas.book import BookSchema
from book_service.app.schemas.response import ResponseSchema




async def db_rent_book(book_id: str, db : AsyncSession):
    result = await db.execute(select(Book).filter(Book.id == book_id))
    book = result.scalars().first()

    if not book:
        raise HTTPException(404, detail="Book not found")

    if book.availability == 0:
        raise HTTPException(status_code=400, detail="Book is not available")

    setattr(book, "availability", book.availability - 1)

    await db.commit()

    await db.refresh(book)

    return ResponseSchema(
        status_code=200,
        message="success",
        data=BookSchema.model_validate(book)
    )


async def db_return_book(book_id: str, db : AsyncSession):
    result = await db.execute(select(Book).filter(Book.id == book_id))
    book = result.scalars().first()

    if not book:
        raise HTTPException(404, detail="Book not found")

    setattr(book, "availability", book.availability + 1)

    await db.commit()

    await db.refresh(book)

    return ResponseSchema(
        status_code=200,
        message="success",
        data=BookSchema.model_validate(book)
    )