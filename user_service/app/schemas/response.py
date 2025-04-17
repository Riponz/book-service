from typing import Optional, Union, List

from user_service.app.schemas.rentals import RentalSchema
from user_service.app.schemas.user import UserSchema
from user_service.app.schemas.base import Base

class ResponseSchema(Base):
    status_code: int
    message : str
    data: Optional[Union[UserSchema, List[UserSchema], List[str], List[RentalSchema]]] = None
    user: Optional[UserSchema] = None
    book: Optional[str] = None