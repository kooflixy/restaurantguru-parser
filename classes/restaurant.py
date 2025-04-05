from pydantic import BaseModel
from classes.base import Base

class RestaurantSchema(Base):
    ...

class RestaurantDTO(RestaurantSchema):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)