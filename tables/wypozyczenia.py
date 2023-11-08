import random
from random import randrange
from datetime import datetime, timedelta
import tools

class Wypozyczenie:
    def __init__(self, id, przebieg):
         self.id_wypozyczenia = id
         self.typ = random.choice(['calodobowy', 'nieograniczony'])
         self.czas_wypozyczenia, self.czas_zakonczenia = self.create_rental_time()
         self.przebieg = przebieg
         self.poziom_paliwa = str(random.randint(0, 100))

    def create_rental_time(self):
        d1 = datetime.strptime('1/1/2019 1:30 PM', '%m/%d/%Y %I:%M %p')
        d2 = datetime.now()
        start_time = tools.random_date(d1, d2)
        end_time = start_time + timedelta(hours=random.randint(1, 24)) + timedelta(minutes=random.randint(0, 59)) + timedelta(seconds=random.randint(0, 59))

        return start_time, end_time

    def __str__(self):
        return str(self.id_wypozyczenia) \
            + ";" + str(self.typ) \
            + ";" + str(self.czas_wypozyczenia) \
            + ";" + str(self.czas_zakonczenia) \
            + ";" + str(self.przebieg) \
            + ";" + str(self.poziom_paliwa) + "\n"