from abc import ABC, abstractmethod

class EstrategiaTarifa(ABC):

    @abstractmethod
    def calcularTarifa(self, distancia, tiempo):
        raise NotImplementedError("se debe implementar este metodo")

class TarifaFija(EstrategiaTarifa):
    def calcularTarifa(self, distancia, tiempo):
        return 300
    
class TarifaHora(EstrategiaTarifa):
    def calcularTarifa(self, distancia, tiempo):
        return tiempo * 25
    
class TarifaKilometro(EstrategiaTarifa):
    def calcularTarifa(self, distancia, tiempo):
        return distancia * 2
    
class CalculadoraTarifa:
    def __init__(self, Estrategia):
        self.Estrategia = Estrategia

    def CambiarEstrategia(self, Estrategia):
        self.Estrategia = Estrategia

    def Calcular(self, distancia, tiempo):
        return self.Estrategia.calcularTarifa(distancia, tiempo)
    
arriendo1 = TarifaFija()
calculadora = CalculadoraTarifa(arriendo1)
print("Tarifa fija: ", calculadora.Calcular(10, 5))


calculadora.CambiarEstrategia(TarifaHora)
print("Tarifa por hora: ", calculadora.Calcular(100, 2))

calculadora.CambiarEstrategia(TarifaKilometro)
print("Tarifa por kilometro: ", calculadora.Calcular(100, 3))

    