from geonamescache import GeonamesCache
import random
class Miejsca:
    def __init__(self, Id_miejsca):
        self.Id_miejsca = Id_miejsca
        self.Miasto = ""
        self.Wspolrzedne
        self.czy_miejsce_dedykowane = random.randint(0, 1)


    def create_city(self):
        gc = GeonamesCache()
        cities = gc.get_cities()
        pomorskie_cities = []
        for city in cities.values():
            if city.get('countrycode') == 'PL' and city.get('admin1code') == '82':
                pomorskie_cities.append(city)
        if pomorskie_cities:
            city = random.choice(pomorskie_cities)
        else:
            city = random.choice(list(cities.values()))
        self.Miasto = city.get('name')