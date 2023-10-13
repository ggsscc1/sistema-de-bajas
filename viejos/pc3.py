from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from DBconection import *
from GeneraCarta import * 
import customtkinter
import consulta
import consultaG
import os

def limpiainfo():
    clave_alumno_label.grid_remove()
    nombre_alumno_label.grid_remove()
    carrera_alumno_label.grid_remove()
    generacion_alumno_label.grid_remove()
    boton_registrar.grid_remove()
    boton_limpia.grid_remove()

# Función que permite insertar al alumno en la lista de espera
def insertaEnLista(clave):
    conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='datosalumnosbajas'
    )

    cursor = conn.cursor()

    # Consulta SQL para obtener los datos
    query = f"SELECT * FROM alumnos_infbasica WHERE clave_unica = '{clave}'"

    # Ejecutar la consulta SQL
    cursor.execute(query)

    # Obtener los resultados de la consulta
    results = cursor.fetchall()

    #print(results[0][1])

    if(results is not NONE):
        sql_insercion = f"INSERT INTO lista_de_espera (clave_unica, nombre, ap_paterno, ap_materno, carrera, generacion) VALUES ('{results[0][0]}', '{results[0][1]}', '{results[0][2]}', '{results[0][3]}', '{results[0][4]}', '{results[0][5]}')"
        cursor.execute(sql_insercion)
        conn.commit()

    # Consulta SQL para validar la insercion de datos
    validacion = f"SELECT * FROM lista_de_espera WHERE clave_unica = '{clave}'"
    cursor.execute(validacion)
    validar= cursor.fetchall()
    
    # Mensajes de validación
    if validar is not NONE:
        limpiainfo()
        messagebox.showinfo(message="Alumno registrado con éxito", title="Éxito")
        cursor.close()
        conn.close()
        
    else:
        limpiainfo()
        messagebox.showerror(message="Alumno no registrado", title="Error")
        cursor.close()
        conn.close()



def mostrar_informacion_alumno():
    clave_alumno_label.grid()
    nombre_alumno_label.grid()
    carrera_alumno_label.grid()
    generacion_alumno_label.grid()
    claveAlumno = claveR.get() 
    clave_alumno_label.config(text="Clave única del alumno: " + claveR.get())
    nombre_alumno_label.config(text="Nombre del Alumno: " + nombreR.get())
    carrera_alumno_label.config(text="Carrera del Alumno: " + carreraR.get())
    generacion_alumno_label.config(text="Generación del Alumno: " + generacionR.get())
    # Crear un botón para buscar al alumno
    global boton_registrar, boton_limpia
    boton_registrar = tk.Button(frame, text="Registrar en la lista de espera.", command=lambda:insertaEnLista(claveAlumno))
    boton_registrar.grid(row=6, column=1, padx=10, pady=10)
    #Boton para limpiar informacion
    # Crear un botón para buscar al alumno
    boton_limpia = tk.Button(frame, text="Limpiar", command=limpiainfo)
    boton_limpia.grid(row=7, column=1, padx=10, pady=10)


