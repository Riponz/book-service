from fastapi import APIRouter, Depends, Response, HTTPException
from typing import Annotated
from user_service.app.schemas.response import ResponseSchema
from user_service.app.exception_handlers import UserIntegrityException, UserTimeOutException
from user_service.app.exception_handlers import UserDataException, UserOperationalException
from sqlalchemy.exc import IntegrityError, OperationalError, DataError, TimeoutError
from user_service.app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from user_service.app.schemas.user import UserSchema, UserCreateSchema, UserUpdateSchema
from user_service.app.controllers.users.add import add_user
from user_service.app.controllers.users.get import all_users
from user_service.app.controllers.users.update import update_user
from user_service.app.controllers.users.delete import delete_user
from user_service.app.controllers.users.rent import rent_book, return_book
from user_service.app.utils.authentication import get_current_user
from user_service.app.utils.user import get_user


router = APIRouter()

db_dependency = Annotated[AsyncSession, Depends(get_db)]
user_dependency = Annotated[UserSchema, Depends(get_current_user)]

@router.get("/health")
async def health_check():
    return {
        "health" : "OK"
    }


@router.get("/")
async def get_all_users(response: Response, db : db_dependency):
    try:
        data =  await all_users(db)
        response.status_code = 200

        return data
    except IntegrityError as e:
        raise UserIntegrityException(str(e.orig))

    except OperationalError as e:
        raise UserOperationalException(str(e.orig))

    except DataError as e:
        raise UserDataException(str(e.orig))

    except TimeoutError as e:
        raise UserTimeOutException("Took longer than expected")


@router.post("/add")
async def add_users(user_details: UserCreateSchema, response: Response, db : db_dependency):
    try:
        db_user = await get_user(user_details.username, db)

        if db_user:
            raise HTTPException(400, detail="user already exists")

        data = await add_user(user_details, db)
        response.status_code = 201

        return data

    except IntegrityError as e:
        raise UserIntegrityException(str(e.orig))

    except OperationalError as e:
        raise UserOperationalException(str(e.orig))

    except DataError as e:
        raise UserDataException(str(e.orig))

    except TimeoutError as e:
        raise UserTimeOutException("Took longer than expected")

@router.patch("/{user_id}/update")
async def update(update_details: UserUpdateSchema ,user_id: str, response:Response, current_user : user_dependency, db : db_dependency):
    try:
        data = await update_user(update_details, user_id, db)
        response.status_code = 200

        return data

    except IntegrityError as e:
        raise UserIntegrityException(str(e.orig))

    except OperationalError as e:
        raise UserOperationalException(str(e.orig))

    except DataError as e:
        raise UserDataException(str(e.orig))

    except TimeoutError as e:
        raise UserTimeOutException("Took longer than expected")


@router.delete("/{user_id}/delete",response_model=ResponseSchema , response_model_exclude_none=True)
async def user_delete(user_id: str, response : Response, current_user : user_dependency, db : db_dependency):
    try:
        data = await  delete_user(user_id, db)
        response.status_code = 204

        return data

    except IntegrityError as e:
        raise UserIntegrityException(str(e.orig))

    except OperationalError as e:
        raise UserOperationalException(str(e.orig))

    except DataError as e:
        raise UserDataException(str(e.orig))

    except TimeoutError as e:
        raise UserTimeOutException("Took longer than expected")


@router.post("/{user_id}/rent/{book_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def rent(user_id: str, book_id: str, response: Response, current_user : user_dependency, db: db_dependency):
    try:
        data = await rent_book(user_id, book_id, db)
        response.status_code = 200


        return data

    except IntegrityError as e:
        raise UserIntegrityException(str(e.orig))

    except OperationalError as e:
        raise UserOperationalException(str(e.orig))

    except DataError as e:
        raise UserDataException(str(e.orig))

    except TimeoutError as e:
        raise UserTimeOutException("Took longer than expected")


@router.post("/{user_id}/return/{book_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def rent(user_id: str, book_id: str, response: Response, current_user : user_dependency, db: db_dependency):
    try:
        data = await return_book(user_id, book_id, db)
        response.status_code = 200

        return data

    except IntegrityError as e:
        raise UserIntegrityException(str(e.orig))

    except OperationalError as e:
        raise UserOperationalException(str(e.orig))

    except DataError as e:
        raise UserDataException(str(e.orig))

    except TimeoutError as e:
        raise UserTimeOutException("Took longer than expected")

