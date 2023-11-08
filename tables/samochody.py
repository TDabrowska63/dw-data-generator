import random

class Samochod:

    def __init__(self):
        self.nr_rejestracyjny = "G"
        self.marka =  random.choice(["Reno", "Dacia", "Tesla", "Audi"])
        self.typ = random.choice(["Osobowy", "Dostawczy"])
        self.create_license_plate_num()

    def create_license_plate_num(self):
        option = random.choice(["2_digit_region", "3_digit_region"])
        if option == "2_digit_region":
            self.nr_rejestracyjny += random.choice('DAS')
        elif option == "3_digit_region":
            self.nr_rejestracyjny += random.choice(["SP", "BY", "CH", "CZ", "DA", "KA", "KS", "KW", "LE", "MB", "ND"])
        self.nr_rejestracyjny += " "
        for _ in range(5):
            self.nr_rejestracyjny += random.choice('ACEFGHJKLMNPRSTUWXYZ0123456789')

    def __str__(self):
        return f"{str(self.nr_rejestracyjny)}|" \
               f"{str(self.marka)}|" \
               f"{str(self.typ)}\n"
