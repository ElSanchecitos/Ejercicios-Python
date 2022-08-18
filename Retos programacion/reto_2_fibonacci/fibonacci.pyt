"""
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
*/
"""

def fibonacci(rango):
    fibo = [0,1]
    for num in range(rango-2):
        fibo.append(fibo[-1]+fibo[-2])
    return fibo

print(fibonacci(10))