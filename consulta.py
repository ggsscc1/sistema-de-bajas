from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import DateEntry
import mysql.connector
import pandas as pd
import excel
from DBconection import *
from pathlib import Path

#Función para la creación de las consultas
def haz_consulta():
    # Tomar valores necesarios
    anioConsulta = anioC.get()
    fechaConsulta = fechaC.get()
    generacionConsulta = generacionC.get()
    nombreConsulta = nombreC.get()
    claveConsulta = claveC.get()
    carreraConsulta = carreraC.get()
    tipoConsulta = tipoC.get()
    motivoConsulta = motivoC.get()
    materiaConsulta = materiaC.get()
    escuelaConsulta = escuelaC.get()

    # Conexión a la base de datos
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='datosalumnosbajas'
    )

    cursor = conn.cursor()

    # Construir la consulta SQL con los filtros ingresados
    query = f" SELECT * FROM formulario WHERE 1=1"

    if anioConsulta:
        query += f" AND (fecha_solicitud >= '{anioConsulta}-01-01' AND fecha_solicitud <= '{anioConsulta}-12-31')"
    if fechaConsulta:
        query += f" AND fecha_solicitud = '{fechaConsulta}'"
    if generacionConsulta:
        query += f" AND generacion = {generacionConsulta}"
    if nombreConsulta:
        query += f" AND nombre = '{nombreConsulta}'"
    if claveConsulta:
        query += f" AND clave_unica = {claveConsulta}"
    if carreraConsulta:
        query += f" AND carrera = '{carreraConsulta}'"
    if tipoConsulta:
        query += f" AND tipobaja = '{tipoConsulta}'"
    if motivoConsulta:
        query += f" AND motbaja = '{motivoConsulta}'"
    if materiaConsulta:
        query += f" AND (matdif1 = '{materiaConsulta}' OR matdif2 = '{materiaConsulta}' OR matdif3 = '{materiaConsulta}')"
    if escuelaConsulta:
        query += f" AND prepa_origen = '{escuelaConsulta}'"

    # Ejecutar la consulta SQL
    cursor.execute(query)

    # Obtener los resultados de la consulta
    results = cursor.fetchall()

    # Crear una ventana para mostrar los resultados
    ventana_resultados = Tk()
    ventana_resultados.title("Resultados de la búsqueda")
    ventana_resultados.geometry("800x300")

    # Add a Scrollbar(horizontal)
    h=Scrollbar(ventana_resultados, orient='horizontal')
    h.pack(side=BOTTOM, fill='x')
    
    # Crear una tabla para mostrar los resultados
    global tabla_resultados
    tabla_resultados = ttk.Treeview(ventana_resultados, xscrollcommand=h.set)
    tabla_resultados['columns'] = ('ID', 'Clave', 'Nombre', 'Apellido paterno', 'Apellido materno',
                                   'Correo', 'Fecha de solicitud', 'Carrera', 'Generación', 'Tipo baja',
                                   'Motivo baja', 'Prepa origen', 'Materia difícil I', 'Materia difícil II',
                                   'Materia difícil III', 'Forma titulación', 'Fecha egel', 'Detalles baja', 'Empresa')

    tabla_resultados.column('#0', width=0, stretch=NO)
    tabla_resultados.column('ID', anchor=CENTER, width=40)
    tabla_resultados.column('Clave', anchor=CENTER, width=60)
    tabla_resultados.column('Nombre', anchor=CENTER, width=80)
    tabla_resultados.column('Apellido paterno', anchor=CENTER, width=110)
    tabla_resultados.column('Apellido materno', anchor=CENTER, width=110)
    tabla_resultados.column('Correo', anchor=CENTER, width=160)
    tabla_resultados.column('Fecha de solicitud', anchor=CENTER, width=120)
    tabla_resultados.column('Carrera', anchor=CENTER, width=130)
    tabla_resultados.column('Generación', anchor=CENTER, width=90)
    tabla_resultados.column('Tipo baja', anchor=CENTER, width=90)
    tabla_resultados.column('Motivo baja', anchor=CENTER, width=110)
    tabla_resultados.column('Prepa origen', anchor=CENTER, width=120)
    tabla_resultados.column('Materia difícil I', anchor=CENTER, width=130)
    tabla_resultados.column('Materia difícil II', anchor=CENTER, width=130)
    tabla_resultados.column('Materia difícil III', anchor=CENTER, width=130)
    tabla_resultados.column('Forma titulación', anchor=CENTER, width=130)
    tabla_resultados.column('Fecha egel', anchor=CENTER, width=120)
    tabla_resultados.column('Detalles baja', anchor=CENTER, width=110)
    tabla_resultados.column('Empresa', anchor=CENTER, width=100)

    tabla_resultados.heading('#0', text='', anchor=CENTER)
    tabla_resultados.heading('ID', text='ID', anchor=CENTER)
    tabla_resultados.heading('Clave', text='Clave', anchor=CENTER)
    tabla_resultados.heading('Nombre', text='Nombre', anchor=CENTER)
    tabla_resultados.heading('Apellido paterno', text='Apellido paterno', anchor=CENTER)
    tabla_resultados.heading('Apellido materno', text='Apellido materno', anchor=CENTER)
    tabla_resultados.heading('Correo', text='Correo', anchor=CENTER)
    tabla_resultados.heading('Fecha de solicitud', text='Fecha de solicitud', anchor=CENTER)
    tabla_resultados.heading('Carrera', text='Carrera', anchor=CENTER)
    tabla_resultados.heading('Generación', text='Generación', anchor=CENTER)
    tabla_resultados.heading('Tipo baja', text='Tipo baja', anchor=CENTER)
    tabla_resultados.heading('Motivo baja', text='Motivo baja', anchor=CENTER)
    tabla_resultados.heading('Prepa origen', text='Prepa origen', anchor=CENTER)
    tabla_resultados.heading('Materia difícil I', text='Materia difícil I', anchor=CENTER)
    tabla_resultados.heading('Materia difícil II', text='Materia difícil II', anchor=CENTER)
    tabla_resultados.heading('Materia difícil III', text='Materia difícil III', anchor=CENTER)
    tabla_resultados.heading('Forma titulación', text='Forma titulación', anchor=CENTER)
    tabla_resultados.heading('Fecha egel', text='Fecha egel', anchor=CENTER)
    tabla_resultados.heading('Detalles baja', text='Detalles baja', anchor=CENTER)
    tabla_resultados.heading('Empresa', text='Empresa', anchor=CENTER)

    # Insertar los resultados en la tabla
    for row in results:
        tabla_resultados.insert('', 'end', values=row)

    tabla_resultados.pack(expand=YES, fill=BOTH)

    # Attach the scrollbar with the text widget
    h.config(command=tabla_resultados.xview)

    # Agregar botón de exportar a Excel
    btn_exportar = Button(ventana_resultados, text="Exportar a Excel", command=exportar_a_excel)
    btn_exportar.pack()

    ventana_resultados.mainloop()

