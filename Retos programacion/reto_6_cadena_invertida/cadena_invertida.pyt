
"""
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
*/
"""

def cadena_invertida(string: str):
    contador = 1
    pala_invertida = ""
    while contador <= len(string):
        pala_invertida += string[-contador]
        contador += 1
    return pala_invertida


print(cadena_invertida("hola mundo"))


def invertir_cadena(string: str):
    palabra_inver = ""
    for i in range(len(string)-1,-1,-1):
        palabra_inver += string[i]
    return palabra_inver
print(invertir_cadena("hola"))