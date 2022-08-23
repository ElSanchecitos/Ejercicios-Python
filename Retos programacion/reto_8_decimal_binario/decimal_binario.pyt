"""
/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
*/
"""

def decimal_binario(numero: int):
    residuo = 0
    concat_resi = ""
    binario = ""
    while numero >= 1:
        residuo = numero % 2
        numero /= 2
        residuo = str(int(residuo))
        concat_resi+=residuo
    for i in range(len(concat_resi)-1,-1,-1):
        binario += concat_resi[i]
    return binario

print(decimal_binario(28))
#print(int(725/2))