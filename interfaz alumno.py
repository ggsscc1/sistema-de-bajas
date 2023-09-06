from tkinter import *
from tkinter import ttk
from DBconection import *
from recorrido_listaEspera import lectura_listaEspera
from datetime import date
from tkcalendar import DateEntry

#Función que se encarga de insertar la información del alumno en la base de datos: inserta en la tabla "formulario" y borra al alumno de "lista de espera"
def inserta_Form():
    
    #Obtención de las variables requeridas en el llenado del formulario
    fechaI = fechaF
    nombreI = nombreF
    ap_patI = ap_patF
    ap_matI = ap_matF
    cve_unicaI = cve_unicaF
    generacionI = generacionF
    carreraI = carreraF
    emailI = emailF.get()
    materia1I = materia1F.get()
    materia2I = materia2F.get()
    materia3I = materia3F.get()
    prepaI = prepaF.get()
    mot_realI = mot_realF.get()
    inconvenienteI = inconvenienteF.get()
    trabajoI = trabajoF.get()
    formaTitI = formaTitF.get()
    tipo_bajaI = tipo_bajaF.get()
    fechaEgelI = fechaEgelF.get()
    
    #Conexión con la base de datos
    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')

    conexion.conectar()

    #Ejecución de las consultas
    insertar = f"INSERT INTO datosalumnosbajas.formulario (fecha_solicitud, clave_unica, nombre, ap_paterno, ap_materno, generacion, carrera, email_alumno, matdif1, matdif2, matdif3, prepa_origen, tipobaja, detalles_baja, empresa, formatit, fecha_egel, motbaja) VALUES ('{fechaI}','{cve_unicaI}','{nombreI}','{ap_patI}','{ap_matI}','{generacionI}','{carreraI}','{emailI}','{materia1I}','{materia2I}','{materia3I}','{prepaI}','{tipo_bajaI}','{inconvenienteI}','{trabajoI}','{formaTitI}','{fechaEgelI}','{mot_realI}')"
    resultado1 = conexion.ejecutar_consulta(insertar)
    eliminar = f"DELETE FROM datosalumnosbajas.lista_de_espera WHERE clave_unica = {cve_unicaI}"
    resultado2 = conexion.ejecutar_consulta(eliminar)

    print(resultado1)
    print(resultado2)

