def sprawdz_x(x):
    if x < -5:
        wynik = (x - 1)
    elif -5 <= x <= 5:
        wynik = x ** 2 + 3 * x - 2
    else:
        wynik = (1 ** (1 / 6)) / (x - 1)

    return wynik

x = float(input("Podaj wartość x: "))
wynik = sprawdz_x(x)
print("Wynik:", wynik)