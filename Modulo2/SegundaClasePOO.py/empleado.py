class empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self._salario = salario
        self._salarioMinimo = 1300000

    def mostrarInformacion(self):
        return f"Nombre: {self.nombre} - Edad: {self.edad} - Salario: {self._salario}"
    

    def obtenerSalario(self):
        return self._salario
    

    def establecerSalario(self, nuevoSalario):
        if nuevoSalario < 1300000:
            return "El salario no puede ser menor al salario minimo."
        self._salario = nuevoSalario
        return f"el nuevo salario es: {self._salario}"
    
    def asignacionSalariales(self):
        if self._salario < 1300000:
            return "El salario no puede ser menor al salario minimo."
    

    def deducionesSalariales(self):
        pass

empleado1 = empleado("jose", 25, 1500000)
print(empleado1.mostrarInformacion())
print(empleado1.obtenerSalario())
print(empleado1.establecerSalario(2000000))
print(empleado1.asignacionSalariales())
print(empleado1.deducionesSalariales())