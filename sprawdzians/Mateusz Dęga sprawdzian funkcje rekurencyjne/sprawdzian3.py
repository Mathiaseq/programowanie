def T(n):
    if n == 0:
        return T(1)
    elif n == 1:
        return 1
    elif n > 1 and n % 2 == 0:
        return T(n - 1)+1
    elif n > 1 and n % 2 != 0:
        return T(n - 1)+T(n-2)-1

while True:
    liczba = input("Podaj liczbę albo zostaw puste aby zakończyć: ")
    if liczba != "":
        print(T(int(liczba)))
    else:
        break
