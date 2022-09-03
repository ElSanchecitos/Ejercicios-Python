"""
/*
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cierran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
*/
"""


parentesis_open = "("
parentesis_close = ")"
corchetes_open = "["
corchetes_close = "]"
llaves_open = "{"
llaves_close = "}"

def expresiones(texto):
    
    expresiones_open = []
    expresiones_close = []
    
    for num in range(len(texto)):
        if texto[num] == parentesis_open:
            expresiones_open.append(texto[num])
        elif texto[num] == parentesis_close:
            expresiones_close.append(texto[num])
        elif texto[num] == corchetes_open:
            expresiones_open.append(texto[num])
        elif texto[num] == corchetes_close:
            expresiones_close.append(texto[num])
        elif texto[num] == llaves_open:
            expresiones_open.append(texto[num])
        elif texto[num] == llaves_close:
            expresiones_close.append(texto[num])
    
    return expresiones_open, expresiones_close

#Solucion a Presentar
def expresiones_equilibradas(expresion):
    expresiones_var = expresiones(expresion)
    list_item_zero = expresiones_var[0]
    list_item_one = expresiones_var[1]
    
    if len(list_item_zero) != len(list_item_one):
        return "No es está equilibrada"
    elif len(list_item_zero) == len(list_item_one):
        return "Está equilibrada"

print(expresiones_equilibradas("{ a * [ ( c + d ) ] - 5 } ( { a * [ c + d ] } - 5 ) { a * ( c + d ) ] - 5 }"))

