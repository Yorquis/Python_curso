from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def area(self):
        pass

class circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return f"El area del circulo es:{3.1416 * self.radio**2}"

    def perimetro(self):
        return f"El perimetro del circulo es: {2 * 3.1416 * self.radio}"

class retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return f"El area del retangulo es: {self.base * self.altura}"
    
    def perimetro(self):
        return f"El perimetro del retangulo es: {2 * (self.base + self.altura)}"
    
class cuadrado(Forma):
    def __init__(self):
        pass

    def area(self):
        return f"El area del cuadrado es: {self.lado ** 2}"
    
formas = [circulo(5),
          retangulo(2, 10),
          cuadrado(8),
          retangulo(10, 20),
          circulo (22)
          
]

print("Area de las formas")
for forma in formas:
    print(forma.area())


    
   
    



        


            