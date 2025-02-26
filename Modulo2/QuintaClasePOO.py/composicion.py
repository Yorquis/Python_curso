class vehiculo:
    
      def __init__(self, motor, transmision):
        self.motor = motor
        self.transmision = transmision

      def encender(self):
          print("Encendiendo vehiculo")
          self.motor.iniciar()
        

class motor:
    def __init__(self):
        pass

    def iniciar(self):
        pass
        

class motorGasolina(motor):

    def __init__(self):
        pass
    def iniciar(self):
        print("Iniciando motor gasolina")
        

class motorElectrico(motor):
    def __init__(self):
        pass
    def iniciar(self):
        print("Iniciando motor electrico")
        

motor_gasolina = motorGasolina()

motor_electrico = motorElectrico()

auto_gasolina = vehiculo(motor_gasolina, "automatica")

auto_electrico = vehiculo(motorElectrico(), "automatica")

auto_gasolina.encender()
auto_electrico.encender()
