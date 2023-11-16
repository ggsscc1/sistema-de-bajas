from tkinter import *
import tkinter as tk
from tkinter import ttk
from DBconection import *
import RegistroUsuario
from tkinter import messagebox
from tkcalendar import DateEntry
from GeneraCarta import * 
import os


#Función que se ejecuta cuando se presiona el botón "Cerrar Sesión"
def cerrar_sesion():
    ventanaInicioAdmin.destroy()

#Función que llama a la ventana para registrar a usuario
def admin_agregarUsuario():
    #agrega = App.__init__()
    RegistroUsuario.ventana_regU()

#Función para mostrar la ventana con los formularios llenos
def ventana_InicioVerForm():
    global ventana_Iniverform
    ventana_Iniverform = Toplevel()

    #Realizar consulta
    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT * FROM formulario"
    resultado = conexion.ejecutar_consulta(consulta)
    
    # Configurar el tamaño y el título de la ventana
    screen_width = ventana_Iniverform.winfo_screenwidth()
    screen_height = ventana_Iniverform.winfo_screenheight()
    screen_resolution = str(screen_width)+'x'+str(screen_height)
    ventana_Iniverform.geometry(screen_resolution)
    ventana_Iniverform.title("Sistema de Bajas")
    
    # Crear label para identificar usuario
    lbl_US = Label(ventana_Iniverform, text="Usuario: Administrador", fg="black")
    lbl_US.place(x=screen_width-120, y=screen_height-960)

    # Agregar el titulo sistema de bajas
    lbl_SB = Label(ventana_Iniverform, text="Sistema de bajas", fg="white", bg="darkblue", width="300", height="2", font=("Arial", 30))
    lbl_SB.pack()

    #label formulario
    iniform = Label(ventana_Iniverform, text="Selecciona tu formulario")
    iniform.place( x=screen_width/4, y=screen_height/5)

    # Crear un frame para la tabla y el botón
    frame = Frame(ventana_Iniverform, bg="lightgrey")
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
    btn_formulario = Button(frame, text="Abrir Formulario", command=lambda: ventana_verFormulario(treeview.item(treeview.focus(), "values")))
    btn_formulario.pack(side=RIGHT, padx=10, pady=10)


    ventana_Iniverform.mainloop()

#Función que abre la ventana para la eleccion del formulario a editar
def ventana_InicioEditaForm():
    global ventana_IniEditaform
    ventana_IniEditaform = Toplevel()

    #Consulta a realizar
    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT * FROM formulario"
    resultado = conexion.ejecutar_consulta(consulta)
    
    # Configurar el tamaño y el título de la ventana
    screen_width = ventana_IniEditaform.winfo_screenwidth()
    screen_height = ventana_IniEditaform.winfo_screenheight()
    screen_resolution = str(screen_width)+'x'+str(screen_height)
    ventana_IniEditaform.geometry(screen_resolution)
    ventana_IniEditaform.title("Sistema de Bajas")
    
    # Crear label para identificar usuario
    lbl_US = Label(ventana_IniEditaform, text="Usuario: Administrador", fg="black")
    lbl_US.place(x=screen_width-120, y=screen_height-960)

    # Agregar el titulo sistema de bajas
    lbl_SB = Label(ventana_IniEditaform, text="Sistema de bajas", fg="white", bg="darkblue", width="300", height="2", font=("Arial", 30))
    lbl_SB.pack()

    #label formulario
    iniform = Label(ventana_IniEditaform, text="Selecciona tu formulario")
    iniform.place( x=screen_width/4, y=screen_height/5)

    # Crear un frame para la tabla y el botón
    frame = Frame(ventana_IniEditaform, bg="lightgrey")
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
    btn_formulario = Button(frame, text="Editar Formulario", command=lambda: ventana_EditaFormulario(treeview.item(treeview.focus(), "values")))
    btn_formulario.pack(side=RIGHT, padx=10, pady=10)

    """
    # Crear un botón "Generar Formulario" que muestra la ventana con los datos correspondientes
    btn_formulariover = Button(frame, text="Abrir Formulario", command=lambda: ventana_verFormulario(treeview.item(treeview.focus(), "values")))
    btn_formulariover.pack(side=RIGHT, padx=10, pady=10)
    """
    ventana_IniEditaform.mainloop()

