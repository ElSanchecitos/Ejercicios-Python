"""
/*
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
*/
"""



def factorial(numero: int):
    facto = 1
    for num in range(1,numero+1):
        facto = facto * num
    return facto

print(factorial(2))
