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
    },
    {
        "id": 3,
        "nazwa": "motor",
        "ilosc": 1,
        "cena jednostkowa": 250
    }
]

historia = ["Utworzylem magazyn", "Zakupilem 1 lodke za 1000 zl", "Kupilem auto za 500 zl", "Sprzedalem 2 auta za 1000 zl"]
print(f"Konto: {len(magazyn)}")
argumenty = sys.argv
for index, wartosc in enumerate(argumenty):
    if index == 1:
        operacja = wartosc

if operacja == "saldo":         # <int wartosc> <str komentarz>
    saldo += int(sys.argv[2])
    historia.append(sys.argv[3])

#wprowadzić sprzedaż
elif operacja == "sprzedaż":    # <str identyfikator produktu> <int cena> <int liczba sprzedanych>
    kwota_sprzedazy = int(sys.argv[3]) * int(sys.argv[4])
    id_produktu = int(sys.argv[2])
    for przedmiot in magazyn:
        if id_produktu == przedmiot.get("id"):
            if int(sys.argv[4]) <= przedmiot["ilosc"]:
                przedmiot["ilosc"] -= int(sys.argv[4])
                saldo += kwota_sprzedazy
            else:
                print(f"Niestety nie masz takiej ilości przedmiotów.\n")
    print(f"Stan magazynu: {magazyn}")

elif operacja == "zakup":       # <str identyfikator produktu> <int cena> <int liczba zakupionych> jak dodać do listy w obecnej formie
    kwota_zakupu = int(sys.argv[3]) * int(sys.argv[4])
    id_produktu = int(sys.argv[2])
    if saldo - kwota_zakupu >= 0:
        saldo -= kwota_zakupu
        for przedmiot in magazyn:
            if id_produktu == przedmiot.get("id"):
                przedmiot["ilosc"] += int(sys.argv[4])
        print(magazyn)
    else:
        print(f"Niestety nie masz środków na zakup.\n")
elif operacja == "konto":
    print(saldo)
elif operacja == "magazyn":     # <str identyfikator produktu 1> <str identyfikator produktu 2> <str identyfikator produktu 3> ...
    idetyfikatory_produktow = sys.argv[2:]
    for przedmiot in magazyn:
        if str(przedmiot.get("id")) in idetyfikatory_produktow:
            print(f"{przedmiot.get('id')}: {przedmiot.get('ilosc')}")
    pass
elif operacja == "przegląd":    # <indeks początkowy> <indeks końcowy>
    print(historia[int(sys.argv[2]):int(sys.argv[3])])
else:
    print(f"Błąd. Brak funkcji")

print(f"Obecne saldo wynosi: {saldo}")