#Función para exportar la consulta que hayamos creado a un archivo de excel
def exportar_a_excel():
    # Obtener los datos de la tabla
    datos = []
    for item in tabla_resultados.get_children():
        datos.append(tabla_resultados.item(item)['values'])

    # Crear un DataFrame de pandas con los datos
    df = pd.DataFrame(datos, columns=['ID', 'Clave', 'Nombre', 'Apellido paterno', 'Apellido materno',
                                      'Correo', 'Fecha de solicitud', 'Carrera', 'Generación', 'Tipo baja',
                                      'Motivo baja', 'Prepa origen', 'Materia difícil I', 'Materia difícil II',
                                      'Materia difícil III', 'Forma titulación', 'Fecha egel', 'Detalles baja', 'Empresa'])

    # Obtener el directorio y nombre del archivo para guardar
    directorio = filedialog.askdirectory()
    nombre_archivo = filedialog.asksaveasfilename(defaultextension=".xlsx")

    if directorio and nombre_archivo:
        # Crear un objeto Path para el directorio y el archivo
        directorio_path = Path(directorio)
        archivo_path = Path(nombre_archivo)

        # Combinar el directorio y el nombre de archivo correctamente
        archivo_guardar = directorio_path / archivo_path

        # Guardar el DataFrame en un archivo Excel
        df.to_excel(archivo_guardar, index=False)
        messagebox.showinfo("Exportar a Excel", "Los datos se exportaron correctamente.")
    else:
        messagebox.showwarning("Exportar a Excel", "Debes seleccionar un directorio y proporcionar un nombre de archivo.")

