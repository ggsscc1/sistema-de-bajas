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

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de bajas - Recepción")
        #self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


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

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["System", "Light", "Dark"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        #cambiando fuentes
        self.home_frame_Titulo = customtkinter.CTkLabel(self.home_frame, text="Sistema de bajas", fg_color="darkblue", font=customtkinter.CTkFont(size=20, weight="bold"), padx=5, pady=5, corner_radius=15)
        self.home_frame_Titulo.grid(row=0, column=0, padx=20, pady=10, columnspan=3)
        
        self.home_frame_Clave = customtkinter.CTkLabel(self.home_frame, text="Clave única\ndel alumno: ", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.home_frame_Clave.grid(row=1, column=0, padx=20, pady=10)
        
        global claveA
        claveA = tk.StringVar()
        self.home_frame_Clave_Entry = customtkinter.CTkEntry(self.home_frame, textvariable=claveA)
        self.home_frame_Clave_Entry.grid(row=1, column=1, padx=20, pady=10)

        

    # Crear etiquetas para mostrar la información del alumno
        self.home_frame_claveR = tk.StringVar()
        self.home_frame_nombreR = tk.StringVar()
        self.home_frame_carreraR = tk.StringVar()
        self.home_frame_generacionR = tk.StringVar()

        self.home_frame_clave_alumno_label = customtkinter.CTkLabel(self.home_frame, text="",font=customtkinter.CTkFont(size=15, weight="normal"))
        self.home_frame_nombre_alumno_label = customtkinter.CTkLabel(self.home_frame, text="", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.home_frame_carrera_alumno_label = customtkinter.CTkLabel(self.home_frame, text="", font=customtkinter.CTkFont(size=15, weight="normal"))
        self.home_frame_generacion_alumno_label = customtkinter.CTkLabel(self.home_frame, text="", font=customtkinter.CTkFont(size=15, weight="normal"))

        self.home_frame_button_Buscar = customtkinter.CTkButton(self.home_frame, text="Buscar", command=lambda:self.buscaAlumno())
        self.home_frame_button_Buscar.grid(row=1, column=2, padx=20, pady=10)

        
        self.home_frame_clave_alumno_label.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_nombre_alumno_label.grid(row=2, column=1, padx=20, pady=10)
        self.home_frame_carrera_alumno_label.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_generacion_alumno_label.grid(row=3, column=1, padx=20, pady=10)

        self.home_frame_button_Registrar = customtkinter.CTkButton(self.home_frame, text="Registrar")
        #""", command=lambda:insertaEnLista(claveAlumno)"""
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
        
        

    def mostrar_informacion_alumno(self):
        self.home_frame_clave_alumno_label.grid()
        self.home_frame_nombre_alumno_label.grid()
        self.home_frame_carrera_alumno_label.grid()
        self.home_frame_generacion_alumno_label.grid()
        self.home_frame_button_Registrar.grid()
        self.home_frame_button_Limpiar.grid()
        claveAlumno = self.home_frame_claveR.get() 
        self.home_frame_clave_alumno_label.configure(text="Clave única del alumno: " + self.home_frame_claveR.get())
        self.home_frame_nombre_alumno_label.configure(text="Nombre del Alumno: " + self.home_frame_nombreR.get())
        self.home_frame_carrera_alumno_label.configure(text="Carrera del Alumno: " + self.home_frame_carreraR.get())
        self.home_frame_generacion_alumno_label.configure(text="Generación del Alumno: " + self.home_frame_generacionR.get())

    def buscaAlumno(self):
        claveAlumno = claveA.get()
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



if __name__ == "__main__":
    app = App()
    app.mainloop()

