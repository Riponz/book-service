from typing import Annotated
from sqlalchemy import select
from schemas.user import UserSchema
from models.rental import Rental
from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from utils.authentication import get_current_user
from schemas.response import ResponseSchema
from schemas.rentals import RentalSchema

router = APIRouter()

db_dependency = Annotated[AsyncSession, Depends(get_db)]
user_dependency = Annotated[UserSchema, Depends(get_current_user)]

@router.get('/')
async def get_all_rentals(db: db_dependency):
    result = await db.execute(select(Rental))
    rentals = result.scalars().all()

    return ResponseSchema(
        status_code=200,
        message="success",
        data=[RentalSchema.model_validate(rent) for rent in rentals]
    )




@router.get('/{user_id}')
async def books_rented(user_id: str, db: db_dependency, curr_user: user_dependency):

    result = await db.execute(
        select(Rental.book_id).where(
            (Rental.user_id == user_id) &
            (Rental.returned == False)
        )
    )
    rents = result.scalars().all()


    return ResponseSchema(
        status_code=200,
        message="success",
        data=list({rent for rent in rents})
    )

