"""
/*
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/
 *   mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
*/
"""



#from PIL import Image
#import time

#De forma en la lcoal
# def abrir_imagen(img: str):
#     tiempoIn = time.time()
#     ruta = ("C:/Users/user/Downloads/" + img)
#     img = Image.open(ruta)
#     img.show()
#     tiempoFin = time.time()
#     print(f"El proceso tardo, {tiempoFin - tiempoIn} segundos")


# abrir_imagen("caño_cristales.jpg")





#import urllib.request
# with urllib.request.urlopen("http://www.google.org") as url:
#     s = url.read()
#     print(s)


# Abrir imagen desde una url
import urllib.request
from PIL import Image

try:
    #url_img = "https://www.notebookcheck.org/fileadmin/Notebooks/News/_nc3/Lenovo_Legion_5_Pro_Back_Ports_Stingray_e1610420265467_1536x530.png"
    #url_img = "https://media.geeksforgeeks.org/wp-content/uploads/20210318103632/gfg-300x300.png"
    #url_img = "https://www.professionalwireless.com.co/wp-content/uploads/2022/05/Legion-5-Pro-16ITH6-82JF0000US_4.png"
    url_img = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"
    ruta_archivo = "D:/Repositorios Github/Ejercicios-Python/Retos programacion/reto_5_aspect_ratio_imagen/img/mouredev.png"
    urllib.request.urlretrieve(url_img, ruta_archivo)

    img = Image.open(ruta_archivo)
    img.show()
except Exception as e:
    print("Ocurrió un error: ", e)