#Función que abre la ventana que muestra los campos del formulario para su edición
def ventana_EditaFormulario(fila_seleccionada):
    global ventana_Editaformulario
    ventana_Editaformulario = Toplevel()

    #Consulta a realizar
    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    print(fila_seleccionada[1])
    consulta = f"SELECT * FROM formulario WHERE clave_unica = '{fila_seleccionada[1]}'"
    resultado = conexion.ejecutar_consulta(consulta)

    # Configurar el tamaño y el título de la ventana
    screen_width = ventana_Editaformulario.winfo_screenwidth()
    screen_height = ventana_Editaformulario.winfo_screenheight()
    screen_resolution = str(screen_width) + 'x' + str(screen_height)
    ventana_Editaformulario.geometry(screen_resolution)
    ventana_Editaformulario.title("Sistema de Bajas")

    # Agregar el título sistema de bajas
    lbl_Sb = Label(ventana_Editaformulario, text="Sistema de bajas", fg="white", bg="darkblue", width="300", height="2",
                   font=("Arial", 30))
    lbl_Sb.pack()

    # Crear un frame para mostrar los datos
    frame_datos = Frame(ventana_Editaformulario, bg="light grey")
    frame_datos.place(x=100, y=(screen_height / 5) + 20, width=screen_width - 230, height=50)

    # Crear etiquetas para los campos fecha, clave y nombre
    lbl_fecha = Label(frame_datos, text="Fecha:")
    lbl_fecha.grid(row=0, column=0, padx=10, pady=10)

    global lbl_fecha_valor
    lbl_fecha_valor = DateEntry(frame_datos, selectmode='day', date_pattern='yyyy/mm/dd')
    lbl_fecha_valor.delete(0, "end")  ## limpia el campo.
    lbl_fecha_valor.insert(0, resultado[0][6])
    lbl_fecha_valor.grid(row=0,column=1,padx=10, pady=10)

    lbl_clave = Label(frame_datos, text="Clave:")
    lbl_clave.grid(row=0, column=2, padx=10, pady=10)

    global lbl_clave_valor
    lbl_clave_valor = Entry(frame_datos)
    lbl_clave_valor.insert(0, resultado[0][1])
    lbl_clave_valor.grid(row=0, column=3, padx=10, pady=10)

    lbl_nombre = Label(frame_datos, text="Nombre:")
    lbl_nombre.grid(row=0, column=4, padx=10, pady=10)

    global lbl_nombre_valor
    lbl_nombre_valor = Entry(frame_datos)
    lbl_nombre_valor.insert(0, resultado[0][2] + " " + resultado[0][3] + " " + resultado[0][4])
    lbl_nombre_valor.grid(row=0, column=5, padx=10, pady=10)

    lbl_correo = Label(frame_datos, text="Correo electrónico:")
    lbl_correo.grid(row=0, column=6, padx=10, pady=10)
    
    #Etiqueta para el correo
    global lbl_correo_valor
    lbl_correo_valor = Entry(frame_datos)
    lbl_correo_valor.insert(0, resultado[0][5])
    lbl_correo_valor.grid(row=0, column=7, padx=10, pady=10)

    lbl_carrera = Label(frame_datos, text="Carrera:")
    lbl_carrera.grid(row=0, column=8, padx=10, pady=10)

    #Etiqueta para la carrera
    valor_seleccionado = tk.StringVar()
    global lbl_carrera_valor
    lbl_carrera_valor = ttk.Combobox(frame_datos, state="readonly", textvariable = valor_seleccionado)
    lbl_carrera_valor.grid(row=0, column=11, padx=10, pady=10)  

    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT Carrera FROM carreras"
    resultados = conexion.ejecutar_consulta(consulta)
    conexion.desconectar()

    valor_resultado = resultado[0][7]

    # Agregar los resultados al ComboBox
    lbl_carrera_valor['values'] = [""] + [result[0] for result in resultados]
    valor_seleccionado.set(valor_resultado)

    #Etiqueta para la generación
    lbl_generacion = Label(frame_datos, text="Generación:")
    lbl_generacion.grid(row=0, column=12, padx=10, pady=10)
    
    global lbl_generacion_valor
    lbl_generacion_valor = Entry(frame_datos, width=10) 
    lbl_generacion_valor.insert(0, resultado[0][8])
    lbl_generacion_valor.grid(row=0, column=13, padx=10, pady=10)

    # Crear un frame para mostrar los datos
    frame_datos2 = Frame(ventana_Editaformulario, bg="light grey")
    frame_datos2.place(x=100, y=(screen_height / 5) + 80, width=screen_width - 230, height=100)

    # "Motivo de Baja"
    lbl_motivo = Label(frame_datos2, text="Motivo de Baja:")
    lbl_motivo.grid(row=1, column=0, padx=10, pady=10)

    global lbl_motivo_valor
    motivoC = StringVar()
    lbl_motivo_valor = ttk.Combobox(frame_datos2, state="readonly", textvariable=motivoC)
    lbl_motivo_valor.grid(row=1, column=1, padx=10, pady=10)

    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT nombre_motbaja FROM motivo_baja"
    resultados = conexion.ejecutar_consulta(consulta)
    conexion.desconectar()
    
    # Agregar los resultados al ComboBox
    lbl_motivo_valor['values'] = [""] + [resultado[0] for resultado in resultados]

    #poner el valor de la consulta
    motivoC.set(resultado[0][10])

    #Etiqueta para preparatoria
    lbl_prpa = Label(frame_datos2, text="Preparatoria de procedencia:")
    lbl_prpa.grid(row=1, column=2, padx=10, pady=10)

    global lbl_prepa_valor

    escuelaC = StringVar()
    lbl_prepa_valor = ttk.Combobox(frame_datos2, state="readonly", width=30, textvariable=escuelaC)
    lbl_prepa_valor.grid(row=1, column=3, padx=10, pady=10)
    
    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT nombre_prepa FROM prepa_procedencia"
    resultados = conexion.ejecutar_consulta(consulta)
    conexion.desconectar()

    # Agregar los resultados al ComboBox
    lbl_prepa_valor['values'] = [""] + [resultado[0] for resultado in resultados]
    escuelaC.set(resultado[0][11])

    #Etiquetas para materias
    lbl_materia = Label(frame_datos2, text="Materia más difícil:")
    lbl_materia.grid(row=1, column=4, padx=10, pady=10)

    global lbl_materia_valor
    
    materiaC=StringVar()
    lbl_materia_valor = ttk.Combobox(frame_datos2, state="readonly", width=30, textvariable=materiaC)
    lbl_materia_valor.grid(row=1, column=5, padx=10, pady=10)

    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT nombre_materia FROM materias_dificiles"
    resultados = conexion.ejecutar_consulta(consulta)
    conexion.desconectar()

    # Agregar los resultados al ComboBox
    lbl_materia_valor['values'] = [""] + [resultado[0] for resultado in resultados]
    materiaC.set(resultado[0][12])

    lbl_materia2 = Label(frame_datos2, text="Materia más difícil II:")
    lbl_materia2.grid(row=2, column=0, padx=10, pady=10)

    global lbl_materia2_valor
    
    materia2C=StringVar()
    lbl_materia2_valor = ttk.Combobox(frame_datos2, state="readonly", width=30, textvariable=materia2C)
    lbl_materia2_valor.grid(row=2, column=1, padx=10, pady=10)

    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT nombre_materia FROM materias_dificiles"
    resultados = conexion.ejecutar_consulta(consulta)
    conexion.desconectar()

    # Agregar los resultados al ComboBox
    lbl_materia2_valor['values'] = [""] + [resultado[0] for resultado in resultados]
    materia2C.set(resultado[0][13])

    lbl_materia3 = Label(frame_datos2, text="Materia más difícil III:")
    lbl_materia3.grid(row=2, column=2, padx=10, pady=10)

    global lbl_materia3_valor
    
    materia3C=StringVar()
    lbl_materia3_valor = ttk.Combobox(frame_datos2, state="readonly", width=30, textvariable=materia3C)
    lbl_materia3_valor.grid(row=2, column=3, padx=10, pady=10)

    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT nombre_materia FROM materias_dificiles"
    resultados = conexion.ejecutar_consulta(consulta)
    conexion.desconectar()

    # Agregar los resultados al ComboBox
    lbl_materia3_valor['values'] = [""] + [resultado[0] for resultado in resultados]
    materia3C.set(resultado[0][14])

    #Etiqueta para tipo de baja
    lbl_tipoB = Label(frame_datos2, text="Tipo de baja:")
    lbl_tipoB.grid(row=2, column=4, padx=10, pady=10)

    global lbl_tipoB_valor
    tipoC = StringVar()
    lbl_tipoB_valor = ttk.Combobox(frame_datos2, state="readonly", textvariable=tipoC)
    lbl_tipoB_valor.grid(row=2, column=5, padx=10, pady=10)

    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT nombre_tipobaja FROM tipo_de_baja"
    resultados = conexion.ejecutar_consulta(consulta)
    conexion.desconectar()

    # Agregar los resultados al ComboBox
    lbl_tipoB_valor['values'] = [""] + [resultado[0] for resultado in resultados]
    tipoC.set(resultado[0][9])

    # Crear un frame para mostrar los datos
    frame_datos4 = Frame(ventana_Editaformulario, bg="light grey")
    frame_datos4.place(x=100, y=(screen_height / 5) + 200, width=screen_width - 230, height=50)

    # Agregar etiquetas para mostrar los datos adicionales
    lbl_motivotexto = Label(frame_datos4, text="Porqué se da de baja:")
    lbl_motivotexto.grid(row=1, column=0, padx=10, pady=10)

    global lbl_motivotexto_valor
    lbl_motivotexto_valor = Entry(frame_datos4)
    lbl_motivotexto_valor.insert(0, resultado[0][17])
    lbl_motivotexto_valor.grid(row=1, column=1, padx=10, pady=10)

    lbl_formatexto = Label(frame_datos4, text="Forma Titulación:")
    lbl_formatexto.grid(row=1, column=2, padx=10, pady=10)

    global lbl_formatexto_valor
    formaC = StringVar()
    lbl_formatexto_valor = ttk.Combobox(frame_datos4, state="readonly", textvariable=formaC)
    lbl_formatexto_valor.grid(row=1, column=3, padx=10, pady=10)

    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT nombre_formatit FROM forma_titulacion"
    resultados = conexion.ejecutar_consulta(consulta)
    conexion.desconectar()

    # Agregar los resultados al ComboBox
    lbl_formatexto_valor['values'] = [""] + [resultado[0] for resultado in resultados]
    if resultado[0][15] is not None:
        formaC.set(resultado[0][15])
    else:
        formaC.set("No aplica")

    lbl_fechaTtexto = Label(frame_datos4, text="Fecha EGEL:")
    lbl_fechaTtexto.grid(row=1, column=4, padx=10, pady=10)

    global lbl_fechaTtexto_valor
    lbl_fechaTtexto_valor = DateEntry(frame_datos4, selectmode='day', date_pattern='yyyy/mm/dd')
    lbl_fechaTtexto_valor.delete(0, "end")  ## Only this line needed to be added to clear the field.
    lbl_fechaTtexto_valor.grid(row=1,column=5,padx=10, pady=10)
    if resultado[0][16]:
        lbl_fechaTtexto_valor.insert(0,resultado[0][16])
    else:
        lbl_fechaTtexto_valor.insert(0, "No aplica")

    lbl_empresa = Label(frame_datos4, text="Empresa la que trabaja:")
    lbl_empresa.grid(row=1, column=6, padx=10, pady=10)

    global lbl_empresa_valor
    lbl_empresa_valor = Entry(frame_datos4)
    lbl_empresa_valor.grid(row=1, column=7, padx=10, pady=10)
    if resultado[0][18] is not None:
        lbl_empresa_valor.insert(0, resultado[0][18])
    else:
        lbl_empresa_valor.insert(0, "No aplica")
    
    frame_botones = Frame(ventana_Editaformulario, bg="light grey")
    frame_botones.place(x=(screen_width / 2) - 50, y=screen_height - 200, width=140, height=50)

    # Crear un botón para editar
    btn_cont = Button(frame_botones, text="Editar", command=updateBase, width=15)
    btn_cont.grid(row=0, column=0, padx=10, pady=10)

    conexion.desconectar()
    ventana_Editaformulario.mainloop()

