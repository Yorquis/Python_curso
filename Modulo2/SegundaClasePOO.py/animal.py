class animal:
    def __init__(self, name):
        self.name = name

    def hablar(self):
        return "todo animal habla"
    
    def __str__(self):
        return f"el nombre del animal: {self.name}"
        
class perro(animal):
    def __init__(self, name, raza):
        super().__init__(name)
        self.raza = raza
    def hablar(self):
        return "Guau guau!"
    def __str__(self):
        return f"El perro {self.name} es de la raza {self.raza}"
        

animal1 = animal("Foco")
print(animal1.hablar())
print(animal1.__str__())

perro1 = perro("Paco, pitbull")
print(perro1.hablar())
print(perro1)