# Importación de módulos necesarios
from abc import ABC, abstractmethod  # Para definir clases y métodos abstractos
from datetime import datetime  # Para manejar fechas y horas


# Clase abstracta Persona
class Persona(ABC):
    def __init__(self, nombre, contacto, direccion):
        # Constructor de la clase Persona
        self.nombre = nombre  # Nombre de la persona
        self.contacto = contacto  # Información de contacto
        self.direccion = direccion  # Dirección de la persona

    @abstractmethod
    def mostrarInformacion(self):
        # Método abstracto que debe ser implementado por las subclases
        pass


# Clase abstracta Mascota
class Mascota(ABC):
    def __init__(self, nombre, especie, raza, edad):
        # Constructor de la clase Mascota
        self.nombre = nombre  # Nombre de la mascota
        self.especie = especie  # Especie de la mascota
        self.raza = raza  # Raza de la mascota
        self.edad = edad  # Edad de la mascota
        self.historialCitas = []  # Lista para almacenar el historial de citas

    @abstractmethod
    def agregarHistorial(self, detalleServicio):
        # Método abstracto para agregar detalles al historial de la mascota
        pass


# Clase abstracta Cita
class Cita(ABC):
    def __init__(self, fecha, hora, servicio, veterinario):
        # Constructor de la clase Cita
        self.fecha = fecha  # Fecha de la cita
        self.hora = hora  # Hora de la cita
        self.servicio = servicio  # Servicio a realizar
        self.veterinario = veterinario  # Veterinario asignado

    @abstractmethod
    def actualizar(self, **kwargs):
        # Método abstracto para actualizar los detalles de la cita
        pass


# Clase Cliente que hereda de Persona
class Cliente(Persona):
    def __init__(self, nombre, contacto, direccion):
        # Constructor de la clase Cliente
        super().__init__(nombre, contacto, direccion)  # Llama al constructor de la clase base (Persona)
        self.mascotas = []  # Lista para almacenar las mascotas del cliente

    def agregarMascota(self, mascota):
        # Método para agregar una mascota a la lista de mascotas del cliente
        self.mascotas.append(mascota)

    def mostrarInformacion(self):
        # Implementación del método abstracto para mostrar la información del cliente
        return f"Cliente: {self.nombre} - Contacto: {self.contacto} - Dirección: {self.direccion}"


# Clase RegistroMascota que hereda de Mascota
class RegistroMascota(Mascota):
    def agregarHistorial(self, detalleServicio):
        # Implementación del método abstracto para agregar detalles al historial de la mascota
        self.historialCitas.append(detalleServicio)

    def obtenerHistorial(self):
        # Método para obtener el historial de citas de la mascota
        return self.historialCitas


# Clase CitaMascota que hereda de Cita
class CitaMascota(Cita):
    def actualizar(self, **kwargs):
        # Implementación del método abstracto para actualizar los detalles de la cita
        for clave, valor in kwargs.items():
            if hasattr(self, clave):  # Verifica si la cita tiene el atributo
                setattr(self, clave, valor)  # Actualiza el atributo con el nuevo valor


