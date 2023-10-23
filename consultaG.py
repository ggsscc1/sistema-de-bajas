import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import openpyxl
from openpyxl.chart import BarChart, PieChart, Reference
import matplotlib.pyplot as plt
import mysql.connector
import numpy as np
from collections import defaultdict

# Funciones para manejar los eventos de los botones

def guardar_grafica(libro_excel):
    # Obtener la ubicación seleccionada para guardar el archivo
    ubicacion = filedialog.asksaveasfilename(defaultextension='.xlsx')
    
    # Guardar el archivo de Excel
    libro_excel.save(ubicacion)
    
    # Mostrar mensaje de confirmación
    messagebox.showinfo(message="Archivo guardado con exito", title="Guardado")

def consulta_carrera2(resultados):
    plt.close()
    # Crear la gráfica de barras en el mostrador
    #generaciones = [resultado[8] for resultado in resultados]
    #cantidades = [resultado[8] for resultado in resultados]
    # Procesa los resultados para contar la cantidad de cada generación
    carrera_count = defaultdict(int)
    for fila in resultados:
            carrera = fila[7]  # Supongamos que la generación está en el tercer campo (índice 2)
            carrera_count[carrera] += 1

    # Separa las generaciones y cantidades en listas separadas
    carreras = (list(carrera_count.keys()))
    cantidades = list(carrera_count.values())
    plt.figure(figsize=(16, 9)) 
    plt.pie(cantidades, labels=carreras, autopct = '%1.1f%%')
    plt.title('Cantidad de alumnos por carrera')
    # Mostrar la gráfica en una ventana
    plt.show()



def consulta_generacion2(resultados):
    plt.close()
    generacion_count = defaultdict(int)
    for fila in resultados:
            generacion = fila[8]  # Supongamos que la generación está en el tercer campo (índice 2)
            generacion_count[generacion] += 1

    # Separa las generaciones y cantidades en listas separadas
    generaciones = list(generacion_count.keys())
    cantidades = list(generacion_count.values())
    # Ajusta el ancho y alto de la figura
    plt.figure(figsize=(16, 9)) 
    # Configurar las etiquetas en el eje X
    plt.xticks(rotation=-15, fontsize=10)
    plt.bar(generaciones, cantidades)
    plt.xlabel('Generación')
    plt.ylabel('Cantidad de alumnos')
    plt.xscale('linear')
    max_value = max(cantidades)
    plt.yticks(np.arange(0, max_value+1, 1))
    plt.title('Cantidad de alumnos por generación')

    # Mostrar la gráfica en una ventana
    plt.show()

def consulta_escuela2(resultados):
    
    plt.close()
    # Procesa los resultados para contar la cantidad de cada generación
    escuela_count = defaultdict(int)
    #mayor
    
    for fila in resultados:
            escuela = fila[11]  # Supongamos que la generación está en el tercer campo (índice 2)
            escuela_count[escuela] += 1


    # Separa las generaciones y cantidades en listas separadas
    
    escuelas = list(escuela_count.keys())
    cantidades = list(escuela_count.values())
    # Ajusta el ancho y alto de la figura
    plt.figure(figsize=(16, 9)) 
    # Configurar las etiquetas en el eje X
    plt.xticks(rotation=-15, fontsize=7)
    plt.bar(escuelas, cantidades)
    plt.xlabel('Escuela de procedencia')
    plt.ylabel('Cantidad de alumnos')
    plt.yscale('linear')
    max_value = max(cantidades)
    plt.yticks(np.arange(0, max_value+1, 1))
    plt.title('Cantidad de alumnos por Escuela')

    # Mostrar la gráfica en una ventana
    plt.show()