#Función para mostrar el formulario seleccionada de la lista de formularios
def ventana_verFormulario(fila_seleccionada):
    global ventana_verformulario
    ventana_verformulario = Toplevel()

    #Realizar consulta
    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    print(fila_seleccionada[1])
    consulta = f"SELECT * FROM formulario WHERE clave_unica = '{fila_seleccionada[1]}'"
    resultado = conexion.ejecutar_consulta(consulta)

    # Configurar el tamaño y el título de la ventana
    screen_width = ventana_verformulario.winfo_screenwidth()
    screen_height = ventana_verformulario.winfo_screenheight()
    screen_resolution = str(screen_width) + 'x' + str(screen_height)
    ventana_verformulario.geometry(screen_resolution)
    ventana_verformulario.title("Sistema de Bajas")

    # Agregar el título sistema de bajas
    lbl_Sb = Label(ventana_verformulario, text="Sistema de bajas", fg="white", bg="darkblue", width="300", height="2",
                   font=("Arial", 30))
    lbl_Sb.pack()

    # Crear un frame para mostrar los datos
    frame_datos = Frame(ventana_verformulario, bg="light grey")
    frame_datos.place(x=100, y=(screen_height / 5) + 20, width=screen_width - 230, height=50)

    # Crear etiquetas para los campos fecha, clave, nombre, email, carrera, generacion
    print(resultado[0][6])
    lbl_fechaver = Label(frame_datos, text="Fecha:")
    lbl_fechaver.grid(row=0, column=0, padx=10, pady=10)
    lbl_fecha_valorver = Label(frame_datos, text=resultado[0][6])
    lbl_fecha_valorver.grid(row=0, column=1, padx=10, pady=10)

    lbl_clavever = Label(frame_datos, text="Clave:")
    lbl_clavever.grid(row=0, column=2, padx=10, pady=10)
    lbl_clavever_valor = Label(frame_datos, text=resultado[0][1])
    lbl_clavever_valor.grid(row=0, column=3, padx=10, pady=10)

    lbl_nombrever = Label(frame_datos, text="Nombre:")
    lbl_nombrever.grid(row=0, column=4, padx=10, pady=10)
    lbl_nombrever_valor = Label(frame_datos, text=resultado[0][2]+" "+resultado[0][3]+" "+resultado[0][4])
    lbl_nombrever_valor.grid(row=0, column=5, padx=10, pady=10) 

    lbl_correover = Label(frame_datos, text="Correo electronico:")
    lbl_correover.grid(row=0, column=6, padx=10, pady=10)
    lbl_correover_valor = Label(frame_datos, text=resultado[0][5])
    lbl_correover_valor.grid(row=0, column=7, padx=10, pady=10)

    lbl_carreraver = Label(frame_datos, text="Carrera:")
    lbl_carreraver.grid(row=0, column=8, padx=10, pady=10)
    
    lbl_carreraver_valor = Label(frame_datos, text=resultado[0][7])
    lbl_carreraver_valor.grid(row=0, column=11, padx=10, pady=10)

    lbl_generacionver = Label(frame_datos, text="Generación:")
    lbl_generacionver.grid(row=0, column=12, padx=10, pady=10)
    lbl_generacionver_valor = Label(frame_datos, text=resultado[0][8])
    lbl_generacionver_valor.grid(row=0, column=13, padx=10, pady=10)

    # Crear un frame para mostrar los datos
    frame_datos2 = Frame(ventana_verformulario, bg="light grey")
    frame_datos2.place(x=100, y=(screen_height / 5) + 80, width=screen_width - 230, height=100)

    #"Motivo de Baja"
    lbl_motivover = Label(frame_datos2, text="Motivo de Baja:")
    lbl_motivover.grid(row=1, column=0, padx=10, pady=10)

    lbl_motivover_valor = Label(frame_datos2, text=resultado[0][10])
    lbl_motivover_valor.grid(row=1, column=1, padx=10, pady=10)

    #Preparatoria
    lbl_prpaver = Label(frame_datos2, text="Preparatoria de procedencia:")
    lbl_prpaver.grid(row=1, column=2, padx=10, pady=10)
    
    lbl_prepaver_valor = Label(frame_datos2, text=resultado[0][11])
    lbl_prepaver_valor.grid(row=1, column=3, padx=10, pady=10)

    #Materias mas dificiles
    lbl_materiaver = Label(frame_datos2, text="Materia más dificil:")
    lbl_materiaver.grid(row=1, column=4, padx=10, pady=10)
    
    lbl_materia_valorver = Label(frame_datos2, text=resultado[0][12])
    lbl_materia_valorver.grid(row=1, column=5, padx=10, pady=10)

    lbl_materia2ver = Label(frame_datos2, text="Materia más dificil II:")
    lbl_materia2ver.grid(row=1, column=6, padx=10, pady=10)
    
    lbl_materia2ver_valor = Label(frame_datos2, text=resultado[0][13])
    lbl_materia2ver_valor.grid(row=1, column=7, padx=10, pady=10)

    lbl_materia3ver = Label(frame_datos2, text="Materia más dificil III:")
    lbl_materia3ver.grid(row=2, column=0, padx=10, pady=10)
    
    lbl_materia3ver_valor = Label(frame_datos2, text=resultado[0][14])
    lbl_materia3ver_valor.grid(row=2, column=1, padx=10, pady=10)

    #Tipo de baja
    lbl_tipoBver = Label(frame_datos2, text="Tipo de baja:")
    lbl_tipoBver.grid(row=2, column=2, padx=10, pady=10)
    
    lbl_tipoBver_valor = Label(frame_datos2, text=resultado[0][9])
    lbl_tipoBver_valor.grid(row=2, column=3, padx=10, pady=10)
    

    # Crear un frame para mostrar los datos
    frame_datos4 = Frame(ventana_verformulario, bg="light grey")
    frame_datos4.place(x=100, y=(screen_height / 5) + 200, width=screen_width - 230, height=50)

    # Agregar etiquetas para mostrar los datos adicionales
    lbl_motivotextover = Label(frame_datos4, text="Porqué se da de baja:")
    lbl_motivotextover.grid(row=1, column=0, padx=10, pady=10)
    
    lbl_motivotextover_valor = Label(frame_datos4, text=resultado[0][17])
    lbl_motivotextover_valor.grid(row=1, column=1, padx=10, pady=10)

    lbl_formatextover = Label(frame_datos4, text="Forma Titulacion:")
    lbl_formatextover.grid(row=1, column=2, padx=10, pady=10)
    
    lbl_formatexto_valorver = Label(frame_datos4)
    if resultado[0][15]:
        lbl_formatexto_valorver['text']= resultado[0][15]
    else:
        lbl_formatexto_valorver['text']="No aplica"
       
    lbl_formatexto_valorver.grid(row=1, column=3, padx=10, pady=10)

    lbl_fechaTtextover = Label(frame_datos4, text="Fecha EGEL:")
    lbl_fechaTtextover.grid(row=1, column=4, padx=10, pady=10)
    
    lbl_fechaTtextover_valor = Label(frame_datos4)
    if resultado[0][16]:
        lbl_fechaTtextover_valor['text']=resultado[0][16]
    else:
        lbl_fechaTtextover_valor ['text']="No aplica"
    lbl_fechaTtextover_valor.grid(row=1, column=5, padx=10, pady=10)

    conexion.desconectar()
    ventana_verformulario.mainloop()

