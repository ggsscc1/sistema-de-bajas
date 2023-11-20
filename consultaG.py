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