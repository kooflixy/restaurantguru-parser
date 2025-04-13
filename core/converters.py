from bs4 import BeautifulSoup

from classes.restaurant import RestaurantDTO
from classes.found_restaurant import FoundRestaurantDTO


class SoupConverter:
    @staticmethod
    def to_restaurant(soup: BeautifulSoup) -> RestaurantDTO:
        
        title = (
            soup
            .find('div', class_='title_container')
            .find('h1', class_='notranslate')
        )

        name = (
            title
            .text
            .strip()
        )

        url = (
            title
            .find('a')
            .attrs
            ['href']
        )


        info_section = soup.find('div', class_='info-section')

        address = (
            info_section
            .find(id='info_location')
            .find_all('div')
            [-1]
            .text
            .strip()
        )

        peculiarities = [
            pec.text.strip()
            for pec in
            info_section.find_all('span', class_='feature_item')
        ]

        website = (
            info_section
            .find(class_='website')
        )
        if website:
            website = (
                website
                .find('a')
                .attrs
                ['href']
            )

        instagram = (
            info_section
            .find(class_='instagram')
        )
        if instagram:
            instagram = (
                instagram
                .find('a')
                .attrs
                ['href']
            )


        phone_number = (
            soup
            .find(id='call_wrap')
        )
        if phone_number:
            phone_number = phone_number.text.strip()

        description = (
            soup
            .find(class_='description')
        )
        if description:
            description = description.text.strip()


        rating_field = (
            soup
            .find('div', class_=['card__rating-stars', 'card__rating-stars--tapscroll'])
        )
        number_of_ratings = None
        rating = None
        if rating_field:
            number_of_ratings_field = (
                rating_field
                .find('span', class_='rating-stars__text')
            )
            if number_of_ratings_field:
                number_of_ratings = number_of_ratings_field.text
                number_of_ratings = int(number_of_ratings[:-7])
            
            rating_field2 = (
                rating_field
                .find('div', class_='rating-stars__fill')
            )
            if rating_field2:
                rating = rating_field2.attrs['style']
                rating = round(int(rating[6:-1])/20, 2)

        restaurant = RestaurantDTO(
            name=name,
            address=address,
            phone_number=phone_number,
            description=description,
            url=url,
            rating=rating,
            number_of_ratings=number_of_ratings,
            peculiarities=peculiarities,
            website=website,
            instagram=instagram,
        )

        return restaurant
    
    @staticmethod
    def to_found_restaurant(soup: BeautifulSoup) -> FoundRestaurantDTO:

        name = (
            soup
            .find('h3', class_='item__title')
            .text
            .strip()
        )
        name = name[name.find(' ')+1:]

        type = (
            soup
            .find('span', class_='grey')
        )
        if type:
            type = type.text.strip()

        url = (
            soup
            .find('a', class_=['notranslate', 'title_url'])
            .attrs
            ['href']
        )

        return FoundRestaurantDTO(
            name=name,
            type=type,
            url=url,
        )

    @staticmethod
    def to_found_restaurant_list(soup: BeautifulSoup) -> list[FoundRestaurantDTO]:
        restaurants_soups = soup.find_all('div', class_=['restaurant_row', 'show', 'words_review_link', 'with_snippet'])
        restaurants_list = [SoupConverter.to_found_restaurant(restaurants_soup) for restaurants_soup in restaurants_soups]

        return restaurants_list