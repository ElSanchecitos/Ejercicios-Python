"""
/*
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
*/
"""


#Forma 1
def code_morse(cadena: str):
    str_morse = ""
    morse = {" ":" ","A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","N":"-.","M":"--","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----."}
    for letra in cadena:
        for clave, valor in morse.items():
            if letra.upper() == clave:
                str_morse+=valor
    return str_morse

#print(code_morse("Diego Miguel Sanchez Buitrago"))

# cadena = "Hola123"
# for e in cadena:
#     print(type(e))

MORSE = {" ":" ","A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","N":"-.","M":"--","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----."}


#Forma 2
def code_morse_2(frase: str):
    frase = frase.upper()
    frase_codificada = ""
    for letra in frase:
        frase_codificada += MORSE[letra] + " "
    return frase_codificada

print(code_morse_2("Cat"))