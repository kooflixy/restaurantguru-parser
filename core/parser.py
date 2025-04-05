from cloudscraper import CloudScraper
from bs4 import BeautifulSoup
from classes.restaurant import RestaurantDTO
from core.converters import SoupConverter

scraper = CloudScraper()

class RestaurantGuruParser:
    @staticmethod
    def get_restaurant(url: str):
        data = scraper.get(url)
        soup = BeautifulSoup(data.text, 'lxml')
        restaurant = SoupConverter.to_restaurant(soup)

        return restaurant