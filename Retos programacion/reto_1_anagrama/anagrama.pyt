"""
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""


"""
def anagrama(palabra_1: str, palabra_2: str):
    palabra_1.lower()
    palabra_2.lower()
    new_palabra_1 = set()
    new_palabra_2 = set()
    if palabra_1 == palabra_2:
        return False
    else:
        for letra_1 in palabra_1:
            for letra_2 in palabra_2:
                if letra_1 == letra_2:
                    new_palabra_1.add(letra_1)
                    new_palabra_2.add(letra_2)
                    print(new_palabra_1, new_palabra_2)
                    print(len(new_palabra_1), (new_palabra_2))

        if len(palabra_1) == len(new_palabra_1) and len(palabra_2) == len(new_palabra_2):
            return True
        else:
            return False
"""
#print(anagrama("trata", "tarta"))
# print(anagrama("jabon", "banjo"))
# print(anagrama("amor", "roma"))
# print(anagrama("saco", "sapo"))
# print(anagrama("hola", "alof"))

def is_anagrama(pala_1: str, pala_2: str):
    if pala_1 == pala_2:
        return False
    else:
        lista_1 = list(pala_1)
        lista_1.sort()
        lista_2 = list(pala_2)
        lista_2.sort()
        if lista_1 == lista_2:
            return True
        else:
            return False

print(is_anagrama("trata", "tarta"))
print(is_anagrama("jabon", "banjo"))
print(is_anagrama("amor", "roma"))
print(is_anagrama("saco", "sapo"))
print(is_anagrama("hola", "alof"))

