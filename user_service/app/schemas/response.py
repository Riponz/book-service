from typing import Optional, Union, List

from schemas.rentals import RentalSchema
from schemas.user import UserSchema
from schemas.base import Base

class ResponseSchema(Base):
    status_code: int
    message : str
    data: Optional[Union[UserSchema, List[UserSchema], List[str], List[RentalSchema]]] = None
    user: Optional[UserSchema] = None
    book: Optional[str] = None