"""
/*
 * Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
 * que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""

def mcm(num_1: int, num_2: int):
    num_mayor = 0
    nums_primos = []
    contador_primos = 0
    mcd = 0
    
    if num_1 > num_2:
        num_mayor = num_1
    else: 
        num_mayor = num_2
    
    for divisible in range(1,num_mayor+1, 1):
        contador_primos = 0
        for divisor in range(1, num_mayor+1, 1):
            if divisible%divisor == 0:
                contador_primos += 1
        if contador_primos == 2:
            nums_primos.append(divisible)

    mcd = num_1 * num_2
    
    for primo in nums_primos:
        if num_1%primo==0 and num_2%primo==0:
            mcd = (num_1 * num_2) / primo

    return mcd

#print(mcm(3, 9))
#print(mcm(51, 21))
#print(mcm(52, 21))



#print(9%3==0 and 9%3==1)


def mcd(num_1: int, num_2: int):
    nums_primos = []
    contador_primos = 0
    mcm_num_1 = []
    mcm_num_2 = []
    items_comunes = []
    mcd = 0
    
    if num_1 > num_2:
        num_mayor = num_1
    else:
        num_mayor = num_2
    
    for divisible in range(1,num_mayor+1, 1):
        contador_primos = 0
        for divisor in range(1, num_mayor+1, 1):
            if divisible%divisor == 0:
                contador_primos += 1
        if contador_primos == 2:
            nums_primos.append(divisible)

    for primo in nums_primos:
        if num_1%primo == 0:
            while num_1%primo == 0:
                temp = num_1 / primo
                var = temp
                num_1= var
                mcm_num_1.append(primo)
    
    for primo in nums_primos:
        while num_2%primo == 0:
            temp = num_2 / primo
            var = temp
            num_2 = var
            mcm_num_2.append(primo)

#mcd(225, 300)




#Descomponiendo en factores primos
a = 1024
lista = []
primos = [2,3,5,7,11,13,17,19]

a = 225
lista_1 = []
for primo in primos:
    while a%primo == 0:
        temp = a / primo
        b = temp
        a = b
        lista_1.append(primo)

#print(lista_1)


c = 300
lista_2 = []

for primo in primos:
    while c%primo == 0:
        temp = c / primo
        b = temp
        c = b
        lista_2.append(primo)
#print(lista_2)

mcm_num_1 = [3,3,5,5]
mcm_num_2 = [2,2,3,5,5]
lista = []
temp_count = 0

mcm_num_2.sort(reverse=True)
mcm_num_1.sort(reverse=True)

print(mcm_num_1, mcm_num_2)
