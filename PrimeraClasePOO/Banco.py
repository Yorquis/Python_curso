class Banco:
   
    TASA_INTERES = 0.03
    def __init__(self, name):
        self.name = name
  
    @classmethod
    def cambiarTasa(cls, nuevaTasa):
        cls.TASA_INTERES = nuevaTasa

    @classmethod
    def conversionDolaresEuros(Dolares):
      return Dolares * 0.85