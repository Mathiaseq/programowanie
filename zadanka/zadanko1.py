from pathlib import Path

suma = 0
liczba_uczniow = 0

with open(Path(__file__).with_name("plik.txt"), encoding="utf-8") as plik:
    next(plik)  # pomiń nagłówek
    for linia in plik:
        dane = linia.strip().split(". ", 1)[1]
        imie, srednia = dane.rsplit(" ", 1)
        srednia = srednia.replace(",", ".")

        print(imie.rstrip(","), srednia.replace(".", ","))
        suma += float(srednia)
        liczba_uczniow += 1

print("Średnia całej klasy:", round(suma / liczba_uczniow, 2))
