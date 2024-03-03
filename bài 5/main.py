import random


city_names = ['Paris', 'London', 'Rome', 'marid']

city_temps = {city: random.randint(20, 30) for city in city_names}
print(city_temps)

above_25 = {city: temp for (city, temp)in city_temps.itemp()if temp > 25}
print(above_25)