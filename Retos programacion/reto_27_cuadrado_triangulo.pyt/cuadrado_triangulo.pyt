"""
/*
 * Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 * - EXTRA: ¿Eres capaz de dibujar más figuras?
 */
"""

def dibujarFiguras(figura):
    if figura.lower() == "cuadrado":
        def cuadrado(lado):
            pass
    
    elif figura.lower() == "triangulo":
        def triangulo(base, altura):
            pass
    
    
    elif figura.lower() == "rectangulo":
        def rectangulo(base, altura):
            pass
    
    else:
        return "No se reconoce la figura"


lado = 11
new_lado = lado-2
for i in range(0,lado):
    if i == 0:
        print("*"*lado)
    elif i == lado-1:
        print("*"*lado)
    else:
        print("*"+" "*(new_lado)+"*")
        

base = 7
altura = 11
new_base = base-2
for i in range(0,altura):
    if i == 0:
        print("*"*base)
    elif i == altura-1:
        print("*"*base)
    else:
        print("*"+" "*(new_base)+"*")


base = 5
altura = 5
new_base = int(base/2) + 1
