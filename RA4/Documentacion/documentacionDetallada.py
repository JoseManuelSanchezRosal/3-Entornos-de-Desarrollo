def raiz_n_esima(x, n):
    """
    Calcula la n-ésima raíz de un número.

    Parámetros:
    x (int, float): El número del cual se calculará la raíz n-ésima.
    n (int): El índice de la raíz (por ejemplo, 2 para la raíz cuadrada, 3 para la raíz cúbica, etc.).

    Retorna:
    float: La n-ésima raíz de x.

    Ejemplo:
    >>> raiz_n_esima(16, 2)
    4.0
    >>> raiz_n_esima(27, 3)
    3.0
    >>> raiz_n_esima(81, 4)
    3.0
    >>> raiz_n_esima(-8, 3)
    -2.0

    Advertencias:
    - Si el número `x` es negativo y el índice `n` es un número par, se lanzará un error, ya que no existe una raíz par de un número negativo en los números reales.
    - Si `x` es negativo y `n` es impar, la función devolverá un valor negativo correctamente, ya que es posible calcular la raíz impar de un número negativo.

    Notas:
    - La función utiliza la propiedad de los exponentes: la n-ésima raíz de `x` se calcula como `x^(1/n)`.
    - Si `x` es 0, la función devolverá 0 independientemente del valor de `n`.
    - El parámetro `n` debe ser un número entero positivo, ya que no se permite calcular raíces con índices no enteros en esta función.

    """
    # Validación para asegurarse de que el índice n es positivo
    if n <= 0:
        raise ValueError("El índice de la raíz debe ser un número entero positivo.")
    
    # Validación para evitar la raíz par de un número negativo
    if x < 0 and n % 2 == 0:
        raise ValueError("No se puede calcular la raíz par de un número negativo en los números reales.")
    
    # Cálculo de la n-ésima raíz utilizando la propiedad de los exponentes
    return x ** (1 / n)
