# __init__.py
"""Importamos del archivo geometria las funciones para calcular el area del circulo y el perimetro del rectangulo.
"""
from .geometria import area_circulo, perimetro_rectangulo

from .algebra import resolver_ecuacion_lineal, determinante_matriz_2x2



if __name__ == "__main__":
    """Usamos la funcion para calcular el area de un circulo de radio 5
    """
    # Funciones de geometría
    print(area_circulo(5))  # 78.53981633974483
    print(perimetro_rectangulo(4, 5))  # 18

    # Funciones de álgebra
    print(resolver_ecuacion_lineal(2, -4))  # 2.0
    print(determinante_matriz_2x2(1, 2, 3, 4))  # -2