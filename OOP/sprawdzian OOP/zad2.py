class Stos:
    def __init__(self):
        self.dane=[]
    def dodaj(self, element):
        self.dane.append(element)
    def usun(self):
        if not self.czy_pusty():
            return self.dane.pop()
        return "Stos jest pusty"
    def czy_pusty(self):
        return len(self.dane) == 0
    def wyswietl(self):
        print("Zawartość stosu:", self.dane)

stos = Stos()

stos.dodaj(int(input("Podaj element do dodania na stos: ")))
stos.dodaj(int(input("Podaj element do dodania na stos: ")))
stos.dodaj(int(input("Podaj element do dodania na stos: ")))
stos.dodaj(int(input("Podaj element do dodania na stos: ")))
stos.wyswietl()

print("Usunięto element:", stos.usun())
print("Usunięto element:", stos.usun())
print("Usunięto element:", stos.usun())
print("Usunięto element:", stos.usun())
stos.wyswietl()