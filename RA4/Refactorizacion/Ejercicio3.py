# Código inicial
productos = []

accion = input("¿Qué deseas hacer? (agregar/eliminar/mostrar): ")

if accion == "agregar":
    producto = input("Introduce el nombre del producto: ")
    productos.append(producto)
    print(f"Producto '{producto}' agregado.")
elif accion == "eliminar":
    producto = input("Introduce el nombre del producto a eliminar: ")
    if producto in productos:
        productos.remove(producto)
        print(f"Producto '{producto}' eliminado.")
    else:
        print("El producto no existe en el inventario.")
elif accion == "mostrar":
    print("Productos en el inventario:")
    for producto in productos:
        print(f"- {producto}")
else:
    print("Acción no válida.")