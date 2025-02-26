from abc import ABC, abstractmethod

class Sujeto:
    def __init__(self):
        self._observadores = []

    def agregarObservador(self, observador):
        self._observadores.append(observador)

    def quitarObservador(self, observador):
        self._observadores.remove(observador)

    def notificarObservadores(self, mensaje):
        for observador in self._observadores:
            observador.actualizar(mensaje)

class observador(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def actualizar(self, mensaje):
        raise NotImplementedError("Subclases deben estar implementadas")
    
class observadorConcreto(observador):
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, mensaje):
        print(f"{self.nombre} ha recibido el mensaje: {mensaje}")

sujeto = Sujeto()

observador1 = observadorConcreto("Observador 1")
observador2 = observadorConcreto("Observador 2")

sujeto.agregarObservador(observador1)
sujeto.agregarObservador(observador2)

sujeto.notificarObservadores("Nuevo mensaje de advertencia LPTx")