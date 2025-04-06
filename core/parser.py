from typing import Optional
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
        '''Gets all the information about the restaurant from the website'''
        data = scraper.get(url)
        soup = BeautifulSoup(data.text, 'lxml')
        restaurant = SoupConverter.to_restaurant(soup)

        return restaurant

    @staticmethod
    def get_page_restaurant_list_bycity(city_slug: str, page: int = 1) -> Optional[list[FoundRestaurantDTO]]:
        '''Gets one page(20 restaurants) of restaurants found by city.
        Returns None if there is no such page.'''
        data = scraper.get(Urls.city_restaurants(city_slug, page))
        if data.history: return

        soup = BeautifulSoup(data.text, 'lxml')
        soup = soup.find('div', class_=['restaurant_result', 'scroll-container'])
        restaurant_list = SoupConverter.to_found_restaurant_list(soup)

        return restaurant_list
    
    @staticmethod
    def get_restaurant_list_bycity(city_slug: str) -> list[FoundRestaurantDTO]:
        '''Gets all restaurants in the selected city (up to 10000) and returns their list.
        It is recommended to use a page loop instead of this function using RestaurantGuruParser.get_page_restaurant_list_bycity(), which returns fewer restaurants, making further manipulation of the list more convenient.'''
        page=1
        res = []
        while True:
            data = RestaurantGuruParser.get_page_restaurant_list_bycity(city_slug, page)
            if not data: break

            res+=data
            page+=1
        return res