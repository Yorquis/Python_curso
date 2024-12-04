class Animall:

    cantidadAnimales = 0

    def __init__(self, name):
        self.name = name
        Animall.cantidadAnimales += 1

    @classmethod
    def totalAnimales(cls):
        return f"tengo ¨{cls.cantidadAnimales} animalitos"

animalito1 = Animall("ron")
animalito2 = Animall("rayo")
animalito3 = Animall("luna")    


print(animalito3.name)
print(Animall.cantidadAnimales)
print(Animall.totalAnimales())