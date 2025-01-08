# matematicas.py

def suma(a, b):
    """
    Suma dos números.

    Parámetros:
    a (int, float): El primer número.
    b (int, float): El segundo número.

    Retorna:
    int, float: La suma de a y b.

    Ejemplo:
    >>> suma(3, 5)
    8
    >>> suma(-1, 4)
    3
    >>> suma(2.5, 3.1)
    5.6
    """
    return a + b

def resta(a, b):
    """
    Resta el segundo número al primero.

    Parámetros:
    a (int, float): El número del cual se va a restar.
    b (int, float): El número que se va a restar.

    Retorna:
    int, float: El resultado de la resta de a y b.

    Ejemplo:
    >>> resta(10, 5)
    5
    >>> resta(4, 9)
    -5
    >>> resta(3.5, 1.2)
    2.3
    """
    return a - b

def multiplicacion(a, b):
    """
    Multiplica dos números.

    Parámetros:
    a (int, float): El primer número.
    b (int, float): El segundo número.

    Retorna:
    int, float: El producto de a y b.

    Ejemplo:
    >>> multiplicacion(3, 5)
    15
    >>> multiplicacion(-2, 4)
    -8
    >>> multiplicacion(1.5, 2.5)
    3.75
    """
    return a * b

def division(a, b):
    """
    Divide el primer número entre el segundo.

    Parámetros:
    a (int, float): El numerador.
    b (int, float): El denominador.

    Retorna:
    float: El resultado de la división de a entre b.

    Lanza:
    ValueError: Si el denominador es cero.

    Ejemplo:
    >>> division(10, 2)
    5.0
    >>> division(7, 3)
    2.3333333333333335
    >>> division(5, 0)
    Traceback (most recent call last):
        ...
    ValueError: No se puede dividir por cero
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b
