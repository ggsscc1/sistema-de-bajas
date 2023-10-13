import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter 
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
import pandas as pd

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
        self.home_frame_Titulo = customtkinter.CTkLabel(self.home_frame, text="Sistema de bajas", fg_color="darkblue", text_color="white",font=customtkinter.CTkFont(size=20, weight="bold"), padx=5, pady=5, corner_radius=15)
        self.home_frame_Titulo.grid(row=0, column=0, padx=20, pady=10, columnspan=3)
        
        self.home_frame_Clave = customtkinter.CTkLabel(self.home_frame, text="Clave única del alumno: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.home_frame_Clave.grid(row=1, column=0, padx=5, pady=10, sticky="e")
        
        
        self.home_frame_claveA = tk.StringVar()
        self.home_frame_Clave_Entry = customtkinter.CTkEntry(self.home_frame, textvariable=self.home_frame_claveA)
        self.home_frame_Clave_Entry.grid(row=1, column=1, padx=5, pady=10)

        

    # Crear etiquetas para mostrar la información del alumno
        self.home_frame_claveR = tk.StringVar()
        self.home_frame_nombreR = tk.StringVar()
        self.home_frame_carreraR = tk.StringVar()
        self.home_frame_generacionR = tk.StringVar()

        self.home_frame_clave_alumno_label = customtkinter.CTkLabel(self.home_frame, anchor="w",text="",font=customtkinter.CTkFont(size=15, weight="normal"))
        self.home_frame_nombre_alumno_label = customtkinter.CTkLabel(self.home_frame, anchor="w",text="", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.home_frame_carrera_alumno_label = customtkinter.CTkLabel(self.home_frame, anchor="w",text="", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.home_frame_generacion_alumno_label = customtkinter.CTkLabel(self.home_frame, anchor="w",text="", font=customtkinter.CTkFont(size=15, weight="normal"))

        self.home_frame_clave_alumno_valor = customtkinter.CTkLabel(self.home_frame, anchor="w",text="",font=customtkinter.CTkFont(size=15, weight="normal"))
        self.home_frame_nombre_alumno_valor = customtkinter.CTkLabel(self.home_frame, anchor="w",text="", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.home_frame_carrera_alumno_valor = customtkinter.CTkLabel(self.home_frame, anchor="w",text="", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.home_frame_generacion_alumno_valor = customtkinter.CTkLabel(self.home_frame, anchor="w",text="", font=customtkinter.CTkFont(size=15, weight="normal"))

        self.home_frame_button_Buscar = customtkinter.CTkButton(self.home_frame, text="Buscar", command=lambda:self.buscaAlumno())
        self.home_frame_button_Buscar.grid(row=1, column=2, padx=20, pady=10)

        
        self.home_frame_clave_alumno_label.grid(row=2, column=0, padx=5, pady=10, sticky="e")
        self.home_frame_nombre_alumno_label.grid(row=3, column=0, padx=5, pady=10, sticky="e")
        self.home_frame_carrera_alumno_label.grid(row=4, column=0, padx=5, pady=10, sticky="e")
        self.home_frame_generacion_alumno_label.grid(row=5, column=0, padx=5, pady=10, sticky="e")

        self.home_frame_clave_alumno_valor.grid(row=2, column=1, padx=5, pady=10, sticky="w")
        self.home_frame_nombre_alumno_valor.grid(row=3, column=1, padx=5, pady=10, sticky="w")
        self.home_frame_carrera_alumno_valor.grid(row=4, column=1, padx=5, pady=10, sticky="w")
        self.home_frame_generacion_alumno_valor.grid(row=5, column=1, padx=5, pady=10, sticky="w")

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

        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 13)) # Modify the font of the body
        self.style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        self.style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

     

        # Crear un Treeview con 3 columnas
        treeview = ttk.Treeview(self.second_frame, columns=('fecha', 'clave', 'nombre', 'completado'), show='headings', style="mystyle.Treeview")
        treeview.grid(row= 1, column=0, pady=10, padx=20, sticky="nsew", rowspan=2, columnspan=6)

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
        self.lbl_fecha.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.lbl_fecha_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_fecha_valor.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        self.lbl_clave = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_clave.grid(row=4, column=2, padx=5, pady=5, sticky="e")
        self.lbl_clave_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_clave_valor.grid(row=4, column=3, padx=5, pady=5, sticky="w")

        self.lbl_nombre = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_nombre.grid(row=4, column=4, padx=5, pady=5, sticky="e")
        self.lbl_nombre_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_nombre_valor.grid(row=4, column=5, padx=5, pady=5, sticky="w") 
        
        self.lbl_correo = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_correo.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.lbl_correo_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_correo_valor.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        
        self.lbl_carrera = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_carrera.grid(row=5, column=2, padx=5, pady=5, sticky="e")
        self.lbl_carrera_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_carrera_valor.grid(row=5, column=3, padx=5, pady=5, sticky="w")

        self.lbl_generacion = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_generacion.grid(row=5, column=4, padx=5, pady=5, sticky="e")
        self.lbl_generacion_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_generacion_valor.grid(row=5, column=5, padx=5, pady=5, sticky="w")
        
        #"Motivo de Baja"
        self.lbl_motivo = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_motivo.grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.lbl_motivo_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_motivo_valor.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        #Escuela de procedencia
        self.lbl_prpa = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_prpa.grid(row=6, column=2, padx=5, pady=5, sticky="e")
        self.lbl_prepa_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_prepa_valor.grid(row=6, column=3, padx=5, pady=5, sticky="w")

        #materias mas dificiles
        
        self.lbl_materia = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_materia.grid(row=6, column=4, padx=5, pady=5, sticky="e")
        self.lbl_materia_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_materia_valor.grid(row=6, column=5, padx=5, pady=5, sticky="w")

        self.lbl_materia2 = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_materia2.grid(row=7, column=0, padx=5, pady=5, sticky="e")
        self.lbl_materia2_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_materia2_valor.grid(row=7, column=1, padx=5, pady=5, sticky="w")

        self.lbl_materia3 = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_materia3.grid(row=7, column=2, padx=5, pady=5, sticky="e")    
        self.lbl_materia3_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_materia3_valor.grid(row=7, column=3, padx=5, pady=5, sticky="w")
        
        self.lbl_tipoB = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_tipoB.grid(row=7, column=4, padx=5, pady=5, sticky="e")
        self.lbl_tipoB_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_tipoB_valor.grid(row=7, column=5, padx=5, pady=5, sticky="w")

        # Agregar etiquetas para mostrar los datos adicionales
        self.lbl_motivotexto = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_motivotexto.grid(row=8, column=0, padx=5, pady=5, sticky="e")
        self.lbl_motivotexto_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_motivotexto_valor.grid(row=8, column=1, padx=5, pady=5, sticky="w")

        self.lbl_formatexto = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_formatexto.grid(row=8, column=2, padx=5, pady=5, sticky="e")
        self.lbl_formatexto_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_formatexto_valor.grid(row=8, column=3, padx=5, pady=5, sticky="w")

        self.lbl_fechaTtexto = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_fechaTtexto.grid(row=8, column=4, padx=5, pady=5, sticky="e")
        self.lbl_fechaTtexto_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_fechaTtexto_valor.grid(row=8, column=5, padx=5, pady=5, sticky="w")

        self.lbl_empresa = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_empresa.grid(row=9, column=0, padx=5, pady=5, sticky="e")
        self.lbl_empresa_valor = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_empresa_valor.grid(row=9, column=1, padx=5, pady=5, sticky="w")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        #label consultas
        #cambiando fuentes
        self.third_frame_Titulo = customtkinter.CTkLabel(self.third_frame, text="Consultas", fg_color="darkblue", text_color="white", font=customtkinter.CTkFont(size=20, weight="bold"), padx=5, pady=5, corner_radius=15)
        self.third_frame_Titulo.grid(row=0, column=0, padx=20, pady=10, columnspan=4)
        

         #Inicialización de variables para la realización de las consultas en cada filtro
        self.anioC = StringVar()
        self.generacionC = StringVar()
        self.carreraC = StringVar()
        self.tipoC = StringVar()
        self.motivoC = StringVar()
        self.materiaC = StringVar()
        self.escuelaC = StringVar()

        #Búsqueda por AÑO en el que se creó el formulario. En la línea de values es dónde se anexan los valores del combobox. 
        Anio = customtkinter.CTkLabel(self.third_frame, text="Año:")
        Anio.grid(row=1, column=0, padx=10, pady=10, sticky="e", columnspan=1)

        #combobox para la busqueda por anio de completacion de formulario
        BuscarAnio = customtkinter.CTkComboBox(self.third_frame, state="readonly", variable=self.anioC)
        BuscarAnio.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
        conexion.conectar()
        consulta = f"SELECT * FROM datosalumnosbajas.view_anio;"
        
        resultados = conexion.ejecutar_consulta(consulta)
        conexion.desconectar()
        
        
        #BuscarAnio.configure(values= "" + [str(resultado[0]) for resultado in resultados])
        BuscarAnio.configure(values=[""]+[str(resultado[0]) for resultado in resultados])
        

        # Limpiar el ComboBox
        
        #BuscarAnio['values'] = ()
        
        # Agregar los resultados al ComboBox
        #BuscarAnio.configure(values=[""] + [resultado[0] for resultado in resultados])
        #BuscarAnio['values'] = [""] + [resultado[0] for resultado in resultados]
        
        #SELECT * FROM datosalumnosbajas.view_generaciones;

        #Búsqueda por GENERACIÓN. En la línea de values es dónde se anexan los valores del combobox. 
        Generacion = customtkinter.CTkLabel(self.third_frame, text="Generación:")
        Generacion.grid(row=1, column=2, padx=10, pady=10, sticky="e")

        #BuscarGeneracion = ttk.Entry(self.third_frame, width=20, variable=generacionC)
        #BuscarGeneracion.place(x=85, y=100)

        #combobox para la busqueda por generacion de los alumnos
        BuscarGen = customtkinter.CTkComboBox(self.third_frame, state="readonly", variable=self.generacionC)
        BuscarGen.grid(row=1, column=3, padx=10, pady=10, sticky="e")

        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
        conexion.conectar()
        consulta = f"SELECT * FROM datosalumnosbajas.view_generaciones;"
        resultados = conexion.ejecutar_consulta(consulta)
        conexion.desconectar()

        BuscarGen.configure(values=[""]+[str(resultado[0]) for resultado in resultados])


        #Búsqueda por CARRERA. En la línea de values es dónde se anexan los valores del combobox. 
        Carrera = customtkinter.CTkLabel(self.third_frame, text="Carrera:")
        Carrera.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        BuscarCarrera = customtkinter.CTkComboBox(self.third_frame, state="readonly", variable=self.carreraC)
        BuscarCarrera.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
        conexion.conectar()
        consulta = f"SELECT * FROM datosalumnosbajas.view_carreras;"
        resultados = conexion.ejecutar_consulta(consulta)
        conexion.desconectar()

        BuscarCarrera.configure(values=[""]+[str(resultado[0]) for resultado in resultados])

        #Búsqueda por TIPO DE BAJA. En la línea de values es dónde se anexan los valores del combobox. 
        TipoBaja = customtkinter.CTkLabel(self.third_frame, text="Tipo de baja:")
        TipoBaja.grid(row=2, column=2, padx=10, pady=10, sticky="e")

        BuscarTipoBaja = customtkinter.CTkComboBox(self.third_frame, state="readonly", variable=self.tipoC)
        BuscarTipoBaja.grid(row=2, column=3, padx=10, pady=10, sticky="w")

        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
        conexion.conectar()
        consulta = f"SELECT nombre_tipobaja FROM tipo_de_baja"
        resultados = conexion.ejecutar_consulta(consulta)
        conexion.desconectar()

        BuscarTipoBaja.configure(values=[""]+[str(resultado[0]) for resultado in resultados])

        #Búsqueda por MOTIVO DE BAJA. En la línea de values es dónde se anexan los valores del combobox. 
        MotivoBaja = customtkinter.CTkLabel(self.third_frame, text="Motivo de baja:")
        MotivoBaja.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        BuscarMotivoBaja = customtkinter.CTkComboBox(self.third_frame, state="readonly", variable=self.motivoC)
        BuscarMotivoBaja.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
        conexion.conectar()
        consulta = f"SELECT nombre_motbaja FROM motivo_baja"
        resultados = conexion.ejecutar_consulta(consulta)
        conexion.desconectar()

        # Agregar los resultados al ComboBox
        BuscarMotivoBaja.configure(values=[""]+[str(resultado[0]) for resultado in resultados])

        #Búsqueda por MATERIA MÁS DIFÍCIL. En la línea de values es dónde se anexan los valores del combobox. 
        MateriaDificil = customtkinter.CTkLabel(self.third_frame, text="Materia más difícil:")
        MateriaDificil.grid(row=3, column=2, padx=10, pady=10, sticky="e")

        BuscarMateriaDificil = customtkinter.CTkComboBox(self.third_frame, state="readonly", variable=self.materiaC)
        BuscarMateriaDificil.grid(row=3, column=3, padx=10, pady=10, sticky="w")

        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
        conexion.conectar()
        consulta = f"SELECT nombre_materia FROM materias_dificiles"
        resultados = conexion.ejecutar_consulta(consulta)
        conexion.desconectar()

        # Agregar los resultados al ComboBox
        BuscarMateriaDificil.configure(values=[""]+[str(resultado[0]) for resultado in resultados])

        #Búsqueda por ESCUELA DE PROCEDENCIA. En la línea de values es dónde se anexan los valores del combobox. 
        EscuelaProc = customtkinter.CTkLabel(self.third_frame, text="Escuela de procedencia:")
        EscuelaProc.grid(row=4, column=0, padx=10, pady=10, sticky="e")

        BuscarEscuelaProc = customtkinter.CTkComboBox(self.third_frame, state="readonly", variable=self.escuelaC)
        BuscarEscuelaProc.grid(row=4, column=1, padx=10, pady=10, sticky="w")
        
        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
        conexion.conectar()
        consulta = f"SELECT nombre_prepa FROM prepa_procedencia"
        resultados = conexion.ejecutar_consulta(consulta)
        conexion.desconectar()

        # Agregar los resultados al ComboBox
        BuscarEscuelaProc.configure(values=[""]+[str(resultado[0]) for resultado in resultados])

        #, command=haz_consulta
        self.btn_RB = customtkinter.CTkButton(self.third_frame, text="Haz Consulta", command=lambda:self.haz_consulta())
        self.btn_RB.grid(row=5, column=0, padx=10, pady=10, sticky="w")

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
        self.home_frame_clave_alumno_valor.grid_remove()
        self.home_frame_nombre_alumno_valor.grid_remove()
        self.home_frame_carrera_alumno_valor.grid_remove()
        self.home_frame_generacion_alumno_valor.grid_remove()
        self.home_frame_button_Registrar.grid_remove()
        self.home_frame_button_Limpiar.grid_remove()
        
    def abre_consulta(self):
        consulta.emergente_consulta()

    #Función para la creación de las consultas
    def haz_consulta(self):
        # Tomar valores necesarios
        anioConsulta = self.anioC.get ()
        generacionConsulta = self.generacionC.get()
        carreraConsulta = self.carreraC.get()
        tipoConsulta = self.tipoC.get()
        motivoConsulta = self.motivoC.get()
        materiaConsulta = self.materiaC.get()
        escuelaConsulta = self.escuelaC.get()

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
        if generacionConsulta:
            query += f" AND generacion = {generacionConsulta}"
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
        ventana_resultados = Toplevel()
        ventana_resultados.title("Resultados de la búsqueda")
        #ventana_resultados.geometry("800x480")

        # Crear un Frame principal dentro de la ventana
        frame_principal = customtkinter.CTkScrollableFrame(ventana_resultados, orientation='horizontal')
        frame_principal.pack(fill=BOTH, expand=YES)

        
        
        # Crear una tabla para mostrar los resultados
        
        self.tabla_resultados = ttk.Treeview(frame_principal)
        self.tabla_resultados['columns'] = ('ID', 'Clave', 'Nombre', 'Apellido paterno', 'Apellido materno',
                                    'Correo', 'Fecha de solicitud', 'Carrera', 'Generación', 'Tipo baja',
                                    'Motivo baja', 'Prepa origen', 'Materia difícil I', 'Materia difícil II',
                                    'Materia difícil III', 'Forma titulación', 'Fecha egel', 'Detalles baja', 'Empresa')

        self.tabla_resultados.column('#0', width=0, stretch=NO)
        self.tabla_resultados.column('ID', anchor=CENTER, width=40)
        self.tabla_resultados.column('Clave', anchor=CENTER, width=60)
        self.tabla_resultados.column('Nombre', anchor=CENTER, width=80)
        self.tabla_resultados.column('Apellido paterno', anchor=CENTER, width=110)
        self.tabla_resultados.column('Apellido materno', anchor=CENTER, width=110)
        self.tabla_resultados.column('Correo', anchor=CENTER, width=160)
        self.tabla_resultados.column('Fecha de solicitud', anchor=CENTER, width=120)
        self.tabla_resultados.column('Carrera', anchor=CENTER, width=130)
        self.tabla_resultados.column('Generación', anchor=CENTER, width=90)
        self.tabla_resultados.column('Tipo baja', anchor=CENTER, width=90)
        self.tabla_resultados.column('Motivo baja', anchor=CENTER, width=110)
        self.tabla_resultados.column('Prepa origen', anchor=CENTER, width=120)
        self.tabla_resultados.column('Materia difícil I', anchor=CENTER, width=130)
        self.tabla_resultados.column('Materia difícil II', anchor=CENTER, width=130)
        self.tabla_resultados.column('Materia difícil III', anchor=CENTER, width=130)
        self.tabla_resultados.column('Forma titulación', anchor=CENTER, width=130)
        self.tabla_resultados.column('Fecha egel', anchor=CENTER, width=120)
        self.tabla_resultados.column('Detalles baja', anchor=CENTER, width=110)
        self.tabla_resultados.column('Empresa', anchor=CENTER, width=100)

        self.tabla_resultados.heading('#0', text='', anchor=CENTER)
        self.tabla_resultados.heading('ID', text='ID', anchor=CENTER)
        self.tabla_resultados.heading('Clave', text='Clave', anchor=CENTER)
        self.tabla_resultados.heading('Nombre', text='Nombre', anchor=CENTER)
        self.tabla_resultados.heading('Apellido paterno', text='Apellido paterno', anchor=CENTER)
        self.tabla_resultados.heading('Apellido materno', text='Apellido materno', anchor=CENTER)
        self.tabla_resultados.heading('Correo', text='Correo', anchor=CENTER)
        self.tabla_resultados.heading('Fecha de solicitud', text='Fecha de solicitud', anchor=CENTER)
        self.tabla_resultados.heading('Carrera', text='Carrera', anchor=CENTER)
        self.tabla_resultados.heading('Generación', text='Generación', anchor=CENTER)
        self.tabla_resultados.heading('Tipo baja', text='Tipo baja', anchor=CENTER)
        self.tabla_resultados.heading('Motivo baja', text='Motivo baja', anchor=CENTER)
        self.tabla_resultados.heading('Prepa origen', text='Prepa origen', anchor=CENTER)
        self.tabla_resultados.heading('Materia difícil I', text='Materia difícil I', anchor=CENTER)
        self.tabla_resultados.heading('Materia difícil II', text='Materia difícil II', anchor=CENTER)
        self.tabla_resultados.heading('Materia difícil III', text='Materia difícil III', anchor=CENTER)
        self.tabla_resultados.heading('Forma titulación', text='Forma titulación', anchor=CENTER)
        self.tabla_resultados.heading('Fecha egel', text='Fecha egel', anchor=CENTER)
        self.tabla_resultados.heading('Detalles baja', text='Detalles baja', anchor=CENTER)
        self.tabla_resultados.heading('Empresa', text='Empresa', anchor=CENTER)

        # Insertar los resultados en la tabla
        for row in results:
            self.tabla_resultados.insert('', 'end', values=row)

        #self.tabla_resultados.pack(expand=YES, fill=BOTH)
        self.tabla_resultados.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        

        frame_sec1= Frame(ventana_resultados)
        frame_sec1.pack()

        
        # Agregar botón de exportar a Excel
        btn_exportar = customtkinter.CTkButton(frame_sec1, text="Exportar a Excel", command=lambda:self.exportar_a_excel())
        btn_exportar.grid(row=0, column=0, padx=5, pady=10)

        # Agregar botón de exportar a Excel
        btn_Gen = customtkinter.CTkButton(frame_sec1, text="Grafica Generacion", command=lambda:consultaG.consulta_generacion2(results))
        btn_Gen.grid(row=0, column=1, padx=5, pady=10)

        # Agregar botón de exportar a Excel
        btn_Carrera = customtkinter.CTkButton(frame_sec1, text="Grafica Carrera", command=lambda:consultaG.consulta_carrera2(results))
        btn_Carrera.grid(row=0, column=2, padx=5, pady=10)

        # Agregar botón de exportar a Excel
        btn_escuela = customtkinter.CTkButton(frame_sec1, text="Grafica escuela", command=lambda:consultaG.consulta_escuela2(results))
        btn_escuela.grid(row=0, column=3, padx=5, pady=10)

        # Agregar botón de exportar a Excel
        btn_tramite = customtkinter.CTkButton(frame_sec1, text="Grafica tramite", command=lambda:consultaG.consulta_tramite2(results))
        btn_tramite.grid(row=0, column=4, padx=5, pady=10)

        # Agregar botón de exportar a Excel
        btn_Mat = customtkinter.CTkButton(frame_sec1, text="Materia dificil", command=lambda:consultaG.consulta_materia2(results))
        btn_Mat.grid(row=0, column=5, padx=5, pady=10)

        ventana_resultados.mainloop()

    def exportar_a_excel(self):
        # Obtener los datos de la tabla
        datos = []
        for item in self.tabla_resultados.get_children():
            datos.append(self.tabla_resultados.item(item)['values'])

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


    def abre_consultaG(self):
        consultaG.cosulta_grafica()
        

    def mostrar_informacion_alumno(self):
        self.home_frame_clave_alumno_label.grid()
        self.home_frame_nombre_alumno_label.grid()
        self.home_frame_carrera_alumno_label.grid()
        self.home_frame_generacion_alumno_label.grid()
        self.home_frame_clave_alumno_valor.grid()
        self.home_frame_nombre_alumno_valor.grid()
        self.home_frame_carrera_alumno_valor.grid()
        self.home_frame_generacion_alumno_valor.grid()
        self.home_frame_button_Registrar.grid()
        self.home_frame_button_Limpiar.grid()
         
        self.home_frame_clave_alumno_label.configure(text="Clave única del alumno:")
        self.home_frame_nombre_alumno_label.configure(text="Nombre del Alumno:")
        self.home_frame_carrera_alumno_label.configure(text="Carrera del Alumno:")
        self.home_frame_generacion_alumno_label.configure(text="Generación del Alumno:")
        self.home_frame_clave_alumno_valor.configure(text=self.home_frame_claveR.get())
        self.home_frame_nombre_alumno_valor.configure(text=self.home_frame_nombreR.get())
        self.home_frame_carrera_alumno_valor.configure(text=self.home_frame_carreraR.get())
        self.home_frame_generacion_alumno_valor.configure(text=self.home_frame_generacionR.get())

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
        btn_sell.grid(row=10, column=3, padx=10, pady=10)

        # Crear un botón para generar documento sellos
        btn_cart = customtkinter.CTkButton(self.second_frame, text="Generar carta de no adeudo", fg_color="light blue", text_color="black", command= lambda:GeneraCarta(resultado[0][1]))
        btn_cart.grid(row=10, column=4, padx=10, pady=10)

        # Crear un botón para generar documento sellos
        btn_edit = customtkinter.CTkButton(self.second_frame, text="Regresa a edición", fg_color="transparent", text_color="black", command= lambda:GeneraCarta(resultado[0][1]))
        btn_edit.grid(row=10, column=5, padx=10, pady=10)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()

