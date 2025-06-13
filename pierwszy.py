def kalkulator():
    print("Kalkulator")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        print("Wynik dodawania: ", a + b)
    elif wybor == "2":
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        print("Wynik odejmowania: ", a - b)
    elif wybor == "3":
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        print("Wynik mnożenia: ", a * b)
    elif wybor == "4":
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        if b != 0:
            print("Wynik dzielenia: ", a / b)
        else:
            print("Błąd! Nie można dzielić przez zero.")
    else:
        print("Błąd! Nieprawidłowy wybór.")

kalkulator()