from core.parser import RestaurantGuruParser

rest = RestaurantGuruParser.get_restaurant('your_restaurant_url')

rdict = rest.__dict__
for key in rdict.keys():
    print(key + ' '*(25-len(key)), rdict[key])

# Print restaurant's all info