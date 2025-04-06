from typing import Optional
from classes.base import Base

class FoundRestaurantSchema(Base):
    name: str
    type: Optional[str]
    url: str

class FoundRestaurantDTO(FoundRestaurantSchema):
    def __init_subclass__(cls, **kwargs):
        return super().__init_subclass__(**kwargs)