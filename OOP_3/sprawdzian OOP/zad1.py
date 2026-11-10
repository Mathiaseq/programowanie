import turtle

class kwadrat:
    def __init__(self, bok):
        self.bok = bok
    def pole(self):
        return self.bok**2
    def obwod(self):
        return 4*self.bok
    def rysuj(self):
        t = turtle.Turtle()
        for _ in range(4):
            t.forward(self.bok)
            t.left(90)
        turtle.done()
    def obroc_lewo(self):
        t = turtle.Turtle()
        t.left(90)
        for _ in range(4):
            t.forward(self.bok)
            t.left(90)
            turtle.done()
    def obroc_prawo(self):
        t = turtle.Turtle()
        t.right(90)
        for _ in range(4):
            t.forward(self.bok)
            t.left(90)
        turtle.done()

k1 = kwadrat(100)
print("Pole kwadratu:", k1.pole())
print("Obwód kwadratu:", k1.obwod())
k1.rysuj()

k2 = kwadrat(150)
print("Pole kwadratu:", k2.pole())
print("Obwód kwadratu:", k2.obwod())
k2.rysuj()