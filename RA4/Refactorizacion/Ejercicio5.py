'''Ejercicio 5: Cálculo de estadísticas. El siguiente código calcula estadísticas básicas (promedio, máximo, mínimo) 
de una lista de números. Refactorízalo para que cada cálculo esté en una función separada.'''

def promedio(numeros):
    promedio = sum(numeros) / len(numeros)
    return promedio

def maximo(numeros):
    maximo = max(numeros)
    return maximo

def minimo(numeros):
    minimo = min(numeros)
    return minimo

def imprimir():
    print(f"Promedio: {promedio(numeros)}, Máximo: {maximo(numeros)}, Mínimo: {minimo(numeros)}")
    
def calcular_estadisticas(numeros):
    promedio(numeros)
    maximo(numeros)
    minimo(numeros)
    imprimir()

if __name__ == '__main__':# Declaramos nuestro main menu
    numeros = (4, 6, 88, 1, 56, 78, 99)
    print("La lista original de numeros es: ", numeros)
    calcular_estadisticas(numeros)
    
# HECHO