class Figura:
    def __init__(self):
        pass

    def __str__(self):
        return f"Figura: {self.__class__.__name__}"

    def pole(self):
        return 0


class Punkt(Figura):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt(x={self.x}, y={self.y})"

    def przesunXY(self, dx, dy):
        self.x += dx
        self.y += dy
        return self


class Kwadrat(Figura):
    def __init__(self, bok, punkt=Punkt(0, 0)):
        self.bok = bok
        self.punkt = punkt

    def __str__(self):
        return f"Kwadrat: bok={self.bok}, początek={self.punkt}"

    def pole(self):
        return self.bok ** 2


class Prostokat(Figura):
    def __init__(self, a, b, punkt=Punkt(0, 0)):
        self.a = a
        self.b = b
        self.punkt = punkt

    def __str__(self):
        return f"Prostokąt: a={self.a}, b={self.b}, początek={self.punkt}"

    def pole(self):
        return self.a * self.b


class Kolo(Figura):
    def __init__(self, promien, srodek=Punkt(0, 0)):
        self.promien = promien
        self.srodek = srodek

    def __str__(self):
        return f"Koło: r={self.promien}, środek={self.srodek}"

    def pole(self):
        return 3.14 * self.promien ** 2


if __name__ == "__main__":
    p = Punkt(2, 3)
    print(p)
    p.przesunXY(5, -2)
    print(p)

    kw = Kwadrat(4)
    print(kw)
    print("Pole kwadratu:", kw.pole())

    pr = Prostokat(6, 3)
    print(pr)
    print("Pole prostokąta:", pr.pole())

    ko = Kolo(5)
    print(ko)
    print("Pole koła:", ko.pole())
