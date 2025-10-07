#zadanie 1
def powitanie():
    imie = input("Podaj swoje imię: ")
    nazwisko = input("Podaj swoje nazwisko: ")
    print("Witaj,", imie, nazwisko)
powitanie()
powitanie()
#zadanie 2
import math  
def f(x):
    return math.sqrt(x**2 + 2*x - 1)

while True:
    liczba = float(input("Podaj liczbę (lub wpisz 0, aby zakończyć): "))
    if liczba == 0:
        break
    try:
        wynik = f(liczba)
        print(f"f({liczba}) = {wynik}")
    except ValueError:
        print("Błąd: nie można obliczyć pierwiastka z liczby ujemnej!")

print("Koniec programu.")
#zadanie 3
def odwroc_liste(lista):
    for i in range(len(lista) - 1, -1, -1):
        print(lista[i], end=",")

# przykładowe wywołanie funkcji
dane = [1, 2, 3, 4, 5]
odwroc_liste(dane)
