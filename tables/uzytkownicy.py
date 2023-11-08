import names
import random
from geonamescache import GeonamesCache

class Uzytkownik:
    def __init__(self):
        self.nr_prawa_jazdy = ""
        self.imie = names.get_first_name()
        self.nazwisko = names.get_last_name()
        self.miasto_zamieszkania = ""
        self.create_driving_license_num()
        self.create_city()


    def create_driving_license_num(self):
        for i in range(13):
            if i == 5 or i == 8:
                self.nr_prawa_jazdy += "/"
            else:
                self.nr_prawa_jazdy += str(random.randint(0,9))

    def create_city(self):
        gc = GeonamesCache()
        cities = gc.get_cities()
        pomorskie_cities = []
        for city in cities.values():
            if city.get('countrycode') == 'PL' and city.get('admin1_code') == '82':
                pomorskie_cities.append(city)
        if pomorskie_cities:
            city = random.choice(pomorskie_cities)
        else:
            city = random.choice(list(cities.values()))
        self.miasto_zamieszkania = city.get('name')


    def __str__(self):
        return str(self.nr_prawa_jazdy) + ";" + str(self.imie) + ";" + str(self.nazwisko) + ";" + str(self.miasto_zamieszkania) + "\n"