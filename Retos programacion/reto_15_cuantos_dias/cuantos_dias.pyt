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



MESES = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def diference_year(year_1: str, year_2: str):
    max_year = 0
    min_year = 0
    diferencia_años = 0
    año = 365
    year_1_int = int(year_1)
    year_2_int = int(year_2)

    if year_1_int > year_2_int:
        max_year = year_1_int
        min_year = year_2_int
        diferencia_años = (max_year - min_year) * año
    elif year_2_int > year_1_int:
        max_year = year_2_int
        min_year = year_1_int
        diferencia_años = (max_year - min_year) * año
    
    return diferencia_años

print(diference_year("2019", "2020"))

def difference_days_month_equal(day1:  str, day2: str):
    diferencia = 0
    day1_int = int(day2)
    day2_int = int(day1)

    diferencia = day1_int - day2_int
    
    if diferencia < 0:
        diferencia = diferencia * -1
        
    return diferencia


print(difference_days_month_equal(1, 31))
print(difference_days_month_equal(31, 1))


def difference_days_month_diferent(day1 : str, month1: str, day2: str, month2: str):
    diferencia = 0
    min_month = 0
    max_month = 0
    suma_meses = 0
    
    #conversiones
    day1_int = int(day1)
    day2_int = int(day2)
    month1_int = int(month1)
    month2_int = int(month2)

    if month1 > month2:
        max_month = month1_int
        min_month = month2_int
    elif month2 > month1:
        max_month = month2_int
        min_month = month1_int


    new_month = min_month
    # for num in range(new_month, max_month-1, 1):
    #     suma_meses += MESES[new_month + 1]
    
    while new_month < max_month - 1:
        new_month += 1
        suma_meses += MESES[new_month]

    diferencia = (MESES[month1_int] - day1_int) + day2_int + suma_meses
    
    if diferencia < 0:
        diferencia = diferencia * -1

    return diferencia


print(difference_days_month_diferent(day1=15, day2=17, month1=8, month2=5))
print(difference_days_month_diferent(day1=17, day2=15, month1=5, month2=8))


def daysbetween(date1: str, date2: str):
    split_date1 = date1.split("/")
    split_date2 = date2.split("/")
    new_date1 = []
    new_date2 = []
    diference = 0
    nums = ["0","1","2","3","4","5","6","7","8","9", "/"]


    try:
        #Validaciones
        if len(date1) == len(date2):
            for i in range(len(date1)):
                if date1[i] in nums and date2[i] in nums:
                    for x in range(0,len(split_date1)):
                        new_date1.append(split_date1[x])
                        new_date2.append(split_date2[x])

                elif date1[i] not in nums or date2[i] not in nums:
                    return "Caracter incorrecto"
        else:
            return f"No tienen la misma longitud las dos cadenas o no cumplen las condiciones"
        
        if new_date1[1] == new_date2[1]:
            days = difference_days_month_equal(day1=new_date1[0], day2=new_date2[0])
            years = diference_year(year_1=new_date1[2], year_2=new_date2[2])
            diference = days + years

        elif new_date1[1] != new_date2[1]:
            days = difference_days_month_diferent(day1=new_date1[0], day2=new_date2[0], month1=new_date1[1], month2=new_date2[1])
            years = diference_year(year_1=new_date1[2], year_2=new_date2[2])
            diference = days + years

        return f"{diference} days"

    except Exception as e:
        return f"Ocurrio un error: {e}"


fecha1 = "17/05/2020"
fecha2 = "15/06/2020"
print(daysbetween(fecha1, fecha2))


