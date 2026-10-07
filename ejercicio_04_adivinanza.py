"""
EJERCICIO 04: Adivina el número

1. Selecciona un número entero y almacenalo en una variable. 
2. Pide al usuario que lo adivine dentro de un bucle while. 
3. En cada intento, el programa debe indicar si el número buscado es mayor o menor que el ingresado, hasta que lo adivine.
"""

numero_secreto = 67
intento = None

while intento != numero_secreto:
    try:
        intento = int(input("Adivina el número: "))
        if intento < numero_secreto:
            print("El número es MAYOR.")
        elif intento > numero_secreto:
            print("El número es MENOR.")
    except ValueError:
        print("Ingresa un número entero.")

print("¡Correcto! Adivinaste el número.")