from fastapi import APIRouter, Depends, Response
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, OperationalError, DataError, TimeoutError
from schemas.book import BookUpdateSchema, BookCreateSchema, BookIdsSchema
from database import get_db
from controllers.add import db_add_book
from controllers.get import db_get_book_by_id, db_get_all
from controllers.update import db_update_book
from controllers.delete import db_delete_book
from controllers.rent import db_rent_book, db_return_book
from controllers.get import db_get_books_by_ids

from exception_handlers import (
    BookIntegrityException,
    BookDataException,
    BookOperationalException,
    BookTimeOutException
)

router = APIRouter()

db_dependency = Annotated[AsyncSession, Depends(get_db)]



# Get all books
@router.get("/")
async def get_all_books(response : Response, db : db_dependency):
    try:

        data = await db_get_all(db)
        response.status_code = 200
        return data


    except IntegrityError as e:
        raise BookIntegrityException(str(e.orig))

    except OperationalError as e:
        raise BookOperationalException(str(e.orig))

    except DataError as e:
        raise BookDataException(str(e.orig))

    except TimeoutError as e:
        raise BookTimeOutException("Took longer than expected")



# Get book by id
@router.get("/{book_id}")
async def get_book_by_id(book_id: str, response : Response, db : db_dependency):
    try:
        data = await db_get_book_by_id(book_id, db)
        response.status_code = 200
        return data

    except OperationalError as e:
        raise BookOperationalException(str(e.orig))
    except DataError as e:
        raise BookDataException(str(e.orig))

    except TimeoutError as e:
        raise BookTimeOutException("Took longer than expected")


@router.post("/rents")
async def get_book_by_ids(book_ids: BookIdsSchema, response : Response, db : db_dependency):

    print("$$$$$$$ from routes")
    print(book_ids)

    try:
        data = await db_get_books_by_ids(book_ids, db)
        response.status_code = 200
        return data

    except OperationalError as e:
        raise BookOperationalException(str(e.orig))

    except DataError as e:
        raise BookDataException(str(e.orig))

    except TimeoutError as e:
        raise BookTimeOutException("Took longer than expected")


# Add a book
@router.post("/")
async def add_book(details: BookCreateSchema, response: Response, db : db_dependency):
    try:
        data = await db_add_book(details, db)
        response.status_code = 201
        return data


    except IntegrityError as e:
        raise BookIntegrityException(str(e.orig))

    except OperationalError as e:
        raise BookOperationalException(str(e.orig))

    except DataError as e:
        raise BookDataException(str(e.orig))

    except TimeoutError as e:
        raise BookTimeOutException("Took longer than expected")



# Update a specific book
@router.put("/{book_id}/update")
async def update_book(book_details: BookUpdateSchema, response: Response,  book_id: str, db : db_dependency):
    try:
        data = await db_update_book(book_details, book_id, db)
        response.status_code = 200
        return data

    except IntegrityError as e:
        raise BookIntegrityException(str(e.orig))

    except OperationalError as e:
        raise BookOperationalException(str(e.orig))

    except DataError as e:
        raise BookDataException(str(e.orig))

    except TimeoutError as e:
        raise BookTimeOutException("Took longer than expected")


@router.delete("/{book_id}/delete", response_model_exclude_none=True)
async def delete_book(response: Response,  book_id: str, db : db_dependency):
    try:
        data = await db_delete_book(book_id, db)
        response.status_code = 200
        return data

    except IntegrityError as e:
        raise BookIntegrityException(str(e.orig))

    except OperationalError as e:
        raise BookOperationalException(str(e.orig))

    except DataError as e:
        raise BookDataException(str(e.orig))

    except TimeoutError as e:
        raise BookTimeOutException("Took longer than expected")


# Update book count
@router.patch("/{book_id}/rent")
async def borrow_book(book_id: str, response: Response, db : db_dependency):

    try:
        data = await db_rent_book(book_id, db)
        response.status_code = 200
        return data

    except IntegrityError as e:
        raise BookIntegrityException(str(e.orig))

    except OperationalError as e:
        raise BookOperationalException(str(e.orig))

    except DataError as e:
        raise BookDataException(str(e.orig))

    except TimeoutError as e:
        raise BookTimeOutException("Took longer than expected")


@router.patch("/{book_id}/return")
async def return_book(book_id: str, response: Response, db : db_dependency):

    try:
        data = await db_return_book(book_id, db)
        response.status_code = 200
        return data

    except IntegrityError as e:
        raise BookIntegrityException(str(e.orig))

    except OperationalError as e:
        raise BookOperationalException(str(e.orig))

    except DataError as e:
        raise BookDataException(str(e.orig))

    except TimeoutError as e:
        raise BookTimeOutException("Took longer than expected")