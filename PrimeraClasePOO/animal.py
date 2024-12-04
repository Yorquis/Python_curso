class animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def saludar(self):
        return f"Hola, mi animalito se llama {self.name} y tiene {self.age} años."
    
animal1 = animal("Ginebra", 3)

print(animal1.name)
print(animal1.age)
print(animal1.saludar())