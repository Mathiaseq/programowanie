class Figura:
    def __str__(self, x, y):
        self.x = x
        self.y = y
        return self.x, self.y
    def kolor(self, kolor):
        self.kolor = kolor
        return self.kolor
    def obwod_prostokata(self, bok):
        self.bok = bok
        return 4 * self.bok


x=int(input("Podaj współrzędną x: "))
y=int(input("Podaj współrzędną y: "))
k=str(input("Podaj kolor: "))

print("Kolor punktu:", Figura(k).kolor(k))
print("Obwód prostokąta:", Figura(k).obwod_prostokata(5))
