class vehiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"el vehiculo es de marca {self.marca} y el modelo es {self.modelo}"
    
class carro(vehiculo):

    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def descripcion(self):
        return f"el carro es de marca {self.marca} y el modelo es {self.modelo} y tiene {self.puertas} puertas"
    
mi_auto = carro("Toyota", "Corolla", 4)
print(mi_auto.descripcion())