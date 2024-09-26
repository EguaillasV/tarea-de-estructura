
#Calcular Area


import math

# Clase para el Cuadrado
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

# Clase para el Rectángulo
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

# Clase para el Triángulo
class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

# Clase para la Circunferencia
class Circunferencia:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)


cuadrado = Cuadrado(4)
rectangulo = Rectangulo(5, 3)
triangulo = Triangulo(6, 4)
circunferencia = Circunferencia(3)


print("Área del cuadrado:", cuadrado.area())
print("Área del rectángulo:", rectangulo.area())
print("Área del triángulo:", triangulo.area())
print("Área de la circunferencia:", circunferencia.area())






#Calculadora



# Clase Calculadora
class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(self):
        return self.numero1 + self.numero2

    def restar(self):
        return self.numero1 - self.numero2

    def multiplicar(self):
        return self.numero1 * self.numero2

    def dividir(self):
        if self.numero2 != 0:
            return self.numero1 / self.numero2
        else:
            return "Error: División por cero no permitida"

# Instanciando la clase con dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

calculadora = Calculadora(numero1, numero2)

# Operaciones
print("Suma:", calculadora.sumar())
print("Resta:", calculadora.restar())
print("Multiplicación:", calculadora.multiplicar())
print("División:", calculadora.dividir())
