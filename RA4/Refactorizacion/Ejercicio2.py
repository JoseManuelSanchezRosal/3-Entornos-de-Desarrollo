# Código inicial

def imprime_cabecera():
    print("---- Informe de Ventas ----")
    
def imprime_total(ventas):
    total = 0
    #vamos añadiendo a total la cantidad de cada producto.
    for producto, cantidad in ventas.items():
        total += cantidad
    print(f"Total de ventas: {total} unidades")# Una vez recorrido todo nuestro diccionario, sacamos por pantalla el total de unidades.
    
def imprime_diccionario(ventas):
    for producto, cantidad in ventas.items():# Hacemos un bucle for para recorrer la clave valor de nuestro diccionario.
        print(f"{producto}: {cantidad} unidades") # Sacamos por pantalla cada clave y valor de nuestro diccionario en cada iteración.

def generar_informe(ventas):# En nuestra funcion original, llamamos a las funciones que hemos creado en la refactorizacion
    imprime_cabecera()
    imprime_diccionario(ventas)
    imprime_total(ventas)
    
    
if __name__ == '__main__':# Declaramos nuestro main menu
    ventas = {"Peras":3,"Manzanas":4, "Limones":5}# Creamos un diccionario.
    generar_informe(ventas)# Llamamos a la funcion de generar informe y le pasamos nuestro diccionario "ventas"