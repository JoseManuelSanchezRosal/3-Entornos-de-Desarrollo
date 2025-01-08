# algebra.py

def resolver_ecuacion_lineal(a, b):
    """
    Resuelve una ecuación lineal de la forma ax + b = 0.

    Parámetros:
    a (float): El coeficiente de x.
    b (float): El término independiente.

    Retorna:
    float: El valor de x que satisface la ecuación.

    Ejemplo:
    >>> resolver_ecuacion_lineal(2, -4)
    2.0
    """
    if a == 0:
        raise ValueError("El coeficiente 'a' no puede ser cero.")
    return -b / a

def determinante_matriz_2x2(a, b, c, d):
    """
    Calcula el determinante de una matriz 2x2.

    Parámetros:
    a, b, c, d (float): Los elementos de la matriz 2x2:
                        | a  b |
                        | c  d |

    Retorna:
    float: El determinante de la matriz.

    Ejemplo:
    >>> determinante_matriz_2x2(1, 2, 3, 4)
    -2
    """
    return a * d - b * c
