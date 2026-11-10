class kwadrat:
    def wprowadz(self, x=0, y=0, d=0):
        self.x = x
        self.y = y 
        self.dlugosc = d
    def rysuj(self):
        print("X=", self.x, "Y=", self.y, "Dlugosc=", self.dlugosc)
k=kwadrat()
k.wprowadz(5,3,10)
k.rysuj()