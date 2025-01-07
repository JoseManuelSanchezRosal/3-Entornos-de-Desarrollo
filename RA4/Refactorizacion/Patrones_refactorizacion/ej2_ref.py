'''Ejercicio 2: Extraer Método
Objetivo: Extraer bloques de código repetidos en una función que calcula el promedio de edades.'''

def process_ages(ages):
    total = 0
    for age in ages:
        if age > 0:
            total += age
    average = calculate_total(ages, total)
    print(f"Total: {total}, Average: {average}")

def calculate_total(ages, total):
    average = total / len(ages)
    return average