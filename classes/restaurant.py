from typing import Optional
from classes.base import Base

class RestaurantSchema(Base):
    address: str
    phone_number: str
    description: str
    url: str
    rating: float
    number_of_ratings: int
    peculiarities: list[Optional[str]]
    website: Optional[str] = None
    instagram: Optional[str] = None

class RestaurantDTO(RestaurantSchema):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)