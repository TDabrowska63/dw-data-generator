from geonamescache import GeonamesCache
import random


class Miejsce:
    def __init__(self, Id_miejsca):
        self.id_miejsca = Id_miejsca
        self.miasto = ""
        self.wspolrzedne = ""
        self.czy_miejsce_dedykowane = random.choice(["Y", "N"])
        self.create_city()

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
        self.miasto = city.get('name')
        longi = city.get('longitude') + random.uniform(-0.05, 0.05)
        lati = city.get('latitude') + random.uniform(-0.05, 0.05)
        self.wspolrzedne = str(lati) + ", " + str(longi)

    def __str__(self):
        return f"{str(self.id_miejsca)}|" \
               f"{str(self.miasto)}|" \
               f"{str(self.wspolrzedne)}|" \
               f"{str(self.czy_miejsce_dedykowane)}\n"