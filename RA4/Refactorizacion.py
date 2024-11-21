# Ejercicio 1 refactorización:
def hacer_suma(a, b):
    return a + b
    
def hacer_resta(a, b):
    return a - b
def hacer_multiplicacion(a, b):
    return a * b

def hacer_division (a, b):
    return a / b


def calculadora(a, b):
    print(f"Suma: {hacer_suma(a,b)}, Resta: {hacer_resta(a,b)}, Multiplicación: {hacer_multiplicacion(a, b)}, División: {hacer_division(a, b)}")

a = int(input("Introduzca numero a: "))
b = int(input("Introduzca numero b: "))

calculadora(a, b)