import sys

argumenty = sys.argv[1:]
koniec_programu = False
print("Witaj w naszej szkole, podaj opcję jaką chcesz wykonać.")

lista_uczniow = []
lista_nauczycieli = []
lista_wychowawcow = []


def znajdz_uzytkownika_w_nauczycielach(dane_uzytkownika):
    print(argumenty)
    print("Kod do znalezienia danych z argumentów systemowych wśród uczniów")

class Uczen:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = klasa

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
        while not pusty_input:
            numer_klasy = input("Podaj kolejna klasę")
            imie_input = input("Podaj imię nauczyciela: ")
            nazwisko_input = input("Podaj nazwisko nauczyciela: ")
            przedmiot_input = input("Podaj przedmiot: ")
            if numer_klasy == "":
                pusty_input = True

    elif wybrana_opcja == "3":      #dodać wychowawcę
        print("Dodajemy wychowawcę") #nazwy klas
        pusty_input = False
        while not pusty_input:
            numer_klasy = input("Podaj kolejna klasę: ")
            imie_input = input("Podaj imię nauczyciela: ")
            nazwisko_input = input("Podaj nazwisko nauczyciela: ")
            if numer_klasy == "":
                pusty_input = True

    elif wybrana_opcja == "4":
        print("koniec - wykonujemy operacje z argumentów systemowych")
        print(argumenty)
        dane_uzytkownika = argumenty[0]
        znajdz_uzytkownika_w_nauczycielach(dane_uzytkownika)
        koniec_programu = True

