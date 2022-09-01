"""
/*
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
*/
"""


MAYUSCULAS = {" ":" ","a":"A","b":"B","c":"C","d":"D","e":"E","f":"F","g":"G","h":"H","i":"I","j":"J","k":"K","l":"L","n":"N","m":"M","o":"O","p":"P","q":"Q","r":"R","s":"S","t":"T","u":"U","v":"V","w":"W","x":"X","y":"Y","z":"Z"}

def mayusculas(text: str):
    text_minus = ""
    text_mayus = ""

    #Convertir todo el texto en minúscula
    for letra in text:
        for clave, valor in MAYUSCULAS.items():
            if letra == clave:
                text_minus += clave
            elif letra == valor:
                text_minus+= clave
    
    #Convertimos la primera letra en mayúscula y añadimos el cuerpo faltante
    text_mayus = MAYUSCULAS[text_minus[0]] + text_minus[1::]
    
    return text_mayus

print(mayusculas("DiEgO"))
print(mayusculas("hOLA"))



#Mayuscula la primera letra del texto
def mayusculas(text:  str):
    text_mayus = ""
    body_text = text[1::]
    #Convertimos la primera letra en mayúscula y añadimos a mayus_text
    for clave, valor in MAYUSCULAS.items():
        if clave == text[0]:
            text_mayus += valor
        elif text[0] == valor:
            text_mayus += valor
    #Convertimos el faltante en minúsculas y lo añadimos a mayus_text
    for letra in body_text:
        for clave, valor in MAYUSCULAS.items():
            if letra == valor:
                text_mayus += clave
            elif letra == clave:
                text_mayus += clave
    return text_mayus

#print(mayusculas("JOlA"))





text = "hola"
text_mayus = ""
text_mayus = MAYUSCULAS[text[0]]
print(text_mayus)















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

