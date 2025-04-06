CITY_RESTAURANTS_URL = 'https://restaurantguru.ru/restaurant-{city_slug}-t1'

class Urls:
    @staticmethod
    def city_restaurants(city_slug: str, page: int = 1) -> str:
        return CITY_RESTAURANTS_URL.format(city_slug=city_slug) + f'/{page}'