"""
/*
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información 
 * al respecto.
*/
"""


def arsmtrong(numero: int):
    str_num = str(numero)
    largo = len(str_num)
    suma = 0
    for i in range(largo):
        suma += int(str_num[i])**largo
        
    if suma == numero:
        return True
    else:
        return False

print(arsmtrong(153))
print(arsmtrong(407))
print(arsmtrong(371))
print(arsmtrong(54748))
print(arsmtrong(100))