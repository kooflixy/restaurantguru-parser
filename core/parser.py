from classes.found_restaurant import FoundRestaurantDTO
from classes.restaurant import RestaurantDTO
from cloudscraper import CloudScraper
from bs4 import BeautifulSoup
from core.converters import SoupConverter
from core.urls import Urls

scraper = CloudScraper()

class RestaurantGuruParser:
    @staticmethod
    def get_restaurant(url: str) -> RestaurantDTO:
        data = scraper.get(url)
        soup = BeautifulSoup(data.text, 'lxml')
        restaurant = SoupConverter.to_restaurant(soup)

        return restaurant

    @staticmethod
    def get_page_restaurant_list_bycity(city_slug: str, page: int = 1) -> list[FoundRestaurantDTO]:
        data = scraper.get(Urls.city_restaurants(city_slug, page))
        soup = BeautifulSoup(data.text, 'lxml')
        soup = soup.find('div', class_=['restaurant_result', 'scroll-container'])
        restaurant_list = SoupConverter.to_found_restaurant_list(soup)

        return restaurant_list
    
    @staticmethod
    def get_restaurant_list_bycity(city_slug: str) -> list[FoundRestaurantDTO]:
        page=1
        res = []
        while True:
            data = RestaurantGuruParser.get_page_restaurant_list_bycity(city_slug, page)
            res+=data
            page+=1
            if page==100: break
        return res