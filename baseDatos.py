import mysql.connector

def createTable():
    sql = """ CREATE TABLE IF NOT EXISTS `pydb`.`usuarios` (
        `id` INT NOT NULL AUTO_INCREMENT,
        `nombre` VARCHAR(45) NULL,
        `apellido` VARCHAR(45) NULL,
        `email` VARCHAR(45) NULL,
        `password` VARCHAR(45) NULL,
        PRIMARY KEY (`id`))
        ENGINE = InnoDB
        DEFAULT CHARACTER SET = utf8;
        """
    dbGet(sql)


def dbGet(sql):

    # Configurar la conexión a la base de datos
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="pydb"
    )

    # Crear un cursor para interactuar con la base de datos
    cursor = conexion.cursor()

    print("Conexión establecida")
    print("Ejecutando consulta...")
    print(sql)

    # Ejecutar una consulta SQL
    cursor.execute(sql)

    # Obtener los resultados de la consulta
    resultados = cursor.fetchall()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()
    return resultados


def dbUpdate(sql, values):

    # Configurar la conexión a la base de datos
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="pydb"
    )

    # Crear un cursor para interactuar con la base de datos
    cursor = conexion.cursor()

    print("Conexión establecida")
    print("Ejecutando consulta...")
    print(sql)
    print(values)

    # Ejecutar una consulta SQL
    cursor.execute(sql, values)

    conexion.commit()

    # Obtener los resultados de la consulta
    resultados = cursor.fetchall()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()
    return resultados

def insertarUsuario(nombre, apellido, email, password):
    sql = "INSERT INTO usuarios (nombre, apellido, email, password) VALUES (%s, %s, %s, %s)" 
    values = (nombre, apellido, email, password)
    dbUpdate(sql, values)

def obtenerUsuarios():
    sql = "SELECT * FROM usuarios"
    resultado = dbGet(sql)
    return resultado

insertarUsuario("Juan", "Perez", "a", "1234")
print(obtenerUsuarios())