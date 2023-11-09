from tables.samochody import Samochod
from tables.uzytkownicy import Uzytkownik
from tables.wypozyczenia import Wypozyczenie
from tables.miejsca import Miejsce
from tables.oceny_przejazdu import Oceny_przejazdu
from generate_csv.create_zgloszenia import generate_zgloszenia
from generate_csv.create_zgloszenia import write_reports
import random
import names
from tools import create_city

class Generator:
    def __init__(self, n):
        self.users_list = []
        self.cars_list = []
        self.rental_list = []
        self.opinion_list = []
        self.places_list = []
        self.report_list = []
        self.generate_snapshot_1(n)

        self.generate_snapshot_2(2)

    def generate_rents(self, n):
        id_miejsca = 1
        for i in range(n):

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

            wypozyczenie = Wypozyczenie(i, przebieg, samochod.nr_rejestracyjny, uzytkownik.nr_prawa_jazdy,
                                        miejsce_rozp.id_miejsca, miejsce_zak.id_miejsca)
            self.rental_list.append(wypozyczenie)

    def write_all(self, folder_name):
        with open('./'+ folder_name +'/opinions.bulk', 'w', encoding="utf-8") as file:
            for opinion in self.opinion_list:
                file.write(str(opinion))

        with open('./'+ folder_name +'/cars.bulk', 'w', encoding="utf-8") as file:
            for car in self.cars_list:
                file.write(str(car))

        with open('./'+ folder_name +'/users.bulk', 'w', encoding="utf-8") as file:
            for user in self.users_list:
                file.write(str(user))

        with open('./'+ folder_name +'/places.bulk', 'w', encoding="utf-8") as file:
            for place in self.places_list:
                file.write(str(place))

        with open('./'+ folder_name +'/rents.bulk', 'w', encoding="utf-8") as file:
            for rent in self.rental_list:
                file.write(str(rent))


    def generate_opinions(self):
        for rent in self.rental_list:
            opinion = Oceny_przejazdu(rent.id_wypozyczenia)
            self.opinion_list.append(opinion)

    def generate_cars(self, n):
        for _ in range(n):
            car = Samochod()
            self.cars_list.append(car)


    def generate_users(self, n):
        for i in range(n):
            uzytkownik = Uzytkownik()
            self.users_list.append(uzytkownik)

    def generate_snapshot_1(self, n):
        self.generate_cars(n)
        self.generate_users(n)
        self.generate_rents(2*n)
        self.generate_opinions()
        self.report_list = generate_zgloszenia(n, self.cars_list)
        self.write_all('bulks')
        write_reports('zgloszenia1.csv', self.report_list)



    def generate_snapshot_2(self, n):
        num_of_users = random.randint(0, n)
        for _ in range(num_of_users):
            i = random.randint(0, n-1)
            change = random.choice(['imie', 'nazwisko', 'adres'])
            if change == 'imie':
                self.users_list[i].imie = names.get_first_name()
            elif change == 'nazwisko':
                self.users_list[i].nazwisko = names.get_last_name()
            else:
                self.users_list[i].miasto_zamieszkania = create_city().get('name')

        self.generate_cars(n)
        self.generate_users(n)
        self.generate_rents(3*n)
        self.generate_opinions()
        new_reports = generate_zgloszenia(n, self.cars_list)
        self.report_list.extend(new_reports)
        self.write_all('bulks2')
        write_reports('zgloszenia2.csv', self.report_list)


