"""
/*
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
 * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
*/
"""

def palindromo(string: str):
    return string[0::].lower() == string[::-1].lower()

print(palindromo("ANA"))

str1 = "lucia"
# print(str1[0:])
# print(str1[::-1])
# print(str1[::-1] == str1[0::])