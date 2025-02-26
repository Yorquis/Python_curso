class libro:

    def __init__ (self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def descripcion (self):
        return f"El libro {self.titulo} Autor {self.autor}"

    def __str__(self):
        return f"El libro {self.titulo} Autor {self.autor} STR"
        

class libroDigital(libro):

    def __init__ (self, titulo, autor, formato):
        super().__init__(titulo, autor)
        self.formato = formato    
        pass

    def descripcion (self):
        return f"El libro {self.titulo} Autor {self.autor} formato: {self.formato}"
        

    def __str__(self):
        return f"El libro {self.titulo} Autor {self.autor} STR"

libro1 = libro("El señor de los anillos", "Tolkien")
libroDigital1 = libroDigital("la peste", "Alberto Campo", "PDF")

print(libro1.__str__())
print(libro1.descripcion())

print(libroDigital1.__str__())
print(libroDigital1.descripcion())