from core.parser import RestaurantGuruParser
from core.export import RestaurantDTOExporter

city = input('Введите город для парсинга: ')

data = RestaurantGuruParser.get_restaurant_list_bycity(city)

res = []
a = 1
for rest in data:
    res.append(RestaurantGuruParser.get_restaurant(rest.url))

RestaurantDTOExporter.to_excel(f'upload/{city.lower()}.xlsx', res)