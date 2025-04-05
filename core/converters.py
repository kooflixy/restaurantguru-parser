from bs4 import BeautifulSoup

from classes.restaurant import RestaurantDTO


class SoupConverter:
    @staticmethod
    def to_restaurant(soup: BeautifulSoup) -> RestaurantDTO:
        
        name = (
            soup
            .find('div', class_='title_container')
            .find('h1', class_='notranslate')
            .text
            .replace('\n', '')
        )
        
        restaurant = RestaurantDTO(
            name=name
        )

        return restaurant