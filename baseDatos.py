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
    dbCall(sql)


def dbCall(sql):

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

    # Iterar a través de los resultados
    for fila in resultados:
        print(fila)

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

def insertarUsuario(nombre, apellido, email, password):
    sql = "INSERT INTO `usuarios` (`nombre`, `apellido`, `email`, `password`) VALUES ('%s', '%s', '%s', '%s')" % (nombre, apellido, email, password,)
    print(sql)
    dbCall(sql)

def obtenerUsuarios():
    sql = "SELECT * FROM usuarios"
    resultado = dbCall(sql)
    return resultado

# insertarUsuario("Juan", "Perez", "a", "1234")
print(obtenerUsuarios())