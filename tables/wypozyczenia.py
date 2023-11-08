import random
from random import randrange
from datetime import datetime, timedelta
import tools

class Wypozyczenie:
    def __init__(self, id, przebieg, nr_rejestracyjny_samochodu, nr_prawa_jazdy, id_miejsca_rozpoczecia, id_miejsca_zakonczenia):
        self.id_wypozyczenia = id
        self.typ = random.choice(['calodobowy', 'nieograniczony'])
        self.czas_wypozyczenia, self.czas_zakonczenia = self.create_rental_time()
        self.przebieg = przebieg
        self.poziom_paliwa = str(random.randint(0, 100))
        self.nr_rejestracyjny_samochodu = nr_rejestracyjny_samochodu
        self.nr_prawa_jazdy = nr_prawa_jazdy
        self.id_miejsca_rozpoczecia = id_miejsca_rozpoczecia
        self.id_miejsca_zakonczenia = id_miejsca_zakonczenia



    def create_rental_time(self):
        d1 = datetime.strptime('1/1/2019 1:30 PM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.now()
        start_time = tools.random_date(d1, d2)
        end_time = start_time + timedelta(hours=random.randint(1, 24)) + timedelta(minutes=random.randint(0, 59)) + timedelta(seconds=random.randint(0, 59))

        return start_time, end_time

    def __str__(self):
        return f"{str(self.id_wypozyczenia)}|" \
               f"{str(self.typ)}|" \
               f"{str(self.czas_wypozyczenia)}|" \
               f"{str(self.czas_zakonczenia)}|" \
               f"{str(self.przebieg)}|" \
               f"{str(self.poziom_paliwa)}|" \
               f"{str(self.nr_rejestracyjny_samochodu)}|" \
               f"{str(self.nr_prawa_jazdy)}|" \
               f"{str(self.id_miejsca_rozpoczecia)}|" \
               f"{str(self.id_miejsca_zakonczenia)}\n"
