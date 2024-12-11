from abc import ABC, abstractmethod

#clase abstracta
class clases:
    @abstractmethod
    def operacion(self):
        pass

#creacion de subclases
class claseA(clases):
    def operacion(self):
        return "esta es la clase A"
    
class claseB(clases):
    def operacion(self):
        return "esta es la clase B"
    def impresion(self):
        pass
    def consulta(self):
        pass
    def retiro(self):
        pass
    
#clase factory, factoria, fabrica
class fabricaClases:
    @staticmethod
    def creacionObjetos(tipoObjeto):
        if tipoObjeto == "A":
            return claseA()
        elif tipoObjeto == "B":
            return claseB()
        else:
            raise ValueError(f"la clase {tipoObjeto} no existe")
objeto1 = fabricaClases.creacionObjetos("A")
#objeto2 = fabricaClases.creacionObjetos("B")

print(objeto1.operacion())
#print(objeto2.operacion())