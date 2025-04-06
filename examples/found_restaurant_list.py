from core.parser import RestaurantGuruParser

data = RestaurantGuruParser.get_restaurant_list_bycity('your city')

for rest in data:
    r = ''
    rdict = rest.__dict__
    for key in rdict.keys():
        r += f'{key}={rdict[key]}, '
    print(r)

# Print found restaurant list by city