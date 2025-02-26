import threading
from abc import ABC, abstractmethod

#patron singlenton
class sitemaFacturacion:
    _instancia = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instancia:
            cls._instancia = super(sitemaFacturacion, cls).__new__(cls)
            cls._instancia._inicializacionHistorico()                 
        return cls._instancia


#opcional
"""
with cls._lock:
    if cls._instancia is None:
        cls._instancia = super(sitemaFacturacion, cls).__new__(cls)
        cls._instancia._inicializacionHistorico()                 
    return cls._instancia
"""            

def _inicializacionHistorico(self):
    self.historico = []
    print("sistema de facturacion Inicializado")

def registrarOperaciones(self, operacion):
    self.historico.append(operacion)
    print("la operacion registrada: {operacion}")

#clase abstracta

class procesoNegocio(ABC):
    @abstractmethod
    def ejecutar(self):
        pass
class procesarPedido(procesoNegocio):
    def ejecutar(self):
        print("procesando pedido...")
        return "pedido procesado"
class procesarFactura(procesoNegocio):
    def ejecutar(self):
        print("procesando factura...")
        return "factura procesando"
    
#crear la fabrica (Factory)
class fabricaProcesoNegocio:
    @staticmethod
    def crearProceso(tipoProceso):
        if tipoProceso == "pedido":
            return procesarFactura()
        elif tipoProceso == "factura":
            return procesarFactura()
        else:
            raise ValueError(f"el proceso {tipoProceso} no existe")
        
if __name__ == "__main__":
    sistemaFacturacion = sitemaFacturacion()

    proceso1 = fabricaProcesoNegocio.crearProceso("pedido")
    #proceso1.ejecutar()

    proceso2 = fabricaProcesoNegocio.crearProceso("factura")
    #proceso2.ejecutar()

    resultadoPedido1 = procesarPedido.ejecutar()
    sistemaFacturacion.registrarOperaciones(resultadoPedido1)

    resultadoPedido2 = procesarPedido.ejecutar()
    sistemaFacturacion.registrarOperaciones(resultadoPedido2)

    print("\n*** Historico de procesos de negocio ***\n")   
    for operacion in sistemaFacturacion.historial:
        print(f"Transacción: {operacion}")