import random
import names

class Zgloszenia:
    def __init__(self, Id_zgloszenia):
        self.Id_zgloszenia = Id_zgloszenia
        self.Zglaszany_nr_rejestracyjny = ''
        self.Nr_telefonu = ''
        self.Godzina_wpisu = ''
        self.Data_wpisu = ''
        self.ID_Pracownika = str(random.randint(0, 1000))
        self.Imie = names.get_first_name()
        self.Nazwisko = names.get_last_name()
        self.create_telephone_number()
        self.create_car()       #placeholder
        self.create_entry_date()
        self.create_entry_time()
        self.Powod = str(random.randint(0, 27))
        self.Potwierdzone = str(random.randint(0, 1))

    def create_telephone_number(self):
        for _ in range(9):
            self.Nr_telefonu = self.Nr_telefonu + str(random.randint(0, 9))

    def create_car(self):
        for _ in range(9):
            self.Zglaszany_nr_rejestracyjny += str(random.randint(0, 9))

    def create_entry_time(self):
        hour = self.fill_with_zero(1, 12)
        minute = self.fill_with_zero(0, 60)
        self.Godzina_wpisu = hour + ':' + minute

    def create_entry_date(self):
        day = self.fill_with_zero(1, 31)
        month = self.fill_with_zero(1, 12)
        year = str(random.randint(2019, 2024))
        self.Data_wpisu = year + '-' + month + '-' + day

    def fill_with_zero(self, start, end):
        num = random.randint(start, end)
        if num < 10:
            string = '0' + str(num)
        else:
            string = str(num)

        return string
    def __str__(self):
        return str(self.ID_Pracownika) \
            + ";" + str(self.Data_wpisu) \
            + ";" + str(self.Godzina_wpisu) \
            + ";" + str(self.Imie) \
            + ";" + str(self.Nazwisko) \
            + ";" + str(self.Nr_telefonu) \
            + ";" + str(self.Id_zgloszenia) \
            + ";" + str(self.Zglaszany_nr_rejestracyjny) \
            + ";" + str(self.Powod) \
            + ";" + str(self.Potwierdzone) + "\n"