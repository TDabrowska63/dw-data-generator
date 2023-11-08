from generate_csv.zgloszenia import Zgloszenia

def generate_zgloszenia(num_of_records:int):
    with open('./generate_csv/zgloszenia.csv', 'w' , encoding="utf-8") as file:
        file.write("id_pracownika;data_wpisu;godzina_wpisu;imie;nazwisko;nr_telefonu;id_zgloszenia;zglaszany_numer_rejestracyjny;powod;potwierdzone\n")
        for i in range(num_of_records):
            zgloszenie = Zgloszenia(i)
            file.write(str(zgloszenie))