#Función para editar el formulario seleccionado y actualizar sus datos en la base de datos
def updateBase():
    fecha_valor = lbl_fecha_valor.get()
    clave_valor = lbl_clave_valor.get()
    nombre_valor = lbl_nombre_valor.get()
    correo_valor = lbl_correo_valor.get()
    carrera_valor = lbl_carrera_valor.get()
    generacion_valor = lbl_generacion_valor.get()
    motivo_valor = lbl_motivo_valor.get()
    prepa_valor = lbl_prepa_valor.get()
    materia_valor = lbl_materia_valor.get()#depennde
    materia2_valor = lbl_materia2_valor.get()#depennde
    materia3_valor = lbl_materia3_valor.get()#depennde
    tipoB_valor = lbl_tipoB_valor.get()
    motivoTexto_valor = lbl_motivotexto_valor.get()#depende
    formatexto_valor = lbl_formatexto_valor.get()#depende
    fechaTtexto_valor = lbl_fechaTtexto_valor.get()#depende
    empresa_valor = lbl_empresa_valor.get()#depende

     # Conexión a la base de datos
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='datosalumnosbajas'
    )

    cursor = conn.cursor()

   # Realizar el update en la base de datos
    query = f"UPDATE formulario SET fecha_solicitud = '{fecha_valor}', clave_unica = '{clave_valor}', email_alumno = '{correo_valor}', carrera = '{carrera_valor}', generacion = '{generacion_valor}', motbaja = '{motivo_valor}', prepa_origen = '{prepa_valor}', tipobaja = '{tipoB_valor}'"
    #, materia_dificil = '{materia_valor}', materia_dificil2 = '{materia2_valor}', materia_dificil3 = '{materia3_valor}', detalles_baja = '{motivotexto_valor}', forma_titulacion = '{formatexto_valor}', fecha_egel = '{fechaTtexto_valor}'

    if materia_valor:
        query += f", matdif1 = '{materia_valor}'"
    if materia2_valor:
        query += f", matdif2 = '{materia2_valor}'"
    if materia3_valor:
        query += f", matdif3 = '{materia3_valor}'"
    if motivoTexto_valor:
        query += f", detalles_baja = '{motivoTexto_valor}'"
    if formatexto_valor != "No aplica":
        query += f", formatit = '{formatexto_valor}'"
    if fechaTtexto_valor != "No aplica":
        query += f", fecha_egel = '{fechaTtexto_valor}'"
    if empresa_valor != "No aplica":
        query += f", empresa = '{empresa_valor}'"

    query2 = f"WHERE clave_unica = '{lbl_clave_valor.get()}'"
    queryFinal = query + " " +query2
    
    # Ejecutar la consulta SQL
    cursor.execute(queryFinal)

    # Confirmar los cambios en la base de datos
    conn.commit()

    # Consultar la base de datos para verificar el resultado actualizado
    select_query = f"SELECT * FROM formulario WHERE clave_unica = '{lbl_clave_valor.get()}'"
    cursor.execute(select_query)
    result = cursor.fetchone()

    if result:
        # Mostrar el resultado actualizado
        # Confirmación de actualización
        messagebox.showinfo("Confirmación", "El registro ha sido actualizado correctamente.")
    else:
        messagebox.showinfo("Error", "El registro no se ha encontradp.")

    # Cerrar la conexión a la base de datos
    cursor.close()
    conn.close()

