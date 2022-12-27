"""
/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel)
 *   o "T" (tijera).
 * - Ejemplo. Entrada: [("R","T"), ("T","R"), ("P","T")]. Resultado: "Player 2".
 */
"""

def piedra_papel_tijera(jugadas: list):
    nums_player_1 = 0
    nums_player_2 = 0

    for j in range(0,len(jugadas)):
        #Forma larga
        if jugadas[j][0].lower() == "r" and jugadas[j][1].lower() == "t":
            nums_player_1 += 1
        elif jugadas[j][0].lower() == "t" and jugadas[j][1].lower() == "p":
            nums_player_1 += 1
        elif jugadas[j][0].lower() == "p" and jugadas[j][1].lower() == "r":
            nums_player_1 += 1
        else:
            nums_player_2 += 1

    if nums_player_1 > nums_player_2:
        return "Jugador 1 Gana"
    elif nums_player_2 > nums_player_1:
        return "Jugador 2 Gana"
    else:
        return "Empate"

entrada = [("R","T"), ("T","R"), ("P","T"),("P","R")]

print(piedra_papel_tijera(entrada))



#Forma corta
        # if jugadas[j][0] == "R" and jugadas[j][1] == "T" or jugadas[j][0] == "T" and jugadas[j][1] == "P" or jugadas[j][0] == "P" and jugadas[j][1] == "R":
        #     nums_player_1 += 1