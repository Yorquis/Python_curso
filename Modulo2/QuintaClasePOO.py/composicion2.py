class tarea:

    def __init__(self):
        pass

    def ejecutar(self):
        pass

class trabajoProyecto(tarea):

    def __init__(self):
        pass
    def ejecutar(self):
        return("trabajando en un proyecto")

class capacitacion(tarea):

    def __init__(self): 
        pass

    def ejecutar(self):
        return("tomando una capacitacion")
    
class evaluacion(tarea):

    def __init__(self):
        pass

    def ejecutar(self):
        return("desarrollando una evaluacion de personal")
    
class empleado(tarea):

    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def asignarTarea(self, tarea):
        self.tareas.append(tarea)
        

    def realizarTarea(self, tarea):
        print(f"{self.nombre}, esta realizando las siguientes tareas:")
        for tarea in self.tareas:
            print(f"- {tarea.ejercer()}")

proyecto = trabajoProyecto()
capacitacion = capacitacion()
evaluacion = evaluacion()

empleado = empleado("jose")
empleado.asignarTarea(proyecto)
empleado.asignarTarea(eval)
empleado.asignarTarea(evaluacion)
empleado.asignarTarea(capacitacion)


empleado.realizarTarea()

