"""
/*
 * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
 * de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se
 *   lanzará una excepción.
*/
"""

from datetime import date, datetime, time

def cuantos_dias(date1: str, date2: str):
    date1_list = date1.split("/")
    date2_list = date2.split("/")
    date1_clock = date(day=int(date1_list[0]), month=int(date1_list[1]), year=int(date1_list[2]))
    date2_clock = date(day=int(date1_list[0]), month=int(date1_list[1]), year=int(date1_list[2]))

    #
    return date2_list
    
    #Validar 

print()

fecha1 = date(2020,5,13)
fecha2 = date(2020,5,15)
diferencia = fecha1 - fecha2
print(diferencia)
print(type(diferencia))
print(diferencia*-1)




# ENERO = range(1,32)
# FEBRERO = range(1,32)
# MARZO = range(1,32)
# ABRIL = range(1,32)
# MAYO = range(1,32)
# JUNIO = range(1,32)
# JULIO = range(1,32)
# AGOSTO = range(1,32)
# SEPTIEMBRE = range(1,32)
# OCTUBRE = range(1,32)
# NOVIEMBRE = range(1,32)
# DICIEMBRE = range(1,32)

# def date_str_int(date):
    
#     date_conver = []
#     for i in range(3):
#         date_conver.append(int(date[i]))
        
#     return date_conver

# def cuantos_dias(fecha1: str, fecha2: str):
#     diferencia_dias = 0
    
#     #Pasar a lista usando split
#     date1_list = fecha1.split("/")
#     date2_list = fecha2.split("/")
    
#     #Convertir de str a int
#     date1_conver = date_str_int(date1_list)
#     date2_conver = date_str_int(date2_list)

#     # diferencias de dias
#     if date1_conver[1] == date1_conver[1]:
#         diferencia_dias = date1_conver[0] - date2_conver[0]
#     elif date1_conver[1] == date1_conver[1]:
#         pass
#     if diferencia_dias < 0:
#         diferencia_dias = diferencia_dias * -1
    
#     return diferencia_dias
#     #Excepción fecha
#     # for item in fecha1:
#     #     if item =!
    
    
# print(cuantos_dias("13/5/2020", "15/5/2020"))
    
    
# a = -1 * -1
# print(a)
