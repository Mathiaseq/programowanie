#zadanie 1.
# def samochod():
#     marka = input("Podaj marke samochodu: ")
#     model = input("Podaj model samochodu: ")
#     print("Twój samochód to:", marka, model)

# samochod()
# samochod()

#zadanie 2.

import math

def f(x):
    return math.sqrt(x**4) + x - 0.5

while True:
    liczba = float(input("Podaj liczbę (lub wpisz 0, aby zakończyć): "))
    if liczba == 0:
        break
    try:
        wynik = f(liczba)
        print("f(", liczba, ") =", wynik)
    except ValueError:
        print("Nie można obliczyć pierwiastka z liczby ujemnej!")

print("Koniec programu.")