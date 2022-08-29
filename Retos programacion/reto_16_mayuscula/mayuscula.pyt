"""
/*
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
*/
"""


MAYUSCULAS = {" ":" ","a":"A","b":"B","c":"C","d":"D","e":"E","f":"F","g":"G","h":"H","i":"I","j":"J","k":"K","l":"L","n":"N","m":"M","o":"O","p":"P","q":"Q","r":"R","s":"S","t":"T","u":"U","v":"V","w":"W","x":"X","y":"Y","z":"Z"}

#Mayuscula la primera letra del texto
def mayusculas(text:  str):
    text_mayus = ""
    body_text = text[1::]
    for clave, valor in MAYUSCULAS.items():
        if clave == text[0]:
            text_mayus = valor + body_text
        elif text[0] == valor:
            text_mayus = valor + body_text
    return text_mayus

print(mayusculas("jola"))



















#Mayuscula todo el texto
def mayusculas(text:  str):
    text_mayus = ""
    for letra in text:
        text_mayus += MAYUSCULAS[letra]
    return text_mayus

#print(mayusculas("hOla"))

def mayusculas(text:  str):
    text_mayus = ""
    for letra in text:
        for clave, valor in MAYUSCULAS.items():
            if clave == letra:
                text_mayus+= valor
            elif letra == valor:
                text_mayus+= valor
    return text_mayus

#print(mayusculas("hOlA"))

