import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from DBconection import *
import customtkinter
import consulta
import consultaG
import os


class App2(customtkinter.CTk):
    def __init__(self):
        #Conexion a la base de datos
        conexionPrin = ConexionBD(user='root',password='root',host='localhost',database='datosalumnosbajas')
        conexionPrin.conectar()
        
        #Consulta a base de datos para las materias
        consultaMaterias = f"SELECT nombre_materia FROM materias_dificiles"
        resMaterias = conexionPrin.ejecutar_consulta(consultaMaterias)
        listaMaterias = [mat[0] for mat in resMaterias]
        
        #Consulta a base de datos para las preparatorias
        consultaPrepas = f"SELECT nombre_prepa FROM prepa_procedencia"
        resPrepas = conexionPrin.ejecutar_consulta(consultaPrepas)
        listaPrepas = [tb[0] for tb in resPrepas]
        
        #Consulta a base de datos para los tipos de bajas
        consultaTipoBaja = f"SELECT nombre_tipobaja FROM tipo_de_baja"
        restiposBaja = conexionPrin.ejecutar_consulta(consultaTipoBaja)
        listaTiposBaja = [tb[0] for tb in restiposBaja]
        
        #Consulta a base de datos para los motivos de baja
        consultaMotBaja = f"SELECT nombre_motbaja FROM motivo_baja"
        resMotBaja = conexionPrin.ejecutar_consulta(consultaMotBaja)
        listaMotivosBaja = [mot[0] for mot in resMotBaja]
        
        #Consulta a base de datos para los tipos de titulacion
        consultaFormaTitulacion = f"SELECT nombre_formatit FROM forma_titulacion"
        resFormaTitulacion = conexionPrin.ejecutar_consulta(consultaFormaTitulacion)
        listaFormaTitulacion = [mot[0] for mot in resFormaTitulacion]

        conexionPrin.desconectar()


        super().__init__()

        self.title("Sistema de bajas - Administrador")
        #self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.__appearance_mode=customtkinter.set_appearance_mode("light")


        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Formularios",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Editar usuario",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Agregar Usuario",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_logoutbutton = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Cerrar sesión",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("red", "gray30"),
                                                      anchor="w", command=self.frame_4_button)
        self.frame_logoutbutton.grid(row=4, column=0, sticky="ews")

        #################################################################################################
        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_columnconfigure(1, weight=1)
        self.home_frame.grid_columnconfigure(2, weight=1)
        

        #label formulario
        iniform = customtkinter.CTkLabel(self.home_frame, text="Selecciona tu formulario")
        iniform.grid(row=0, column=0, padx=10, pady=10)

        self.botonrecargar = customtkinter.CTkButton(self.home_frame, text="Recarga la tabla", command=lambda:self.updatetreeviewFORMS())
        self.botonrecargar.grid(row=0, column=1, padx=10, pady=10)

        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 13)) # Modify the font of the body
        self.style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        self.style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders


        # Crear un Treeview con 3 columnas
        self.treeview2 = ttk.Treeview(self.home_frame, columns=('fecha', 'clave', 'nombre', 'completado'), show='headings', style="mystyle.Treeview")
        self.treeview2.grid(row= 1, column=0, pady=10, padx=20, sticky="nsew", rowspan=2, columnspan=6)

        self.treeview2.bind("<Double-1>", lambda event: self.open_formularios(event))

        # Configurar encabezados de columna
        self.treeview2.heading('fecha', text='Fecha')
        self.treeview2.heading('clave', text='Clave')
        self.treeview2.heading('nombre', text='Nombre')
        self.treeview2.heading('completado', text='¿Completado?')

        # Establecer ancho de columna
        self.treeview2.column('fecha', width=100)
        self.treeview2.column('clave', width=100)
        self.treeview2.column('nombre', width=100)
        self.treeview2.column('completado', width=110)

        # Crear un botón "Generar Formulario" que muestra la ventana con los datos correspondientes
        btn_formulario = customtkinter.CTkButton(self.home_frame, text="Abrir Formulario", command=lambda: self.formularios(self.treeview2.item(self.treeview2.focus(), "values")))
        btn_formulario.grid(row= 3, column=0, padx=10, pady=10)

        #Crea boton no se mostrara hasta mostrar un formulario y que realiza la accion de editar

        self.btn_EDITAformulario = customtkinter.CTkButton(self.home_frame, text="Editar Formulario", command=lambda: self.updateBase())
        self.btn_EDITAformulario.grid(row= 5, column=2, padx=10, pady=10)
        self.btn_EDITAformulario.grid_remove()

        self.firstInterFrame = customtkinter.CTkFrame(self.home_frame)
        self.firstInterFrame.grid(row=4, column=0, padx=5, pady=5, rowspan=1)
        self.firstInterFrame.grid_remove()

        self.secondInterFrame = customtkinter.CTkFrame(self.home_frame)
        self.secondInterFrame.grid(row=4, column=1, padx=5, pady=5, rowspan=1)
        self.secondInterFrame.grid_remove()
        
        self.thirdInterFrame = customtkinter.CTkFrame(self.home_frame)
        self.thirdInterFrame.grid(row=4, column=2, padx=5, pady=5, rowspan=1)
        self.thirdInterFrame.grid_remove()

        self.lbl_fecha = customtkinter.CTkLabel(self.firstInterFrame, text="")
        self.lbl_fecha.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.lbl_fecha_valor = customtkinter.CTkEntry(self.firstInterFrame)
        self.lbl_fecha_valor.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.lbl_correo = customtkinter.CTkLabel(self.firstInterFrame, text="")
        self.lbl_correo.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.lbl_correo_valor = customtkinter.CTkEntry(self.firstInterFrame)
        self.lbl_correo_valor.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        #"Motivo de Baja"
        self.lbl_motivo = customtkinter.CTkLabel(self.firstInterFrame, text="")
        self.lbl_motivo.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.lbl_motivo_valor = customtkinter.CTkComboBox(self.firstInterFrame, values=listaMotivosBaja)
        self.lbl_motivo_valor.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.lbl_materia2 = customtkinter.CTkLabel(self.thirdInterFrame, text="")
        self.lbl_materia2.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.lbl_materia2_valor = customtkinter.CTkComboBox(self.thirdInterFrame, values=listaMaterias)
        self.lbl_materia2_valor.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Agregar etiquetas para mostrar los datos adicionales
        self.lbl_motivotexto = customtkinter.CTkLabel(self.firstInterFrame, text="")
        self.lbl_motivotexto.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.lbl_motivotexto_valor = customtkinter.CTkEntry(self.firstInterFrame)
        self.lbl_motivotexto_valor.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        
        self.lbl_empresa = customtkinter.CTkLabel(self.thirdInterFrame, text="")
        self.lbl_empresa.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.lbl_empresa_valor = customtkinter.CTkEntry(self.thirdInterFrame)
        self.lbl_empresa_valor.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        
        self.lbl_clave = customtkinter.CTkLabel(self.secondInterFrame, text="")
        self.lbl_clave.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.lbl_clave_valor = customtkinter.CTkEntry(self.secondInterFrame)
        self.lbl_clave_valor.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.lbl_carrera = customtkinter.CTkLabel(self.secondInterFrame, text="")
        self.lbl_carrera.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.lbl_carrera_valor = customtkinter.CTkEntry(self.secondInterFrame)
        self.lbl_carrera_valor.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        #Escuela de procedencia
        self.lbl_prpa = customtkinter.CTkLabel(self.secondInterFrame, text="")
        self.lbl_prpa.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.lbl_prepa_valor = customtkinter.CTkComboBox(self.secondInterFrame, values=listaPrepas)
        self.lbl_prepa_valor.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.lbl_materia3 = customtkinter.CTkLabel(self.firstInterFrame, text="")
        self.lbl_materia3.grid(row=3, column=0, padx=5, pady=5, sticky="e")    
        self.lbl_materia3_valor = customtkinter.CTkComboBox(self.firstInterFrame, values=listaMaterias)
        self.lbl_materia3_valor.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.lbl_formatexto = customtkinter.CTkLabel(self.secondInterFrame, text="")
        self.lbl_formatexto.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.lbl_formatexto_valor = customtkinter.CTkComboBox(self.secondInterFrame, values=listaFormaTitulacion)
        self.lbl_formatexto_valor.grid(row=3, column=1, padx=5, pady=5, sticky="w")


        #row 6 y 7

        self.lbl_nombre = customtkinter.CTkLabel(self.thirdInterFrame, text="")
        self.lbl_nombre.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.lbl_nombre_valor = customtkinter.CTkEntry(self.thirdInterFrame)
        self.lbl_nombre_valor.grid(row=0, column=1, padx=5, pady=5, sticky="w") 
        
        self.lbl_generacion = customtkinter.CTkLabel(self.thirdInterFrame, text="")
        self.lbl_generacion.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.lbl_generacion_valor = customtkinter.CTkEntry(self.thirdInterFrame)
        self.lbl_generacion_valor.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        #materias mas dificiles
        
        self.lbl_materia = customtkinter.CTkLabel(self.secondInterFrame, text="")
        self.lbl_materia.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.lbl_materia_valor = customtkinter.CTkComboBox(self.secondInterFrame, values=listaMaterias)
        self.lbl_materia_valor.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.lbl_tipoB = customtkinter.CTkLabel(self.thirdInterFrame, text="")
        self.lbl_tipoB.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.lbl_tipoB_valor = customtkinter.CTkComboBox(self.thirdInterFrame, values=listaTiposBaja)
        self.lbl_tipoB_valor.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.lbl_fechaTtexto = customtkinter.CTkLabel(self.secondInterFrame, text="")
        self.lbl_fechaTtexto.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.lbl_fechaTtexto_valor = customtkinter.CTkComboBox(self.secondInterFrame, values=["Marzo", "Agosto", "Diciembre"])
        self.lbl_fechaTtexto_valor.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        
        
        ##########################################################################################################
        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)
        self.second_frame.grid_columnconfigure(1, weight=1)
        self.second_frame.grid_columnconfigure(2, weight=1)
 


       

        #label usuarios
        self.home_frame_titleUsuario = customtkinter.CTkLabel(self.second_frame, text="Usuarios", fg_color="white", font=customtkinter.CTkFont(size=20, weight="bold"), padx=5, pady=5, corner_radius=15)
        self.home_frame_titleUsuario.grid(row=0, column=0, padx=20, pady=10)

        self.botonrecargar2 = customtkinter.CTkButton(self.second_frame, text="Recarga la tabla", command=lambda:self.updatetreeview())
        self.botonrecargar2.grid(row=0, column=1, padx=10, pady=10)

        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 13)) # Modify the font of the body
        self.style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        self.style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        # Crear un Treeview con 5 columnas
        self.treeview = ttk.Treeview(self.second_frame, columns=('Nom Usuario', 'Email', 'Nombre', 'Ap Paterno', 'Tipo', 'Activo'), show='headings', style="mystyle.Treeview")
        self.treeview.grid(row= 1, column=0, pady=10, padx=20, sticky="nsew", rowspan=2, columnspan=6)

        self.treeview.bind("<Double-1>", lambda event: self.open_usuarios(event))
        
        # Configurar encabezados de columna
        self.treeview.heading('Nom Usuario', text='Nombre de usuario')
        self.treeview.heading('Email', text='Correo')
        self.treeview.heading('Nombre', text='Nombre')
        self.treeview.heading('Ap Paterno', text='Apellido Paterno')
        self.treeview.heading('Tipo', text='Tipo')
        self.treeview.heading('Activo', text='Activo')
        
        # Establecer ancho de columna
        self.treeview.column('Nom Usuario', width=200)
        self.treeview.column('Email', width=200)
        self.treeview.column('Nombre', width=200)
        self.treeview.column('Ap Paterno', width=210)
        self.treeview.column('Tipo', width=100)
        self.treeview.column('Activo', width=100)

        # Crear un botón "Generar Formulario" que muestra la ventana con los datos correspondientes
        
        btn_editar = customtkinter.CTkButton(self.second_frame, text="Ver información", command=lambda: self.usuarios(self.treeview.item(self.treeview.focus(), "values")))
        btn_editar.grid(row= 3, column=0, padx=5, pady=5)


        self.btn_formularioUser = customtkinter.CTkButton(self.second_frame, text="Editar Información", command=lambda: self.updateBase2())
        self.btn_formularioUser.grid(row= 5, column=2, padx=5, pady=5)
        self.btn_formularioUser.grid_remove()

        self.firstInterFrameUSER = customtkinter.CTkFrame(self.second_frame)
        self.firstInterFrameUSER.grid(row=4, column=0, padx=5, pady=5, rowspan=1)
        self.firstInterFrameUSER.grid_remove()

        self.secondInterFrameUSER = customtkinter.CTkFrame(self.second_frame)
        self.secondInterFrameUSER.grid(row=4, column=1, padx=5, pady=5, rowspan=1)
        self.secondInterFrameUSER.grid_remove()
        
        self.thirdInterFrameUSER = customtkinter.CTkFrame(self.second_frame)
        self.thirdInterFrameUSER.grid(row=4, column=2, padx=5, pady=5, rowspan=1)
        self.thirdInterFrameUSER.grid_remove()

        self.lbl_Nom_usuario = customtkinter.CTkLabel(self.firstInterFrameUSER, text="")
        self.lbl_Nom_usuario.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.lbl_Nom_usuario.grid_remove()
        self.lbl_Nom_usuario_valor = customtkinter.CTkEntry(self.firstInterFrameUSER)
        self.lbl_Nom_usuario_valor.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.lbl_Nom_usuario_valor.grid_remove()
        self.lbl_Nom_usuario_valor.configure(validate="key")
        self.lbl_Nom_usuario_valor.configure(validatecommand=(self.register(self.validate_entry35CHAR), "%S", "%P"))


        self.lbl_clave2 = customtkinter.CTkLabel(self.firstInterFrameUSER, text="")
        self.lbl_clave2.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.lbl_clave2.grid_remove()
        self.lbl_clave_valor2 = customtkinter.CTkEntry(self.firstInterFrameUSER)
        self.lbl_clave_valor2.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.lbl_clave_valor2.grid_remove()
        self.lbl_clave_valor2.configure(validate="key")
        self.lbl_clave_valor2.configure(validatecommand=(self.register(self.validate_entry30CHAR), "%S", "%P"))

        self.lbl_nombre2 = customtkinter.CTkLabel(self.firstInterFrameUSER, text="")
        self.lbl_nombre2.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.lbl_nombre2.grid_remove()
        self.lbl_nombre_valor2 = customtkinter.CTkEntry(self.firstInterFrameUSER)
        self.lbl_nombre_valor2.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.lbl_nombre_valor2.grid_remove()
        self.lbl_nombre_valor2.configure(validate="key")
        self.lbl_nombre_valor2.configure(validatecommand=(self.register(self.validate_entry45CHAR), "%S", "%P"))
        
        self.lbl_Ap_paterno = customtkinter.CTkLabel(self.secondInterFrameUSER, text="")
        self.lbl_Ap_paterno.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.lbl_Ap_paterno.grid_remove()
        self.lbl_Ap_paterno_valor = customtkinter.CTkEntry(self.secondInterFrameUSER)
        self.lbl_Ap_paterno_valor.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.lbl_Ap_paterno_valor.grid_remove()
        # Set up validation of characters
        self.lbl_Ap_paterno_valor.configure(validate="key")
        self.lbl_Ap_paterno_valor.configure(validatecommand=(self.register(self.validate_entry30CHAR), "%S", "%P"))
        
        self.lbl_Ap_materno = customtkinter.CTkLabel(self.secondInterFrameUSER, text="")
        self.lbl_Ap_materno.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.lbl_Ap_materno.grid_remove()
        self.lbl_Ap_materno_valor = customtkinter.CTkEntry(self.secondInterFrameUSER)
        self.lbl_Ap_materno_valor.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.lbl_Ap_materno_valor.grid_remove()
        # Set up validation of characters
        self.lbl_Ap_materno_valor.configure(validate="key")
        self.lbl_Ap_materno_valor.configure(validatecommand=(self.register(self.validate_entry30CHAR), "%S", "%P"))

        self.lbl_Email = customtkinter.CTkLabel(self.secondInterFrameUSER, text="")
        self.lbl_Email.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.lbl_Email.grid_remove()
        self.lbl_Email_valor = customtkinter.CTkEntry(self.secondInterFrameUSER)
        self.lbl_Email_valor.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.lbl_Email_valor.grid_remove()
        # Set up validation of characters
        self.lbl_Email_valor.configure(validate="key")
        self.lbl_Email_valor.configure(validatecommand=(self.register(self.validate_entry50CHAR), "%S", "%P"))
        
        #tipo de usuario
        self.lbl_tipoUs = customtkinter.CTkLabel(self.thirdInterFrameUSER, text="")
        self.lbl_tipoUs.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.lbl_tipoUs.grid_remove()
        self.lbl_tipoUs_valor = customtkinter.CTkEntry(self.thirdInterFrameUSER)
        self.lbl_tipoUs_valor.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.lbl_tipoUs_valor.grid_remove()
        self.lbl_tipoUs_valor.configure(validate="key")
        self.lbl_tipoUs_valor.configure(validatecommand=(self.register(self.digitos), "%S", "%P"))

        #activo
        self.lbl_activo = customtkinter.CTkLabel(self.thirdInterFrameUSER, text="")
        self.lbl_activo.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.lbl_activo.grid_remove()
        self.lbl_activo_valor = customtkinter.CTkEntry(self.thirdInterFrameUSER)
        self.lbl_activo_valor.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.lbl_activo_valor.grid_remove()
        self.lbl_activo_valor.configure(validate="key")
        self.lbl_activo_valor.configure(validatecommand=(self.register(self.digitos), "%S", "%P"))
        
        
        # create third frame
        ############################################################################
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        self.third_frame.grid_columnconfigure(0, weight=1)
        

        

        #cambiando fuentes
        self.third_frame_Titulo = customtkinter.CTkLabel(self.third_frame, text="Registrar nuevo usuario", fg_color="white", font=customtkinter.CTkFont(size=20, weight="bold"), padx=5, pady=5, corner_radius=15)
        self.third_frame_Titulo.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        self.oneInterFrame = customtkinter.CTkFrame(self.third_frame)
        self.oneInterFrame.grid(row=1, column=0, padx=5, pady=5, rowspan=1)
        

        self.twoInterFrame = customtkinter.CTkFrame(self.third_frame)
        self.twoInterFrame.grid(row=2, column=0, padx=5, pady=5, rowspan=1)
        

        self.third_frame_Clave = customtkinter.CTkLabel(self.oneInterFrame, text="Información básica: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.third_frame_Clave.grid(row=0, column=0,padx=5, pady=10, sticky = "nswe", columnspan=2)
        
        self.third_frame_Clave = customtkinter.CTkLabel(self.oneInterFrame, text="Nombre: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.third_frame_Clave.grid(row=1, column=0,padx=5, pady=10, sticky = "e")
        
        self.third_frame_Clave = customtkinter.CTkLabel(self.oneInterFrame, text="Primer apellido: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.third_frame_Clave.grid(row=2, column=0,padx=5, pady=10, sticky = "e")
        
        self.third_frame_Clave = customtkinter.CTkLabel(self.oneInterFrame, text="Segundo apellido: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.third_frame_Clave.grid(row=3, column=0,padx=5, pady=10, sticky = "e")

        ###################################################################
        #inter frame 2
        
        self.third_frame_Clave = customtkinter.CTkLabel(self.twoInterFrame, text="Información de usuario: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.third_frame_Clave.grid(row=0, column=0,padx=5, pady=10, sticky = "nswe", columnspan=2)

        self.third_frame_Clave = customtkinter.CTkLabel(self.twoInterFrame, text="Correo electrónico: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.third_frame_Clave.grid(row=1, column=0,padx=5, pady=10, sticky = "e")

        self.third_frame_Clave = customtkinter.CTkLabel(self.twoInterFrame, text="Nombre de usuario: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.third_frame_Clave.grid(row=2, column=0,padx=5, pady=10, sticky = "e")

        self.third_frame_Clave = customtkinter.CTkLabel(self.twoInterFrame, text="Contraseña: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.third_frame_Clave.grid(row=3, column=0,padx=5, pady=10, sticky = "e")


        self.third_frame_Clave_Entry1 = customtkinter.CTkEntry(self.oneInterFrame)
        self.third_frame_Clave_Entry1.grid(row=1, column=1,padx=5, pady=10, sticky = "w")

        # Set up validation to allow only 45 characters
        self.third_frame_Clave_Entry1.configure(validate="key")
        self.third_frame_Clave_Entry1.configure(validatecommand=(self.register(self.validate_entry45CHAR), "%S", "%P"))

        self.third_frame_Clave_Entry2 = customtkinter.CTkEntry(self.oneInterFrame)
        self.third_frame_Clave_Entry2.grid(row=2, column=1,padx=5, pady=10, sticky = "w")

        # Set up validation of characters
        self.third_frame_Clave_Entry2.configure(validate="key")
        self.third_frame_Clave_Entry2.configure(validatecommand=(self.register(self.validate_entry30Apellidos), "%S", "%P"))

        self.third_frame_Clave_Entry3 = customtkinter.CTkEntry(self.oneInterFrame)
        self.third_frame_Clave_Entry3.grid(row=3, column=1,padx=5, pady=10, sticky = "w")

        # Set up validation of characters
        self.third_frame_Clave_Entry3.configure(validate="key")
        self.third_frame_Clave_Entry3.configure(validatecommand=(self.register(self.validate_entry30Apellidos), "%S", "%P"))


        ############################################
        #second frame

        self.third_frame_Clave_Entry4 = customtkinter.CTkEntry(self.twoInterFrame)
        self.third_frame_Clave_Entry4.grid(row=1, column=1,padx=5, pady=10, sticky = "w")

        # Set up validation of characters
        self.third_frame_Clave_Entry4.configure(validate="key")
        self.third_frame_Clave_Entry4.configure(validatecommand=(self.register(self.validate_entry50CHAR), "%S", "%P"))

        self.third_frame_Clave_Entry5 = customtkinter.CTkEntry(self.twoInterFrame)
        self.third_frame_Clave_Entry5.grid(row=2, column=1,padx=5, pady=10, sticky = "w")

        # Set up validation of characters
        self.third_frame_Clave_Entry5.configure(validate="key")
        self.third_frame_Clave_Entry5.configure(validatecommand=(self.register(self.validate_entry35CHAR), "%S", "%P"))

        self.third_frame_Clave_Entry6 = customtkinter.CTkEntry(self.twoInterFrame, show='*')
        self.third_frame_Clave_Entry6.grid(row=3, column=1,padx=5, pady=10, sticky = "w")

        # Set up validation of characters
        self.third_frame_Clave_Entry6.configure(validate="key")
        self.third_frame_Clave_Entry6.configure(validatecommand=(self.register(self.validate_entry30CHAR), "%S", "%P"))


        self.third_frame_button_Registrar = customtkinter.CTkButton(self.third_frame, text="Registrar")
        
        self.third_frame_button_Buscar = customtkinter.CTkButton(self.third_frame, text="Registrar", command=lambda:self.registro())
        self.third_frame_button_Buscar.grid(row=3, column=0, pady=10)


        ##########################################################################################
        # select default frame
        self.select_frame_by_name("Formularios")

    def digitos(self, char, current_value):
        # Allow the user to enter characters
        if char.isalpha() or char.isspace():
            return False

        # Check if the entered character is between 0 and 1
        return len(current_value) <=1 and 0 <= float(char) <= 1 if char.isdigit() or char == '.' else False

    
    def validate_entry30CHAR(self, char, current_value):
        # Check if the length of the current value is less than or equal to 
        return len(current_value + char) <= 30 #tamanio en la base de datos
    
    def validate_entry30Apellidos(self, char, current_value):
        # Check if the length of the current value is less than or equal to 
        return len(current_value + char) <= 30 and char.isalpha()#tamanio en la base de datos
    
    def validate_entry35CHAR(self, char, current_value):
        # Check if the length of the current value is less than or equal to 
        return len(current_value + char) <= 35#tamanio en la base de datos
    
    def validate_entry45CHAR(self, char, current_value):
        # Check if the length of the current value is less than or equal to 
        return len(current_value + char) <= 45 and char.isalpha()

    def validate_entry50CHAR(self, char, current_value):
        return len(current_value + char) <= 50#tamanio en la base de datos
    
    def validate_entry60CHAR(self, char, current_value):
        return len(current_value + char) <= 60 and char.isalpha() #tamanio en la base de datos
    
    
    
   
    

    def updateBase(self):
        #obtien los campos del formulario
        fecha_valor = self.lbl_fecha_valor.get()
        clave_valor = self.lbl_clave_valor.get()
        nombre_valor = self.lbl_nombre_valor.get()
        correo_valor = self.lbl_correo_valor.get()
        carrera_valor = self.lbl_carrera_valor.get()
        generacion_valor = self.lbl_generacion_valor.get()
        motivo_valor = self.lbl_motivo_valor.get()
        prepa_valor = self.lbl_prepa_valor.get()
        materia_valor = self.lbl_materia_valor.get()#depennde
        materia2_valor = self.lbl_materia2_valor.get()#depennde
        materia3_valor = self.lbl_materia3_valor.get()#depennde
        tipoB_valor = self.lbl_tipoB_valor.get()
        motivoTexto_valor = self.lbl_motivotexto_valor.get()#depende
        formatexto_valor = self.lbl_formatexto_valor.get()#depende
        fechaTtexto_valor = self.lbl_fechaTtexto_valor.get()#depende
        empresa_valor = self.lbl_empresa_valor.get()#depende

        # Conexión a la base de datos
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='datosalumnosbajas'
        )

        cursor = conn.cursor()

        # consulta a Realizar el update en la base de datos
        query = f"UPDATE formulario SET fecha_solicitud = '{fecha_valor}', clave_unica = '{clave_valor}', email_alumno = '{correo_valor}', carrera = '{carrera_valor}', generacion = '{generacion_valor}', motbaja = '{motivo_valor}', prepa_origen = '{prepa_valor}', tipobaja = '{tipoB_valor}'"
        
        #dependiendo si estan estos valores si no no
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

        query2 = f"WHERE clave_unica = '{clave_valor}'"
        queryFinal = query + " " +query2
        
        # Ejecutar la consulta SQL
        cursor.execute(queryFinal)

        # Confirmar los cambios en la base de datos
        conn.commit()

        # Consultar la base de datos para verificar el resultado actualizado
        select_query = f"SELECT * FROM formulario WHERE clave_unica = '{clave_valor}'"
        cursor.execute(select_query)
        result = cursor.fetchone()

        if result:
            # Mostrar el resultado actualizado
            # Confirmación de actualización
            messagebox.showinfo("Confirmación", "El registro ha sido actualizado correctamente.")
        else:
            messagebox.showinfo("Error", "El registro no se ha encontrado.")

        # Cerrar la conexión a la base de datos
        cursor.close()
        conn.close()
    
    def updateBase2(self):
        nom_user = self.lbl_Nom_usuario_valor.get()
        password = self.lbl_clave_valor2.get()
        nombre_valor = self.lbl_nombre_valor2.get()
        Ap = self.lbl_Ap_paterno_valor.get()
        Am = self.lbl_Ap_materno_valor.get()
        email = self.lbl_Email_valor.get()
        tipo_us = self.lbl_tipoUs_valor.get()
        activo = self.lbl_activo_valor.get()
       

        # Conexión a la base de datos
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='datosalumnosbajas'
        )

        cursor = conn.cursor()

    # Realizar el update en la base de datos
        query = f"UPDATE usuarios SET nom_usuario = '{nom_user}', password = '{password}', nombre = '{nombre_valor}', ap_paterno = '{Ap}', ap_materno = '{Am}', email = '{email}', tipo_usuario = '{tipo_us}', activo = '{activo}'"
        #, materia_dificil = '{materia_valor}', materia_dificil2 = '{materia2_valor}', materia_dificil3 = '{materia3_valor}', detalles_baja = '{motivotexto_valor}', forma_titulacion = '{formatexto_valor}', fecha_egel = '{fechaTtexto_valor}'

       

        query2 = f"WHERE nom_usuario = '{nom_user}'"
        queryFinal = query + " " +query2
        
        # Ejecutar la consulta SQL
        cursor.execute(queryFinal)

        # Confirmar los cambios en la base de datos
        conn.commit()

        # Consultar la base de datos para verificar el resultado actualizado
        select_query = f"SELECT * FROM usuarios WHERE nom_usuario = '{nom_user}'"
        cursor.execute(select_query)
        result = cursor.fetchone()

        if result:
            # Mostrar el resultado actualizado
            # Confirmación de actualización
            messagebox.showinfo("Confirmación", "El registro ha sido actualizado correctamente.")
        else:
            messagebox.showinfo("Error", "El registro no se ha encontrado.")

        # Cerrar la conexión a la base de datos
        cursor.close()
        conn.close()
    
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "Formularios" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "Editar usuario" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "Agregar usuario" else "transparent")

        # show selected frame
        if name == "Agregar usuario":
            self.third_frame.grid(row=0, column=1, sticky="nsew")

        else:
            self.third_frame.grid_forget()

        if name == "Editar usuario":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "Formularios":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()


    def home_button_event(self):
        self.select_frame_by_name("Formularios")

    def frame_2_button_event(self):
        self.select_frame_by_name("Editar usuario")

    def frame_3_button_event(self):
        self.select_frame_by_name("Agregar usuario")

    def frame_4_button(self):#clase actual
        import Loginc2
        self.destroy()#cierra la clase actual (el programa)
        Loginc2.run()
    
    def registro(self):
        bd_nombre = self.third_frame_Clave_Entry1.get()
        bd_ap_paterno = self.third_frame_Clave_Entry2.get()
        bd_ap_materno = self.third_frame_Clave_Entry3.get()
        bd_email = self.third_frame_Clave_Entry4.get()
        bd_nom_usuario = self.third_frame_Clave_Entry5.get()
        bd_password = self.third_frame_Clave_Entry6.get()

        if not all([bd_nombre, bd_ap_paterno, bd_email, bd_nom_usuario, bd_password]) :
            messagebox.showerror(message="Ingresa los campos obligatorios", title="Error")
            return
        
        # Verificar si bd_email contiene el carácter "@"
        if "@" not in bd_email:
            messagebox.showerror(message="Ingresa un correo electrónico valido", title="Error")
            return
        

        # Hash the password before storing itS
        

        # Database interaction
        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
        conexion.conectar()

        insertar = f"INSERT INTO usuarios (nom_usuario, password, nombre, ap_paterno, ap_materno, email, tipo_usuario, activo) " \
                f"VALUES ('{bd_nom_usuario}', '{bd_password}', " \
                f"'{bd_nombre}', '{bd_ap_paterno}', '{bd_ap_materno}', '{bd_email}', '1', '0')"

        # Execute the query and check for errors
        try:
            resultado = conexion.ejecutar_consulta(insertar)
           

            if resultado is not None:
                messagebox.showinfo(message="Usuario registrado con éxito", title="Éxito")
                self.clear_entry_fields()
            else:
                messagebox.showerror(message="Error en el registro", title="Error")
        except Exception as e:
            messagebox.showerror(message=f"Error en el registro: {str(e)}", title="Error")

        conexion.desconectar()

    def clear_entry_fields(self):
    # Clear all entry fields
        for entry in [self.third_frame_Clave_Entry1, self.third_frame_Clave_Entry2,
                    self.third_frame_Clave_Entry3, self.third_frame_Clave_Entry4,
                    self.third_frame_Clave_Entry5, self.third_frame_Clave_Entry6]:
            entry.delete(0, "end")

        

    def formularios(self, fila_seleccionada):
        #Consulta a realizar
        conexion = ConexionBD(user='root',password='root',host='localhost',database='datosalumnosbajas')
        conexion.conectar()
        #print (fila_seleccionada[1])
        consulta = f"SELECT * FROM formulario WHERE clave_unica = '{fila_seleccionada[1]}'"
        resultado = conexion.ejecutar_consulta(consulta)
        conexion.desconectar()

        # Crear etiquetas para los campos fecha, clave y nombre
        #print(resultado[0][6])


        self.btn_EDITAformulario.grid()
        self.firstInterFrame.grid()
        self.secondInterFrame.grid()
        self.thirdInterFrame.grid()

        
        self.lbl_fecha.configure(text="Fecha:")
        self.lbl_fecha_valor.delete(0, tk.END)
        self.lbl_fecha_valor.insert(0,resultado[0][6])
        #self.lbl_fecha_valor.configure(text=resultado[0][6])

        self.lbl_clave.configure(text="Clave:")
        self.lbl_clave_valor.delete(0, tk.END)
        self.lbl_clave_valor.insert(0,resultado[0][1])
        #self.lbl_clave_valor.configure(text=resultado[0][1])

        self.lbl_nombre.configure(text="Nombre:")
        self.lbl_nombre_valor.delete(0, tk.END)
        self.lbl_nombre_valor.insert(0,resultado[0][2]+" "+resultado[0][3]+" "+resultado[0][4])
        #self.lbl_nombre_valor.configure(text=resultado[0][2]+" "+resultado[0][3]+" "+resultado[0][4])

        self.lbl_correo.configure(text="Correo electrónico:")
        self.lbl_correo_valor.delete(0, tk.END)
        self.lbl_correo_valor.insert(0,resultado[0][5])
        #self.lbl_correo_valor.configure(text=resultado[0][5])

        self.lbl_carrera.configure(text="Carrera:")
        self.lbl_carrera_valor.delete(0, tk.END)
        self.lbl_carrera_valor.insert(0,resultado[0][7])
        #self.lbl_carrera_valor.configure(text=resultado[0][7])

        self.lbl_generacion.configure(text="Generación:")
        self.lbl_generacion_valor.delete(0, tk.END)
        self.lbl_generacion_valor.insert(0,resultado[0][8])
        #self.lbl_generacion_valor.configure( text=resultado[0][8])

        self.lbl_motivo.configure(text="Motivo de baja:")
        self.lbl_motivo_valor.set("")
        self.lbl_motivo_valor.set(resultado[0][10])
        #self.lbl_motivo_valor.configure(text=resultado[0][10])
        
        self.lbl_prpa.configure(text="Preparatoria de procedencia:")
        self.lbl_prepa_valor.set("")
        self.lbl_prepa_valor.set(resultado[0][11])
        #self.lbl_prepa_valor.configure(text=resultado[0][11])

        self.lbl_materia.configure(text="Materia más difícil:")
        self.lbl_materia_valor.set("")
        self.lbl_materia_valor.set(resultado[0][12])
        #self.lbl_materia_valor.configure(text=resultado[0][12])
        self.lbl_materia2.configure(text="Materia más difícil II:")
        self.lbl_materia2_valor.set("")
        self.lbl_materia2_valor.set(resultado[0][13])
        #self.lbl_materia2_valor.configure(text=resultado[0][13])
        self.lbl_materia3.configure(text="Materia más difícil III:")
        self.lbl_materia3_valor.set("")
        self.lbl_materia3_valor.set(resultado[0][14])
        #self.lbl_materia3_valor.configure(text=resultado[0][14])

        self.lbl_tipoB.configure(text="Tipo de baja:")
        self.lbl_tipoB_valor.set("")
        self.lbl_tipoB_valor.set(resultado[0][9])
        #self.lbl_tipoB_valor.configure(text=resultado[0][9])

        self.lbl_motivotexto.configure(text="Porque se da de baja:")
        self.lbl_motivotexto_valor.delete(0, tk.END)
        self.lbl_motivotexto_valor.insert(0,resultado[0][17])

        self.lbl_formatexto.configure(text="Forma titulación:")
        if resultado[0][15]:
            self.lbl_formatexto_valor.set("")
            self.lbl_formatexto_valor.set(resultado[0][15])
            #self.lbl_formatexto_valor.configure(text=resultado[0][15])
            #self.lbl_formatexto_valor['text']= resultado[0][15]
        else:
            self.lbl_formatexto_valor.set("")
            self.lbl_formatexto_valor.set("No aplica")
            #self.lbl_formatexto_valor.configure(text="No aplica")
        
        

        self.lbl_fechaTtexto.configure(text="Fecha aproximada EGEL:")
        if resultado[0][16]:
            self.lbl_fechaTtexto_valor.set("")
            self.lbl_fechaTtexto_valor.set(resultado[0][16])
           # self.lbl_fechaTtexto_valor.configure(text=resultado[0][16])
        else:
            self.lbl_fechaTtexto_valor.set("")
            self.lbl_fechaTtexto_valor.set( "No aplica")
            #self.lbl_fechaTtexto_valor.configure(text="No aplica")
    

        self.lbl_empresa.configure(text="Empresa la que trabaja:")
        if resultado[0][18]:
            self.lbl_empresa_valor.delete(0, tk.END)
            self.lbl_empresa_valor.insert(0, resultado[0][18])
            #self.lbl_empresa_valor.configure(text=resultado[0][18])
            #self.lbl_empresa_valor['text']=resultado[0][18]
        else:
            self.lbl_empresa_valor.delete(0, tk.END)
            self.lbl_empresa_valor.insert(0, "No aplica")
            #self.lbl_empresa_valor.configure(text="No aplica")


    def realizar_busqueda(self, event):
        # Coloca aquí el código para realizar la búsqueda
        # Por ejemplo, puedes obtener el texto del Entry con entry.get()
        self.buscaAlumno()

    # The open_formularios method can retrieve the selected row's data
    def open_formularios(self, event):

        self.formularios(self.treeview2.item(self.treeview2.focus(), "values"))
       
    # The open_usuarios method can retrieve the selected row's data
    def open_usuarios(self, event):

        self.usuarios(self.treeview.item(self.treeview.focus(), "values"))

        #funcion para abrir la información del usuario


    def usuarios(self, fila_seleccionada):
        #Consulta a realizar
        conexion = ConexionBD(user='root',password='root',host='localhost',database='datosalumnosbajas')
        conexion.conectar()
        #print (fila_seleccionada[1])
        consulta = f"SELECT * FROM usuarios WHERE nom_usuario = '{fila_seleccionada[0]}'"
        resultado = conexion.ejecutar_consulta(consulta)
        conexion.desconectar()

        self.firstInterFrameUSER.grid()
        self.secondInterFrameUSER.grid()
        self.thirdInterFrameUSER.grid()

        # Crear etiquetas para los campos fecha, clave y nombre
        #print(resultado[0][6])
        self.btn_formularioUser.grid()
        self.lbl_Nom_usuario_valor.delete(0, tk.END)
        self.lbl_Nom_usuario.grid()
        self.lbl_Nom_usuario.configure(text="Nombre de usuario:")
        self.lbl_Nom_usuario_valor.grid()
        self.lbl_Nom_usuario_valor.insert(0, resultado[0][0])
        #self.lbl_Nom_usuario_valor.configure(value=resultado[0][0])

        self.lbl_clave_valor2.delete(0, tk.END)
        self.lbl_clave2.grid()
        self.lbl_clave2.configure(text="Contraseña:")
        self.lbl_clave_valor2.grid()
        self.lbl_clave_valor2.insert(0, resultado[0][1])

        self.lbl_nombre_valor2.delete(0, tk.END)
        self.lbl_nombre2.grid()
        self.lbl_nombre2.configure(text="Nombre:")
        self.lbl_nombre_valor2.grid()
        self.lbl_nombre_valor2.insert(0, resultado[0][2])

        self.lbl_Ap_paterno_valor.delete(0, tk.END)
        self.lbl_Ap_paterno.grid()
        self.lbl_Ap_paterno.configure(text="Apellido paterno:")
        self.lbl_Ap_paterno_valor.grid()
        self.lbl_Ap_paterno_valor.insert(0, resultado[0][3])

        self.lbl_Ap_materno_valor.delete(0, tk.END)
        self.lbl_Ap_materno.grid()
        self.lbl_Ap_materno.configure(text="Apellido materno:")
        self.lbl_Ap_materno_valor.grid()
        self.lbl_Ap_materno_valor.insert(0, resultado[0][4])

        self.lbl_Email_valor.delete(0, tk.END)
        self.lbl_Email.grid()
        self.lbl_Email.configure(text="Correo electrónico:")
        self.lbl_Email_valor.grid()
        self.lbl_Email_valor.insert(0, resultado[0][5])

        self.lbl_tipoUs_valor.delete(0, tk.END)
        self.lbl_tipoUs.grid()
        self.lbl_tipoUs.configure(text="Tipo de usuario:")
        self.lbl_tipoUs_valor.grid()
        self.lbl_tipoUs_valor.insert(0, resultado[0][6])

        self.lbl_activo_valor.delete(0, tk.END)
        self.lbl_activo.grid()
        self.lbl_activo.configure(text="Activo:")
        self.lbl_activo_valor.grid()
        self.lbl_activo_valor.insert(0, resultado[0][7])
        

    def updatetreeviewFORMS(self):#self = clase actual
        #remueve la tabla y los campos de formulario en caso de que esten abiertos asi como el boton de editar
        self.treeview2.grid_remove()
        self.firstInterFrame.grid_remove()
        self.secondInterFrame.grid_remove()
        self.thirdInterFrame.grid_remove()
        self.btn_EDITAformulario.grid_remove()

        # Consulta a realizar
        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
        conexion.conectar()
        consulta = f"SELECT * FROM formulario"
        resultado = conexion.ejecutar_consulta(consulta)
        
        completado = "NO"

        #elimina los registros de la tabla
        self.treeview2.delete(*self.treeview2.get_children())

        # Agregar datos en la tabla
        for result in resultado:
            if resultado[0][10] :
                completado = "SI"
                #insserta los datos en la tabla
                self.treeview2.insert('', tk.END , text=result[0], values=(result[6], result[1], result[2], completado))

        # Llamar a la función después de 1000 milisegundos (1 segundo)
        self.after(500, self.show_treeviewFORMS)

        conexion.desconectar()

    def show_treeviewFORMS(self):#self = clase actual
        self.treeview2.grid()#muestra la tabla

    def updatetreeview(self):#self = clase actual
        #remueve la tabla y los campos de formulario en caso de que esten abiertos asi como el boton de editar usuario
        self.treeview.grid_remove()
        self.firstInterFrameUSER.grid_remove()
        self.secondInterFrameUSER.grid_remove()
        self.thirdInterFrameUSER.grid_remove()
        self.btn_formularioUser.grid_remove()

        # Consulta a realizar
        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
        conexion.conectar()
        consulta = f"SELECT * FROM usuarios"
        resultado = conexion.ejecutar_consulta(consulta)

        #elimino lo que tenga la tabla
        self.treeview.delete(*self.treeview.get_children())
        # Agregar datos
        for res in resultado:
            if resultado[0][6] is not NONE:
                if res[7] != 1:
                    activo = "Si (0)"
                else:
                    activo = "No (1)"
                if res[6] == 0:
                    tipo = "Admin (0)"
                else:
                    tipo = "Recepcion (1)"
                #inserta datos en la tabla
                self.treeview.insert('', tk.END , text=res[0], values=(res[0], res[5], res[2], res[3], tipo, activo))
        
        # Llamar a la función después de 500 milisegundos (0.5 segundo)
        self.after(500, self.show_treeview)

        conexion.desconectar()

    def show_treeview(self):#self = clase actual
        self.treeview.grid()#muestra la tabla
    
def crea_y_ejecuta():
    app = App2()
    app.updatetreeview()
    app.updatetreeviewFORMS()
    app.mainloop()
    return app

if __name__ == "__main__":
   app_instance = crea_y_ejecuta()
    