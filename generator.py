from tables.samochody import Samochod
from tables.uzytkownicy import Uzytkownik
from tables.wypozyczenia import Wypozyczenie


class Generator:
    def __init__(self):
        samochod = Samochod()
        uzytkownik = Uzytkownik()
        wypozyczenie = Wypozyczenie(1, 300)
        print(samochod)
        print(uzytkownik)
        print(wypozyczenie)