#Función para mostrar la 
def ventana_Formulario(fila_seleccionada):

    global ventana_formulario
    ventana_formulario = Toplevel()

    #Inicialización de variables 
    global fechaF
    global nombreF
    global ap_patF
    global ap_matF
    global cve_unicaF
    global generacionF
    global carreraF
    global emailF
    global materia1F
    global materia2F
    global materia3F
    global prepaF
    global inconvenienteF
    global tipo_bajaF
    global fechaEgelF

    fechaEgelF = StringVar()
    fechaF= StringVar()
    nombreF= StringVar()
    ap_patF= StringVar()
    ap_matF= StringVar()
    cve_unicaF= StringVar()
    generacionF= StringVar()
    carreraF= StringVar()
    emailF= StringVar()
    materia1F= StringVar()
    materia2F= StringVar()
    materia3F= StringVar()
    prepaF= StringVar()
    inconvenienteF= StringVar()
    tipo_bajaF= StringVar()


    #Consulta que nos servira para consultar de los catalogos cuando se le requiera
    conexionPrin = ConexionBD(user='root',password='root',host='localhost',database='datosalumnosbajas')
    conexionPrin.conectar()

    # Configurar el tamaño y el título de la ventana
    screen_width = ventana_formulario.winfo_screenwidth()
    screen_height = ventana_formulario.winfo_screenheight()
    screen_resolution = str(screen_width)+'x'+str(screen_height)
    ventana_formulario.geometry(screen_resolution)
    ventana_formulario.title("Sistema de Bajas")

    # Agregar el titulo sistema de bajas
    lbl_Sb = Label(ventana_formulario, text="Sistema de bajas", fg="white", bg="darkblue", width="300", height="2", font=("Arial", 30))
    lbl_Sb.pack()

    # Crear un frame para mostrar los datos 1er renglon
    frame_datos = Frame(ventana_formulario, bg="light grey")
    frame_datos.place(x=100, y=(screen_height/5)+20, width=screen_width-230, height=50)

    # Label para mostrar la fecha del día en que se llena el formulario
    fecha_actual = date.today().strftime("%Y-%m-%d")
    lbl_fecha = Label(frame_datos, text="Fecha:")
    lbl_fecha.grid(row=0, column=0, padx=10, pady=10)
    lbl_fecha_valor = Label(frame_datos, text=fecha_actual)
    lbl_fecha_valor.grid(row=0, column=1, padx=10, pady=10)

    # Label para mostrar la clave unica del alumno
    lbl_clave = Label(frame_datos, text="Clave:")
    lbl_clave.grid(row=0, column=2, padx=10, pady=10)
    lbl_clave_valor = Label(frame_datos, text=fila_seleccionada[0])
    lbl_clave_valor.grid(row=0, column=3, padx=10, pady=10)

    # Label para mostrar el nombre del alumno
    lbl_nombre = Label(frame_datos, text="Nombre:")
    lbl_nombre.grid(row=0, column=4, padx=10, pady=10)
    lbl_nombre_valor = Label(frame_datos, text=(fila_seleccionada[3] + " " + fila_seleccionada[1] + " " + fila_seleccionada[2]))
    lbl_nombre_valor.grid(row=0, column=5, padx=10, pady=10)

    # Label para mostrar la carrera del alumno
    lbl_carrera = Label(frame_datos, text="Carrera:")
    lbl_carrera.grid(row=0, column=6, padx=10, pady=10)
    lbl_carrera_valor = Label(frame_datos, text=("Ingeniería en ") + fila_seleccionada[4])
    lbl_carrera_valor.grid(row=0, column=7, padx=10, pady=10)

    # Label para mostrar la generación del alumno
    lbl_generacion = Label(frame_datos, text="Generación:")
    lbl_generacion.grid(row=0, column=8, padx=10, pady=10)
    lbl_generacion_valor = Label(frame_datos, text=(fila_seleccionada[5]))
    lbl_generacion_valor.grid(row=0, column=9, padx=10, pady=10)

    # Crear entry para el correo electronico
    lbl_correo = Label(frame_datos, text="Correo electronico:")
    lbl_correo.grid(row=0, column=10, padx=10, pady=10)
    txt_correo = Entry(frame_datos, textvariable=emailF)
    txt_correo.grid(row=0, column=11, padx=10, pady=10)

    # Guardar los valores en las variables
    fechaF = fecha_actual
    cve_unicaF = fila_seleccionada[0]
    ap_patF = fila_seleccionada[1]
    ap_matF = fila_seleccionada[2]
    nombreF = fila_seleccionada[3]
    carreraF = fila_seleccionada[4]
    generacionF = fila_seleccionada[5]

    # Crear un frame para mostrar los datos 2do renglon
    frame_datos2 = Frame(ventana_formulario, bg="light grey")
    frame_datos2.place(x=100, y=(screen_height/5)+80, width=screen_width-230, height=50)

    # Crear dropdown para la eleccion del tipo de Baja 
    lbl_motivo = Label(frame_datos2, text="Tipo de Baja:")
    lbl_motivo.grid(row=1, column=0, padx=10, pady=10)
    tipo_bajaF = StringVar(ventana_formulario)
    
    consultaTipoBaja = f"SELECT nombre_tipobaja FROM tipo_de_baja"
    restiposBaja = conexionPrin.ejecutar_consulta(consultaTipoBaja)
    listaTiposBaja = [tb[0] for tb in restiposBaja]

    tipo_bajaF.set(" ")
    dropdown_motivos = OptionMenu(frame_datos2, tipo_bajaF, *listaTiposBaja)
    dropdown_motivos.grid(row=1, column=1, padx=10, pady=10)

    # Crear dropdown para la eleccion del motivo real de la baja 
    consultaMotBaja = f"SELECT nombre_motbaja FROM motivo_baja"
    resMotBaja = conexionPrin.ejecutar_consulta(consultaMotBaja)
    listaMotivos = [mot[0] for mot in resMotBaja]
    tipo_bajaF.trace("w", lambda *args: detecta_tipo(tipo_bajaF.get(), frame_datos2, listaMotivos))
    
    # Crear entry para el incoveniente del alumno
    lbl_incov = Label(frame_datos2, text="Inconveniente con la carrera:")
    lbl_incov.grid(row=1, column=4, padx=10, pady=10)
    txt_incov = Entry(frame_datos2, width = 80, textvariable=inconvenienteF)
    txt_incov.grid(row=1, column=5, padx=10, pady=10)

    # Crear dropdown para la eleccion de la preparatoria de origen
    lbl_prpa = Label(frame_datos2, text="Preparatoria de procedencia:")
    lbl_prpa.grid(row=1, column=6, padx=10, pady=10)

    consultaPrepas = f"SELECT nombre_prepa FROM prepa_procedencia"
    resPrepas = conexionPrin.ejecutar_consulta(consultaPrepas)
    listaPrepas = [tb[0] for tb in resPrepas]

    prepaF = StringVar(ventana_formulario)
    prepaF.set(" ")
    dropdown_prepas = OptionMenu(frame_datos2, prepaF, *listaPrepas)
    dropdown_prepas.grid(row=1, column=7, padx=10, pady=10)

    # Crear un frame para mostrar los datos 3er renglon
    frame_datos3 = Frame(ventana_formulario, bg="light grey")
    frame_datos3.place(x=100, y=(screen_height/5)+140, width=screen_width-230, height=50)

    #Crear 3 dropdowns para la eleccion de materias dificiles
    lbl_materia = Label(frame_datos3, text="Materias más dificiles:")
    lbl_materia.grid(row=2, column=0, padx=10, pady=10)
    
    consultaMaterias = f"SELECT nombre_materia FROM materias_dificiles"
    resMaterias = conexionPrin.ejecutar_consulta(consultaMaterias)
    listaMaterias = [mat[0] for mat in resMaterias]

    materia1F = StringVar(ventana_formulario)
    materia1F.set(" ")
    dropdown_opciones_mat = OptionMenu(frame_datos3, materia1F, *listaMaterias)
    dropdown_opciones_mat.grid(row=2, column=1, padx=10, pady=10)
    
    materia2F = StringVar(ventana_formulario)
    materia2F.set(" ")
    dropdown_opciones_mat2 = OptionMenu(frame_datos3, materia2F, *listaMaterias)
    dropdown_opciones_mat2.grid(row=2, column=2, padx=10, pady=10)
    
    materia3F = StringVar(ventana_formulario)
    materia3F.set(" ")
    dropdown_opciones_mat3 = OptionMenu(frame_datos3, materia3F, *listaMaterias)
    dropdown_opciones_mat3.grid(row=2, column=3, padx=10, pady=10)
    
    # Crear un botón para salir del formulario
    btn_cont = Button(ventana_formulario, text="Confirmar formulario", width=20, bg="light grey", command=inserta_Form)
    btn_cont.place(relx=0.5, rely=0.9, anchor=CENTER)

    ventana_formulario.mainloop()

