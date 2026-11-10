suma = 0
liczba = 0

with open("plik.txt", encoding="utf-8") as plik:
    next(plik)
    for linia in plik:
        imie, ocena = linia.strip().split(". ", 1)[1].rsplit(" ", 1)
        ocena = float(ocena.replace(",", "."))
        print(imie.strip(","), ocena)
        suma += ocena
        liczba += 1

print("Średnia klasy:", round(suma / liczba, 2))
