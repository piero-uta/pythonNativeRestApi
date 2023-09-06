import mysql.connector

# Configurar la conexión a la base de datos
conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="pydb"
)

# Crear un cursor para interactuar con la base de datos
cursor = conexion.cursor()

# Ejecutar una consulta SQL
cursor.execute("SELECT * FROM prueba")

# Obtener los resultados de la consulta
resultados = cursor.fetchall()

# Iterar a través de los resultados
for fila in resultados:
    print(fila)

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