#Función para mostrar la ventana con las funcionalidades del administrador
def ventana_IniA():
    # Crear la ventana
    global ventanaInicioAdmin
    ventanaInicioAdmin = Tk()

    # Configurar el tamaño y el título de la ventana
    screen_width = ventanaInicioAdmin.winfo_screenwidth()
    screen_height = ventanaInicioAdmin.winfo_screenheight()
    screen_resolution = str(screen_width)+'x'+str(screen_height)
    ventanaInicioAdmin.geometry(screen_resolution)
    ventanaInicioAdmin.title("Sistema de Bajas")

    # Agregar el titulo sistema de bajas
    lbl_SB = Label(text="Sistema de bajas", fg="white", bg="darkblue", width="300", height="2", font=("Arial", 30))
    lbl_SB.pack()

    # Agregar el texto "Inicio" 
    lbl_IN = Label(text="Inicio", fg="black", width="70", height="2", font=("Arial", 16))
    lbl_IN.pack()

    # Agregar los botones en un Frame
    frame_botones = Frame(bg="lightgrey")
    Label(frame_botones, text="", background="lightgrey").pack()

    btn_VIn = Button(frame_botones, text="Ver información", bg="#86CEEB", height=2, width=30, command=ventana_InicioVerForm).pack()
    Label(frame_botones, text="", background="lightgrey").pack()

    btn_EdIn = Button(frame_botones, text="Editar información", bg="#86CEEB", height=2, width=30, command=ventana_InicioEditaForm).pack()
    Label(frame_botones, text="", background="lightgrey").pack()

    btn_AGUS = Button(frame_botones, text="Agregar Usuario", bg="#86CEEB", height=2, width=30, command=admin_agregarUsuario).pack()
    Label(frame_botones, text="", background="lightgrey").pack()

    frame_botones.place(relx=0.5, rely=0.5, anchor=CENTER, width=300, height=200)

    # Agregar la línea negra
    canvas_linea = Canvas(ventanaInicioAdmin, width=screen_width, height=2, bg="black")
    canvas_linea.place(x=0, y=170)

    # Agregar el texto "Usuario: Administrador"
    lbl_US = Label(text="Usuario: Administrador", fg="black")
    lbl_US.place(x=screen_width-150, y=screen_height-970)

    # Crear un botón rojo "Cerrar Sesión"
    btn_CS = Button(text="Cerrar Sesión", command=cerrar_sesion, bg="red", fg="white")
    btn_CS.place(x=screen_width-100, y=screen_height-940)

    # Ejecutar el bucle principal de la ventana
    ventanaInicioAdmin.mainloop()
    