def formularios(fila_seleccionada):
    frame.grid_remove()
    frame.grid()
    #Consulta a realizar
    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    print (fila_seleccionada[1])
    consulta = f"SELECT * FROM formulario WHERE clave_unica = '{fila_seleccionada[1]}'"
    resultado = conexion.ejecutar_consulta(consulta)
    conexion.desconectar()

    global lbl_fecha_valor

    # Crear etiquetas para los campos fecha, clave y nombre
    #print(resultado[0][6])
    lbl_fecha = Label(frame, text="Fecha:")
    lbl_fecha.grid(row=1, column=3, padx=10, pady=10)

    lbl_fecha_valor = Label(frame, text=resultado[0][6])
    lbl_fecha_valor.grid_remove()
    lbl_fecha_valor.grid()
    lbl_fecha_valor.grid(row=1, column=4, padx=10, pady=10)

    lbl_clave = Label(frame, text="Clave:")
    lbl_clave.grid(row=1, column=5, padx=10, pady=10)
    lbl_clave_valor = Label(frame, text=resultado[0][1])
    lbl_clave_valor.grid_remove()
    lbl_clave_valor.grid()
    lbl_clave_valor.grid(row=1, column=6, padx=10, pady=10)

    lbl_nombre = Label(frame, text="Nombre:")
    lbl_nombre.grid(row=2, column=3, padx=10, pady=10)
    lbl_nombre_valor = Label(frame, text=resultado[0][2]+" "+resultado[0][3]+" "+resultado[0][4])
    lbl_nombre_valor.grid_remove()
    lbl_nombre_valor.grid()
    lbl_nombre_valor.grid(row=2, column=4, padx=10, pady=10) 

    lbl_correo = Label(frame, text="Correo electronico:")
    lbl_correo.grid(row=2, column=5, padx=10, pady=10)
    lbl_correo_valor = Label(frame, text=resultado[0][5])
    lbl_correo_valor.grid_remove()
    lbl_correo_valor.grid()
    lbl_correo_valor.grid(row=2, column=6, padx=10, pady=10)

    lbl_carrera = Label(frame, text="Carrera:")
    lbl_carrera.grid(row=3, column=3, padx=10, pady=10)
    lbl_carrera_valor = Label(frame, text=resultado[0][7])
    lbl_carrera_valor.grid_remove()
    lbl_carrera_valor.grid()
    lbl_carrera_valor.grid(row=3, column=4, padx=10, pady=10)

    lbl_generacion = Label(frame, text="Generación:")
    lbl_generacion.grid(row=3, column=5, padx=10, pady=10)
    lbl_generacion_valor = Label(frame, text=resultado[0][8])
    lbl_generacion_valor.grid_remove()
    lbl_generacion_valor.grid()
    lbl_generacion_valor.grid(row=3, column=6, padx=10, pady=10)

    #"Motivo de Baja"
    lbl_motivo = Label(frame, text="Motivo de Baja:")
    lbl_motivo.grid(row=4, column=3, padx=10, pady=10)
    lbl_motivo_valor = Label(frame, text=resultado[0][10])
    lbl_motivo_valor.grid_remove()
    lbl_motivo_valor.grid()
    lbl_motivo_valor.grid(row=4, column=4, padx=10, pady=10)
    
    
    lbl_prpa = Label(frame, text="Preparatoria de procedencia:")
    lbl_prpa.grid(row=4, column=5, padx=10, pady=10)
    lbl_prepa_valor = Label(frame, text=resultado[0][11])
    lbl_prepa_valor.grid_remove()
    lbl_prepa_valor.grid()
    lbl_prepa_valor.grid(row=4, column=6, padx=10, pady=10)

    lbl_materia = Label(frame, text="Materia más dificil:")
    lbl_materia.grid(row=5, column=3, padx=10, pady=10)
    lbl_materia_valor = Label(frame, text=resultado[0][12])
    lbl_materia_valor.grid_remove()
    lbl_materia_valor.grid()
    lbl_materia_valor.grid(row=5, column=4, padx=10, pady=10)

    lbl_materia2 = Label(frame, text="Materia más dificil II:")
    lbl_materia2.grid(row=5, column=5, padx=10, pady=10)
    lbl_materia2_valor = Label(frame, text=resultado[0][13])
    lbl_materia2_valor.grid_remove()
    lbl_materia2_valor.grid()
    lbl_materia2_valor.grid(row=5, column=6, padx=10, pady=10)

    lbl_materia3 = Label(frame, text="Materia más dificil III:")
    lbl_materia3.grid(row=6, column=3, padx=10, pady=10)    
    lbl_materia3_valor = Label(frame, text=resultado[0][14])
    lbl_materia3_valor.grid_remove()
    lbl_materia3_valor.grid()
    lbl_materia3_valor.grid(row=6, column=4, padx=10, pady=10)
    
    lbl_tipoB = Label(frame, text="Tipo de baja:")
    lbl_tipoB.grid(row=6, column=5, padx=10, pady=10)
    lbl_tipoB_valor = Label(frame, text=resultado[0][9])
    lbl_tipoB_valor.grid_remove()
    lbl_tipoB_valor.grid()
    lbl_tipoB_valor.grid(row=6, column=6, padx=10, pady=10)

    # Agregar etiquetas para mostrar los datos adicionales
    lbl_motivotexto = Label(frame, text="Porqué se da de baja:")
    lbl_motivotexto.grid(row=7, column=3, padx=10, pady=10)
    lbl_motivotexto_valor = Label(frame, text=resultado[0][17])
    lbl_motivotexto_valor.grid_remove()
    lbl_motivotexto_valor.grid()
    lbl_motivotexto_valor.grid(row=7, column=4, padx=10, pady=10)

    lbl_formatexto = Label(frame, text="Forma Titulacion:")
    lbl_formatexto.grid(row=7, column=5, padx=10, pady=10)
    lbl_formatexto_valor = Label(frame)
    if resultado[0][15]:
        lbl_formatexto_valor['text']= resultado[0][15]
    else:
        lbl_formatexto_valor['text']="No aplica"
       
    lbl_formatexto_valor.grid_remove()
    lbl_formatexto_valor.grid()
    lbl_formatexto_valor.grid(row=7, column=6, padx=10, pady=10)

    lbl_fechaTtexto = Label(frame, text="Fecha EGEL:")
    lbl_fechaTtexto.grid(row=8, column=3, padx=10, pady=10)
    lbl_fechaTtexto_valor = Label(frame)
    if resultado[0][16]:
        lbl_fechaTtexto_valor['text']=resultado[0][16]
    else:
        lbl_fechaTtexto_valor ['text']="No aplica"
    lbl_fechaTtexto_valor.grid_remove()
    lbl_fechaTtexto_valor.grid()
    lbl_fechaTtexto_valor.grid(row=8, column=4, padx=10, pady=10)

    lbl_empresa = Label(frame, text="Empresa la que trabaja:")
    lbl_empresa.grid(row=8, column=5, padx=10, pady=10)

    lbl_empresa_valor = Label(frame)
    if resultado[0][18] is not None:
        lbl_empresa_valor['text']=resultado[0][18]
    else:
        lbl_empresa_valor['text']="No aplica"

    lbl_empresa_valor.grid_remove()
    lbl_empresa_valor.grid()
    lbl_empresa_valor.grid(row=8, column=6, padx=10, pady=10)
    
    # Crear un botón para generar documento sellos
    btn_sell = Button(frame, text="Generar carta de sellos", command= lambda:GeneraCarta(resultado[0][1]))
    btn_sell.grid(row=9, column=3, padx=10, pady=10)

    # Crear un botón para generar documento sellos
    btn_cart = Button(frame, text="Generar carta de no adeudo", command= lambda:GeneraCarta(resultado[0][1]))
    btn_cart.grid(row=9, column=4, padx=10, pady=10)

    # Crear un botón para generar documento sellos
    btn_edit = Button(frame, text="Regresa a edición", command= lambda:GeneraCarta(resultado[0][1]))
    btn_edit.grid(row=9, column=5, padx=10, pady=10)

    # Función que llama al módulo de consultas
