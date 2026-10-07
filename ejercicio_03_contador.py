"""
EJERCICIO 03: Contador de vocales

Dada una frase escrita por el usuario, recorre cada letra e indica la cantidad de vocales (a, e, i, o, u) que tiene la palabra.
"""

frase = input("Ingresa una frase: ")
vocales = ["a","A","e","E","i","I","o","O","u","U"]
contador = 0

for letra in frase:
    if letra.lower() in vocales:
        contador += 1

print(f"La frase contiene {contador} vocales.")
