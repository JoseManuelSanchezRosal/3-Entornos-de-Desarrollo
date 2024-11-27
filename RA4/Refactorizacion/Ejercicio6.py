'''Ejercicio 6: Generación de contraseñas. El siguiente código genera contraseñas. Refactorízalo para separar la 
generación de caracteres, mezcla de caracteres y la impresión de la contraseña.'''


def generacionCaracteres(caracteres):
    import string
    caracteres = string.ascii_letters + string.digits
    return caracteres

def mezclaCaracteres(caracteres):
    import random
    contraseña = ''.join(random.choice(caracteres))
    return contraseña
                         
    
def imprimirContrasenia(longitud):
    for _ in range(longitud):
        print(f"Contraseña generada: {mezclaCaracteres()}")
    
    
    

def generar_contraseña(longitud):
    generacionCaracteres()
    mezclaCaracteres()
    imprimirContrasenia(6)

if __name__ == '__main__':# Declaramos nuestro main menu
    generar_contraseña(6)

# SIN TERMINAR