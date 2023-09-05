from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from DBconection import *
from GeneraCarta import * 
import consulta
import consultaG
import os

# Función para tomar los datos del alumno en la base de datos e ingresarlos en la lista de espera
def buscaAlumno():
    claveAlumno = claveA.get()
    print(claveAlumno)
    #Realizar la consulta del alumno mediante su clave unica
    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT * FROM alumnos_infbasica WHERE clave_unica = '{claveAlumno}'"
    resultado = conexion.ejecutar_consulta(consulta)

    if resultado:
        ventanaClave.destroy()
        global claveR
        global nombreR 
        global carreraR
        global generacionR

        claveR = resultado[0][0]
        nombreR = resultado[0][1]
        carreraR = resultado[0][4]
        generacionR = resultado[0][5]

        ventana_NuevoFormulario(claveR, nombreR, carreraR, generacionR)
        conexion.desconectar()   
    else:
        ventanaClave.destroy()
        messagebox.showerror(message="Alumno no encontrado", title="Error")
        conexion.desconectar()
    
# Función que se ejecuta cuando se presiona el botón "Cerrar Sesión"
def cerrar_sesion():
    ventana_inicior.destroy()

# Crear la ventana con las opciones de Recepción
def ventana_InicioR():
    global ventana_inicior
    ventana_inicior = Tk()

    # Configurar el tamaño y el título de la ventana
    screen_width = ventana_inicior.winfo_screenwidth()
    screen_height = ventana_inicior.winfo_screenheight()
    screen_resolution = str(screen_width)+'x'+str(screen_height)
    ventana_inicior.geometry(screen_resolution)
    ventana_inicior.title("Sistema de Bajas")

    # Agregar el titulo sistema de bajas
    lbl_SB = Label(text="Sistema de bajas", fg="white", bg="darkblue", width="300", height="2", font=("Arial", 30))
    lbl_SB.pack()

    # Agregar el texto "Inicio" 
    lbl_IN = Label(text="Inicio", fg="black", width="70", height="2", font=("Arial", 16))
    lbl_IN.pack()

    # Agregar la línea negra
    canvas_linea = Canvas(ventana_inicior, width=screen_width, height=2, bg="black")
    canvas_linea.place(x=0, y=170)

    # CRear label para identificar usuario
    lbl_US = Label(ventana_inicior, text="Usuario: Recepción", fg="black")
    lbl_US.place(x=120, y=980)

    # Crear un botón rojo "Cerrar Sesión"
    btn_CS = Button(ventana_inicior, text="Cerrar Sesión", command=cerrar_sesion, bg="red", fg="white")
    btn_CS.place(x = screen_width-100, y = screen_height-950)

    # Agregar los botones en un Frame
    frame_botones = Frame(bg="lightgrey")
    Label(frame_botones, text="", background="lightgrey").pack()

    btn_VIn = Button(frame_botones, text="Registro nuevo alumno", bg="#86CEEB", height=2, width=30, command=abrir_ventana).pack()
    Label(frame_botones, text="", background="lightgrey").pack()

    btn_EdIn = Button(frame_botones, text="Ver formulario", bg="#86CEEB", height=2, width=30, command=ventana_InicioForm).pack()
    Label(frame_botones, text="", background="lightgrey").pack()

    btn_AGUS = Button(frame_botones, text="Generar consulta", bg="#86CEEB", height=2, width=30, command=abre_consulta).pack()
    Label(frame_botones, text="", background="lightgrey").pack()

    btn_GRAF = Button(frame_botones, text="Generar consulta graficas", bg="#86CEEB", height=2, width=30, command=abre_consultaG).pack()
    Label(frame_botones, text="", background="lightgrey").pack()

    frame_botones.place(x=(screen_width/2)-150, y=180, width=300, height=270)

    # Ejecutar el bucle principal de la ventana
    ventana_inicior.mainloop()
   
