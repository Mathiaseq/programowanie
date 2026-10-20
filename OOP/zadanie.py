class Figura:
    def __init__(self, kolor):
        self.kolor = kolor
    def __str__(self):
        return "Figura: kolor = " + self.kolor
    def zmien_kolor(self, nowy_kolor):
        self.kolor = nowy_kolor
        return self.kolor
    def rysuj(self, kolor):
        return "Rysuję figurę w kolorze: " + kolor


class Punkt(Figura):
    def __init__(self, x, y, kolor="czarny"):
        super().__init__(kolor)
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt: x={self.x}, y={self.y}, kolor={self.kolor}"

    def zmien_xy(self, x, y):
        self.x = x
        self.y = y
        return (self.x, self.y)

    def rysuj(self):
        return f"Rysuję punkt ({self.x}, {self.y}) w kolorze {self.kolor}."


class Prostokat(Figura):
    def __init__(self, dlugosc, szerokosc, kolor="niebieski"):
        super().__init__(kolor)
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def __str__(self):
        return f"Prostokąt: długość={self.dlugosc}, szerokość={self.szerokosc}, kolor={self.kolor}"

    def pole(self):
        return self.dlugosc * self.szerokosc

    def obwod(self):
        return 2 * (self.dlugosc + self.szerokosc)

    def rysuj(self):
        return f"Rysuję prostokąt {self.dlugosc}x{self.szerokosc} w kolorze {self.kolor}."



fig1 = Figura("czerwony")
print(fig1)
print(fig1.zmien_kolor("zielony"))
print(fig1.rysuj())

punkt = Punkt(10, 20, "czarny")
print(punkt)
print(punkt.zmien_xy(15, 25))
print(punkt.rysuj())

prostokat = Prostokat(5, 3, "niebieski")
print(prostokat)
print("Pole:", prostokat.pole())
print("Obwód:", prostokat.obwod())
print(prostokat.rysuj())