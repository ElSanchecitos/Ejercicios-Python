"""
/*
 * Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
 * y retorne lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
 *   O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta.
 * Se podría representar con un vacío "", por ejemplo.
*/
"""

def tres_raya(matriz3x3: list):

    # Vamos con X

    #Horizontal
    if matriz3x3[0][0] == "X" and matriz3x3[1][0] == "X" and matriz3x3[2][0] == "X":
        return "Gana: X"
    elif matriz3x3[3][0] == "X" and matriz3x3[4][0] == "X" and matriz3x3[5][0] == "X":
        return "Gana: X"
    elif matriz3x3[6][0] == "X" and matriz3x3[7][0] == "X" and matriz3x3[8][0] == "X":
        return "Gana: X"

    #Vertical
    elif matriz3x3[0][0] == "X" and matriz3x3[3][0] == "X" and matriz3x3[6][0] == "X":
        return "Gana: X"
    elif matriz3x3[1][0] == "X" and matriz3x3[4][0] == "X" and matriz3x3[7][0] == "X":
        return "Gana: X"
    elif matriz3x3[2][0] == "X" and matriz3x3[5][0] == "X" and matriz3x3[8][0] == "X":
        return "Gana: X"

    #Diagonal
    elif matriz3x3[0][0] == "X" and matriz3x3[4][0] == "X" and matriz3x3[8][0] == "X":
        return "Gana: X"
    elif matriz3x3[2][0] == "X" and matriz3x3[4][0] == "X" and matriz3x3[6][0] == "X":
        return "Gana: X"
    
    #Vamos con O

    #Horizontal
    if matriz3x3[0][0] == "O" and matriz3x3[1][0] == "O" and matriz3x3[2][0] == "O":
        return "Gana: O"
    elif matriz3x3[3][0] == "O" and matriz3x3[4][0] == "O" and matriz3x3[5][0] == "O":
        return "Gana: O"
    elif matriz3x3[6][0] == "O" and matriz3x3[7][0] == "O" and matriz3x3[8][0] == "O":
        return "Gana: O"

    #Vertical
    elif matriz3x3[0][0] == "O" and matriz3x3[3][0] == "X" and matriz3x3[6][0] == "O":
        return "Gana: O"
    elif matriz3x3[1][0] == "O" and matriz3x3[4][0] == "X" and matriz3x3[7][0] == "O":
        return "Gana: O"
    elif matriz3x3[2][0] == "O" and matriz3x3[5][0] == "X" and matriz3x3[8][0] == "O":
        return "Gana: O"

    #Diagonal
    elif matriz3x3[0][0] == "O" and matriz3x3[4][0] == "O" and matriz3x3[8][0] == "O":
        return "Gana: O"
    elif matriz3x3[2][0] == "O" and matriz3x3[4][0] == "O" and matriz3x3[6][0] == "O":
        return "Gana: O"

    else:
        return "Nadie Gana: NULO"

matriz_2 = [

        ["O"],["X"],["O"],

        ["O"],["X"],["O"],

        ["X"],["O"],["X"]
]

matriz_1 = [

        ["X"],["O"],["X"],

        ["X"],["X"],["O"],

        ["O"],["O"],["X"]
]

print(tres_raya(matriz3x3=matriz_2))