# Función para crear la ventana que muestra la información básica del alumno
def ventana_NuevoFormulario(clave, nombre, carrera, generacion):
    #Inicializacion de objeto - Ventana Nuevo Formulario
    global ventana_nf
    ventana_nf = Toplevel()

    #Cálculo de la resolución de la ventana del usuario para autoajuste.
    screen_width = ventana_nf.winfo_screenwidth()
    screen_height = ventana_nf.winfo_screenheight()
    #screen_resolution = str(screen_width)+'x'+str(screen_height)
    ventana_nf.geometry("1280x720")
    ventana_nf.title("Sistema de bajas de CiComp")

    #Cambio de icono de la ventana
    ventana_nf.iconbitmap("emblema_facultad.ico")

    #Barra Superior "Sistema de bajas"
    label_barraSup = Label(ventana_nf, text="Sistema de bajas", fg="white", bg="darkblue", width="300", height="2", font=("Calibri", 30))
    label_barraSup.pack(anchor="center")

    #Creacion de Frame contenedor
    miFrame = Frame(ventana_nf, width=200, height=300)
    miFrame.pack(anchor="center")

    #Entry
    global digita_clave
    digita_clave = StringVar()

    #Labels con la información del alumno
    label_InfoAlumnoClave = Label(miFrame, text= "Clave: ", font="Calibri 22 bold")
    label_InfoAlumnoClave.grid(row="0", column="0", sticky="e", padx=1, pady=30)

    label_InfoAlumnoNombre = Label(miFrame, text= "Nombre : ", font="Calibri 22 bold")
    label_InfoAlumnoNombre.grid(row="1", column="0", sticky="e", padx=1, pady=30)

    label_InfoAlumnoCarrera = Label(miFrame, text= "Carrera: ", font="Calibri 22 bold")
    label_InfoAlumnoCarrera.grid(row="0", column="2", sticky="e", padx=1, pady=30)

    label_InfoAlumnoGeneracion = Label(miFrame, text= "Generación: ", font="Calibri 22 bold")
    label_InfoAlumnoGeneracion.grid(row="1", column="2", sticky="e", padx=1, pady=30)
    
    label_InfoMuestraClave = Label(miFrame, font="Calibri 22")
    label_InfoMuestraClave.config(text=clave)
    label_InfoMuestraClave.grid(row="0", column="1", columnspan="1", sticky="w", padx=1, pady=30)

    label_InfoMuestraNombre = Label(miFrame, font="Calibri 22")
    label_InfoMuestraNombre.config(text=nombre)
    label_InfoMuestraNombre.grid(row="1", column="1", columnspan="1", sticky="w", padx=1, pady=30)

    label_InfoMuestraCarrera = Label(miFrame, font="Calibri 22")
    label_InfoMuestraCarrera.config(text=carrera)
    label_InfoMuestraCarrera.grid(row="0", column="3", columnspan="1", sticky="w", padx=1, pady=30)

    label_InfoMuestraGeneracion = Label(miFrame, font="Calibri 22")
    label_InfoMuestraGeneracion.config(text=generacion)
    label_InfoMuestraGeneracion.grid(row="1", column="3", columnspan="1", sticky="w", padx=1, pady=30)

    boton_agregarAlumno = Button(miFrame, bg="darkblue", text="Registrar en la lista de espera", fg="white", font="Calibri 18 bold", cursor="hand2", command= lambda: insertaEnLista(clave))
    boton_agregarAlumno.grid(row="2", column="2")

    ventana_nf.mainloop()

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
        ventana_nf.destroy()
        messagebox.showinfo(message="Alumno registrado con éxito", title="Éxito")
        cursor.close()
        conn.close()
        
    else:
        ventana_nf.destroy()
        messagebox.showerror(message="Alumno no registrado", title="Error")
        cursor.close()
        conn.close()

# Función para mostrar los formularios de los alumnos
def ventana_InicioForm():
    global ventana_Iniform
    ventana_Iniform = Toplevel()

    # Consulta a realizar
    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT * FROM formulario"
    resultado = conexion.ejecutar_consulta(consulta)
    
    # Configurar el tamaño y el título de la ventana
    screen_width = ventana_Iniform.winfo_screenwidth()
    screen_height = ventana_Iniform.winfo_screenheight()
    screen_resolution = str(screen_width)+'x'+str(screen_height)
    ventana_Iniform.geometry(screen_resolution)
    ventana_Iniform.title("Sistema de Bajas")
    
    # Crear label para identificar usuario
    lbl_US = Label(ventana_Iniform, text="Usuario: Recepción", fg="black")
    lbl_US.place(x=screen_width-120, y=screen_height-960)

    # Agregar el titulo sistema de bajas
    lbl_SB = Label(ventana_Iniform, text="Sistema de bajas", fg="white", bg="darkblue", width="300", height="2", font=("Arial", 30))
    lbl_SB.pack()

    #label formulario
    iniform = Label(ventana_Iniform, text="Selecciona tu formulario")
    iniform.place( x=screen_width/4, y=screen_height/5)

    # Crear un frame para la tabla y el botón
    frame = Frame(ventana_Iniform, bg="lightgrey")
    frame.place(x=(screen_width/4), y=(screen_height/5)+20, width=600, height=500)

    # Crear un Treeview con 3 columnas
    global treeview
    treeview = ttk.Treeview(frame, columns=('fecha', 'clave', 'nombre'), show='headings')

    # Configurar encabezados de columna
    treeview.heading('fecha', text='Fecha')
    treeview.heading('clave', text='Clave')
    treeview.heading('nombre', text='Nombre')

    # Agregar datos
    for result in resultado:
        treeview.insert('', tk.END , text=result[0], values=(result[6], result[1], result[2]))
    
    # Establecer ancho de columna
    treeview.column('fecha', width=130)
    treeview.column('clave', width=150)
    treeview.column('nombre', width=150)

    # Mostrar Treeview
    treeview.pack(side=LEFT, padx=10, pady=10)

    # Crear un botón "Generar Formulario" que muestra la ventana con los datos correspondientes
    btn_formulario = Button(frame, text="Abrir Formulario", command=lambda: ventana_Formulario(treeview.item(treeview.focus(), "values")))
    btn_formulario.pack(side=RIGHT, padx=10, pady=10)

    ventana_Iniform.mainloop()

