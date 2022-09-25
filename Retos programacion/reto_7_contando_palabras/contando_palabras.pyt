"""
/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
*/
"""

LETTERS = ["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","n","N","m","M","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","X","y","Y","z","Z"]


def list_letters(text: str):
    list_letters = []
    for letter in text:
        for valor in LETTERS:
            if letter == valor:
                list_letters.append(letter)
    return list_letters


def count_letters(text: str):
    letters_list = list_letters(text)
    count_letter = {}
    contador = 0 
    for letter in text:
        contador = 0
        for valor in letters_list:
            if letter == valor:
                contador += 1
                count_letter[letter] = contador
    return count_letter



print(count_letters("Hola, mi nombre es brais. Mi nombre completo es Brais Moure (MoureDev)."))
print(count_letters("ccwwwerrsasdasdasdjsadkjasvdjvsadas"))


# def eliminar_repetidos(string=None, iterable=None):
#     sin_repe_str = []
#     sin_repe_list = []
#     if isinstance(string, str):
#         string.lower()
#         for letra in string:
#             if letra not in sin_repe_str:
#                 sin_repe_str.append(letra)
#     elif isinstance(iterable, list):
#         for item in iterable:
#             if item not in sin_repe_list:
#                 sin_repe_list.append(item)

#     return sin_repe_list
