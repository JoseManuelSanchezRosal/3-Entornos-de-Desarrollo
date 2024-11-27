'''Ejercicio 3: Gestión de inventario. El siguiente código gestiona un inventario. Refactorízalo para que haya funciones separadas 
para agregar, eliminar y mostrar productos.'''

# Código inicial


def agregarProducto(producto):
    productos.append(producto)
    print(f"Producto '{producto}' agregado.")

def eliminarProducto(producto):
    if producto in productos:
        productos.remove(producto)
        print(f"Producto '{producto}' eliminado.")
    else:
        print("El producto no existe en el inventario.")

def mostrarProducto(producto):
    print("Productos en el inventario:")
    for producto in productos:
        print(f"- {producto}")

def pedirProducto():
    producto = input("Introduce el nombre del producto: ")
    return producto
    

if __name__ == '__main__':# Declaramos nuestro main menu
    productos = []

    opcion = 100
        
    while opcion !=0:
        
        opcion = int(input("¿Qué deseas hacer? (1 para agregar/2 para eliminar/3 para mostrar/0 para salir): "))
        
    
        if opcion == 1:
            #producto = pedirProducto()
            #agregarProducto(producto)
            agregarProducto(pedirProducto())
            
        elif opcion == 2:
            eliminarProducto(pedirProducto())
        elif opcion == 3:
            mostrarProducto(pedirProducto())
        elif opcion == 0:
            print("Saliendo del programa....")
        else:
            print("Acción no válida.")
        
        
