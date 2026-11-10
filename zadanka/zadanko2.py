from pathlib import Path

imiona = []
srednie = []

with open(Path(__file__).with_name("plik.txt"), encoding="utf-8-sig") as plik:
    next(plik)

    for linia in plik:
        dane = linia.strip().split(". ", 1)[1]
        imie, srednia = dane.rsplit(" ", 1)

        imiona.append(imie.strip(" ,"))
        srednie.append(float(srednia.replace(",", ".")))

for imie, srednia in zip(imiona, srednie):
    print(f"{imie} średnia: {srednia:.2f}".replace(".", ","))

srednia_klasy = sum(srednie) / len(srednie)
print(f"Średnia klasy: {srednia_klasy:.2f}".replace(".", ","))