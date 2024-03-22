class Operaciones:
    def __init__(self):
        self.num1 = int(input("Ingrese el primer numero entero: "))
        self.num2 = int(input("Ingrese el segundo numero entero: "))
        self.realizar_operaciones()

    def realizar_operaciones(self):
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()

    def suma(self):
        resultado = self.num1 + self.num2
        print(f"suma: {self.num1} + {self.num2} = {resultado}")

    def resta(self):
        resultado = self.num1 - self.num2
        print(f"resta: {self.num1} - {self.num2} = {resultado}")

    def multiplicacion(self):
        resultado = self.num1 * self.num2
        print(f"multiplicacion: {self.num1} * {self.num2} = {resultado}")

    def division(self):
        if self.num2 != 0:
            resultado = self.num1 / self.num2
            print(f"division: {self.num1} / {self.num2} = {resultado}")
        else:
            print("no se puede dividir por cero")

operaciones = Operaciones()
