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




    

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de bajas - Registrar nuevo usuario")
        #self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Ver información",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Agregar información",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Agregar usuario",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")


        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        #cambiando fuentes
        self.home_frame_Titulo = customtkinter.CTkLabel(self.home_frame, text="Registrar nuevo usuario", fg_color="darkblue", font=customtkinter.CTkFont(size=20, weight="bold"), padx=5, pady=5, corner_radius=15)
        self.home_frame_Titulo.grid(row=0, column=0, padx=20, pady=10, columnspan=3)
        
        self.home_frame_Clave = customtkinter.CTkLabel(self.home_frame, text="Nombre: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.home_frame_Clave.grid(row=1, column=0, padx=20, pady=10, sticky = "w")
        
        self.home_frame_Clave = customtkinter.CTkLabel(self.home_frame, text="Primer apellido: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.home_frame_Clave.grid(row=2, column=0, padx=20, pady=10, sticky = "w")
        
        self.home_frame_Clave = customtkinter.CTkLabel(self.home_frame, text="Segundo apellido: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.home_frame_Clave.grid(row=3, column=0, padx=20, pady=10, sticky = "w")

        self.home_frame_Clave = customtkinter.CTkLabel(self.home_frame, text="Email: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.home_frame_Clave.grid(row=4, column=0, padx=20, pady=10, sticky = "w")

        self.home_frame_Clave = customtkinter.CTkLabel(self.home_frame, text="Nuevo nombre de usuario: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.home_frame_Clave.grid(row=5, column=0, padx=20, pady=10, sticky = "w")

        self.home_frame_Clave = customtkinter.CTkLabel(self.home_frame, text="Nueva contraseña: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.home_frame_Clave.grid(row=6, column=0, padx=20, pady=10, sticky = "w")

        
        self.clave1 = tk.StringVar()
        self.clave2 = tk.StringVar()
        self.clave3 = tk.StringVar()
        self.clave4 = tk.StringVar()
        self.clave5 = tk.StringVar()
        self.clave6 = tk.StringVar()
        self.home_frame_Clave_Entry = customtkinter.CTkEntry(self.home_frame, textvariable=self.clave1)
        self.home_frame_Clave_Entry.grid(row=1, column=1, padx=20, pady=10)

        self.home_frame_Clave_Entry = customtkinter.CTkEntry(self.home_frame, textvariable=self.clave2)
        self.home_frame_Clave_Entry.grid(row=2, column=1, padx=20, pady=10)

        self.home_frame_Clave_Entry = customtkinter.CTkEntry(self.home_frame, textvariable=self.clave3)
        self.home_frame_Clave_Entry.grid(row=3, column=1, padx=20, pady=10)

        self.home_frame_Clave_Entry = customtkinter.CTkEntry(self.home_frame, textvariable=self.clave4)
        self.home_frame_Clave_Entry.grid(row=4, column=1, padx=20, pady=10)

        self.home_frame_Clave_Entry = customtkinter.CTkEntry(self.home_frame, textvariable=self.clave5)
        self.home_frame_Clave_Entry.grid(row=5, column=1, padx=20, pady=10)

        self.home_frame_Clave_Entry = customtkinter.CTkEntry(self.home_frame, textvariable=self.clave6)
        self.home_frame_Clave_Entry.grid(row=6, column=1, padx=20, pady=10)

        self.home_frame_button_Registrar = customtkinter.CTkButton(self.home_frame, text="Registrar")
        
        self.home_frame_button_Buscar = customtkinter.CTkButton(self.home_frame, text="Registrar", command=lambda:self.registro())
        self.home_frame_button_Buscar.grid(row=7, column=1, padx=20, pady=10)

        self.home_frame_button_Registrar.grid(row=4, column=1, padx=20, pady=10)
        self.home_frame_button_Registrar.grid_remove()
        
        self.home_frame_button_Limpiar = customtkinter.CTkButton(self.home_frame, text="Limpiar", command=lambda:self.limpiainfo())
        self.home_frame_button_Limpiar.grid(row=4, column=2, padx=20, pady=10)
        self.home_frame_button_Limpiar.grid_remove()

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")


        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        # Consulta a realizar
        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
        conexion.conectar()
        consulta = f"SELECT * FROM formulario"
        resultado = conexion.ejecutar_consulta(consulta)

        #label formulario
        iniform = customtkinter.CTkLabel(self.third_frame, text="Selecciona tu formulario")
        iniform.grid(row=0, column=0, padx=10, pady=10, sticky="w", columnspan=3)

        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 13)) # Modify the font of the body
        self.style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        self.style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

        # Crear un Treeview con 3 columnas
        treeview2 = ttk.Treeview(self.third_frame, columns=('fecha', 'clave', 'nombre', 'completado'), show='headings', style="mystyle.Treeview")
        treeview2.grid(row= 1, column=0, pady=10, padx=20, sticky="nsew", rowspan=2, columnspan=6)

        # Configurar encabezados de columna
        treeview2.heading('fecha', text='Fecha')
        treeview2.heading('clave', text='Clave')
        treeview2.heading('nombre', text='Nombre')
        treeview2.heading('completado', text='Completado?')
        completado = "NO"
        
        # Agregar datos
        for result in resultado:
            if resultado[0][10] :
                completado = "SI"
                treeview2.insert('', tk.END , text=result[0], values=(result[6], result[1], result[2], completado))
        
        # Establecer ancho de columna
        treeview2.column('fecha', width=100)
        treeview2.column('clave', width=100)
        treeview2.column('nombre', width=100)
        treeview2.column('completado', width=110)

        # Crear un botón "Generar Formulario" que muestra la ventana con los datos correspondientes
        
        btn_formulario2 = customtkinter.CTkButton(self.third_frame, text="Abrir Formulario", command=lambda: self.formularios(treeview2.item(treeview2.focus(), "values")))
        btn_formulario2.grid(row= 3, column=0, padx=10, pady=10, sticky="w")

        # Crear un botón para editar formulario
        btn_sell = customtkinter.CTkButton(self.third_frame, text="Editar formulario", command= lambda:GeneraCarta(resultado[0][1]))
        btn_sell.grid(row=3, column=1, padx=10, pady=10, sticky = "w")

        self.lbl_fecha = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_fecha.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.lbl_fecha_valor = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_fecha_valor.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        self.lbl_clave = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_clave.grid(row=4, column=2, padx=5, pady=5, sticky="e")
        self.lbl_clave_valor = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_clave_valor.grid(row=4, column=3, padx=5, pady=5, sticky="w")

        self.lbl_nombre = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_nombre.grid(row=4, column=4, padx=5, pady=5, sticky="e")
        self.lbl_nombre_valor = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_nombre_valor.grid(row=4, column=5, padx=5, pady=5, sticky="w") 
        
        self.lbl_correo = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_correo.grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.lbl_correo_valor = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_correo_valor.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        
        self.lbl_carrera = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_carrera.grid(row=5, column=2, padx=5, pady=5, sticky="e")
        self.lbl_carrera_valor = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_carrera_valor.grid(row=5, column=3, padx=5, pady=5, sticky="w")

        self.lbl_generacion = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_generacion.grid(row=5, column=4, padx=5, pady=5, sticky="e")
        self.lbl_generacion_valor = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_generacion_valor.grid(row=5, column=5, padx=5, pady=5, sticky="w")
        
        #"Motivo de Baja"
        self.lbl_motivo = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_motivo.grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.lbl_motivo_valor = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_motivo_valor.grid(row=6, column=1, padx=5, pady=5, sticky="w")

        #Escuela de procedencia
        self.lbl_prpa = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_prpa.grid(row=6, column=2, padx=5, pady=5, sticky="e")
        self.lbl_prepa_valor = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_prepa_valor.grid(row=6, column=3, padx=5, pady=5, sticky="w")

        #materias mas dificiles
        
        self.lbl_materia = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_materia.grid(row=6, column=4, padx=5, pady=5, sticky="e")
        self.lbl_materia_valor = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_materia_valor.grid(row=6, column=5, padx=5, pady=5, sticky="w")

        self.lbl_materia2 = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_materia2.grid(row=7, column=0, padx=5, pady=5, sticky="e")
        self.lbl_materia2_valor = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_materia2_valor.grid(row=7, column=1, padx=5, pady=5, sticky="w")

        self.lbl_materia3 = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_materia3.grid(row=7, column=2, padx=5, pady=5, sticky="e")    
        self.lbl_materia3_valor = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_materia3_valor.grid(row=7, column=3, padx=5, pady=5, sticky="w")
        
        self.lbl_tipoB = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_tipoB.grid(row=7, column=4, padx=5, pady=5, sticky="e")
        self.lbl_tipoB_valor = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_tipoB_valor.grid(row=7, column=5, padx=5, pady=5, sticky="w")

        # Agregar etiquetas para mostrar los datos adicionales
        self.lbl_motivotexto = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_motivotexto.grid(row=8, column=0, padx=5, pady=5, sticky="e")
        self.lbl_motivotexto_valor = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_motivotexto_valor.grid(row=8, column=1, padx=5, pady=5, sticky="w")

        self.lbl_formatexto = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_formatexto.grid(row=8, column=2, padx=5, pady=5, sticky="e")
        self.lbl_formatexto_valor = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_formatexto_valor.grid(row=8, column=3, padx=5, pady=5, sticky="w")

        self.lbl_fechaTtexto = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_fechaTtexto.grid(row=8, column=4, padx=5, pady=5, sticky="e")
        self.lbl_fechaTtexto_valor = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_fechaTtexto_valor.grid(row=8, column=5, padx=5, pady=5, sticky="w")

        self.lbl_empresa = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_empresa.grid(row=9, column=0, padx=5, pady=5, sticky="e")
        self.lbl_empresa_valor = customtkinter.CTkLabel(self.third_frame, text="")
        self.lbl_empresa_valor.grid(row=9, column=1, padx=5, pady=5, sticky="w")

        # select default frame
        self.select_frame_by_name("Ver información")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "Ver información" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "Agregar información" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "Agregar usuario" else "transparent")

        # show selected frame
        if name == "Ver información":
            self.third_frame.grid(row=0, column=1, sticky="nsew")

        else:
            self.third_frame.grid_forget()

        if name == "Agregar información":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "Agregar usuario":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()


    def home_button_event(self):
        self.select_frame_by_name("Ver información")

    def frame_2_button_event(self):
        self.select_frame_by_name("Agregar información")

    def frame_3_button_event(self):
        self.select_frame_by_name("Agregar usuario")
    
    def limpiainfo(self):
        self.home_frame_clave_alumno_label.grid_remove()
        self.home_frame_nombre_alumno_label.grid_remove()
        self.home_frame_carrera_alumno_label.grid_remove()
        self.home_frame_generacion_alumno_label.grid_remove()
        self.home_frame_button_Registrar.grid_remove()
        self.home_frame_button_Limpiar.grid_remove()
        
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
        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
        conexion.conectar()
        insertar = f"INSERT INTO usuarios (nom_usuario, password, nombre, ap_paterno, ap_materno, email, tipo_usuario) VALUES ('{bd_nom_usuario}','{bd_password}','{bd_nombre}','{bd_ap_paterno}','{bd_ap_materno}','{bd_email}','1')"
        resultado = conexion.ejecutar_consulta(insertar)

        validacion = f"SELECT * FROM usuarios WHERE nom_usuario = '{bd_nom_usuario}"
        resVal = conexion.ejecutar_consulta(validacion)

        conexion.desconectar()

        #Validar
        if(resVal is not NONE):
            messagebox.showinfo(message="Usuario registrado con éxito", title="Éxito")
        else:
            messagebox.showerror(message="Error en el registro", title="Error")
    

    #funcion para abrir los formularios
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

        
        

    
if __name__ == "__main__":
    app = App()
    app.mainloop()
    