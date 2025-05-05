#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcula el factorial de un número de manera recursiva.

    Parámetros:
    - n (int): Número entero para el cual se desea calcular el factorial.

    Retornos:
    - int: Resultado del factorial de n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
