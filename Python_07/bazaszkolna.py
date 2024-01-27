import sys

argumenty = sys.argv[1:]
koniec_programu = False
print("Witaj w naszej szkole, podaj opcję jaką chcesz wykonać.")

lista_uczniow = []
lista_nauczycieli = []
lista_wychowawcow = []
lista_przedmiotow = []


def znajdz_nauczycielach_w_klasach_nauczycieli(dane_uzytkownika):
    lista_nauczycieli = []
    lista_wychowawcow_klasy = []
    lista_klas = []
    klasy_wychowawcy = []

    for nauczyciel in lista_nauczycieli:
        if nauczyciel.imie == imie and nauczyciel.nazwisko == nazwisko:
            lista_klas

    for wychowawca in lista_wychowawcow:
        if wychowawca.imie == imie and wychowawca.nazwisko == nazwisko:
            klasy_wychowawcy = wychowawca.klasy

    print(argumenty)
    print("wypisz wychowawców wszystkich klas, z którym ma zajęcia nauczyciel")

def znajdz_wychowawce_i_uczniow_w_klasie(numer_klasy):
    lista_uczniow_w_klasie = []
    lista_wychowawcow_klasy = []
    for uczen in lista_uczniow:
        if uczen.klasa == numer_klasy:
            lista_uczniow_w_klasie.append(uczen)
    for wychowawca in lista_wychowawcow:
        if numer_klasy in wychowawca.klasy:
            lista_wychowawcow_klasy.append(wychowawca)
    print(f"Uczniowie: {lista_uczniow_w_klasie}, wychowawca: {lista_wychowawcow_klasy}")

def znajdz_uczniow_wychowawcy(imie, nazwisko):
    klasy_wychowawcy = []
    lista_uczniow_w_klasie = []
    for wychowawca in lista_wychowawcow:
        if wychowawca.imie == imie and wychowawca.nazwisko == nazwisko:
            klasy_wychowawcy = wychowawca.klasy
    for uczen in lista_uczniow:
        if uczen.klasa in klasy_wychowawcy:
            lista_uczniow_w_klasie.append(uczen)
    print(f"Uczniowie wychowawcy {lista_uczniow_w_klasie}")

class Uczen:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa

    def __repr__(self):
        return f"{self.imie}, {self.nazwisko}, {self.klasa}"

class Nauczyciel:
    def __init__(self, imie, nazwisko, klasy, przedmiot):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasy = klasy
        self.przedmiot = przedmiot

class Wychowawca:
    def __init__(self, imie, nazwisko, klasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasy = klasy


while not koniec_programu:
    wybrana_opcja = input("1. Dodaj ucznia\n2. Dodaj nauczyciela\n3. Dodaj wychowawcę\n4. Koniec\n")

    if wybrana_opcja == "1":
        imie_input = input("Podaj imię ucznia: ")
        nazwisko_input = input("Podaj nazwisko ucznia: ")
        klasa_input = input("Podaj klasę ucznia: ")
        nowy_uczen = Uczen(imie=imie_input, nazwisko=nazwisko_input, klasa=klasa_input)
        lista_uczniow.append(nowy_uczen)

    elif wybrana_opcja == "2":
        print("Dodajemy nauczyciela") #nazwę przedmiotu prowadzonego, nazwy klas
        pusty_input = False
        imie_input = input("Podaj imię nauczyciela: ")
        nazwisko_input = input("Podaj nazwisko nauczyciela: ")
        klasy_nauczyciela=[]
        przedmiot_input = input("Podaj przedmiot: ")
        while not pusty_input:
            numer_klasy = input("Podaj kolejna klasę: ")
            if numer_klasy == "":
                pusty_input = True
            else:
                klasy_nauczyciela.append(numer_klasy)
        nowy_nauczyciel = Nauczyciel(imie=imie_input, nazwisko=nazwisko_input,
                                     przedmiot=przedmiot_input, klasy=klasy_nauczyciela)
        lista_nauczycieli.append(nowy_nauczyciel)
    elif wybrana_opcja == "3":      #dodać wychowawcę
        klasy_wychowawcy = []
        pusty_input = False
        imie_input = input("Podaj imię wychowawcy: ")
        nazwisko_input = input("Podaj nazwisko wychowawcy: ")
        while not pusty_input:
            numer_klasy = input("Podaj kolejna klasę: ")
            if numer_klasy == "":
                pusty_input = True
            else:
                klasy_wychowawcy.append(numer_klasy)
        nowy_wychowawca = Wychowawca(imie=imie_input, nazwisko=nazwisko_input, klasy=klasy_wychowawcy)
        lista_wychowawcow.append(nowy_wychowawca)

    elif wybrana_opcja == "4":
        print("koniec - wykonujemy operacje z argumentów systemowych")
        print(argumenty)
        rodzaj_operacji = argumenty[0]
        if rodzaj_operacji == "klasy":
            znajdz_wychowawce_i_uczniow_w_klasie(argumenty[1])
        elif rodzaj_operacji == "wychowawca":
            znajdz_uczniow_wychowawcy(argumenty[1],argumenty[2])
        # znajdz_uzytkownika_w_nauczycielach(dane_uzytkownika)
        koniec_programu = True

