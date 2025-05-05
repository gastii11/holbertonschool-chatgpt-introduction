#!/usr/bin/python3
import sys

# Verificamos si hay argumentos
if len(sys.argv) > 1:
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")
else:
    print("No se proporcionaron argumentos.")
