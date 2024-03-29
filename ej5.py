class Persona:
    def __init__(self,):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))

    def imprimir_datos(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")


class Empleado(Persona):
    def __init__(self, sueldo):
        super().__init__()
        self.sueldo = sueldo

    def pagar_impuestos(self):
        if self.sueldo > 3000:
            print(f"El empleado {self.nombre} debe pagar impuestos")
        else:
            print("El empleado no debe pagar impuestos")


persona1 = Persona()
persona1.imprimir_datos()

empleado1 = Empleado(3500)
empleado1.imprimir_datos()
empleado1.pagar_impuestos()

