import random
class Oceny_przejazdu:
    def __init__(self, Id_wypozyczenia):
        self.Id_wypozyczenia = Id_wypozyczenia
        self.Ocena_predkosci = random.uniform(0, 5)
        self.Ocena_techniki_jazdy = random.uniform(0, 5)
        self.Ocena_uzytkownika = random.uniform(0, 5)
        if self.Ocena_uzytkownika < 3:
            self.Powod = random.randint(1, 27)
        else:
            self.Powod = 0

    def __str__(self):
        return str(self.Id_wypozyczenia) \
            + ";" + str(self.Ocena_predkosci) \
            + ";" + str(self.Ocena_techniki_jazdy) \
            + ";" + str(self.Ocena_uzytkownika) \
            + ";" + str(self.Powod) + "\n"