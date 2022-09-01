"""
/*
 * Crea una función que reciba días, horas, minutos y segundos (como enteros)
 * y retorne su resultado en milisegundos.
*/
"""

def milisegundos(days: int , hours: int, minutes: int, seconds: int):
    ONE_DAY =  86400 # segundos
    ONE_HOUR = 3600 # segundos
    ONE_MINUTE= 60 # segundos
    ONE_SECONDS = seconds # segundos
    
    convertidor_segundos = (days * ONE_DAY) + (hours * ONE_HOUR) + (minutes * ONE_MINUTE) + ONE_SECONDS
    convertidor_milisegundos = convertidor_segundos * 1000
    
    return convertidor_milisegundos

print(milisegundos(1, 3, 40, 50))



