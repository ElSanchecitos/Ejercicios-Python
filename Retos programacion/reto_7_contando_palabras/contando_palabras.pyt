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




def count_letter(string, letter):
    string.lower()
    letter.lower()

    repeticiones = 0
    for letra in string:
        repeticiones = 0
        for sub_letra in string:
            if sub_letra == letter:
                repeticiones += 1
    return repeticiones


def eliminar_repetidos(string=None, iterable=None):
    sin_repe_str = []
    sin_repe_list = []
    if isinstance(string, str):
        string.lower()
        for letra in string:
            if letra not in sin_repe_str:
                sin_repe_str.append(letra)
    elif isinstance(iterable, list):
        for item in iterable:
            if item not in sin_repe_list:
                sin_repe_list.append(item)

    return sin_repe_list


#print(eliminar_repetidos(string="eexwwwr"))
## \
def eliminar_simbolos(text: str):
    simbolos = [")","(",",",".","  "]
    for simbolo in simbolos:
        for letra in text:
            if letra == simbolo:
                new_text = text.replace(letra, ",")
    
    new_text_split = new_text.split(" ")
    new_text_join = " ,".join(new_text_split)
    new_text_join.replace("(", ",")
    #new_text_split = new_text_join.split(",")
    #new_text_join = " ,".join(new_text_split)
    print(new_text_join)

eliminar_simbolos("Hola, mi nombre es brais. Mi nombre completo es Brais Moure (MoureDev).")

def count_letters_text(string: str):
    new_lista = []
    for palabra in string:
        contador = count_letter(string,palabra)
        #diccionario[palabra] = contador
        valor = [palabra, contador]
        new_lista.append(valor)

    result = eliminar_repetidos(iterable=new_lista)
    for lista in result:
        print(f"La letra {lista[0]} se repite {lista[1]} veces")


    #for llave, valor in diccionario.items():
        #print(f"La palabra {llave} se repite {valor} veces")

count_letters_text("inicio")
#count_words("Hola, mi nombre es brais. Mi nombre completo es Brais Moure (MoureDev).")


#print(count_letter("Hola", "o"))


lista = [1,2]
print(bool(lista))



lista = [1,2,3,4]
print(len(lista)-1)
lista.pop(0)
print(lista)

num = 10
print(type(num) == int)

print(["1",3] == ["1",3])
