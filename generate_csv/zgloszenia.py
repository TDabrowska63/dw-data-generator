import random
import names

class Zgloszenia:
    def init(self, Id_zgloszenia):
        self.Zglaszany_nr_rejestracyjny = None
        self.Nr_telefonu = None
        self.Godzina_wpisu = None
        self.Data_wpisu = None
        self.Id_zgloszenia = Id_zgloszenia
        self.ID_Pracownika = str(random.randint(0, 1000))
        self.Imie = names.get_first_name()
        self.Nazwisko = names.get_last_name()
        self.create_telephone_number()
        self.create_car()       #placeholder
        self.Powod = str(random.randint(0, 27))
        self.Potwierdzone = str(random.randint(0, 1))

    def create_telephonenumber(self):
        for _ in range(9):
            self.Nr_telefonu += str(random.randint(0, 9))

    def createcar(self):
        for _ in range(9):
            self.Zglaszany_nr_rejestracyjny += str(random.randint(0, 9))

    def create_entry_time(self):
        self.Godzina_wpisu = self.fill_with_zero(1, 12) + ':' + self.fill_with_zero(0, 60)

    def create_entry_date(self):
        self.Data_wpisu = str(random.randint(2019, 2024)) \
                          + '-' + self.fill_with_zero(1, 12)\
                          + '-' + self.fill_with_zero(1, 31)

    def fill_with_zero(self, start, end):
        num = random.randint(start, end)
        if num < 10:
            string = '0' + str(num)
        else:
            string = str(num)

        return string
    def str(self):
        return str(self.ID_Pracownika) \
            + ";" + str(self.Data_wpisu) \
            + ";" + str(self.Godzina_wpisu) \
            + ";" + str(self.Imie) \
            + ";" + str(self.Nazwisko) \
            + ";" + str(self.Nr_telefonu) \
            + ";" + str(self.Id_zgloszenia) \
            + ";" + str(self.Zglaszany_nr_rejestracyjny) \
            + ";" + str(self.Powod) \
            + ";" + str(self.Potwierdzone)