from DBconection import *

#Función auxiliar que hace un recorrido a la lista de espera para poder tomar los datos de los alumnos
def lectura_listaEspera():
    #Inicialización de variables necesarias
    generacionL = str
    claveL = str
    nombreL = str
    ap_patL = str
    ap_matL = str
    carreraL = str

    #Inicialización de una lista para guardar los datos
    lista_alumnos = []

    #Consulta de la lista de espera, ordenada por el apellido paterno del alumno
    conexion = ConexionBD(user='newuser',password='root',host='148.224.51.68',database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT clave_unica, nombre, ap_paterno, ap_materno, carrera, generacion FROM lista_de_espera ORDER BY ap_paterno"
    resultado = conexion.ejecutar_consulta(consulta)

    inc = int
    inc = 0
    #Se recorre la lista hasta que ya no haya datos
    while inc < len(resultado) and resultado[inc][0] is not None:
        #Se guardan los valores
        claveL= resultado[inc][0]
        nombreL = resultado[inc][1]
        ap_patL = resultado[inc][2]
        ap_matL = resultado[inc][3]
        carreraL = resultado[inc][4]
        generacionL = resultado[inc][5]
        #Se ingresan en la lista
        lista_alumnos.append([ claveL, nombreL, ap_patL, ap_matL, carreraL, generacionL])

        inc += 1
    
    #Se regresa la lista de los alumnos que estaban en lista de espera
    return lista_alumnos