# Clase principal SistemaVeterinaria
class SistemaVeterinaria:
    def __init__(self):
        # Constructor de la clase SistemaVeterinaria
        self.clientes = []  # Lista para almacenar los clientes registrados

    def registrarCliente(self):
        # Método para registrar un nuevo cliente
        try:
            nombre = input("Ingrese el nombre del cliente: ").strip()
            contacto = input("Ingrese el contacto del cliente: ").strip()
            direccion = input("Ingrese la dirección del cliente: ").strip()

            # Validación de campos obligatorios
            if not nombre or not contacto or not direccion:
                raise ValueError("Todos los campos son obligatorios.")

            # Creación de un nuevo cliente y agregación a la lista de clientes
            cliente = Cliente(nombre, contacto, direccion)
            self.clientes.append(cliente)
            print("Cliente registrado exitosamente.")

        except ValueError as e:
            # Manejo de errores
            print(f"Error: {e}")

    def registrarMascota(self):
        # Método para registrar una mascota para un cliente existente
        try:
            nombreCliente = input("Ingrese el nombre del cliente a quien pertenece la mascota: ").strip()
            cliente = next((c for c in self.clientes if c.nombre == nombreCliente), None)

            # Validación de existencia del cliente
            if not cliente:
                raise ValueError("El cliente no existe.")

            # Solicitud de datos de la mascota
            nombreMascota = input("Ingrese el nombre de la mascota: ").strip()
            especie = input("Ingrese la especie de la mascota: ").strip()
            raza = input("Ingrese la raza de la mascota: ").strip()
            edad = int(input("Ingrese la edad de la mascota: "))

            # Validación de datos de la mascota
            if not nombreMascota or not especie or not raza or edad <= 0:
                raise ValueError("Datos de la mascota inválidos.")

            # Creación de una nueva mascota y agregación al cliente
            mascota = RegistroMascota(nombreMascota, especie, raza, edad)
            cliente.agregarMascota(mascota)
            print("Mascota registrada exitosamente.")

        except ValueError as e:
            # Manejo de errores
            print(f"Error: {e}")

    def programarCita(self):
        # Método para programar una cita para una mascota
        try:
            nombreCliente = input("Ingrese el nombre del cliente a quien pertenece la mascota: ").strip()
            nombreMascota = input("Ingrese el nombre de la mascota: ").strip()

            # Búsqueda del cliente
            cliente = next((c for c in self.clientes if c.nombre == nombreCliente), None)
            if not cliente:
                raise ValueError("El cliente no existe.")

            # Búsqueda de la mascota
            mascota = next((m for m in cliente.mascotas if m.nombre == nombreMascota), None)
            if not mascota:
                raise ValueError("Mascota no encontrada.")

            # Solicitud de datos de la cita
            fecha = input("Ingrese la fecha de la cita (YYYY-MM-DD): ").strip()
            hora = input("Ingrese la hora de la cita (HH:MM): ").strip()
            servicio = input("Ingrese el servicio de la cita (consulta, examen, tratamiento, etc.): ").strip()
            veterinario = input("Ingrese el veterinario de la cita: ").strip()

            # Validación del formato de fecha y hora
            datetime.strptime(fecha, "%Y-%m-%d")
            datetime.strptime(hora, "%H:%M")

            # Validación de campos obligatorios
            if not servicio or not veterinario:
                raise ValueError("Datos de la cita inválidos.")

            # Creación de una nueva cita y agregación al historial de la mascota
            cita = CitaMascota(fecha, hora, servicio, veterinario)
            mascota.agregarHistorial(cita)
            print("Cita programada exitosamente.")

        except ValueError as e:
            # Manejo de errores
            print(f"Error: {e}")

    def actualizarCita(self):
        # Método para actualizar los detalles de una cita existente
        try:
            nombreCliente = input("Ingrese el nombre del cliente: ").strip()
            nombreMascota = input("Ingrese el nombre de la mascota: ").strip()

            # Búsqueda del cliente
            cliente = next((c for c in self.clientes if c.nombre == nombreCliente), None)
            if not cliente:
                raise ValueError("Cliente no encontrado.")

            # Búsqueda de la mascota
            mascota = next((m for m in cliente.mascotas if m.nombre == nombreMascota), None)
            if not mascota:
                raise ValueError("Mascota no encontrada.")

            # Mostrar citas disponibles para actualizar
            print("Citas disponibles para actualizar:")
            for i, cita in enumerate(mascota.obtenerHistorial(), start=1):
                print(f"{i}. Fecha: {cita.fecha}, Hora: {cita.hora}, Servicio: {cita.servicio}, Veterinario: {cita.veterinario}")

            # Selección de la cita a actualizar
            indice = int(input("Ingrese el número de la cita a actualizar: ").strip()) - 1
            if indice < 0 or indice >= len(mascota.obtenerHistorial()):
                raise ValueError("Selección de cita no válida.")

            cita = mascota.obtenerHistorial()[indice]

            # Solicitud de nuevos datos para la cita
            nuevaFecha = input("Ingrese la nueva fecha de la cita (YYYY-MM-DD): ").strip()
            nuevaHora = input("Ingrese la nueva hora de la cita (HH:MM): ").strip()
            nuevoServicio = input("Ingrese el nuevo servicio de la cita: ").strip()
            nuevoVeterinario = input("Ingrese el nuevo veterinario de la cita: ").strip()

            # Actualización de los campos si se proporcionan nuevos valores
            if nuevaFecha:
                datetime.strptime(nuevaFecha, "%Y-%m-%d")
                cita.actualizar(fecha=nuevaFecha)

            if nuevaHora:
                datetime.strptime(nuevaHora, "%H:%M")
                cita.actualizar(hora=nuevaHora)

            if nuevoServicio:
                cita.actualizar(servicio=nuevoServicio)

            if nuevoVeterinario:
                cita.actualizar(veterinario=nuevoVeterinario)

            print("Cita actualizada exitosamente.")
        except ValueError as e:
            # Manejo de errores
            print(f"Error: {e}")

    def consultaHistorial(self):
        # Método para consultar el historial de citas de una mascota
        try:
            nombreCliente = input("Ingrese el nombre del cliente: ").strip()
            nombreMascota = input("Ingrese el nombre de la mascota: ").strip()

            # Búsqueda del cliente
            cliente = next((c for c in self.clientes if c.nombre == nombreCliente), None)
            if not cliente:
                raise ValueError("El cliente no existe.")

            # Búsqueda de la mascota
            mascota = next((m for m in cliente.mascotas if m.nombre == nombreMascota), None)
            if not mascota:
                raise ValueError("Mascota no encontrada.")

            # Obtención del historial de citas
            historial = mascota.obtenerHistorial()
            if not historial:
                print("No hay historial de citas para la mascota.")
            else:
                # Mostrar el historial de citas
                for entrada in historial:
                    print(f"Fecha: {entrada.fecha}, Hora: {entrada.hora}, Servicio: {entrada.servicio}, Veterinario: {entrada.veterinario}")

        except ValueError as e:
            # Manejo de errores
            print(f"Error: {e}")

    def iniciar(self):
        # Método principal que inicia el sistema y muestra un menú de opciones
        while True:
            print("\nSistema de gestión de Veterinaria:")
            print("1. Registrar cliente")
            print("2. Registrar mascota")
            print("3. Programar cita")
            print("4. Actualizar cita")
            print("5. Consultar historial")
            print("6. Salir")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self.registrarCliente()
            elif opcion == "2":
                self.registrarMascota()
            elif opcion == "3":
                self.programarCita()
            elif opcion == "4":
                self.actualizarCita()
            elif opcion == "5":
                self.consultaHistorial()
            elif opcion == "6":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")


# Bloque principal de ejecución
if __name__ == "__main__":
    sistema = SistemaVeterinaria()  # Creación de una instancia del sistema
    sistema.iniciar()  # Inicio del sistema