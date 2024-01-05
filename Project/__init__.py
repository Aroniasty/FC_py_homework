'''
Porównanie kosztów życia w różnych stanach USA (Flask/CLI).
Aplikacja używa bazy danych z tabeli:
https://www.kaggle.com/code/eugeniokukes/us-cost-of-living
Użytkownik wybiera stan - Texas, Florida, California, New York, Illinois
Aplikacja zwraca:
- Średni koszt życia w wybranym stanie
- 3 miasta o najwyższych kosztach życia w danym stanie
- O ile procent powyżej średniej wynoszą koszty życia w tych miastach w porównaniu do średnich kosztów życia w danym stanie
- Rekomendacja, w którym mieście jest najbardziej ekonomiczne miejsce do zamieszkania, biorąc pod uwagę koszt życia.

Wymagania:
Flask
Bazadanych SQLite
HTML/CSS do napisania templatek

1. Stworzenie tabeli odzwierciedlającej, to co mamy w pliku csv
2. W app context zrobienie db.creata_all() i załadowanie wszystkich danych z pliku
3. Stworzenie endpointow

'''