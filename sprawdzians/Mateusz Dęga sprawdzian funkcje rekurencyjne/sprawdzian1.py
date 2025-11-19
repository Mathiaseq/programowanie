def fibonacci(i):
    if i < 1:
        return None
    if i < 3:
        return 1
    return fibonacci(i - 1) + fibonacci(i - 2)
liczba = int(input("Podaj dla jakiej liczby obliczyć ciąg Fibonacciego: "))
print(fibonacci(liczba))