#Función que detecta el motivo de baja que el alumno eligió
def detecta_motivo(motivo):
    global frame_datos4, frame_datos5

    #Inicializar las variables utilizadas en esta sección
    global formaTitF
    formaTitF = StringVar()
    global fechaEgelF
    fechaEgelF = StringVar()
    global trabajoF
    trabajoF = StringVar()

    #Inicializar los frames que serán colocados si se cumple algunas condiciones
    screen_width = ventana_formulario.winfo_screenwidth()
    screen_height = ventana_formulario.winfo_screenheight()
    frame_datos4 = Frame(ventana_formulario, bg="light grey")
    frame_datos5 = Frame(ventana_formulario, bg="light grey")
    frame_datos6 = Frame(ventana_formulario,  highlightthickness=0)

    #Consulta para solicitar las formas de titulación
    conexionPrin = ConexionBD(user='root',password='root',host='localhost',database='datosalumnosbajas')
    conexionPrin.conectar()
    consultaformatit = f"SELECT nombre_formatit FROM forma_titulacion"
    resformatit = conexionPrin.ejecutar_consulta(consultaformatit)
    listaformatit = [formatit[0] for formatit in resformatit]

    #Si el motivo de baja es Trabajo, se colocará el frame correspondiente
    if motivo == 'Trabajo':
        frame_datos5.place_forget()
        frame_datos4.place(x=100, y=(screen_height/5)+200, width=screen_width-230, height=50)

        # Crear entry para el nombre la empresa
        lbl_Empresa = Label(frame_datos4, text="Empresa en la que trabaja:")
        lbl_Empresa.grid(row=3, column=0, padx=10, pady=10)
        txt_Empresa = Entry(frame_datos4, width=50, textvariable=trabajoF)
        txt_Empresa.grid(row=3, column=1, padx=10, pady=10)
        formaTitF.set("")
    #Si el motivo de baja es Titulación, se colocará el frame correspondiente
    elif motivo == 'Titulación':
        trabajoF.set("")
        frame_datos4.place_forget()
        frame_datos5.place(x=100, y=(screen_height/5)+200, width=screen_width-230, height=50)
        lbl_titulo = Label(frame_datos5, text="Forma de titulación:")
        lbl_titulo.grid(row=3, column=0, padx=10, pady=10)
        formaTitF = StringVar(ventana_formulario)
        formaTitF.trace("w", lambda *args: detecta_titulacion(formaTitF.get()))       
        formaTitF.set(" ")
        dropdown_listaformatit = OptionMenu(frame_datos5, formaTitF, *listaformatit)
        dropdown_listaformatit.grid(row=3, column=1, padx=10, pady=10)
    else:
        #Si no es ninguno de los dos, se colocará un frame vacío
        frame_datos6.place(x=100, y=(screen_height/5)+200, width=screen_width-230, height=50)
        formaTitF.set("")
        trabajoF.set("")

