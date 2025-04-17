from schemas.base import Base
from typing import Union, List
from schemas.book import BookSchema


class ResponseSchema(Base):
    status_code: int
    message : str
    data: Union[BookSchema, List[BookSchema]] = None