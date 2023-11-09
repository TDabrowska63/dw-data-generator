from tables.samochody import Samochod
from tables.uzytkownicy import Uzytkownik
from tables.wypozyczenia import Wypozyczenie
from tables.miejsca import Miejsce
from tables.oceny_przejazdu import Oceny_przejazdu
from generate_csv.create_zgloszenia import generate_zgloszenia
import random

class Generator:
    def __init__(self, number_of_records):
        self.number_of_records = number_of_records
        self.users_list = []
        self.cars_list = []
        self.rental_list = []
        self.opinion_list = []
        self.places_list = []
        self.generate_cars()
        self.generate_users()
        self.generate_rents()
        self.generate_opinions()
        generate_zgloszenia(number_of_records, self.cars_list)

    def generate_rents(self):
        id_miejsca = 1
        miejsce_zak = Miejsce(id_miejsca)
        with open('./bulks/rents.bulk', 'w', encoding="utf-8") as file:
            for i in range(self.number_of_records):

                miejsce_rozp = Miejsce(id_miejsca)
                id_miejsca = id_miejsca + 1
                miejsce_zak = Miejsce(id_miejsca)
                id_miejsca = id_miejsca + 1
                self.places_list.append(miejsce_rozp)
                self.places_list.append(miejsce_zak)

                samochod = random.choice(self.cars_list)
                podlista = [r for r in self.rental_list if r.nr_rejestracyjny_samochodu == samochod.nr_rejestracyjny]
                przebieg = random.randint(0, 100)
                if len(podlista) != 0:
                    max_przebieg = max(podlista, key=lambda x: x.przebieg, default=None)
                    przebieg += max_przebieg.przebieg

                    miejsce_zak_samochodu = self.places_list[max_przebieg.id_miejsca_zakonczenia - 1]
                    miejsce_rozp.czy_miejsce_dedykowane = miejsce_zak_samochodu.czy_miejsce_dedykowane
                    miejsce_rozp.miasto = miejsce_zak_samochodu.miasto
                    miejsce_rozp.wspolrzedne = miejsce_zak_samochodu.wspolrzedne

                uzytkownik = random.choice(self.users_list)

                wypozyczenie = Wypozyczenie(i, przebieg, samochod.nr_rejestracyjny, uzytkownik.nr_prawa_jazdy, miejsce_rozp.id_miejsca, miejsce_zak.id_miejsca)
                self.rental_list.append(wypozyczenie)
                file.write(str(wypozyczenie))

        with open('./bulks/places.bulk', 'w', encoding="utf-8") as file:
            for place in self.places_list:
                file.write(str(place))

    def generate_opinions(self):
        with open('./bulks/opinions.bulk', 'w', encoding="utf-8") as file:
            for rent in self.rental_list:
                opinion = Oceny_przejazdu(rent.id_wypozyczenia)
                self.opinion_list.append(opinion)
                file.write(str(opinion))

    def generate_cars(self):
        with open('./bulks/cars.bulk', 'w', encoding="utf-8") as file:
            for _ in range(self.number_of_records):
                car = Samochod()
                self.cars_list.append(car)
                file.write(str(car))


    def generate_users(self):
        with open('./bulks/users.bulk', 'w', encoding="utf-8") as file:
            for i in range(self.number_of_records):
                uzytkownik = Uzytkownik()
                self.users_list.append(uzytkownik)
                file.write(str(uzytkownik))
