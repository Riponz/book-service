from user_service.app.schemas.base import Base

class RentalSchema(Base):
    id: str
    user_id: str
    book_id : str
    returned: bool

    class Config:
        from_attributes = True