import psycopg2
import urllib.request
import json

conexion = psycopg2.connect(
    user = "postgres",
    password = "admin",
    host = "127.0.0.1",
    port= "5432",
    database = "test_db")

print(conexion)

"""
#todos los registros
try:
    with conexion:
        with conexion.cursor() as cursor:
            #Leer datos
            sentencia = "SELECT * FROM persona"
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)

except Exception as e:
    print("Ocurrió un error:", e)
finally:
    conexion.close()
"""

"""
#Un solo registro
try:
    with conexion:
        with conexion.cursor() as cursor:
            #leer un dato
            sentencia = "SELECT * FROM persona WHERE id_persona = %s"
            id_persona = input("Proporcione el id_persona: ")
            cursor.execute(sentencia, (id_persona))
            registro = cursor.fetchone()
            print(registro)
except Exception as e:
    print("Ocurrió un erro:", e)
finally:
    conexion.close()
"""

peticion = urllib.request.Request("http://globalmentoring.com.mx/api/personas.json",
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
})

print(peticion)

respuesta = urllib.request.urlopen(peticion)

respuesta_cuerpo = respuesta.read()
print(respuesta_cuerpo)

json_decodificado = json.loads(respuesta_cuerpo.decode("utf-8"))
print(json_decodificado)