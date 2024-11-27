'''Ejercicio 3: Gestión de inventario. El siguiente código gestiona un inventario. Refactorízalo para que haya funciones separadas 
para agregar, eliminar y mostrar productos.'''

# Código inicial
productos = []

accion = input("¿Qué deseas hacer? (agregar/eliminar/mostrar): ")

def agregarProducto():
    producto = input("Introduce el nombre del producto: ")
    productos.append(producto)
    print(f"Producto '{producto}' agregado.")

def eliminarProducto():
    producto = input("Introduce el nombre del producto a eliminar: ")
    if producto in productos:
        productos.remove(producto)
        print(f"Producto '{producto}' eliminado.")
    else:
        print("El producto no existe en el inventario.")

def mostrarProducto():
    print("Productos en el inventario:")
    for producto in productos:
        print(f"- {producto}")

if accion == "agregar":
    agregarProducto()
elif accion == "eliminar":
    eliminarProducto()
elif accion == "mostrar":
    mostrarProducto()
else:
    print("Acción no válida.")