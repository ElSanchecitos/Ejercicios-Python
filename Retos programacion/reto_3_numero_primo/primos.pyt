"""
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""

def primos(limite):
    divisores = 0
    result = ""
    for x in range(1,limite+1):
        divisores = 0
        for i in range(1,limite+1):
            if x % i == 0:
                divisores +=1
        if divisores ==2:
            result = f"Es número primo {x}"
            print(result)
        else:
            result = f"No es número primo {x}"
            print(result)

primos(100)