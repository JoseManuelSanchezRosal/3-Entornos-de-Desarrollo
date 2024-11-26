'''Ejercicio 7: Cálculo de áreas. El siguiente código calcula el área de un círculo y un rectángulo.
Refactorízalo para que cada cálculo sea una función separada.'''

def areaCirculo(radio):
     area_circulo = 3.14 * (radio ** 2)
     return area_circulo
    
def areaRectangulo(base, altura):
     area_rectangulo = base * altura
     return area_rectangulo
    
def imprimirArea():
    print(f"Área del círculo: {areaCirculo()}, Área del rectángulo: {areaRectangulo()}")

def calcular_areas(radio, base, altura):
    areaCirculo()
    areaRectangulo()
    imprimirArea()
    
if __name__ == '__main__':# Declaramos nuestro main menu
    radio = 5
    base = 3
    altura = 3
    calcular_areas()
   
# SIN TERMINAR