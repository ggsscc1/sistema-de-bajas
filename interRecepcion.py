import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from DBconection import *
from GeneraCarta import * 
import customtkinter
from CTkTable import *
import consulta
import consultaG
import os
from PIL import Image

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de bajas - Recepción")
        #self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.__appearance_mode=customtkinter.set_appearance_mode("light")


        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Sistema de bajas\ndel CiComp.",
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Inicio",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Formularios",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Consultas",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "System", "Dark"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        #cambiando fuentes
        self.home_frame_Titulo = customtkinter.CTkLabel(self.home_frame, text="Sistema de bajas", fg_color="grey", font=customtkinter.CTkFont(size=20, weight="bold"), padx=5, pady=5, corner_radius=15)
        self.home_frame_Titulo.grid(row=0, column=0, padx=20, pady=10, columnspan=3)
        
        self.home_frame_Clave = customtkinter.CTkLabel(self.home_frame, text="Clave única\ndel alumno: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.home_frame_Clave.grid(row=1, column=0, padx=20, pady=10)
        
        
        self.home_frame_claveA = tk.StringVar()
        self.home_frame_Clave_Entry = customtkinter.CTkEntry(self.home_frame, textvariable=self.home_frame_claveA)
        self.home_frame_Clave_Entry.grid(row=1, column=1, padx=20, pady=10)

        

    # Crear etiquetas para mostrar la información del alumno
        self.home_frame_claveR = tk.StringVar()
        self.home_frame_nombreR = tk.StringVar()
        self.home_frame_carreraR = tk.StringVar()
        self.home_frame_generacionR = tk.StringVar()

        self.home_frame_clave_alumno_label = customtkinter.CTkLabel(self.home_frame, anchor="w",text="",font=customtkinter.CTkFont(size=15, weight="normal"), justify="left")
        self.home_frame_nombre_alumno_label = customtkinter.CTkLabel(self.home_frame, anchor="w",text="", font=customtkinter.CTkFont(size=15, weight="normal"), justify="left")
        self.home_frame_carrera_alumno_label = customtkinter.CTkLabel(self.home_frame, anchor="w",text="", font=customtkinter.CTkFont(size=15, weight="normal"), justify="left")
        self.home_frame_generacion_alumno_label = customtkinter.CTkLabel(self.home_frame, anchor="w",text="", font=customtkinter.CTkFont(size=15, weight="normal"), justify="left")

        self.home_frame_button_Buscar = customtkinter.CTkButton(self.home_frame, text="Buscar", command=lambda:self.buscaAlumno())
        self.home_frame_button_Buscar.grid(row=1, column=2, padx=20, pady=10)

        
        self.home_frame_clave_alumno_label.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_nombre_alumno_label.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_carrera_alumno_label.grid(row=4, column=0, padx=20, pady=10)
        self.home_frame_generacion_alumno_label.grid(row=5, column=0, padx=20, pady=10)

        self.home_frame_button_Registrar = customtkinter.CTkButton(self.home_frame, text="Registrar", command=lambda:self.insertaEnLista())
        self.home_frame_button_Registrar.grid(row=6, column=2, padx=20, pady=10)
        self.home_frame_button_Registrar.grid_remove()
        
        self.home_frame_button_Limpiar = customtkinter.CTkButton(self.home_frame, text="Limpiar", command=lambda:self.limpiainfo(), fg_color="transparent", text_color="black")
        self.home_frame_button_Limpiar.grid(row=6, column=1, padx=20, pady=10)
        self.home_frame_button_Limpiar.grid_remove()

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        # Consulta a realizar
        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
        conexion.conectar()
        consulta = f"SELECT * FROM formulario"
        resultado = conexion.ejecutar_consulta(consulta)

        #label formulario
        iniform = customtkinter.CTkLabel(self.second_frame, text="Selecciona tu formulario")
        iniform.grid(row=0, column=0, padx=10, pady=10, sticky="w", columnspan=3)

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 13)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

     

        # Crear un Treeview con 3 columnas
        treeview = ttk.Treeview(self.second_frame, columns=('fecha', 'clave', 'nombre', 'completado'), show='headings', style="mystyle.Treeview")
        treeview.grid(row= 1, column=0, pady=10, padx=20, sticky="nsew", rowspan=2)

        # Configurar encabezados de columna
        treeview.heading('fecha', text='Fecha')
        treeview.heading('clave', text='Clave')
        treeview.heading('nombre', text='Nombre')
        treeview.heading('completado', text='Completado?')
        completado = "NO"
        
        # Agregar datos
        for result in resultado:
            if resultado[0][10] :
                completado = "SI"
                treeview.insert('', tk.END , text=result[0], values=(result[6], result[1], result[2], completado))
        
        # Establecer ancho de columna
        treeview.column('fecha', width=100)
        treeview.column('clave', width=100)
        treeview.column('nombre', width=100)
        treeview.column('completado', width=110)



        # Crear un botón "Generar Formulario" que muestra la ventana con los datos correspondientes
        #
        btn_formulario = customtkinter.CTkButton(self.second_frame, text="Abrir Formulario", command=lambda: self.formularios(treeview.item(treeview.focus(), "values")))
        btn_formulario.grid(row= 3, column=0, padx=10, pady=10, sticky="w")

        self.lbl_fecha = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_fecha.grid(row=1, column=3, padx=10, pady=10)
        self.lbl_fecha_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_fecha_valor.grid(row=1, column=4, padx=10, pady=10)

        self.lbl_clave = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_clave.grid(row=1, column=5, padx=10, pady=10)
        self.lbl_clave_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_clave_valor.grid(row=1, column=6, padx=10, pady=10)

        self.lbl_nombre = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_nombre.grid(row=2, column=3, padx=10, pady=10)
        self.lbl_nombre_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_nombre_valor.grid(row=2, column=4, padx=10, pady=10) 
        
        self.lbl_correo = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_correo.grid(row=2, column=5, padx=10, pady=10)
        self.lbl_correo_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_correo_valor.grid(row=2, column=6, padx=10, pady=10)
        
        self.lbl_carrera = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_carrera.grid(row=3, column=3, padx=10, pady=10)
        self.lbl_carrera_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_carrera_valor.grid(row=3, column=4, padx=10, pady=10)

        self.lbl_generacion = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_generacion.grid(row=3, column=5, padx=10, pady=10)
        self.lbl_generacion_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_generacion_valor.grid(row=3, column=6, padx=10, pady=10)
        
        #"Motivo de Baja"
        self.lbl_motivo = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_motivo.grid(row=4, column=3, padx=10, pady=10)
        self.lbl_motivo_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_motivo_valor.grid(row=4, column=4, padx=10, pady=10)

        #Escuela de procedencia
        self.lbl_prpa = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_prpa.grid(row=4, column=5, padx=10, pady=10)
        self.lbl_prepa_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_prepa_valor.grid(row=4, column=6, padx=10, pady=10)

        #materias mas dificiles
        
        self.lbl_materia = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_materia.grid(row=5, column=3, padx=10, pady=10)
        self.lbl_materia_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_materia_valor.grid(row=5, column=4, padx=10, pady=10)

        self.lbl_materia2 = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_materia2.grid(row=5, column=5, padx=10, pady=10)
        self.lbl_materia2_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_materia2_valor.grid(row=5, column=6, padx=10, pady=10)

        self.lbl_materia3 = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_materia3.grid(row=6, column=3, padx=10, pady=10)    
        self.lbl_materia3_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_materia3_valor.grid(row=6, column=4, padx=10, pady=10)
        
        self.lbl_tipoB = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_tipoB.grid(row=6, column=5, padx=10, pady=10)
        self.lbl_tipoB_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_tipoB_valor.grid(row=6, column=6, padx=10, pady=10)

        # Agregar etiquetas para mostrar los datos adicionales
        self.lbl_motivotexto = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_motivotexto.grid(row=7, column=3, padx=10, pady=10)
        self.lbl_motivotexto_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_motivotexto_valor.grid(row=7, column=4, padx=10, pady=10)

        self.lbl_formatexto = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_formatexto.grid(row=7, column=5, padx=10, pady=10)
        self.lbl_formatexto_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_formatexto_valor.grid(row=7, column=6, padx=10, pady=10)

        self.lbl_fechaTtexto = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_fechaTtexto.grid(row=8, column=3, padx=10, pady=10)
        self.lbl_fechaTtexto_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_fechaTtexto_valor.grid(row=8, column=4, padx=10, pady=10)

        self.lbl_empresa = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_empresa.grid(row=8, column=5, padx=10, pady=10)
        self.lbl_empresa_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_empresa_valor.grid(row=8, column=6, padx=10, pady=10)

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        #label consultas
        Cons = customtkinter.CTkLabel(self.third_frame, text="Consultas")
        Cons.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        #, command=abrir_ventana_nueva
        btn_VF = customtkinter.CTkButton(self.third_frame, text="Ver todos los formularios", width=25, height=2)
        btn_VF.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        #Inicialización de variables para la realización de las consultas en cada filtro
        self.anioC = StringVar()
        self.generacionC = StringVar()
        self.carreraC = StringVar()
        self.tipoC = StringVar()
        self.motivoC = StringVar()
        self.materiaC = StringVar()
        self.escuelaC = StringVar()

        #Búsqueda por AÑO en el que se creó el formulario. En la línea de values es dónde se anexan los valores del combobox. 
        Año = customtkinter.CTkLabel(self.third_frame, text="Año:")
        Año.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        #combobox para la busqueda por anio de completacion de formulario
        BuscarAnio = customtkinter.CTkComboBox(self.third_frame, state="readonly", variable=self.anioC)
        BuscarAnio.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
        conexion.conectar()
        consulta = f"SELECT * FROM datosalumnosbajas.view_anio;"
        resultados = conexion.ejecutar_consulta(consulta)
        conexion.desconectar()

        # Limpiar el ComboBox
        BuscarAnio['values'] = ()

        # Agregar los resultados al ComboBox
        BuscarAnio['values'] = [""] + [resultado[0] for resultado in resultados]
        
        #SELECT * FROM datosalumnosbajas.view_generaciones;

        #Búsqueda por GENERACIÓN. En la línea de values es dónde se anexan los valores del combobox. 
        Generacion = customtkinter.CTkLabel(self.third_frame, text="Generación:")
        Generacion.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        #BuscarGeneracion = ttk.Entry(self.third_frame, width=20, variable=generacionC)
        #BuscarGeneracion.place(x=85, y=100)

        #combobox para la busqueda por generacion de los alumnos
        BuscarGen = customtkinter.CTkComboBox(self.third_frame, state="readonly", variable=self.generacionC)
        BuscarGen.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
        conexion.conectar()
        consulta = f"SELECT * FROM datosalumnosbajas.view_generaciones;"
        resultados = conexion.ejecutar_consulta(consulta)
        conexion.desconectar()

        # Limpiar el ComboBox
        BuscarGen['values'] = ()

        # Agregar los resultados al ComboBox
        BuscarGen['values'] = [""] + [resultado[0] for resultado in resultados]

        #Búsqueda por CARRERA. En la línea de values es dónde se anexan los valores del combobox. 
        Carrera = customtkinter.CTkLabel(self.third_frame, text="Carrera:")
        Carrera.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        BuscarCarrera = customtkinter.CTkComboBox(self.third_frame, state="readonly", variable=self.carreraC)
        BuscarCarrera.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
        conexion.conectar()
        consulta = f"SELECT * FROM datosalumnosbajas.view_carreras;"
        resultados = conexion.ejecutar_consulta(consulta)
        conexion.desconectar()

        # Limpiar el ComboBox
        BuscarCarrera['values'] = ()

        # Agregar los resultados al ComboBox
        BuscarCarrera['values'] = [""] + [resultado[0] for resultado in resultados]

        #Búsqueda por TIPO DE BAJA. En la línea de values es dónde se anexan los valores del combobox. 
        TipoBaja = customtkinter.CTkLabel(self.third_frame, text="Tipo de baja:")
        TipoBaja.grid(row=2, column=2, padx=10, pady=10, sticky="w")

        BuscarTipoBaja = customtkinter.CTkComboBox(self.third_frame, state="readonly", variable=self.tipoC)
        BuscarTipoBaja.grid(row=2, column=3, padx=10, pady=10, sticky="w")

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
        MotivoBaja = customtkinter.CTkLabel(self.third_frame, text="Motivo de baja:")
        MotivoBaja.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        BuscarMotivoBaja = customtkinter.CTkComboBox(self.third_frame, state="readonly", variable=self.motivoC)
        BuscarMotivoBaja.grid(row=3, column=1, padx=10, pady=10, sticky="w")

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
        MateriaDificil = customtkinter.CTkLabel(self.third_frame, text="Materia más difícil:")
        MateriaDificil.grid(row=3, column=2, padx=10, pady=10, sticky="w")

        BuscarMateriaDificil = customtkinter.CTkComboBox(self.third_frame, state="readonly", width=30, variable=self.materiaC)
        BuscarMateriaDificil.grid(row=3, column=3, padx=10, pady=10, sticky="w")

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
        EscuelaProc = customtkinter.CTkLabel(self.third_frame, text="Escuela de procedencia:")
        EscuelaProc.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        BuscarEscuelaProc = customtkinter.CTkComboBox(self.third_frame, state="readonly", width=30, variable=self.escuelaC)
        BuscarEscuelaProc.grid(row=4, column=1, padx=10, pady=10, sticky="w")
        
        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
        conexion.conectar()
        consulta = f"SELECT nombre_prepa FROM prepa_procedencia"
        resultados = conexion.ejecutar_consulta(consulta)
        conexion.desconectar()

        # Limpiar el ComboBox
        BuscarEscuelaProc['values'] = ()

        # Agregar los resultados al ComboBox
        BuscarEscuelaProc['values'] = [""] + [resultado[0] for resultado in resultados]

        #, command=haz_consulta
        btn_RB = customtkinter.CTkButton(self.third_frame, text="Realizar búsqueda", width=25, height=2)
        btn_RB.grid(row=5, column=0, padx=10, pady=10, sticky="w")


        # Crear un botón "Haz consulta"
        btn_consulta = customtkinter.CTkButton(self.third_frame, text="Consulta de datos", command=lambda:self.abre_consulta())
        btn_consulta.grid(row= 99, column=0, padx=10, pady=10, sticky="w")

        # Crear un botón "Haz consulta grafica"
        btn_consulta = customtkinter.CTkButton(self.third_frame, text="Consulta grafica", command=lambda:self.abre_consultaG())
        btn_consulta.grid(row= 98, column=0, padx=10, pady=10, sticky="w")
        # select default frame
        self.select_frame_by_name("Inicio")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "Inicio" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "Formularios" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "Consultas" else "transparent")

        # show selected frame
        if name == "Inicio":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "Formularios":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "Consultas":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("Inicio")

    def frame_2_button_event(self):
        self.select_frame_by_name("Formularios")

    def frame_3_button_event(self):
        self.select_frame_by_name("Consultas")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    
    def limpiainfo(self):
        self.home_frame_clave_alumno_label.grid_remove()
        self.home_frame_nombre_alumno_label.grid_remove()
        self.home_frame_carrera_alumno_label.grid_remove()
        self.home_frame_generacion_alumno_label.grid_remove()
        self.home_frame_button_Registrar.grid_remove()
        self.home_frame_button_Limpiar.grid_remove()
        
    def abre_consulta(self):
        consulta.emergente_consulta()

    def abre_consultaG(self):
        consultaG.cosulta_grafica()
        

    def mostrar_informacion_alumno(self):
        self.home_frame_clave_alumno_label.grid()
        self.home_frame_nombre_alumno_label.grid()
        self.home_frame_carrera_alumno_label.grid()
        self.home_frame_generacion_alumno_label.grid()
        self.home_frame_button_Registrar.grid()
        self.home_frame_button_Limpiar.grid()
         
        self.home_frame_clave_alumno_label.configure(text="Clave única del alumno: " + self.home_frame_claveR.get())
        self.home_frame_nombre_alumno_label.configure(text="Nombre del Alumno: " + self.home_frame_nombreR.get())
        self.home_frame_carrera_alumno_label.configure(text="Carrera del Alumno: " + self.home_frame_carreraR.get())
        self.home_frame_generacion_alumno_label.configure(text="Generación del Alumno: " + self.home_frame_generacionR.get())

    def buscaAlumno(self):
        claveAlumno = self.home_frame_claveA.get()
        print(claveAlumno)
        # Realizar la consulta del alumno mediante su clave única
        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
        conexion.conectar()
        consulta = f"SELECT * FROM alumnos_infbasica WHERE clave_unica = '{claveAlumno}'"
        resultado = conexion.ejecutar_consulta(consulta)

        if resultado:
            
            self.home_frame_claveR.set(resultado[0][0])
            self.home_frame_nombreR.set(resultado[0][1])
            self.home_frame_carreraR.set(resultado[0][4])
            self.home_frame_generacionR.set(resultado[0][5])

            
            self.mostrar_informacion_alumno()
            conexion.desconectar()   
        else:
            messagebox.showerror("Error", "No se encontró ningún alumno con la clave proporcionada.")
            conexion.desconectar()

            # Función que permite insertar al alumno en la lista de espera
            
    def insertaEnLista(self):
        clave = self.home_frame_claveR.get()
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
            self.limpiainfo()
            messagebox.showinfo(message="Alumno registrado con éxito", title="Éxito")
            cursor.close()
            conn.close()
            
        else:
            self.limpiainfo()
            messagebox.showerror(message="Alumno no registrado", title="Error")
            cursor.close()
            conn.close()
            

    def formularios(self, fila_seleccionada):
        #Consulta a realizar
        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
        conexion.conectar()
        print (fila_seleccionada[1])
        consulta = f"SELECT * FROM formulario WHERE clave_unica = '{fila_seleccionada[1]}'"
        resultado = conexion.ejecutar_consulta(consulta)
        conexion.desconectar()

        # Crear etiquetas para los campos fecha, clave y nombre
        #print(resultado[0][6])
        
        self.lbl_fecha.configure(text="Fecha:")
        self.lbl_fecha_valor.configure(text=resultado[0][6])

        self.lbl_clave.configure(text="Clave:")
        self.lbl_clave_valor.configure(text=resultado[0][1])

        self.lbl_nombre.configure(text="Nombre:")
        self.lbl_nombre_valor.configure(text=resultado[0][2]+"\n"+resultado[0][3]+" "+resultado[0][4])

        self.lbl_correo.configure(text="Correo electronico:")
        self.lbl_correo_valor.configure(text=resultado[0][5])

        self.lbl_carrera.configure(text="Carrera:")
        self.lbl_carrera_valor.configure(text=resultado[0][7])

        self.lbl_generacion.configure(text="Generacion:")
        self.lbl_generacion_valor.configure( text=resultado[0][8])

        self.lbl_motivo.configure(text="Motivo de baja:")
        self.lbl_motivo_valor.configure(text=resultado[0][10])
        
        self.lbl_prpa.configure(text="Preparatoria de procedencia:")
        self.lbl_prepa_valor.configure(text=resultado[0][11])

        self.lbl_materia.configure(text="Materia más dificil:")
        self.lbl_materia_valor.configure(text=resultado[0][12])
        self.lbl_materia2.configure(text="Materia más dificil II:")
        self.lbl_materia2_valor.configure(text=resultado[0][13])
        self.lbl_materia3.configure(text="Materia más dificil III:")
        self.lbl_materia3_valor.configure(text=resultado[0][14])

        self.lbl_tipoB.configure(text="Tipo de baja:")
        self.lbl_tipoB_valor.configure(text=resultado[0][9])

        self.lbl_motivotexto.configure(text="Porqué se da de baja:")
        self.lbl_motivotexto_valor.configure(text=resultado[0][17])

        self.lbl_formatexto.configure(text="Forma Titulacion:")
        if resultado[0][15]:
            self.lbl_formatexto_valor.configure(text=resultado[0][15])
            #self.lbl_formatexto_valor['text']= resultado[0][15]
        else:
            self.lbl_formatexto_valor.configure(text="No aplica")
        
        

        self.lbl_fechaTtexto.configure(text="Fecha EGEL:")
        if resultado[0][16]:
            self.lbl_fechaTtexto_valor.configure(text=resultado[0][16])
        else:
            self.lbl_fechaTtexto_valor.configure(text="No aplica")
    

        self.lbl_empresa.configure(text="Empresa la que trabaja:")
        if resultado[0][18]:
            self.lbl_empresa_valor.configure(text=resultado[0][18])
            #self.lbl_empresa_valor['text']=resultado[0][18]
        else:
            self.lbl_empresa_valor.configure(text="No aplica")

        
        # Crear un botón para generar documento sellos
        btn_sell = customtkinter.CTkButton(self.second_frame, text="Generar carta de sellos",text_color="black", command= lambda:GeneraCarta(resultado[0][1]))
        btn_sell.grid(row=9, column=3, padx=10, pady=10)

        # Crear un botón para generar documento sellos
        btn_cart = customtkinter.CTkButton(self.second_frame, text="Generar carta de no adeudo", fg_color="light blue", text_color="black", command= lambda:GeneraCarta(resultado[0][1]))
        btn_cart.grid(row=9, column=4, padx=10, pady=10)

        # Crear un botón para generar documento sellos
        btn_edit = customtkinter.CTkButton(self.second_frame, text="Regresa a edición", fg_color="transparent", text_color="black", command= lambda:GeneraCarta(resultado[0][1]))
        btn_edit.grid(row=9, column=5, padx=10, pady=10)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()

