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

    def generate_cars(self):

    def generate_users(self, number_of_users):
        with open('./bulks/Uzytkownicy.bulk', 'w', encoding="utf-8") as file:
            for i in range(number_of_users):
                uzytkownik = Uzytkownik()
                file.write(str(uzytkownik))



