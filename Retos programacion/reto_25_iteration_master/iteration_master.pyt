"""
/*
 * Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
 * ¿De cuántas maneras eres capaz de hacerlo?
 * Crea el código para cada una de ellas.
 */
"""

#Forma 1
for i in range(1,101,1):
    #print(i)
    pass

#Forma 2
a = 1
while a <= 100:
    print(a)
    a += 1

#Forma 3
x = 0
if x + 1 == 100:
    print(x)
else:
    x+=1
    