from abc import ABC, abstractmethod

class EstrategiaDescuento(ABC):
    @abstractmethod
    def __init__(self, monto): 
        pass

    @abstractmethod
    def calcular(self, monto):
        return monto

class sinDescuento(EstrategiaDescuento):

    def __init__(self):     
        pass
    def calcular(self, monto):
        return monto
    
class descuentoPorcentaje(EstrategiaDescuento):

    def __init__(self, porcentaje):     
        self.porcentaje = porcentaje
    def calcular(self, monto):
        return monto - (monto * self.porcentaje / 100)
    
class descuentoFijo(EstrategiaDescuento):

    def __init__(self, montoDescuento):     
        self.montoDescuento = montoDescuento     
        
    def calcular(self, monto):
        return monto - self.montoDescuento
    
class pedido:
    def __init__(self, monto, estrategiaDescuento: EstrategiaDescuento):
        self.monto = monto
        self.estrategiaDescuento = estrategiaDescuento

    def calcularTotal(self):
        return self.estrategiaDescuento.calcular(self.monto)
    
pedido1 = pedido(1000, sinDescuento())
print(f"Total sin descuento: ${pedido1.calcularTotal()}")

pedido2 = pedido(1000, descuentoPorcentaje(50))
print(f"Total con 50% de descuento: ${pedido2.calcularTotal()}")

pedido3 = pedido(1000, descuentoFijo(100))
print(f"Total con descuento fijo de $100: ${pedido3.calcularTotal()}")