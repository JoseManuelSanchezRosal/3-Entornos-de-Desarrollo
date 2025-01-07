'''Ejercicio 3: Convertir Valores en Constantes
Objetivo: Eliminar valores no-estáticos de un cálculo de descuentos.'''

def calculate_price(price):
    discounted_price = price - (price * 0.15)
    final_price = discounted_price + (discounted_price * 0.21)
    print(f"Final price: {final_price}")

calculate_price(100)