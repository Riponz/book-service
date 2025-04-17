import httpx
import os
from dotenv import load_dotenv
from fastapi import HTTPException
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User
from models.rental import Rental
from schemas.user import UserSchema
from schemas.response import ResponseSchema
from exception_handlers import UserNotFoundException

load_dotenv()

# BOOK_API_URL = "https://book-service-7p3c.onrender.com/api/v1/books"


async def rent_book(user_id: str, book_id: str, db: AsyncSession):
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalars().first()

    if not user:
        raise UserNotFoundException("User Not Found")

    user_schema = UserSchema.model_validate(user)

    async with httpx.AsyncClient() as client:
        book = await client.get(f"{os.getenv("BOOK_API_URL")}/{book_id}")

        if book.status_code != 200:
            raise HTTPException(404, detail="Book Not Found")

        rent = await client.patch(f"{os.getenv("BOOK_API_URL")}/{book_id}/rent")

        if rent.status_code != 200:
            raise HTTPException(404, detail="Book Not Available")

        rental = Rental(user_id=user_id, book_id=book_id)
        db.add(rental)
        await db.commit()
        await db.refresh(rental)
        await db.refresh(user)

        return ResponseSchema(
            status_code=200,
            message="rent successfull",
            user=user_schema,
            book=book_id
        )


async def return_book(user_id: str, book_id: str, db: AsyncSession):
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalars().first()

    if not user:
        raise UserNotFoundException("User Not Found")

    user_schema = UserSchema.model_validate(user)

    async with httpx.AsyncClient() as client:
        book = await client.get(f"{BOOK_API_URL}/{book_id}")

        if book.status_code != 200:
            raise HTTPException(404, detail="Book Not Found")

        rent = await client.patch(f"{BOOK_API_URL}/{book_id}/return")

        if rent.status_code != 200:
            raise HTTPException(404, detail="Book Not Available")

        result = await db.execute(
            select(Rental).where(
                and_(
                    Rental.user_id == user_id,
                    Rental.book_id == book_id,
                    Rental.returned == False
                )
            )
        )
        rental = result.scalars().first()

        if rental and rental.returned == False:
            rental.returned = True
            await db.commit()
            await db.refresh(rental)
        elif rental and rental.returned == True:
            raise HTTPException(status_code=400, detail="Already Returned")
        else:
            raise HTTPException(status_code=404, detail="Rental not found")

        return ResponseSchema(
            status_code=200,
            message="Return Successfull",
            user=user_schema,
            book=book_id
        )
