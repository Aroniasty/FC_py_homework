# Program do generowania życzeń urodzinowych
import datetime

print("Program do generowania życzeń urodzinowych\n")

imie_odbiorcy = input("Podaj imię odbiorcy: ")
rok_urodzenia_uzytkownika = input("Podaj rok urodzenia: ")
rok_urodzenia_uzytkownika_jako_liczba = int(rok_urodzenia_uzytkownika)
spersonalizowana_wiadomosc = input("Podaj spersonalizowaną wiadomość: ")
imie_nadawcy = input("Podaj imię nadawcy: ")

obecna_data = datetime.date.today()
obecny_rok = obecna_data.year
# print(obecna_data)
# print(obecny_rok)

wiek_odbiorcy = (obecny_rok - rok_urodzenia_uzytkownika_jako_liczba)
# print(wiek_odbiorcy)

print(f"\n{imie_odbiorcy}, Wszystkiego najlepszego z okazji ukończenia: {wiek_odbiorcy} lat\n")
print(f"{spersonalizowana_wiadomosc}\n")
print(f"{imie_nadawcy}")