def abre_consulta():
    consulta.emergente_consulta()

def abre_consultaG():
    consultaG.cosulta_grafica()

def buscaAlumno():
    claveAlumno = claveA.get()
    print(claveAlumno)
    # Realizar la consulta del alumno mediante su clave única
    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT * FROM alumnos_infbasica WHERE clave_unica = '{claveAlumno}'"
    resultado = conexion.ejecutar_consulta(consulta)

    if resultado:
        global claveR
        global nombreR 
        global carreraR
        global generacionR

        claveR.set(resultado[0][0])
        nombreR.set(resultado[0][1])
        carreraR.set(resultado[0][4])
        generacionR.set(resultado[0][5])

        mostrar_informacion_alumno()
        conexion.desconectar()   
    else:
        messagebox.showerror("Error", "No se encontró ningún alumno con la clave proporcionada.")
        conexion.desconectar()

def ventana_recPrincipal():
    # Crear la ventana principal
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
    global ventana_RecP
    ventana_RecP = customtkinter.CTk()
    #ventana_RecP = tk.Tk()
    ventana_RecP.title("Sistema de Alumnos")

    # Configurar el ancho de la ventana para que sea igual al ancho de la pantalla
   
    #ventana_RecP.title("Sistema de Bajas")

    # Crear el frame que contendrá los elementos en el grid
    global frame
    frame = ttk.Frame(ventana_RecP)
    frame.grid(row=0, column=0, sticky="nsew")

    # Agregar el titulo sistema de bajas
    #lbl_Sb = Label(ventana_RecP, text="Sistema de bajas", fg="white", bg="darkblue", font=("Arial", 30))
    #lbl_Sb.grid(row=0, column=0, sticky="nsew")

    # Crear una barra horizontal azul en la parte superior de la ventana
    barra_azul = tk.Canvas(frame, bg="darkblue")
    barra_azul.grid(row=0, column=0, columnspan=8, sticky="nsew")  # Cambia el columnspan para que se extienda por 3 columnas

    # Agrega un label en la barra azul
    texto_barra_azul = tk.Label(barra_azul, text="Sistema de Bajas", fg="white", bg="blue", font=("Helvetica", 20))
    texto_barra_azul.pack(fill=tk.BOTH, expand=True)  # Usamos pack para que el label ocupe todo el espacio de la barra


    # Crear un label y un entry para ingresar la clave única
    label_clave = tk.Label(frame, text="Clave única del alumno:")
    label_clave.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    global claveA
    claveA = tk.StringVar()
    entry_clave = tk.Entry(frame, textvariable=claveA)
    entry_clave.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    # Crear un botón para buscar al alumno
    boton_buscar = tk.Button(frame, text="Buscar", command=buscaAlumno)
    boton_buscar.grid(row=1, column=2, padx=10, pady=10)

    global claveR, nombreR, carreraR, generacionR, clave_alumno_label, nombre_alumno_label, carrera_alumno_label, generacion_alumno_label

    # Crear etiquetas para mostrar la información del alumno
    claveR = tk.StringVar()
    nombreR = tk.StringVar()
    carreraR = tk.StringVar()
    generacionR = tk.StringVar()

    clave_alumno_label = tk.Label(frame, text="")
    nombre_alumno_label = tk.Label(frame, text="")
    carrera_alumno_label = tk.Label(frame, text="")
    generacion_alumno_label = tk.Label(frame, text="")

    clave_alumno_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    nombre_alumno_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    carrera_alumno_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    generacion_alumno_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")


    # Consulta a realizar
    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT * FROM formulario"
    resultado = conexion.ejecutar_consulta(consulta)

    #label formulario
    iniform = Label(frame, text="Selecciona tu formulario")
    iniform.grid(row=7, column=0, padx=10, pady=10, sticky="w")

     # Crear un Treeview con 3 columnas
    global treeview
    treeview = ttk.Treeview(frame, columns=('fecha', 'clave', 'nombre', 'completado'), show='headings')
    treeview.grid(row= 8, column=0, pady=10, sticky="w")

    # Configurar encabezados de columna
    treeview.heading('fecha', text='Fecha')
    treeview.heading('clave', text='Clave')
    treeview.heading('nombre', text='Nombre')
    treeview.heading('completado', text='Completado?')
    completado = "NO"
    
    if resultado[0][10] :
        completado = "SI"

    # Agregar datos
    for result in resultado:
        treeview.insert('', tk.END , text=result[0], values=(result[6], result[1], result[2], completado))
    
    # Establecer ancho de columna
    treeview.column('fecha', width=100)
    treeview.column('clave', width=100)
    treeview.column('nombre', width=100)
    treeview.column('completado', width=90)

    # Mostrar Treeview
    #treeview.pack(side=LEFT, padx=10, pady=10)

    # Crear un botón "Generar Formulario" que muestra la ventana con los datos correspondientes
    btn_formulario = Button(frame, text="Abrir Formulario", command=lambda:formularios(treeview.item(treeview.focus(), "values")))
    btn_formulario.grid(row= 11, column=0, padx=10, pady=10, sticky="w")
    #"""command=lambda: ventana_Formulario(treeview.item(treeview.focus(), "values"))"""
    #btn_formulario.pack(side=RIGHT, padx=10, pady=10)

    #label consultas
    Cons = Label(frame, text="Consultas")
    Cons.grid(row=12, column=0, padx=10, pady=10, sticky="w")

    # Crear un botón "Haz consulta"
    btn_consulta = Button(frame, text="Consulta de datos", command=lambda:abre_consulta())
    btn_consulta.grid(row= 13, column=0, padx=10, pady=10, sticky="w")

    # Crear un botón "Haz consulta grafica"
    btn_consulta = Button(frame, text="Consulta grafica", command=lambda:abre_consultaG())
    btn_consulta.grid(row= 13, column=1, padx=10, pady=10, sticky="w")

    # Iniciar la aplicación
    ventana_RecP.mainloop()

ventana_recPrincipal()