def consulta_tramite2(resultados):
    
    plt.close()
    # Procesa los resultados para contar la cantidad de cada generación
    tramite_count = defaultdict(int)
    #mayor
    
    for fila in resultados:
            tramite = fila[10]  
            tramite_count[tramite] += 1


    # Separa las generaciones y cantidades en listas separadas
    
    tramites = list(tramite_count.keys())
    cantidades = list(tramite_count.values())
    #plt.figure().set_figwidth(18)
    # Obtener el valor más grande de las cantidades
    

    # Ajusta el ancho y alto de la figura
    plt.figure(figsize=(16, 9)) 
    # Configurar las etiquetas en el eje X
    plt.xticks(rotation=-15, fontsize=10)
    plt.bar(tramites, cantidades)
    plt.xlabel('Tramites de baja.')
    plt.ylabel('Cantidad de alumnos')
    plt.yscale('linear')
    max_value = max(cantidades)
    plt.yticks(np.arange(0, max_value+1, 1))
    plt.title('Cantidad de alumnos por tramite')

    # Mostrar la gráfica en una ventana
    plt.show()



def consulta_materia2(resultados):
    plt.close()
    columnas_materias = [fila[12] for fila in resultados] + [fila[13] for fila in resultados] + [fila[14] for fila in resultados]

    # Combina los valores de las tres columnas en una sola lista
    materias = [materia for materia in columnas_materias if materia]
    #print(materias)
    # Cuenta la cantidad de repeticiones de cada materia en la lista
    materia_count = defaultdict(int)
    for materia in materias:
        materia_count[materia] += 1

    # Separa las materias y cantidades en listas separadas
    materias = list(materia_count.keys())
    cantidades = list(materia_count.values())
    
    # Ajusta el ancho y alto de la figura
    plt.figure(figsize=(16, 9)) 
    # Configurar las etiquetas en el eje X
    plt.xticks(rotation=-15, fontsize=7)
    plt.bar(materias, cantidades)
    plt.xlabel('Materias')
    plt.ylabel('Cantidad de Alumnos')
    
    plt.yscale('linear')
    max_value = max(cantidades)
    plt.yticks(range(max_value + 1))
    plt.title('Cantidad de Alumnos por Materia')

    # Mostrar la gráfica en una ventana
    plt.show()








    """plt.bar(materias, cantidades)
    plt.xlabel('Materias')
    plt.ylabel('Cantidad de Alumnos')
    plt.xticks(rotation=90)  # Rotar las etiquetas del eje X para que sean legibles
    plt.yscale('linear')
    max_value = max(cantidades)
    plt.yticks(np.arange(0, max_value+1, 1))
    plt.title('Cantidad de Alumnos por Materia')

    # Mostrar la gráfica en una ventana
    plt.show()"""

