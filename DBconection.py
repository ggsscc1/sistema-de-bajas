import mysql.connector

#Clase principal para la realización de consultas en la base de datos
class ConexionBD:
    #Valores iniciales
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexion = None

    #Función para conectarse a la base de datos
    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            #print("Conexión exitosa a la base de datos")
        except mysql.connector.Error as error:
            print(f"Error al conectar a la base de datos: {error}")

    #Función para desconectarse de la base de datos
    def desconectar(self):
        if self.conexion:
            self.conexion.close()
            #print("Desconexión exitosa de la base de datos")

    #Función para realizar la consulta requerida
    def ejecutar_consulta(self, consulta):
        if self.conexion:
            try:
                cursor = self.conexion.cursor()
                cursor.execute(consulta)
                resultados = cursor.fetchall()
                self.conexion.commit()
                return resultados
                
            except mysql.connector.Error as error:
                print(f"Error al ejecutar la consulta: {error}")    