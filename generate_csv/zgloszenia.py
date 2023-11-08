import random
import names

class Zgloszenia:
    def __init__(self, id_zgloszenia):
        self.id_zgloszenia = id_zgloszenia
        self.zglaszany_nr_rejestracyjny = ''
        self.nr_telefonu = ''
        self.godzina_wpisu = ''
        self.data_wpisu = ''
        self.id_pracownika = str(random.randint(0, 1000))
        self.imie = names.get_first_name()
        self.nazwisko = names.get_last_name()
        self.create_telephone_number()
        self.create_car()       #placeholder
        self.create_entry_date()
        self.create_entry_time()
        self.powod = str(random.randint(0, 27))
        self.potwierdzone = str(random.randint(0, 1))

    def create_telephone_number(self):
        for _ in range(9):
            self.nr_telefonu = self.nr_telefonu + str(random.randint(0, 9))

    def create_car(self):
        for _ in range(9):
            self.zglaszany_nr_rejestracyjny += str(random.randint(0, 9))

    def create_entry_time(self):
        hour = self.fill_with_zero(1, 12)
        minute = self.fill_with_zero(0, 60)
        self.godzina_wpisu = hour + ':' + minute

    def create_entry_date(self):
        day = self.fill_with_zero(1, 31)
        month = self.fill_with_zero(1, 12)
        year = str(random.randint(2019, 2024))
        self.data_wpisu = year + '-' + month + '-' + day

    def fill_with_zero(self, start, end):
        num = random.randint(start, end)
        if num < 10:
            string = '0' + str(num)
        else:
            string = str(num)

        return string
    def __str__(self):
        return str(self.id_pracownika) \
            + ";" + str(self.data_wpisu) \
            + ";" + str(self.godzina_wpisu) \
            + ";" + str(self.imie) \
            + ";" + str(self.nazwisko) \
            + ";" + str(self.nr_telefonu) \
            + ";" + str(self.id_zgloszenia) \
            + ";" + str(self.zglaszany_nr_rejestracyjny) \
            + ";" + str(self.powod) \
            + ";" + str(self.potwierdzone) + "\n"