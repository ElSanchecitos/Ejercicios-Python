"""
/*
 * Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras
 *        "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo)
 *        o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
 *        será correcto y no variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
 * Input: println(checkRace(listOf(AthleteState.RUN, AthleteState.JUMP, AthleteState.RUN, AthleteState.JUMP, AthleteState.RUN), "_|_|_"))
*/
"""

def carrera_obstaculos(array: list, string :str):
    list_array = []
    list_string = []
    validacion_pista = []
    
    for item in array:
        list_array.append(item.lower())
    
    for item in string:
        if item == "|" or item == "_":
            list_string.append(item)

    if len(list_array) == len(list_string):
        for i in range(len(list_array)):
            if (list_array[i] == "jump")== (list_string[i] == "|") or (list_array[i] == "run")== (list_string[i] == "_"):
                validacion_pista.append("/")
            elif (list_array[i] == "run")== (list_string[i] == "|") or (list_array[i] == "jump")== (list_string[i] == "_"):
                validacion_pista.append("x")
        
        for item in validacion_pista:
            if item == "x":
                return False #"No realizó bien la carrera"
            
        return True #"Realizó bien la carrera"
    else:
        return  False #"No completó la carrera"

lista = ["Run", "Jump","Run","Run"]
cadena = "____"
print(carrera_obstaculos(array=lista, string=cadena))