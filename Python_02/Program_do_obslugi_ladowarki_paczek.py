print("Witaj w programie do obsługi ładowarki paczek.\n")

liczba_elementow = int(input("Podaj ilość elementów wysłania: "))
suma_wszystkich_kilogramow = 0
waga_paczki = 0
ilosc_paczek = 1
suma_pustych_kilogramow = 0
paczka_z_najwieksza_iloscia_pustych_kg = 1
najwecej_pustych_kg = 0

for element in range(liczba_elementow):
    waga_elementu = float(input("Podaj wagę elementu (1-10kg): "))
    #suma_wszystkich_kilogramow += waga_elementu
    if float(waga_elementu) == 0:
        #print("\nZakończono pakowanie.")
        break
    # if not int(waga_elementu) in range(0, 11):
    elif waga_elementu < 1 or waga_elementu > 10:
        print("\nBłąd: Nieprawidłowa waga elementu!\n")
        continue

    suma_wszystkich_kilogramow += waga_elementu

    if waga_elementu + waga_paczki <= 20:
        waga_paczki += waga_elementu
    else:
        suma_pustych_kilogramow += (20 - waga_paczki)
        puste_kg_w_tej_paczce = 20 - waga_paczki
        if puste_kg_w_tej_paczce > najwecej_pustych_kg:
            paczka_z_najwieksza_iloscia_pustych_kg = ilosc_paczek
            najwecej_pustych_kg = puste_kg_w_tej_paczce
        ilosc_paczek += 1
        waga_paczki = waga_elementu
puste_kg_w_ostatniej_paczce = 20 - waga_paczki
suma_pustych_kilogramow += (20 - waga_paczki)
if puste_kg_w_ostatniej_paczce > najwecej_pustych_kg:
    paczka_z_najwieksza_iloscia_pustych_kg = ilosc_paczek
    najwecej_pustych_kg = puste_kg_w_ostatniej_paczce

print("\nZakończono pakowanie.")
print(f"Liczba paczek wysłanych: {ilosc_paczek}")
print(f"Liczba kg wysłanych: {round(suma_wszystkich_kilogramow, 1)}")
print(f"Liczba pustych kg w paczkach to: {round(suma_pustych_kilogramow, 1)}")
print(f"Najwięcej pustych kg było w paczce {round(paczka_z_najwieksza_iloscia_pustych_kg, 1)}, "
      f"było to: {round(najwecej_pustych_kg, 1)}")