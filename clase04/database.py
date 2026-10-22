""" 
    Datos necesarios para conectarnos a MYSQL:
    user = root
    contraseña = ""
    nombre_database = star_wars_aula
    nombre_servidor = 127.0.0.1 (localhost)
    puerto = 3306

    Paquete : Instalar un conectar mysql.connector

"""


import mysql.connector

def conectar():
    return mysql.connector.connect(
        host='127.0.0.1',
        port = 3306,
        user='root',
        password='',
        database='star_wars_aula',
        charset= 'utf8mb4',
        # Implementacion interna con python
        use_pure=True
    )



conexion = conectar()
# cursor = me permite trabajar con base datos con python
cursor = conexion.cursor()

try:
    # La query sql que quiero ejecturar
    cursor.execute("SELECT * FROM personajes WHERE nombre LIKE '%Darth%' ")
    # convertirlos en un array
    resultados = cursor.fetchall()

    for fila in resultados:
        print(fila)

finally:
    # cerrar la ejecuciones
    cursor.close()
    # cerrar la conexion
    cursor.close()


