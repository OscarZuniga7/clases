class Saludo:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"hola, {self.nombre}!"
    
mi_saludo = Saludo("Oscar")
print(mi_saludo.saludar())