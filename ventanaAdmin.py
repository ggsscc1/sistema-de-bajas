import customtkinter
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
from PIL import Image
import CTkMessagebox
from ventana_Formulario import ventana_Formulario  
from ventana_Usuario import ventana_Usuario  




    

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de bajas - Registrar nuevo usuario")
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

        #################################################################################################
        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_columnconfigure(1, weight=1)
        self.home_frame.grid_columnconfigure(2, weight=1)
        # Consulta a realizar
        conexion = ConexionBD(user='root',password='root',host='localhost',database='datosalumnosbajas')
        conexion.conectar()
        consulta = f"SELECT * FROM formulario"
        resultado = conexion.ejecutar_consulta(consulta)

        

        #label formulario
        iniform = customtkinter.CTkLabel(self.home_frame, text="Selecciona tu formulario")
        iniform.grid(row=0, column=0, padx=10, pady=10, sticky="w", columnspan=3)

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
        self.treeview2.heading('completado', text='Completado?')
        completado = "NO"
        
        # Agregar datos
        for result in resultado:
            if resultado[0][10] :
                completado = "SI"
                self.treeview2.insert('', tk.END , text=result[0], values=(result[6], result[1], result[2], completado))
        
        # Establecer ancho de columna
        self.treeview2.column('fecha', width=100)
        self.treeview2.column('clave', width=100)
        self.treeview2.column('nombre', width=100)
        self.treeview2.column('completado', width=110)

        # Crear un botón "Generar Formulario" que muestra la ventana con los datos correspondientes
        #
        btn_formulario = customtkinter.CTkButton(self.home_frame, text="Abrir Formulario", command=lambda: self.formularios(self.treeview2.item(self.treeview2.focus(), "values")))
        btn_formulario.grid(row= 3, column=0, padx=10, pady=10)

        btn_formulario = customtkinter.CTkButton(self.home_frame, text="Editar Formulario", command=lambda: self.seleccionar_formulario(self.treeview2))
        #btn_formulario = customtkinter.CTkButton(self.home_frame, text="Editar Formulario", command=lambda: self.seleccionar_formulario(self.treeview2.item(self.treeview2.focus(), "values")))
        btn_formulario.grid(row= 3, column=1, padx=10, pady=10)

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
        self.lbl_motivo_valor = customtkinter.CTkEntry(self.firstInterFrame)
        self.lbl_motivo_valor.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.lbl_materia2 = customtkinter.CTkLabel(self.firstInterFrame, text="")
        self.lbl_materia2.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.lbl_materia2_valor = customtkinter.CTkEntry(self.firstInterFrame)
        self.lbl_materia2_valor.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Agregar etiquetas para mostrar los datos adicionales
        self.lbl_motivotexto = customtkinter.CTkLabel(self.firstInterFrame, text="")
        self.lbl_motivotexto.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.lbl_motivotexto_valor = customtkinter.CTkEntry(self.firstInterFrame)
        self.lbl_motivotexto_valor.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        
        self.lbl_empresa = customtkinter.CTkLabel(self.thirdInterFrame, text="")
        self.lbl_empresa.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.lbl_empresa_valor = customtkinter.CTkEntry(self.thirdInterFrame)
        self.lbl_empresa_valor.grid(row=4, column=1, padx=5, pady=5, sticky="w")


        #self.separator = tk.Frame(self.home_frame, width=2, height=300, background="black")
        #self.separator.grid(row=4, column=2, padx=5, pady=5, rowspan=10)

        #self.lineadivisora = customtkinter.CTkCanvas(self.home_frame)
        #self.lineadivisora.create_line(300, 35, 300, 200)
        #self.lineadivisora.grid(row=4, column=2)
        #canvas.create_line(300, 35, 300, 200, dash=(4, 2))

        #row 3 y 4
        
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
        self.lbl_prepa_valor = customtkinter.CTkEntry(self.secondInterFrame)
        self.lbl_prepa_valor.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.lbl_materia3 = customtkinter.CTkLabel(self.secondInterFrame, text="")
        self.lbl_materia3.grid(row=2, column=0, padx=5, pady=5, sticky="e")    
        self.lbl_materia3_valor = customtkinter.CTkEntry(self.secondInterFrame)
        self.lbl_materia3_valor.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.lbl_formatexto = customtkinter.CTkLabel(self.secondInterFrame, text="")
        self.lbl_formatexto.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.lbl_formatexto_valor = customtkinter.CTkEntry(self.secondInterFrame)
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
        
        self.lbl_materia = customtkinter.CTkLabel(self.thirdInterFrame, text="")
        self.lbl_materia.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.lbl_materia_valor = customtkinter.CTkEntry(self.thirdInterFrame)
        self.lbl_materia_valor.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.lbl_tipoB = customtkinter.CTkLabel(self.thirdInterFrame, text="")
        self.lbl_tipoB.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.lbl_tipoB_valor = customtkinter.CTkEntry(self.thirdInterFrame)
        self.lbl_tipoB_valor.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.lbl_fechaTtexto = customtkinter.CTkLabel(self.secondInterFrame, text="")
        self.lbl_fechaTtexto.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.lbl_fechaTtexto_valor = customtkinter.CTkEntry(self.secondInterFrame)
        self.lbl_fechaTtexto_valor.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        
        
        ##########################################################################################################
        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)
        self.second_frame.grid_columnconfigure(1, weight=1)
        self.second_frame.grid_columnconfigure(2, weight=1)
        self.second_frame.grid_columnconfigure(3, weight=1)
        self.second_frame.grid_columnconfigure(4, weight=1)
        self.second_frame.grid_columnconfigure(5, weight=1)

        # Consulta a realizar
        conexion = ConexionBD(user='root',password='root',host='localhost',database='datosalumnosbajas')
        conexion.conectar()
        consulta = f"SELECT * FROM usuarios"
        resultado = conexion.ejecutar_consulta(consulta)
        #print(resultado)
       

        #label formulario
        
        self.home_frame_titleUsuario = customtkinter.CTkLabel(self.second_frame, text="Usuarios", fg_color="white", font=customtkinter.CTkFont(size=20, weight="bold"), padx=5, pady=5, corner_radius=15)
        self.home_frame_titleUsuario.grid(row=0, column=0, padx=20, pady=10, columnspan=3)

        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 13)) # Modify the font of the body
        self.style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        self.style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        # Crear un Treeview con 5 columnas
        self.treeview = ttk.Treeview(self.second_frame, columns=('Nom Usuario', 'Email', 'Nombre', 'Ap Paterno', 'Tipo', 'Activo'), show='headings', style="mystyle.Treeview")
        self.treeview.grid(row= 1, column=0, pady=10, padx=20, sticky="nsew", rowspan=2, columnspan=6)

        self.treeview.bind("<Double-1>", lambda event: self.open_usuarios(event))
        
        # Configurar encabezados de columna
        self.treeview.heading('Nom Usuario', text='Nom Usuario')
        self.treeview.heading('Email', text='Email')
        self.treeview.heading('Nombre', text='Nombre')
        self.treeview.heading('Ap Paterno', text='Ap Paterno')
        self.treeview.heading('Tipo', text='Tipo')
        self.treeview.heading('Activo', text='Activo')
        

         # Agregar datos
        for res in resultado:
            if resultado[0][6] :
                if res[7] != 1:
                    activo = "Si (0)"
                else:
                    activo = "No (1)"
                if res[6] == 0:
                    tipo = "Admin (0)"
                else:
                    tipo = "Recepcion (1)"
                self.treeview.insert('', tk.END , text=res[0], values=(res[0], res[5], res[2], res[3], tipo, activo))

                



                
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

        self.btn_limpiarINFO = customtkinter.CTkButton(self.second_frame, text="Limpiar info", command=lambda: self.edita_usuario())
        self.btn_limpiarINFO.grid(row= 3, column=1, padx=5, pady=5)

        self.btn_formularioUser = customtkinter.CTkButton(self.second_frame, text="Editar Información", command=lambda: self.edita_usuario())
        self.btn_formularioUser.grid(row= 6, column=5, padx=5, pady=5)
        self.btn_formularioUser.grid_remove()

        self.lbl_Nom_usuario = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_Nom_usuario.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.lbl_Nom_usuario.grid_remove()
        self.lbl_Nom_usuario_valor = customtkinter.CTkEntry(self.second_frame)
        self.lbl_Nom_usuario_valor.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.lbl_Nom_usuario_valor.grid_remove()


        self.lbl_clave2 = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_clave2.grid(row=4, column=2, padx=5, pady=5, sticky="e")
        self.lbl_clave2.grid_remove()
        self.lbl_clave_valor2 = customtkinter.CTkEntry(self.second_frame)
        self.lbl_clave_valor2.grid(row=4, column=3, padx=5, pady=5, sticky="w")
        self.lbl_clave_valor2.grid_remove()

        self.lbl_nombre2 = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_nombre2.grid(row=4, column=4, padx=5, pady=5, sticky="e")
        self.lbl_nombre2.grid_remove()
        self.lbl_nombre_valor2 = customtkinter.CTkEntry(self.second_frame)
        self.lbl_nombre_valor2.grid(row=4, column=5, padx=5, pady=5, sticky="w")
        self.lbl_nombre_valor2.grid_remove() 
        
        self.lbl_Ap_paterno = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_Ap_paterno.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.lbl_Ap_paterno.grid_remove()
        self.lbl_Ap_paterno_valor = customtkinter.CTkEntry(self.second_frame)
        self.lbl_Ap_paterno_valor.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        self.lbl_Ap_paterno_valor.grid_remove()
        
        self.lbl_Ap_materno = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_Ap_materno.grid(row=5, column=2, padx=5, pady=5, sticky="e")
        self.lbl_Ap_materno.grid_remove()
        self.lbl_Ap_materno_valor = customtkinter.CTkEntry(self.second_frame)
        self.lbl_Ap_materno_valor.grid(row=5, column=3, padx=5, pady=5, sticky="w")
        self.lbl_Ap_materno_valor.grid_remove()

        self.lbl_Email = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_Email.grid(row=5, column=4, padx=5, pady=5, sticky="e")
        self.lbl_Email.grid_remove()
        self.lbl_Email_valor = customtkinter.CTkEntry(self.second_frame)
        self.lbl_Email_valor.grid(row=5, column=5, padx=5, pady=5, sticky="w")
        self.lbl_Email_valor.grid_remove()
        
        #tipo de usuario
        self.lbl_tipoUs = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_tipoUs.grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.lbl_tipoUs.grid_remove()
        self.lbl_tipoUs_valor = customtkinter.CTkEntry(self.second_frame)
        self.lbl_tipoUs_valor.grid(row=6, column=1, padx=5, pady=5, sticky="w")
        self.lbl_tipoUs_valor.grid_remove()

        #activo
        self.lbl_activo = customtkinter.CTkLabel(self.second_frame, text="")
        self.lbl_activo.grid(row=6, column=2, padx=5, pady=5, sticky="e")
        self.lbl_activo.grid_remove()
        self.lbl_activo_valor = customtkinter.CTkEntry(self.second_frame)
        self.lbl_activo_valor.grid(row=6, column=3, padx=5, pady=5, sticky="w")
        self.lbl_activo_valor.grid_remove()
        
        
        # create third frame
        ############################################################################
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        self.third_frame.grid_columnconfigure(0, weight=1)
        self.third_frame.grid_columnconfigure(1, weight=1)

        #cambiando fuentes
        self.third_frame_Titulo = customtkinter.CTkLabel(self.third_frame, text="Registrar nuevo usuario", fg_color="white", font=customtkinter.CTkFont(size=20, weight="bold"), padx=5, pady=5, corner_radius=15)
        self.third_frame_Titulo.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
        
        self.third_frame_Clave = customtkinter.CTkLabel(self.third_frame, text="Nombre: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.third_frame_Clave.grid(row=1, column=0,padx=10, pady=10, sticky = "e")
        
        self.third_frame_Clave = customtkinter.CTkLabel(self.third_frame, text="Primer apellido: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.third_frame_Clave.grid(row=2, column=0,padx=10, pady=10, sticky = "e")
        
        self.third_frame_Clave = customtkinter.CTkLabel(self.third_frame, text="Segundo apellido: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.third_frame_Clave.grid(row=3, column=0,padx=10, pady=10, sticky = "e")

        self.third_frame_Clave = customtkinter.CTkLabel(self.third_frame, text="Email: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.third_frame_Clave.grid(row=4, column=0,padx=10, pady=10, sticky = "e")

        self.third_frame_Clave = customtkinter.CTkLabel(self.third_frame, text="Nuevo nombre de usuario: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.third_frame_Clave.grid(row=5, column=0,padx=10, pady=10, sticky = "e")

        self.third_frame_Clave = customtkinter.CTkLabel(self.third_frame, text="Nueva contraseña: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.third_frame_Clave.grid(row=6, column=0,padx=10, pady=10, sticky = "e")

        
        self.clave1 = tk.StringVar()
        self.clave2 = tk.StringVar()
        self.clave3 = tk.StringVar()
        self.clave4 = tk.StringVar()
        self.clave5 = tk.StringVar()
        self.clave6 = tk.StringVar()

        self.third_frame_Clave_Entry1 = customtkinter.CTkEntry(self.third_frame, textvariable=self.clave1)
        self.third_frame_Clave_Entry1.grid(row=1, column=1,padx=10, pady=10, sticky = "w")

        self.third_frame_Clave_Entry2 = customtkinter.CTkEntry(self.third_frame, textvariable=self.clave2)
        self.third_frame_Clave_Entry2.grid(row=2, column=1,padx=10, pady=10, sticky = "w")

        self.third_frame_Clave_Entry3 = customtkinter.CTkEntry(self.third_frame, textvariable=self.clave3)
        self.third_frame_Clave_Entry3.grid(row=3, column=1,padx=10, pady=10, sticky = "w")

        self.third_frame_Clave_Entry4 = customtkinter.CTkEntry(self.third_frame, textvariable=self.clave4)
        self.third_frame_Clave_Entry4.grid(row=4, column=1,padx=10, pady=10, sticky = "w")

        self.third_frame_Clave_Entry5 = customtkinter.CTkEntry(self.third_frame, textvariable=self.clave5)
        self.third_frame_Clave_Entry5.grid(row=5, column=1,padx=10, pady=10, sticky = "w")

        self.third_frame_Clave_Entry6 = customtkinter.CTkEntry(self.third_frame, textvariable=self.clave6, show='*')
        self.third_frame_Clave_Entry6.grid(row=6, column=1,padx=10, pady=10, sticky = "w")

        self.third_frame_button_Registrar = customtkinter.CTkButton(self.third_frame, text="Registrar")
        
        self.third_frame_button_Buscar = customtkinter.CTkButton(self.third_frame, text="Registrar", command=lambda:self.registro())
        self.third_frame_button_Buscar.grid(row=7, column=1, pady=10)


        ##########################################################################################
        # select default frame
        self.select_frame_by_name("Formularios")

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
    
    def registro(self):
        #claveAlumno = self.claveA.get()
        #Consultar los datos necesarios
        bd_nombre = self.clave1.get()
        bd_ap_paterno = self.clave2.get()
        bd_ap_materno = self.clave3.get()
        bd_email = self.clave4.get()
        bd_nom_usuario = self.clave5.get()
        bd_password = self.clave6.get()

        #Consulta necesaria para el registro del usuario
        conexion = ConexionBD(user='root',password='root',host='localhost',database='datosalumnosbajas')
        conexion.conectar()
        insertar = f"INSERT INTO usuarios (nom_usuario, password, nombre, ap_paterno, ap_materno, email, tipo_usuario, activo) VALUES ('{bd_nom_usuario}','{bd_password}','{bd_nombre}','{bd_ap_paterno}','{bd_ap_materno}','{bd_email}','1', '0')"
        resultado = conexion.ejecutar_consulta(insertar)

        validacion = f"SELECT * FROM usuarios WHERE nom_usuario = '{bd_nom_usuario}'"
        resVal = conexion.ejecutar_consulta(validacion)

        conexion.desconectar()

        #Validar
        if(resVal is not NONE):
            messagebox.showinfo(message="Usuario registrado con éxito", title="Éxito")
        else:
            messagebox.showerror(message="Error en el registro", title="Error")

        self.third_frame_Clave_Entry1.delete(0, "end")
        self.third_frame_Clave_Entry2.delete(0, "end")
        self.third_frame_Clave_Entry3.delete(0, "end")
        self.third_frame_Clave_Entry4.delete(0, "end")
        self.third_frame_Clave_Entry5.delete(0, "end")
        self.third_frame_Clave_Entry6.delete(0, "end")

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

        self.lbl_correo.configure(text="Correo electronico:")
        self.lbl_correo_valor.delete(0, tk.END)
        self.lbl_correo_valor.insert(0,resultado[0][5])
        #self.lbl_correo_valor.configure(text=resultado[0][5])

        self.lbl_carrera.configure(text="Carrera:")
        self.lbl_carrera_valor.delete(0, tk.END)
        self.lbl_carrera_valor.insert(0,resultado[0][7])
        #self.lbl_carrera_valor.configure(text=resultado[0][7])

        self.lbl_generacion.configure(text="Generacion:")
        self.lbl_generacion_valor.delete(0, tk.END)
        self.lbl_generacion_valor.insert(0,resultado[0][8])
        #self.lbl_generacion_valor.configure( text=resultado[0][8])

        self.lbl_motivo.configure(text="Motivo de baja:")
        self.lbl_motivo_valor.delete(0, tk.END)
        self.lbl_motivo_valor.insert(0,resultado[0][10])
        #self.lbl_motivo_valor.configure(text=resultado[0][10])
        
        self.lbl_prpa.configure(text="Preparatoria de procedencia:")
        self.lbl_prepa_valor.delete(0, tk.END)
        self.lbl_prepa_valor.insert(0,resultado[0][11])
        #self.lbl_prepa_valor.configure(text=resultado[0][11])

        self.lbl_materia.configure(text="Materia más dificil:")
        self.lbl_materia_valor.delete(0, tk.END)
        self.lbl_materia_valor.insert(0,resultado[0][12])
        #self.lbl_materia_valor.configure(text=resultado[0][12])
        self.lbl_materia2.configure(text="Materia más dificil II:")
        self.lbl_materia2_valor.delete(0, tk.END)
        self.lbl_materia2_valor.insert(0,resultado[0][13])
        #self.lbl_materia2_valor.configure(text=resultado[0][13])
        self.lbl_materia3.configure(text="Materia más dificil III:")
        self.lbl_materia3_valor.delete(0, tk.END)
        self.lbl_materia3_valor.insert(0,resultado[0][14])
        #self.lbl_materia3_valor.configure(text=resultado[0][14])

        self.lbl_tipoB.configure(text="Tipo de baja:")
        self.lbl_tipoB_valor.delete(0, tk.END)
        self.lbl_tipoB_valor.insert(0,resultado[0][9])
        #self.lbl_tipoB_valor.configure(text=resultado[0][9])

        self.lbl_motivotexto.configure(text="Porqué se da de baja:")
        self.lbl_motivotexto_valor.delete(0, tk.END)
        self.lbl_motivotexto_valor.insert(0,resultado[0][17])

        self.lbl_formatexto.configure(text="Forma Titulacion:")
        if resultado[0][15]:
            self.lbl_formatexto_valor.delete(0, tk.END)
            self.lbl_formatexto_valor.insert(0, resultado[0][15])
            #self.lbl_formatexto_valor.configure(text=resultado[0][15])
            #self.lbl_formatexto_valor['text']= resultado[0][15]
        else:
            self.lbl_formatexto_valor.delete(0, tk.END)
            self.lbl_formatexto_valor.insert(0, "No aplica")
            #self.lbl_formatexto_valor.configure(text="No aplica")
        
        

        self.lbl_fechaTtexto.configure(text="Fecha EGEL:")
        if resultado[0][16]:
            self.lbl_fechaTtexto_valor.delete(0, tk.END)
            self.lbl_fechaTtexto_valor.insert(0, resultado[0][16])
           # self.lbl_fechaTtexto_valor.configure(text=resultado[0][16])
        else:
            self.lbl_fechaTtexto_valor.delete(0, tk.END)
            self.lbl_fechaTtexto_valor.insert(0, "No aplica")
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

        # Crear etiquetas para los campos fecha, clave y nombre
        #print(resultado[0][6])
        self.btn_formularioUser.grid()
        self.lbl_Nom_usuario_valor.delete(0, tk.END)
        self.lbl_Nom_usuario.grid()
        self.lbl_Nom_usuario.configure(text="Nom_usuario:")
        self.lbl_Nom_usuario_valor.grid()
        self.lbl_Nom_usuario_valor.insert(0, resultado[0][0])
        #self.lbl_Nom_usuario_valor.configure(value=resultado[0][0])

        self.lbl_clave_valor2.delete(0, tk.END)
        self.lbl_clave2.grid()
        self.lbl_clave2.configure(text="Password:")
        self.lbl_clave_valor2.grid()
        self.lbl_clave_valor2.insert(0, resultado[0][1])

        self.lbl_nombre_valor2.delete(0, tk.END)
        self.lbl_nombre2.grid()
        self.lbl_nombre2.configure(text="Nombre:")
        self.lbl_nombre_valor2.grid()
        self.lbl_nombre_valor2.insert(0, resultado[0][2])

        self.lbl_Ap_paterno_valor.delete(0, tk.END)
        self.lbl_Ap_paterno.grid()
        self.lbl_Ap_paterno.configure(text="Ap paterno:")
        self.lbl_Ap_paterno_valor.grid()
        self.lbl_Ap_paterno_valor.insert(0, resultado[0][3])

        self.lbl_Ap_materno_valor.delete(0, tk.END)
        self.lbl_Ap_materno.grid()
        self.lbl_Ap_materno.configure(text="Ap materno:")
        self.lbl_Ap_materno_valor.grid()
        self.lbl_Ap_materno_valor.insert(0, resultado[0][4])

        self.lbl_Email_valor.delete(0, tk.END)
        self.lbl_Email.grid()
        self.lbl_Email.configure(text="Email:")
        self.lbl_Email_valor.grid()
        self.lbl_Email_valor.insert(0, resultado[0][5])

        self.lbl_tipoUs_valor.delete(0, tk.END)
        self.lbl_tipoUs.grid()
        self.lbl_tipoUs.configure(text="Tipo de usuario:")
        self.lbl_tipoUs_valor.grid()
        self.lbl_tipoUs_valor.insert(0, resultado[0][6])

        self.lbl_activo_valor.delete(0, tk.END)
        self.lbl_activo.grid()
        self.lbl_activo.configure(text="Activo: ")
        self.lbl_activo_valor.grid()
        self.lbl_activo_valor.insert(0, resultado[0][7])
        
        
    # Función para seleccionar un formulario y mostrar la ventana de formulario
    def seleccionar_formulario(self, treeview2):
        # Obtener la fila seleccionada
        seleccion = treeview2.selection()
        if seleccion:
            fila_seleccionada = treeview2.item(seleccion)['values']
            # Mostrar la ventana del formulario con la fila seleccionada
            ventana_Formulario(fila_seleccionada[1])
            #print(fila_seleccionada[1])
        else:
            #messagebox.showinfo("Error", "Por favor, selecciona un formulario primero.")
            CTkMessagebox(title="Error", message="Por favor, selecciona un formulario primero.", icon="cancel")

    # Función para seleccionar un usuario y mostrar la ventana de usuario
    def seleccionar_usuario(self, treeview):
        # Obtener la fila seleccionada
        seleccion = treeview.selection()
        if seleccion:
            fila_seleccionada = treeview.item(seleccion)['values']
            # Mostrar la ventana del formulario con la fila seleccionada
            ventana_Usuario(fila_seleccionada[0])
            #print(fila_seleccionada[0])
        else:
            #messagebox.showinfo("Error", "Por favor, selecciona un formulario primero.")
            CTkMessagebox(title="Error", message="Por favor, selecciona un formulario primero.", icon="cancel")


    def edita_usuario(self):
        suma = 1+1
        print (suma)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
    