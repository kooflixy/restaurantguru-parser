from bs4 import BeautifulSoup

from classes.restaurant import RestaurantDTO


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
            .text
            .strip()
        )

        description = (
            soup
            .find(class_='description')
            .text
            .strip()
        )

        rating_field = (
            soup
            .find('div', class_=['card__rating-stars', 'card__rating-stars--tapscroll'])
        )

        number_of_ratings = (
            rating_field
            .find('span', class_='rating-stars__text')
            .text
        )
        number_of_ratings = int(number_of_ratings[:-7])
        
        rating = (
            rating_field
            .find('div', class_='rating-stars__fill')
            .attrs
            ['style']
        )
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