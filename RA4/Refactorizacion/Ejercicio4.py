'''Ejercicio 4: Formateo de texto. El siguiente código da formato a un texto. Refactorízalo para que 
cada tarea (mayúsculas, minúsculas, capitalización) sea una función separada.'''

def mayusculas(texto):
    print(texto.upper())
    
def minusculas(texto):
    print(texto.lower())

def primeramayusculas(texto):
    print(texto.capitalize())
    
def formatear_texto(texto):
    mayusculas(texto)
    minusculas(texto)
    primeramayusculas(texto)
    
if __name__ == '__main__':# Declaramos nuestro main menu
    formatear_texto("Hola MI nomBRE es JOSe ManueL")# Le damos un texto para aplicar las funciones.
    
# HECHO