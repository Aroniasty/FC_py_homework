import sys

'''
uruchamianie
python accountant.py saldo 1000 "dodano 1000 zl do konta"
'''
saldo = 10000
magazyn = [
    {
        "id": 1,
        "nazwa": "lodka",
        "ilosc": 5,
        "cena jednostkowa": 1000
    },
    {
        "id": 2,
        "nazwa": "auto",
        "ilosc": 4,
        "cena jednostkowa": 500
    }
]

historia = ["Utworzylem magazyn", "Zakupilem 1 lodke za 1000 zl", "Kupilem auto za 500 zl", "Sprzedalem 2 auta za 1000 zl"]
print(len(magazyn))
argumenty = sys.argv
for index, wartosc in enumerate(argumenty):
    if index == 1:
        operacja = wartosc

#skorzystac z instrukcji warunkowych

if operacja == "saldo":         # <int wartosc> <str komentarz>
    saldo += int(sys.argv[2])
    historia.append(sys.argv[3])
elif operacja == "sprzedaż":    # <str identyfikator produktu> <int cena> <int liczba sprzedanych>
    print(f"brak funkcji")
    pass
elif operacja == "zakup":       # <str identyfikator produktu> <int cena> <int liczba zakupionych>
    print(f"brak funkcji")
    pass
elif operacja == "konto":       #
    print(f"brak funkcji")
    pass
elif operacja == "magazyn":     # <str identyfikator produktu 1> <str identyfikator produktu 2> <str identyfikator produktu 3> ...
    print(f"brak funkcji")
    pass
elif operacja == "przegląd":    # <indeks początkowy> <indeks końcowy>
    print(historia[0:3])
print(saldo)
