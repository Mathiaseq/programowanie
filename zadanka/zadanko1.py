from pathlib import Path
import matplotlib.pyplot as plt

imiona = []
oceny = []
with open(Path(__file__).with_name("plik.txt"), encoding="utf-8") as plik:
    next(plik)
    for linia in plik:
        imie, ocena = linia.strip().split(". ", 1)[1].rsplit(" ", 1)
        ocena = float(ocena.replace(",", "."))
        imiona.append(imie.strip(","))
        oceny.append(ocena)

srednia_klasy = sum(oceny) / len(oceny)
plt.bar(imiona, oceny)
plt.axhline(srednia_klasy, color="red", label=f"Średnia klasy: {srednia_klasy:.2f}")
plt.ylabel("Średnia ocen")
plt.legend()
plt.show()
