from tables.samochody import Samochod
from tables.uzytkownicy import Uzytkownik


class Generator:
    def __init__(self):
        samochod = Samochod()
        uzytkownik = Uzytkownik()
        print(samochod)
        print(uzytkownik)

