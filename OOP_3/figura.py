class Figura:
    def __init__(self, kolor="czarny"):
        self.kolor = kolor

    def __str__(self):
        return f"Figura: kolor={self.kolor}"

    def pole(self):
        return 0
class Punkt(Figura):
    def __init__(self, x=0, y=0, kolor="czarny"):
        super().__init__(kolor)
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt(x={self.x}, y={self.y}, kolor={self.kolor})"

    def przesunXY(self, dx, dy):
        self.x += dx
        self.y += dy
        return self
class Kwadrat(Figura):
    def __init__(self, bok, punkt=Punkt(0, 0), kolor="niebieski"):
        super().__init__(kolor)
        self.bok = bok
        self.punkt = punkt

    def __str__(self):
        return f"Kwadrat: bok={self.bok}, początek={self.punkt}, kolor={self.kolor}"

    def pole(self):
        return self.bok ** 2

    def obwod(self):
        return 4 * self.bok
class Prostokat(Figura):
    def __init__(self, a, b, punkt=Punkt(0, 0), kolor="zielony"):
        super().__init__(kolor)
        self.a = a
        self.b = b
        self.punkt = punkt

    def __str__(self):
        return f"Prostokąt: a={self.a}, b={self.b}, początek={self.punkt}, kolor={self.kolor}"

    def pole(self):
        return self.a * self.b

    def obwod(self):
        return 2 * (self.a + self.b)
class Kolo(Figura):
    def __init__(self, promien, srodek=Punkt(0, 0), kolor="czerwony"):
        super().__init__(kolor)
        self.promien = promien
        self.srodek = srodek

    def __str__(self):
        return f"Koło: r={self.promien}, środek={self.srodek}, kolor={self.kolor}"

    def pole(self):
        return 3.14 * self.promien ** 2

    def obwod(self):
        return 2 * 3.14 * self.promien
if __name__ == "__main__":
    p = Punkt(2, 3, "czarny")
    print(p)
    p.przesunXY(5, -2)
    print(p)

    kw = Kwadrat(4, Punkt(0, 0), "niebieski")
    print(kw)
    print("Pole kwadratu:", kw.pole())
    print("Obwód kwadratu:", kw.obwod())

    pr = Prostokat(6, 3, Punkt(0, 0), "zielony")
    print(pr)
    print("Pole prostokąta:", pr.pole())
    print("Obwód prostokąta:", pr.obwod())

    ko = Kolo(5, Punkt(0, 0), "czerwony")
    print(ko)
    print("Pole koła:", ko.pole())
    print("Obwód koła:", ko.obwod())