"""
/*
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
*/
"""

def str_letters_difference(str1, str2):
    out1 = ""
    out2 = ""
    for i in range(len(str1)):
        if str1[i] not in str2:
            formato = str1[i]+","
            out1 += formato
    for x in range(len(str2)):
        if str2[x] not in str1:
            formato = str2[x]+","
            out2 += formato

    return f"Las palabras no repetidas son: {out1}{out2}"


print(str_letters_difference("hola","hacia"))


str1 = "Hola"
str2 = "Hacia"

for st in range(len(str1)):
    if str1[st] not in str2:
        print(str1[st])