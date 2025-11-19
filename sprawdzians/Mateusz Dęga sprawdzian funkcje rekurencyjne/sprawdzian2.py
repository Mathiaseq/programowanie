a = int(input("Podaj długość odcinka a: "))
b = int(input("Podaj długość odcinka b: "))
c = int(input("Podaj długość odcinka c: "))

def Trojkat(a, b, c):
    if a + b < c:
        return False
    elif a + c < b:
        return False
    elif b + c < a:
        return False
    else:
        return True
def prostokatny(a, b, c):
    if b < a and c < a:
        return b**2 + c**2 == a**2
    elif a < b and c < b:
        return a**2 + c**2 == b**2
    elif a < c and b < c:
        return a**2 + b**2 == c**2
    
if Trojkat(a, b, c):
    print("Taki trójkąt istnieje")
    if prostokatny(a, b, c):
        print("Jest to trójkąt prostokątny")
    else:
        print("Nie jest to trójkąt prostokątny")