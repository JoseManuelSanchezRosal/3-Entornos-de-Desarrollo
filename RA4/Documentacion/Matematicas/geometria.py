# geometria.py

def area_circulo(radio):
    """
    Calcula el área de un círculo.

    Parámetros:
    radio (float): El radio del círculo.

    Retorna:
    float: El área del círculo.

    Ejemplo:
    >>> area_circulo(5)
    78.53981633974483
    """
    import math
    return math.pi * radio ** 2

def perimetro_rectangulo(base, altura):
    """
    Calcula el perímetro de un rectángulo.

    Parámetros:
    base (float): La base del rectángulo.
    altura (float): La altura del rectángulo.

    Retorna:
    float: El perímetro del rectángulo.

    Ejemplo:
    >>> perimetro_rectangulo(4, 5)
    18
    """
    return 2 * (base + altura)