#Función que ayuda a detectar el tipo de baja que el alumno eligió
def detecta_tipo(tipo, frame_datos2, lMot):
    #Inicialización de la variable a utilizar
    global mot_realF
    mot_realF = StringVar()
    #Inicialización del label que se utilizará
    lbl_motivo_real = Label(frame_datos2, text="Motivo de Baja:")
    lbl_motivo_real.grid(row=1, column=2, padx=10, pady=10)
    mot_realF = StringVar(ventana_formulario)
    mot_realF.trace("w", lambda *args: detecta_motivo(mot_realF.get()))
    mot_realF.set(" ")
    
    #Si el tipo de baja es definitiva, solamente se colocaran ciertas opciones en "Motivos de baja"
    if tipo == "Definitiva":
        lMotivos = lMot
        dropdown_motivos_real1 = OptionMenu(frame_datos2, mot_realF, *lMotivos)
        dropdown_motivos_real1.grid(row=1, column=3, padx=10, pady=10)

    #Si el tipo de baja es temporal, solamente se colocaran ciertas opciones en "Motivos de baja"    
    if tipo == "Temporal":
        lMotivos = lMot[:4]
        dropdown_motivos_real2 = OptionMenu(frame_datos2, mot_realF, *lMotivos)
        dropdown_motivos_real2.grid(row=1, column=3, padx=10, pady=10)

