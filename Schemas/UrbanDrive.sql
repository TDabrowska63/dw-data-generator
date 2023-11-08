--CREATE DATABASE UrbanDrive


use UrbanDrive

CREATE TABLE Miejsca
(
ID_Miejsca INT IDENTITY(1,1) PRIMARY KEY,
Wspolrzedne VARCHAR(100) NOT NULL,
Nazwa_miasta VARCHAR(20) NOT NULL,
Czy_miejsce_dedykowane CHAR(1) NOT NULL CHECK(Czy_miejsce_dedykowane in ('Y', 'N'))
)

CREATE TABLE Samochody
(
Nr_rejestracyjny CHAR(7) PRIMARY KEY,
Marka VARCHAR(20) NOT NULL,
Typ CHAR(20) NOT NULL CHECK (Typ in ('Osobowy', 'Dostawczy'))
)

CREATE TABLE Uzytkownicy
(
Nr_prawa_jazdy CHAR(13) PRIMARY KEY,
Imie VARCHAR(20) NOT NULL,
Nazwisko VARCHAR(20) NOT NULL,
Miasto_zamieszkania VARCHAR(20) NOT NULL,
)

CREATE TABLE Wypozyczenia
(
ID_wypozyczenia INT IDENTITY(1,1) PRIMARY KEY,
Typ CHAR NOT NULL CHECK(Typ in ('calodobowy', 'nieograniczony')),
Czas_rozpoczecia DATE NOT NULL,
Czas_zakonczenia DATE DEFAULT NULL,
Przebieg INT,
Poziom_paliwa INT CHECK(Poziom_paliwa >=0 AND Poziom_paliwa<=100),
ID_samochodu CHAR(7),
ID_Osoby CHAR(13),
ID_Miejsca_rozpoczecia INT,
ID_Miejsca_zakonczenia INT,

FOREIGN KEY (ID_samochodu) REFERENCES Samochody(Nr_rejestracyjny),
FOREIGN KEY (ID_Osoby) REFERENCES Uzytkownicy(Nr_prawa_jazdy),
FOREIGN KEY (ID_Miejsca_rozpoczecia) REFERENCES Miejsca(ID_Miejsca),
FOREIGN KEY (ID_Miejsca_zakonczenia) REFERENCES Miejsca(ID_Miejsca)
)

CREATE TABLE OcenyPrzejazdu
(
ID_wypozyczenia INT PRIMARY KEY,
Ocena_predkosci FLOAT CHECK(Ocena_predkosci >= 0 AND Ocena_predkosci <= 5),
Ocena_techniki_jazdy FLOAT CHECK(Ocena_techniki_jazdy >= 0 AND Ocena_techniki_jazdy <= 5),
Ocena_uzytkownika FLOAT CHECK(Ocena_uzytkownika >= 0 AND Ocena_uzytkownika <= 5),
Powod INT CHECK(Powod >= 0 AND Powod <= 27),

FOREIGN KEY (ID_wypozyczenia) REFERENCES Wypozyczenia(ID_wypozyczenia)
)


select * from Miejsca
select * from Wypozyczenia
select * from Uzytkownicy
select * from OcenyPrzejazdu
select * from Samochody

/*
drop database UrbanDrive

*/