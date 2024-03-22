class Familia:
    def __init__(self, padre, madre, hijos=[]):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos

    def __str__(self):
        hijos_str = ", ".join(self.hijos)
        return f"Padre: {self.padre}, Madre: {self.madre}, Hijos: {hijos_str}"

familia = Familia("Juan", "María", ["Carlos", "Ana", "Pedro"])
print(familia)
