from generate_csv.zgloszenia import Zgloszenia

def generate_zgloszenia(num_of_records:int):
    with open('./generate_csv/zgloszenia.csv', 'w' , encoding="utf-8") as file:
        file.write("Id_pracownika;Data_wpisu;Godzina_wpisu;Imie;Nazwisko;Nr_telefonu;Id_Zgloszenia;Zglaszany_numer_rejestracyjny;Powod;Potwierdzone\n")
        for i in range(num_of_records):
            zgloszenie = Zgloszenia(i)
            file.write(str(zgloszenie))