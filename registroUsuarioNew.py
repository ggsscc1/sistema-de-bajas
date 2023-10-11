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
        
        

    
       
        #register_button =Button(text="Registrar", borderwidth=5, command=registro)

        self.home_frame_button_Registrar = customtkinter.CTkButton(self.home_frame, text="Registrar")
        #""", command=lambda:insertaEnLista(claveAlumno)"""
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
            
if __name__ == "__main__":
    app = App()
    app.mainloop()
    