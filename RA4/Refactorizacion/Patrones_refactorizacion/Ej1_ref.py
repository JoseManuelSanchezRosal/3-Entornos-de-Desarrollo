'''Ejercicio 1: Renombrar Variables
Objetivo: Cambiar nombres poco descriptivos a otros más significativos en un cálculo de salarios.'''


def calculate_salary(hours, price):
    salary = hours * price
    print(f"Total salary: {salary}")

hourly_price = 15
hours_worked = 40
calculate_salary(hourly_price, hours_worked)