"""
def consulta_generacion():
    # Establecer la conexión con la base de datos
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='datosalumnosbajas'
    )

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Ejecutar la consulta SQL para contar la cantidad de alumnos por generacion
    consulta = "SELECT generacion, COUNT(*) FROM formulario GROUP BY generacion"
    cursor.execute(consulta)

    # Obtener los resultados de la consulta
    resultados = cursor.fetchall()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

    # Crear un nuevo archivo de Excel 
    libro_excel = openpyxl.Workbook()
    hoja = libro_excel.active

    # Agregar los encabezados de columna
    hoja['A1'] = 'Generacion'
    hoja['B1'] = 'Cantidad'

    # Agregar los datos de la consulta
    fila = 2
    for resultado in resultados:
        hoja[f'A{fila}'] = resultado[0]  # Generacion
        hoja[f'B{fila}'] = resultado[1]  # Cantidad de alumnos
        fila += 1

    # Crear la gráfica de barras en excel
    grafica = BarChart()
    datos = Reference(hoja, min_col=2, min_row=1, max_row=fila-1, max_col=2)
    categorias = Reference(hoja, min_col=1, min_row=2, max_row=fila-1)
    grafica.add_data(datos, titles_from_data=True)
    grafica.set_categories(categorias)

    # Agregar la gráfica a la hoja
    hoja.add_chart(grafica, 'D1')


    # Crear la gráfica de barras en el mostrador
    generaciones = [resultado[0] for resultado in resultados]
    cantidades = [resultado[1] for resultado in resultados]
    plt.bar(generaciones, cantidades)
    plt.xlabel('Generación')
    plt.ylabel('Cantidad de alumnos')
    plt.title('Cantidad de alumnos por generación')

    # Mostrar la gráfica en una ventana
    plt.show()

    # Crear la ventana de la aplicación
    ventana = tk.Tk()

    # Agregar el botón "Guardar"
    boton_guardar = tk.Button(ventana, text='Guardar', command=guardar_grafica(libro_excel))
    boton_guardar.pack()

    # Mostrar la ventana
    ventana.mainloop()



def consulta_carrera():
    # Establecer la conexión con la base de datos
    conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='datosalumnosbajas'
    )

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Ejecutar la consulta SQL para contar la cantidad de alumnos por carrera
    consulta = "SELECT carrera, COUNT(*) FROM formulario GROUP BY carrera"
    cursor.execute(consulta)

    # Obtener los resultados de la consulta
    resultados = cursor.fetchall()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

    # Crear un nuevo archivo de Excel
    libro_excel = openpyxl.Workbook()
    hoja = libro_excel.active

    # Agregar los encabezados de columna
    hoja['A1'] = 'Carrera'
    hoja['B1'] = 'Cantidad'

    # Agregar los datos de la consulta
    fila = 2
    for resultado in resultados:
        hoja[f'A{fila}'] = resultado[0]  # Carrera
        hoja[f'B{fila}'] = resultado[1]  # Cantidad de alumnos
        fila += 1

    # Crear la gráfica de pastel
    grafica = PieChart()
    datos = Reference(hoja, min_col=2, min_row=1, max_row=fila-1, max_col=2)
    categorias = Reference(hoja, min_col=1, min_row=2, max_row=fila-1)
    grafica.add_data(datos, titles_from_data=True)
    grafica.set_categories(categorias)

    # Agregar la gráfica a la hoja
    hoja.add_chart(grafica, 'D1')

    # Crear la gráfica de barras en el mostrador
    carrera = [resultado[0] for resultado in resultados]
    cantidades = [resultado[1] for resultado in resultados]
    plt.pie(cantidades, labels=carrera)
    plt.title('Cantidad de alumnos por carrera')

    # Mostrar la gráfica en una ventana
    plt.show()

    # Obtener la ubicación seleccionada para guardar el archivo
    ubicacion = filedialog.asksaveasfilename(defaultextension='.xlsx')
    
    # Guardar el archivo de Excel
    libro_excel.save(ubicacion)
    
    # Mostrar mensaje de confirmación
    messagebox.showinfo(message="Archivo guardado con exito", title="Guardado")


def consulta_escuela():
    # Establecer la conexión con la base de datos
    conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='datosalumnosbajas'
    )

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Ejecutar la consulta SQL para contar la cantidad de alumnos por generacion
    consulta = "SELECT prepa_origen, COUNT(*) FROM formulario GROUP BY prepa_origen"
    cursor.execute(consulta)

    # Obtener los resultados de la consulta
    resultados = cursor.fetchall()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

    # Crear un nuevo archivo de Excel
    libro_excel = openpyxl.Workbook()
    hoja = libro_excel.active

    # Agregar los encabezados de columna
    hoja['A1'] = 'Escuela de procedencia'
    hoja['B1'] = 'Cantidad'

    # Agregar los datos de la consulta
    fila = 2
    for resultado in resultados:
        hoja[f'A{fila}'] = resultado[0]  #Escuela de procedencia
        hoja[f'B{fila}'] = resultado[1]  # Cantidad de alumnos
        fila += 1

    # Crear la gráfica de barras
    grafica = BarChart()
    datos = Reference(hoja, min_col=2, min_row=1, max_row=fila-1, max_col=2)
    categorias = Reference(hoja, min_col=1, min_row=2, max_row=fila-1)
    grafica.add_data(datos, titles_from_data=True)
    grafica.set_categories(categorias)

    # Agregar la gráfica a la hoja
    hoja.add_chart(grafica, 'D1')

     # Crear la gráfica de barras en el mostrador
    escuelas = [resultado[0] for resultado in resultados]
    cantidades = [resultado[1] for resultado in resultados]
    plt.bar(escuelas, cantidades)
    plt.xlabel('Escuelas')
    plt.ylabel('Cantidad de alumnos')
    plt.title('Cantidad de alumnos por escuela de procedencia')

    # Mostrar la gráfica en una ventana
    plt.show()

     # Obtener la ubicación seleccionada para guardar el archivo
    ubicacion = filedialog.asksaveasfilename(defaultextension='.xlsx')
    
    # Guardar el archivo de Excel
    libro_excel.save(ubicacion)
    
    # Mostrar mensaje de confirmación
    messagebox.showinfo(message="Archivo guardado con exito", title="Guardado")

def consulta_materia():
    import openpyxl
    from openpyxl.chart import BarChart, Reference

    import mysql.connector

    # Establecer la conexión con la base de datos
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='datosalumnosbajas'
    )

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Ejecutar la consulta SQL para obtener los datos de la columna "matfi1"
    consulta_matfi1 = "SELECT matdif1, COUNT(*) FROM formulario GROUP BY matdif1"
    cursor.execute(consulta_matfi1)
    resultados_matfi1 = cursor.fetchall()

    # Ejecutar la consulta SQL para obtener los datos de la columna "matdi2"
    consulta_matdi2 = "SELECT matdif2, COUNT(*) FROM formulario GROUP BY matdif2"
    cursor.execute(consulta_matdi2)
    resultados_matdi2 = cursor.fetchall()

    # Ejecutar la consulta SQL para obtener los datos de la columna "matdif3"
    consulta_matdif3 = "SELECT matdif3, COUNT(*) FROM formulario GROUP BY matdif3"
    cursor.execute(consulta_matdif3)
    resultados_matdif3 = cursor.fetchall()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

    # Crear un nuevo archivo de Excel
    libro_excel = openpyxl.Workbook()
    hoja = libro_excel.active

    # Agregar los encabezados de columna
    hoja['A1'] = 'Matdif1'
    hoja['B1'] = 'Matdif2'
    hoja['C1'] = 'Matdif3'

    # Agregar los datos de la columna "matfi1"
    fila = 2
    for resultado in resultados_matfi1:
        hoja[f'A{fila}'] = resultado[0]  # Matfi1
        hoja[f'B{fila}'] = resultado[1]  # Matfi1
        fila += 1

    # Agregar los datos de la columna "matdi2"
    for resultado in resultados_matdi2:
        hoja[f'A{fila}'] = resultado[0]  # Matfi1
        hoja[f'B{fila}'] = resultado[1]  # Matfi1
        fila += 1

    # Agregar los datos de la columna "matdif3"
    for resultado in resultados_matdif3:
        hoja[f'A{fila}'] = resultado[0]  # Matfi1
        hoja[f'B{fila}'] = resultado[1]  # Matfi1
        fila += 1

    # Crear la gráfica de barras para "matfi1"
    grafica_matfi1 = BarChart()
    datos_matfi1 = Reference(hoja, min_col=2, min_row=1, max_row=fila-1, max_col=2)
    categorias = Reference(hoja, min_col=1, min_row=2, max_row=fila-1)
    grafica_matfi1.add_data(datos_matfi1, titles_from_data=True)
    grafica_matfi1.set_categories(categorias)
    hoja.add_chart(grafica_matfi1, 'E1')

    # Crear la gráfica de barras
    #grafica = BarChart()
    #datos = Reference(hoja, min_col=2, min_row=1, max_row=fila-1, max_col=2)
    #categorias = Reference(hoja, min_col=1, min_row=2, max_row=fila-1)
    #grafica.add_data(datos, titles_from_data=True)
    #grafica.set_categories(categorias)

    # Crear la gráfica de barras para "matdi2"
    grafica_matdi2 = BarChart()
    datos_matdi2 = Reference(hoja, min_col=2, min_row=1, max_row=fila-1)
    grafica_matdi2.add_data(datos_matdi2, titles_from_data=True)
    hoja.add_chart(grafica_matdi2, 'E30')

    # Crear la gráfica de barras para "matdif3"
    grafica_matdif3 = BarChart()
    datos_matdif3 = Reference(hoja, min_col=3, min_row=1, max_row=fila-1)
    grafica_matdif3.add_data(datos_matdif3, titles_from_data=True)
    hoja.add_chart(grafica_matdif3, 'E50')

    # Guardar el archivo de Excel
    libro_excel.save('graficas.xlsx')

def consulta_tramite():
    # Establecer la conexión con la base de datos
    conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='datosalumnosbajas'
    )

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Ejecutar la consulta SQL para contar la cantidad de alumnos por carrera
    consulta = "SELECT motbaja, COUNT(*) FROM formulario GROUP BY motbaja"
    cursor.execute(consulta)

    # Obtener los resultados de la consulta
    resultados = cursor.fetchall()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

    # Crear un nuevo archivo de Excel
    libro_excel = openpyxl.Workbook()
    hoja = libro_excel.active

    # Agregar los encabezados de columna
    hoja['A1'] = 'Motivo de baja'
    hoja['B1'] = 'Cantidad'

    # Agregar los datos de la consulta
    fila = 2
    for resultado in resultados:
        hoja[f'A{fila}'] = resultado[0]  # Motivo de baja
        hoja[f'B{fila}'] = resultado[1]  # Cantidad de alumnos
        fila += 1

     # Crear la gráfica de barras para "motbaja"
    grafica_motbaja = BarChart()
    datos_motbaja = Reference(hoja, min_col=2, min_row=1, max_row=fila-1, max_col=2)
    categorias = Reference(hoja, min_col=1, min_row=2, max_row=fila-1)
    grafica_motbaja.add_data(datos_motbaja, titles_from_data=True)
    grafica_motbaja.set_categories(categorias)
    hoja.add_chart(grafica_motbaja, 'E1')

    # Agregar la gráfica a la hoja
    hoja.add_chart(grafica_motbaja, 'D1')

    # Crear la gráfica de barras en el mostrador
    motbj = [resultado[0] for resultado in resultados]
    cantidades = [resultado[1] for resultado in resultados]
    plt.bar(motbj, cantidades)
    plt.xlabel('Motivo de baja')
    plt.ylabel('Cantidad de alumnos')
    plt.title('Cantidad de alumnos por Motivo de baja')

     
    # Mostrar la gráfica en una ventana
    plt.show()

    # Obtener la ubicación seleccionada para guardar el archivo
    ubicacion = filedialog.asksaveasfilename(defaultextension='.xlsx')
    
    # Guardar el archivo de Excel
    libro_excel.save(ubicacion)
    
    # Mostrar mensaje de confirmación
    messagebox.showinfo(message="Archivo guardado con exito", title="Guardado")




def cosulta_grafica():
    # Crear la ventana
    ventana = tk.Tk()
    ventana.title("Consulta")

    # Crear los botones
    btn_generacion = tk.Button(ventana, text="Consulta por Generacion", command=consulta_generacion)
    btn_generacion.pack()

    btn_carrera = tk.Button(ventana, text="Consulta por Carrera", command=consulta_carrera)
    btn_carrera.pack()

    btn_escuela = tk.Button(ventana, text="Consulta por Escuela de procedencia", command=consulta_escuela)
    btn_escuela.pack()

    btn_tramite = tk.Button(ventana, text="Consulta por Tramite", command=consulta_tramite)
    btn_tramite.pack()


    btn_materia = tk.Button(ventana, text="Consulta por materia mas dificil", command=consulta_materia)
    btn_materia.pack()

    # Ejecutar el bucle principal de la ventana
    ventana.mainloop()
"""