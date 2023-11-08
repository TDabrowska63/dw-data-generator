from tables.samochody import Samochod
from tables.uzytkownicy import Uzytkownik
from tables.wypozyczenia import Wypozyczenie
from tables.miejsca import Miejsce


class Generator:
    def __init__(self):
        samochod = Samochod()
        uzytkownik = Uzytkownik()
        wypozyczenie = Wypozyczenie(1, 300)
        miejsce = Miejsce(1)
        print(samochod)
        print(uzytkownik)
        print(wypozyczenie)
        print(miejsce)

    def generate_data(self):
        pass
    def generate_cars(self, num_of_records):
        with open('./bulks/cars.bulk', 'w', encoding="utf-8") as file:
            for _ in range(num_of_records):
                car = Samochod()
                file.write(str(car))


    def generate_users(self):

