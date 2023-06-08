import math

class Esfera:
    def __init__(self, cor, raio): #init -> metodo construtor
        self.cor = cor
        self.raio = raio
        
    def volume(self):
        vol = (4/3) *math.pi*(self.raio**3)
        return vol
    
    def area(self):
        ar = 4*math.pi*(self.raio**2)
        return ar
    
bola1 = Esfera('rosa', 5)
bola2 = Esfera('verde', 8)

print(f"O volume da Bola 1 é {bola1.volume()}cm^3")
print(f"A área da Bola 1 é {bola1.area()}cm^2")

print(bola2.volume())
print(Esfera.area(bola2))