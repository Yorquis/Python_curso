class persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad    
        self.__cuentaBancaria = 123456
       

    def mostrarInformacion(self):
        return f"Nombre: {self.nombre} - Edad: {self._edad}"
    

    def mostrarCuenta(self):
        return f"Cuenta Bancaria: {self.__cuentaBancaria}"
        
    def mostrarInformacionCompleta(self):
        return self__mostrarCuenta()
    
persona1 = persona("Juan", 25)

print(persona1.nombre)
print(persona1._edad)        
print(persona1.mostrarInformacion())

print(persona1.mostrarInformacionCompleta())