def abrir_ventana_nueva():
    # Código para abrir la ventana nueva
        excel.ventanaConsulta()

#Función para mostrar la ventana emergente que servirá para obtener las consultas 
def emergente_consulta():
    global ventana_emergente

    #Variables para la creación del frame
    ventana_emergente = Toplevel()
    ventana_emergente.geometry("800x300")
    ventana_emergente.title("Sistema de bajas de INFOCOMP - Generar consulta")

    #Boton que muestra directamente todos los formularios
    btn_VF = Button(ventana_emergente, text="Ver todos los formularios", width=25, height=2, command=abrir_ventana_nueva)
    btn_VF.place(x=300, y=10)

    #Inicialización de variables para la realización de las consultas en cada filtro
    global anioC, fechaC, generacionC, nombreC, claveC, carreraC, tipoC, motivoC, materiaC, escuelaC

    anioC = StringVar()
    fechaC = StringVar()
    generacionC = StringVar()
    nombreC = StringVar()
    claveC = StringVar()
    carreraC = StringVar()
    tipoC = StringVar()
    motivoC = StringVar()
    materiaC = StringVar()
    escuelaC = StringVar()

    #Búsqueda por AÑO en el que se creó el formulario. En la línea de values es dónde se anexan los valores del combobox. 
    Año = Label(ventana_emergente, text="Año:")
    Año.place(x=15, y=70)

    BuscarAño = ttk.Entry(ventana_emergente, width=20, textvariable=anioC)
    BuscarAño.place(x=85, y=70)

    #Búsqueda por FECHA específica de la creación del formulario a consultar 
    Fecha = Label(ventana_emergente, text="Fecha:")
    Fecha.place(x=15, y=100)

    BuscarFecha = DateEntry(ventana_emergente, selectmode='day', date_pattern='yyyy/mm/dd', textvariable=fechaC)
    BuscarFecha.delete(0, "end")  ## Only this line needed to be added to clear the field.
    BuscarFecha.grid(row=1,column=1,padx=85, pady=100)


    #Búsqueda por GENERACIÓN. En la línea de values es dónde se anexan los valores del combobox. 
    Generacion = Label(ventana_emergente, text="Generación:")
    Generacion.place(x=15, y=130)

    BuscarGeneracion = ttk.Entry(ventana_emergente, width=20, textvariable=generacionC)
    BuscarGeneracion.place(x=85, y=130)

    #Búsqueda por NOMBRE del alumno 
    NombreAlumno = Label(ventana_emergente, text="Nombre:")
    NombreAlumno.place(x=15, y=160)

    BuscarNombreAlumno = ttk.Entry(ventana_emergente, width=23, textvariable=nombreC)
    BuscarNombreAlumno.place(x=85, y=160)

    #Búsqueda por CLAVE del alumno 
    ClaveAlumno = Label(ventana_emergente, text="Clave:")
    ClaveAlumno.place(x=15, y=190)

    BuscarClaveAlumno = ttk.Entry(ventana_emergente, width=11, textvariable=claveC)
    BuscarClaveAlumno.place(x=85, y=190)

    #Búsqueda por CARRERA. En la línea de values es dónde se anexan los valores del combobox. 
    Carrera = Label(ventana_emergente, text="Carrera:")
    Carrera.place(x=15, y=220)

    BuscarCarrera = ttk.Combobox(ventana_emergente, state="readonly", textvariable=carreraC)
    BuscarCarrera.place(x=85, y=220)

    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT Carrera FROM carreras"
    resultados = conexion.ejecutar_consulta(consulta)
    conexion.desconectar()

     # Limpiar el ComboBox
    BuscarCarrera['values'] = ()

    # Agregar los resultados al ComboBox
    BuscarCarrera['values'] = [""] + [resultado[0] for resultado in resultados]

    #Búsqueda por TIPO DE BAJA. En la línea de values es dónde se anexan los valores del combobox. 
    TipoBaja = Label(ventana_emergente, text="Tipo de baja:")
    TipoBaja.place(x=300, y=70)

    BuscarTipoBaja = ttk.Combobox(ventana_emergente, state="readonly", textvariable=tipoC)
    BuscarTipoBaja.place(x=445, y=70)

    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT nombre_tipobaja FROM tipo_de_baja"
    resultados = conexion.ejecutar_consulta(consulta)
    conexion.desconectar()

     # Limpiar el ComboBox
    BuscarTipoBaja['values'] = ()

    # Agregar los resultados al ComboBox
    BuscarTipoBaja['values'] = [""] + [resultado[0] for resultado in resultados]

    #Búsqueda por MOTIVO DE BAJA. En la línea de values es dónde se anexan los valores del combobox. 
    MotivoBaja = Label(ventana_emergente, text="Motivo de baja:")
    MotivoBaja.place(x=300, y=100)

    BuscarMotivoBaja = ttk.Combobox(ventana_emergente, state="readonly", textvariable=motivoC)
    BuscarMotivoBaja.place(x=445, y=100)

    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT nombre_motbaja FROM motivo_baja"
    resultados = conexion.ejecutar_consulta(consulta)
    conexion.desconectar()

     # Limpiar el ComboBox
    BuscarMotivoBaja['values'] = ()

    # Agregar los resultados al ComboBox
    BuscarMotivoBaja['values'] = [""] + [resultado[0] for resultado in resultados]

    #Búsqueda por MATERIA MÁS DIFÍCIL. En la línea de values es dónde se anexan los valores del combobox. 
    MateriaDificil = Label(ventana_emergente, text="Materia más difícil:")
    MateriaDificil.place(x=300, y=130)

    BuscarMateriaDificil = ttk.Combobox(ventana_emergente, state="readonly", width=30, textvariable=materiaC)
    BuscarMateriaDificil.place(x=445, y=130)

    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT nombre_materia FROM materias_dificiles"
    resultados = conexion.ejecutar_consulta(consulta)
    conexion.desconectar()

     # Limpiar el ComboBox
    BuscarMateriaDificil['values'] = ()

    # Agregar los resultados al ComboBox
    BuscarMateriaDificil['values'] = [""] + [resultado[0] for resultado in resultados]

    #Búsqueda por ESCUELA DE PROCEDENCIA. En la línea de values es dónde se anexan los valores del combobox. 
    EscuelaProc = Label(ventana_emergente, text="Escuela de procedencia:")
    EscuelaProc.place(x=300, y=160)

    BuscarEscuelaProc = ttk.Combobox(ventana_emergente, state="readonly", width=30, textvariable=escuelaC)
    BuscarEscuelaProc.place(x=445, y=160)
    
    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT nombre_prepa FROM prepa_procedencia"
    resultados = conexion.ejecutar_consulta(consulta)
    conexion.desconectar()

    # Limpiar el ComboBox
    BuscarEscuelaProc['values'] = ()

    # Agregar los resultados al ComboBox
    BuscarEscuelaProc['values'] = [""] + [resultado[0] for resultado in resultados]

    btn_RB = Button(ventana_emergente, text="Realizar búsqueda", width=25, height=2, command=haz_consulta)
    btn_RB.place(x=600, y=250)

    ventana_emergente.mainloop()
