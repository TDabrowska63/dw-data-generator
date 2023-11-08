import names
import random

class Uzytkownik:
    def __init__(self):
        self.nr_prawa_jazdy = ""
        self.imie = names.get_first_name()
        self.nazwisko = names.get_last_name()
        self.miasto_zamieszkania = ""
        self.create_driving_license_num()


    def create_driving_license_num(self):
        for i in range(13):
            if i == 5 or i == 8:
                self.nr_prawa_jazdy += "/"
            else:
                self.nr_prawa_jazdy += str(random.randint(0,9))

    def __str__(self):
        return str(self.nr_prawa_jazdy) + ";" + str(self.imie) + ";" + str(self.nazwisko) + ";" + str(self.miasto_zamieszkania) + "\n"