#Función que ayuda a detectar el tipo de titulación que el alumno eligió   
def detecta_titulacion(tit):
    #Inicialización de la variable a utilizar
    global fechaEgelF
    fechaEgelF = StringVar()
    esegel = tit
    #Si la forma de titulación es por EGEL, se colacará un label para el ingreso de la fecha de presentación del examen
    if esegel == "EGEL":
        lbl_fechaEX = Label(frame_datos5, text="Fecha de aplicación del Examen EGEL")
        lbl_fechaEX.grid(row=3, column=2, padx=10, pady=10)
        txt_fechaEX = DateEntry(frame_datos5, selectmode='day', date_pattern='yyyy-mm-dd',width=50, textvariable=fechaEgelF)
        txt_fechaEX.delete(0, "end")
        txt_fechaEX.grid(row=3, column=3, padx=10, pady=10)

#Función para inicializar la interfaz del usuario, mostrando primeramente la lista de espera
def ventana_InicioForm():
    global ventana_Iniform
    ventana_Iniform = Tk()

    # Configurar el tamaño y el título de la ventana
    screen_width = ventana_Iniform.winfo_screenwidth()
    screen_height = ventana_Iniform.winfo_screenheight()
    screen_resolution = str(screen_width)+'x'+str(screen_height)
    ventana_Iniform.geometry(screen_resolution)
    ventana_Iniform.title("Sistema de Bajas")
    
    # Agregar el titulo sistema de bajas
    lbl_SB = Label(text="Sistema de bajas", fg="white", bg="darkblue", width="300", height="2", font=("Arial", 30))
    lbl_SB.pack()

    #label formulario
    iniform = Label(text="Selecciona tu formulario")
    iniform.place(x=screen_width/2, y=screen_height/5)

    # Crear un frame para la tabla y el botón
    frame = Frame(bg="lightgrey")
    frame.place(x=(screen_width/6), y=(screen_height/5)+20, width=1200, height=500)

    # Crear un Treeview con 3 columnas
    global treeview
    treeview = ttk.Treeview(frame, columns=('clave', 'ap_pat', 'ap_mat', 'nombre', 'carrera', 'generacion'), show='headings')

    # Configurar encabezados de columna
    treeview.heading('clave', text='Clave')
    treeview.heading('ap_pat', text='Apellido Paterno')
    treeview.heading('ap_mat', text='Apellido Materno')
    treeview.heading('nombre', text='Nombre')
    treeview.heading('carrera', text='Carrera')
    treeview.heading('generacion', text='Generación')
    
    # Leer la lista de espera y preparar los datos para ser mostrados
    datos_listaEspera = lectura_listaEspera()
    if datos_listaEspera is not None and isinstance(datos_listaEspera, list):
        for elemento in datos_listaEspera:
            clave, nombre, ap_pat, ap_mat, carrera, generacion = elemento
            treeview.insert(parent='', index='end', values=(clave, ap_pat, ap_mat, nombre, carrera, generacion))
    else:

        # Manejar el caso en que datos_listaEspera es None o no es una lista
        print("datos_listaEspera no es una lista válida.") 

    # Establecer ancho de columna
    treeview.column('clave', width=60)
    treeview.column('ap_pat', width=100)
    treeview.column('ap_mat', width=100)
    treeview.column('nombre', width=130)
    treeview.column('carrera', width=120)
    treeview.column('generacion', width=70)
    
    # Mostrar Treeview
    treeview.pack(side=LEFT, padx=10, pady=10)

    # Crear un botón "Generar Formulario" que muestra la ventana con los datos correspondientes
    btn_formulario = Button(frame, text="Generar Formulario", command=lambda: [ventana_Formulario(treeview.item(treeview.focus(), "values"))])
    btn_formulario.pack(side=RIGHT, padx=10, pady=10)

    ventana_Iniform.mainloop()

#ejecutar el bucle principal de la ventana
ventana_InicioForm()

