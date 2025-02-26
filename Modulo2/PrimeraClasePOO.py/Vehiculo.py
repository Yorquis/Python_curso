class Vehiculo:
    def __init__(self, tipo):
        self.tipo = tipo
        
    def descripcion(self):
        return f"este Vehiculo de tipo {self.tipo}"
    
class Moto(Vehiculo):

    def __init__(self, tipo, marca):
        super().__init__(tipo)
        self.marca = marca

moto1 = Moto("moto", "Ducati")
print(moto1.descripcion())