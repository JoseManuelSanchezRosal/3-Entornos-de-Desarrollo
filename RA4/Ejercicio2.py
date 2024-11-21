# Código inicial

def imprime_cabecera():
    print("---- Informe de Ventas ----")
    
def imprime_total(ventas):
    total = 0
     #vamos añadiendo a total la cantidad de cada producto.
    for producto, cantidad in ventas.items():
        total += cantidad
    print(f"Total de ventas: {total} unidades")
    
def imprime_diccionario(ventas):
    for producto, cantidad in ventas.items():#Hacemos un bucle for para recorrer la clave valor de nuestro diccionario.
        print(f"{producto}: {cantidad} unidades") #sacamos por pantalla cada clave y valor de nuestro diccionario en cada iteración.

def generar_informe(ventas):
    imprime_cabecera()
    imprime_diccionario(ventas)
    imprime_total(ventas)
    
    
if __name__ == '__main__':
    ventas = {"Peras":3,"Manzanas":4, "Limones":5}#Creamos un diccionario.
    generar_informe(ventas)