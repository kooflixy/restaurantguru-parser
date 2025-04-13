import os
from core.parser import RestaurantGuruParser
from core.export import RestaurantDTOExporter
from datetime import datetime

city = input('Введите город для парсинга: ')
upload_path = f'upload/{city.lower()}.xlsx'

print('Парсер получает рестораны', end='\r')

start_time = datetime.now()

data = RestaurantGuruParser.get_restaurant_list_bycity(city)

res = []
num_s = 1

for rest in data:
    worktime = (datetime.now() - start_time).seconds
    print(f'Парсер получает подробности {num_s} ресторана. Со старта прошло: {worktime} с', end='\r')
    res.append(RestaurantGuruParser.get_restaurant(rest.url))
    num_s+=1

print(f'\nРестораны экспорируются в Excel')
if not os.path.exists('upload'): os.mkdir('upload')
RestaurantDTOExporter.to_excel(upload_path, res)

worktime = (datetime.now() - start_time).seconds
print(f'Файл вывода: "{upload_path}". Время работы: {worktime} с')