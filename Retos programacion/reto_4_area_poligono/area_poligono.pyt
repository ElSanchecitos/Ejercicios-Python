"""
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
"""


def poligono_area(poligono : str):
    poligono.lower()
    if poligono == "cuadrado":
        lado_1 = int(input("Escriba el primer lado:" ))
        lado_2 = int(input("Escriba el segundo lado: "))
        return f"El área del cuadrado es {lado_1 * lado_2}"
    elif poligono ==  "triangulo":
        lado_1 = int(input("Escriba la altura:"))
        lado_2 = int(input("Escriba la base: "))
        return f"El área del triángulo es {(lado_1 * lado_2)/2}"
    elif poligono == "rectangulo":
        lado_1 = int(input("Escriba la altura: " ))
        lado_2 = int(input("Escriba la base: "))
        return f"El área del rectángulo es {(lado_1 * lado_2)}"

print(poligono_area("rectangulo"))
