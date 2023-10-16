# Napisz program do obsługi ładowarki paczek.
# Każda paczka może maksymalnie zmieścić 20 kg towaru. Do paczki dodawane są elementy.
# Każdy z nich może ważyć od 1 do 10 kg.
# Jeśli dodanie elementu do paczki zwiększyłoby ciężar paczki powyżej 20kg, paczka powinna zostać wysłana (nie można już do niej dodać w przyszłości elementów), a bieżący element powinien zostać dodany do nowej paczki.
# Wszystkie elementy powinny zostać wysłane.
# Program powinien pobierać maksymalną liczbę elementów do wysyłki.
# Jeśli podano element o wadze 0, program powinien zakończyć działanie, tak jakby maksymalna liczba elementów została osiągnięta.
# Na koniec działania program powinien wyświetlić w podsumowaniu:
#    - Liczbę paczek wysłanych
#    - Liczbę kilogramów wysłanych
#    - Suma "pustych" - kilogramów (brak optymalnego pakowania). Liczba paczek * 20 - liczba kilogramów wysłanych
#    - Która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik
# Program powinien kończyć się z błędem, gdy element dodawany ma więcej niż 10kg, lub mniej niż 1 kg i nie był dokładnie równy 0.

print("Witaj w programie do obsługi ładowarki paczek.\n")

koniec_programu = False

limit_wagi_paczki = 20 # <=20kg
licznik_paczek = 0
waga_paczki = 0 # <=20kg
licznik_elementow = 0
licznik_kg = 0
licznik_pustch_kg = 0
najciezsza_paczka = 0
paczka_01 = False
paczka_02 = False
paczka_03 = False
paczka_04 = False
paczka_05 = False
paczka_06 = False
paczka_07 = False
paczka_08 = False
paczka_09 = False
paczka_10 = False


while not koniec_programu:
    print("Podaj co chcesz zrobić.\n"
          "1. Dodaj element do paczki.\n"
          "2. Zakończ program i wyświetl podsumowanie.")
    wybor_menu = input("Wybierz opcje: ")
    if int(wybor_menu) == 1:
        while int(waga_paczki) <= 20:  # ustawić nieprzekraczalny limit
            waga_elementu = input("Podaj wagę elementu (1-10kg): ")
            if int(waga_elementu) == 0:
                print("Zakończono pakowanie.")
                break
            if not int(waga_elementu) in range (1,11):
                print("Nieprawidłowa waga elmentu.")
                continue
            waga_paczki += int(waga_elementu)
            print(f"Całkowita waga paczki: {waga_paczki} kg")
        else: #if int(waga_paczki) == 20:
            print("Osiągnięto limit wagi paczki")
            break
# program wychodzi do opcji i nie można już dodawać elementów do paczki.

    elif int(wybor_menu) == 2:
        koniec_programu = True
print("Program zakończył działanie.\nPodsumowanie: ")
#print(f" - Liczba wysłanych paczek: {licznik_paczek} szt.")
print(f" - Całkowita waga paczek: {waga_paczki} kg")
#print(f" - Niewykorzystane: {licznik_pustch_kg} kg")
#print(f" - Najcięższa paczka: {najciezsza_paczka} kg")
