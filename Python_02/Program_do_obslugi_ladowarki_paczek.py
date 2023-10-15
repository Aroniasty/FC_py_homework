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



while waga_paczki <= limit_wagi_paczki:
    print("Podaj wagę elementu (1-10kg): ")
    waga_elementu = int(input())
    if waga_elementu == 0:
        print("Program zakończył działanie.\nOto Twoje zamówienie: ")
        print(f" - Liczba wysłanych paczek: {licznik_paczek} szt.")
        print(f" - Całkowita waga paczek: {licznik_kg} kg")
        print(f" - Niewykorzystane: {licznik_pustch_kg} kg")
        print(f" - Najcięższa paczka: {najciezsza_paczka} kg")
        break
    if waga_elementu < 1 or waga_elementu > 10:
        print("Nieprawidłowa waga elmentu.")
        continue
    waga_paczki += waga_elementu
    print(f"Całkowita waga paczki: {waga_paczki} kg")
else:
    print("Limit wagi paczki osiągnięty.")