# Función para mostrar el formulario del alumno seleccionado
def ventana_Formulario(fila_seleccionada):
    global ventana_formulario
    ventana_formulario = Toplevel()

    #Consulta a realizar
    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    print (fila_seleccionada[1])
    consulta = f"SELECT * FROM formulario WHERE clave_unica = '{fila_seleccionada[1]}'"
    resultado = conexion.ejecutar_consulta(consulta)
    conexion.desconectar()

    print(resultado)
   
    # Configurar el tamaño y el título de la ventana
    screen_width = ventana_formulario.winfo_screenwidth()
    screen_height = ventana_formulario.winfo_screenheight()
    screen_resolution = str(screen_width)+'x'+str(screen_height)
    ventana_formulario.geometry(screen_resolution)
    ventana_formulario.title("Sistema de Bajas")

    # Agregar el titulo sistema de bajas
    lbl_Sb = Label(ventana_formulario, text="Sistema de bajas", fg="white", bg="darkblue", width="300", height="2", font=("Arial", 30))
    lbl_Sb.pack()

    # Crear un frame para mostrar los datos
    frame_datos = Frame(ventana_formulario, bg="light grey")
    frame_datos.place(x=100, y=(screen_height/5)+20, width=screen_width-230, height=50)

    # Crear etiquetas para los campos fecha, clave y nombre
    #print(resultado[0][6])
    lbl_fecha = Label(frame_datos, text="Fecha:")
    lbl_fecha.grid(row=0, column=0, padx=10, pady=10)

    lbl_fecha_valor = Label(frame_datos, text=resultado[0][6])
    lbl_fecha_valor.grid(row=0, column=1, padx=10, pady=10)

    lbl_clave = Label(frame_datos, text="Clave:")
    lbl_clave.grid(row=0, column=2, padx=10, pady=10)
    lbl_clave_valor = Label(frame_datos, text=resultado[0][1])
    lbl_clave_valor.grid(row=0, column=3, padx=10, pady=10)

    lbl_nombre = Label(frame_datos, text="Nombre:")
    lbl_nombre.grid(row=0, column=4, padx=10, pady=10)

    lbl_nombre_valor = Label(frame_datos, text=resultado[0][2]+" "+resultado[0][3]+" "+resultado[0][4])
    lbl_nombre_valor.grid(row=0, column=5, padx=10, pady=10) 

    lbl_correo = Label(frame_datos, text="Correo electronico:")
    lbl_correo.grid(row=0, column=6, padx=10, pady=10)
    
    lbl_correo_valor = Label(frame_datos, text=resultado[0][5])
    lbl_correo_valor.grid(row=0, column=7, padx=10, pady=10)

    lbl_carrera = Label(frame_datos, text="Carrera:")
    lbl_carrera.grid(row=0, column=8, padx=10, pady=10)

    lbl_carrera_valor = Label(frame_datos, text=resultado[0][7])
    lbl_carrera_valor.grid(row=0, column=11, padx=10, pady=10)

    lbl_generacion = Label(frame_datos, text="Generación:")
    lbl_generacion.grid(row=0, column=12, padx=10, pady=10)
    lbl_generacion_valor = Label(frame_datos, text=resultado[0][8])
    lbl_generacion_valor.grid(row=0, column=13, padx=10, pady=10)

    # Crear un frame para mostrar los datos
    frame_datos2 = Frame(ventana_formulario, bg="light grey")
    frame_datos2.place(x=100, y=(screen_height/5)+80, width=screen_width-230, height=100)

    #"Motivo de Baja"
    lbl_motivo = Label(frame_datos2, text="Motivo de Baja:")
    lbl_motivo.grid(row=1, column=0, padx=10, pady=10)

    lbl_motivo_valor = Label(frame_datos2, text=resultado[0][10])
    lbl_motivo_valor.grid(row=1, column=1, padx=10, pady=10)

    lbl_prpa = Label(frame_datos2, text="Preparatoria de procedencia:")
    lbl_prpa.grid(row=1, column=2, padx=10, pady=10)
    
    lbl_prepa_valor = Label(frame_datos2, text=resultado[0][11])
    lbl_prepa_valor.grid(row=1, column=3, padx=10, pady=10)

    lbl_materia = Label(frame_datos2, text="Materia más dificil:")
    lbl_materia.grid(row=1, column=4, padx=10, pady=10)
    
    lbl_materia_valor = Label(frame_datos2, text=resultado[0][12])
    lbl_materia_valor.grid(row=1, column=5, padx=10, pady=10)

    lbl_materia2 = Label(frame_datos2, text="Materia más dificil II:")
    lbl_materia2.grid(row=1, column=6, padx=10, pady=10)
    
    lbl_materia2_valor = Label(frame_datos2, text=resultado[0][13])
    lbl_materia2_valor.grid(row=1, column=7, padx=10, pady=10)

    lbl_materia3 = Label(frame_datos2, text="Materia más dificil III:")
    lbl_materia3.grid(row=2, column=0, padx=10, pady=10)
    
    lbl_materia3_valor = Label(frame_datos2, text=resultado[0][14])
    lbl_materia3_valor.grid(row=2, column=1, padx=10, pady=10)
    
    lbl_tipoB = Label(frame_datos2, text="Tipo de baja:")
    lbl_tipoB.grid(row=2, column=2, padx=10, pady=10)
    
    lbl_tipoB_valor = Label(frame_datos2, text=resultado[0][9])
    lbl_tipoB_valor.grid(row=2, column=3, padx=10, pady=10)

    # Crear un frame para mostrar los datos
    frame_datos4 = Frame(ventana_formulario, bg="light grey")
    frame_datos4.place(x=100, y=(screen_height/5)+200, width=screen_width-230, height=50)

    # Agregar etiquetas para mostrar los datos adicionales
    lbl_motivotexto = Label(frame_datos4, text="Porqué se da de baja:")
    lbl_motivotexto.grid(row=1, column=0, padx=10, pady=10)
    lbl_motivotexto_valor = Label(frame_datos4, text=resultado[0][17])
    lbl_motivotexto_valor.grid(row=1, column=1, padx=10, pady=10)

    lbl_formatexto = Label(frame_datos4, text="Forma Titulacion:")
    lbl_formatexto.grid(row=1, column=2, padx=10, pady=10)
    lbl_formatexto_valor = Label(frame_datos4)
    if resultado[0][15]:
        lbl_formatexto_valor['text']= resultado[0][15]
    else:
        lbl_formatexto_valor['text']="No aplica"
       
    lbl_formatexto_valor.grid(row=1, column=3, padx=10, pady=10)

    lbl_fechaTtexto = Label(frame_datos4, text="Fecha EGEL:")
    lbl_fechaTtexto.grid(row=1, column=4, padx=10, pady=10)
    lbl_fechaTtexto_valor = Label(frame_datos4)
    if resultado[0][16]:
        lbl_fechaTtexto_valor['text']=resultado[0][16]
    else:
        lbl_fechaTtexto_valor ['text']="No aplica"
    lbl_fechaTtexto_valor.grid(row=1, column=5, padx=10, pady=10)

    lbl_empresa = Label(frame_datos4, text="Empresa la que trabaja:")
    lbl_empresa.grid(row=1, column=6, padx=10, pady=10)

    lbl_empresa_valor = Label(frame_datos4)
    lbl_empresa_valor.grid(row=1, column=7, padx=10, pady=10)
    if resultado[0][18] is not None:
        lbl_empresa_valor['text']=resultado[0][18]
    else:
        lbl_empresa_valor['text']="No aplica"

    frame_botones = Frame(ventana_formulario, bg="light grey")
    frame_botones.place(x=(screen_width/2)-50, y=screen_height-200, width=135, height=40)

    # Crear un botón para generar carta de no adeudo
    btn_cont = Button(frame_botones, text="Generar carta",width=15, command= lambda:GeneraCarta(resultado[0][1]))
    btn_cont.grid(row=0, column=0, padx=10, pady=10)
    
    ventana_formulario.mainloop()

# Función que abre la ventana que pide la clave del alumno para buscarlo en la base de datos
def abrir_ventana():
    global ventanaClave
    ventanaClave = Toplevel()
    ventanaClave.title("Ingresa la clave única del alumno")
    ventanaClave.geometry("400x200")
    global claveA
    claveA = StringVar()

    # Crear un label y un entry para ingresar la clave única
    label_clave = Label(ventanaClave, text="Clave única del alumno:")
    label_clave.pack(pady=10)
    entry_clave = Entry(ventanaClave, textvariable=claveA)
    entry_clave.pack(pady=10)
    
    # Crear un botón para cerrar la ventana y obtener la clave única ingresada
    boton_aceptar = Button(ventanaClave, text="Aceptar", command=buscaAlumno)
    boton_aceptar.pack(pady=10)
   
# Función que llama al módulo de consultas
def abre_consulta():
    consulta.emergente_consulta()

def abre_consultaG():
    consultaG.cosulta_grafica()


ventana_InicioR()
