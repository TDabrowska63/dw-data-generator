import random
from tools import create_license_plate_num


class Samochod:

    def __init__(self):
        self.nr_rejestracyjny = create_license_plate_num()
        self.marka =  random.choice(["Reno", "Dacia", "Tesla", "Audi"])
        self.typ = random.choice(["Osobowy", "Dostawczy"])


    def __str__(self):
        return f"{str(self.nr_rejestracyjny)}|" \
               f"{str(self.marka)}|" \
               f"{str(self.typ)}\n"
