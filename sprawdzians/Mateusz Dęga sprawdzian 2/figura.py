class Figura():
    def __init__(self, nazwa, kolor):
        self.nazwa = nazwa
        self.kolor = kolor  
    def oblicz_pole(self):
        pass
    def oblicz_obwod(self):
        pass

class Kwadrat(Figura):
    def __init__(self, nazwa, kolor, bok):
        super().__init__(nazwa, kolor)
        self.bok = bok
    def oblicz_pole(self):
        return self.bok * self.bok
    def oblicz_obwod(self):
        return 4 * self.bok
    def __str__(self):
        return f"Kwadrat o nazwie {self.nazwa}, o kolorze {self.kolor}, bok wynosi {self.bok}, pole jest równe {self.oblicz_pole()}, i obwodzie równym {self.oblicz_obwod()}"
    
k1 = Kwadrat("Kwadrat1", "zielonym", 7)      
k2 = Kwadrat("Kwadrat2", "fioletowym", 12)
print(k1)
print(k2)