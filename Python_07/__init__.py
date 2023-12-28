'''
Program do obsługi bazy szkolnej
Mamy trzy typy użytkowników:

    Wychowawca - ma przypisane klasy
    Nauczyciel - Mentor ma przypisany jeden przedmiot i wiele klas
    Uczeń - jest przypisany do jednej klasy


Napisz program, który ze standardowego wyjścia pobierze dane w następujący sposób:

    Pobierze typ użytkownika: (uczeń, nauczyciel, wychowawca, koniec) Jeśli pobrano koniec,
    przejdź do kroku 5, w przeciwnym przypadku pobierz imię i nazwisko i przejdź do kroku 2,3, lub 4 (w zależności od pobranego typu użytkownika)
    Jeśli typ użytkownika to uczeń, pobierz jedną linię - będzie to nazwa klasy (np. 3C), przejdź do kroku 1
    Jeśli typ użytkownika to nauczyciel, pobierz 1 linię - nazwę przedmiotu prowadzonego, a następnie w nowych liniach nazwy klas, aż do otrzymania pustej linii. Przejdź do korku 1
    Jeśli typ użytkownika to wychowawca, pobieraj w nowych liniach nazwy klas, które prowadzi wychowawca, aż do momentu gdy użytkownik wprowadzi pustą linię, przejdź do kroku 1
    Wykonaj polecenie na podstawie przekazanego argumentu


Program będzie wykonywany w następujący sposób (zakładając nazwę pliku bazaszkolna.py)
python bazaszkolna.py <phrase>
jeśli phrase to nazwa klasy: program wypisze wychowawcę i uczniów w klasie
jeśli phrase to wychowawca: wypisz wszystkich uczniów, których prowadzi wychowawca
jeśli phrase to nauczyciel: wypisz wychowawców wszystkich klas, z którym ma zajęcia nauczyciel
jeśli phrase to uczeń: wypisz wszystkie lekcje, które ma uczeń i nauczycieli, którzy je prowadzą
'''