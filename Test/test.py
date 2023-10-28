# #print("Hello World")
# #
# # limit_wagi_paczki = 20 # <=20kg
# # licznik_paczek = 0
# # waga_paczki = 0 # <=20kg
# # licznik_elementow = 0
# # licznik_kg = 0
# # licznik_pustch_kg = 0
# # najciezsza_paczka = 0
# # paczka_01 = False
# # paczka_02 = False
# # paczka_03 = False
# # paczka_04 = False
# # paczka_05 = False
# # paczka_06 = False
# # paczka_07 = False
# # paczka_08 = False
# # paczka_09 = False
# # paczka_10 = False
# #
# # while waga_paczki <= limit_wagi_paczki:
# #     print("Podaj wagę elementu (1-10kg): ")
# #     waga_elementu = int(input())
# #     if waga_elementu == 0:
# #         print("Program zakończył działanie.\nPodsumowanie: ")
# #         print(f" - Liczba wysłanych paczek: {licznik_paczek} szt.")
# #         print(f" - Całkowita waga paczek: {licznik_kg} kg")
# #         print(f" - Niewykorzystane: {licznik_pustch_kg} kg")
# #         print(f" - Najcięższa paczka: {najciezsza_paczka} kg")
# #         break
# #     if waga_elementu < 1 or waga_elementu > 10:
# #         print("Nieprawidłowa waga elmentu.")
# #         continue
# #     waga_paczki += waga_elementu
# #     print(f"Całkowita waga paczki: {waga_paczki} kg")
# # else:
# #     print("Limit wagi paczki osiągnięty.")
#
#
# print("Witaj w programie do obsługi ładowarki paczek.\n")
#
# wagi_paczek = [] #lista przechowuje zmienne/wartosci
# print (wagi_paczek)
# wagi_paczek.append(3)
# wagi_paczek.append(4)
# wagi_paczek.append(5)
# wagi_paczek.append(6)
# print(wagi_paczek)
# print(wagi_paczek[0])
# print(min(wagi_paczek))
#
# koniec_programu = False
#
# limit_wagi_paczki = 20 # <=20kg
# licznik_paczek = 0
# waga_paczki = 0 # <=20kg
# licznik_elementow = 0
# licznik_kg = 0
# licznik_pustch_kg = 0
# najciezsza_paczka = 0
# paczka_01 = False
# paczka_02 = False
# paczka_03 = False
# paczka_04 = False
# paczka_05 = False
# paczka_06 = False
# paczka_07 = False
# paczka_08 = False
# paczka_09 = False
# paczka_10 = False
#
# while not koniec_programu:
#     print("Podaj co chcesz zrobić.\n"
#           "1. Dodaj element do paczki.\n"
#           "2. Zakończ program i wyświetl podsumowanie.")
#     wybor_menu = input("Wybierz opcje: ")
#     if int(wybor_menu) == 1:
#         while int(waga_paczki) <= 20:  # ustawić nieprzekraczalny limit
#             waga_elementu = input("Podaj wagę elementu (1-10kg): ")
#             if int(waga_elementu) == 0:
#                 print("Zakończono pakowanie.")
#                 break
#             if not int(waga_elementu) in range (1,11):
#                 print("Nieprawidłowa waga elmentu.")
#                 continue
#             if waga_paczki + int(waga_elementu) > 20:
#                 print("Osiągnięto limit wagi paczki")
#                 wagi_paczek.append(waga_paczki)
#                 waga_paczki = waga_elementu
#                 print(wagi_paczek)
#                 break
#             else:
#                 waga_paczki += int(waga_elementu)
#                 print(f"Całkowita waga paczki: {waga_paczki} kg")
#
#         else: #if int(waga_paczki) == 20:
#             print("Osiągnięto limit wagi paczki")
#             break
# # program wychodzi do opcji i nie można już dodawać elementów do paczki.
#
#     # elif int(wybor_menu) == 2:
#     #     koniec_programu = True
# print("Program zakończył działanie.\nPodsumowanie: ")
# #print(f" - Liczba wysłanych paczek: {licznik_paczek} szt.")
# print(f" - Całkowita waga paczek: {waga_paczki} kg")
# #print(f" - Niewykorzystane: {licznik_pustch_kg} kg")
# #print(f" - Najcięższa paczka: {najciezsza_paczka} kg")

