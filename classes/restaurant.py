from typing import Optional
from classes.base import Base

class RestaurantSchema(Base):
    address: str
    phone_number: Optional[str]
    description: Optional[str]
    url: str
    rating: Optional[float]
    number_of_ratings: Optional[int]
    peculiarities: list[Optional[str]]
    website: Optional[str] = None
    instagram: Optional[str] = None

class RestaurantDTO(RestaurantSchema):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

    labels: dict = {
        'name': 'Название',
        'phone_number': 'Номер телефона',
        'address': 'Адрес',
        'description': 'Описание',
        'url': 'URL',
        'rating': 'Рейтинг',
        'number_of_ratings': 'Количество оценок',
        'peculiarities': 'Особенности',
        'website': 'Веб-сайт',
        'instagram': 'Instagram'
    }