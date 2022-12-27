"""
/*
 * Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes
 *   de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes
 *   de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""



def sets(array_1: list, array_2: list, boleano: bool):
    result_array = []
    
    if boleano is True:
        for x in array_1:
            for y in array_2:
                if x == y:
                    result_array.append(x)
    elif boleano is False:
        for x in array_1:
            if x not in array_2:
                result_array.append(x)

        for y in array_2:
            if y not in array_1:
                result_array.append(y)

    return result_array

print(sets(array_1=[1,2,9,3,4,5], array_2=[6,4,2,1,8], boleano=True))
print(sets(array_1=[1,2,9,3,4,5], array_2=[6,4,2,1,8], boleano=False))
