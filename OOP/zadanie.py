class Figura:
    def __str__(self, x, y):
        self.x = x
        self.y = y
        return self.x, self.y
    def kolor(self, kolor):
        self.kolor = kolor
        return self.kolor
    def punkt(self, x, y):
        self.x = x
        self.y = y
        return self.x, self.y
    def kwadrat(self, bok):
        return bok ** 2

print("Współrzędne punktu:", Figura(10, 20).punkt(10, 20))
print("Kolor punktu:", Figura(10, 20).kolor("czerwony"))
print("Pole kwadratu:", Figura(10, 20).kwadrat(5))
