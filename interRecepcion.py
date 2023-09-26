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
        iniform = Label(self.second_frame, text="Selecciona tu formulario")
        iniform.grid(row=0, column=0, padx=10, pady=10, sticky="w", columnspan=3)

        # Crear un Treeview con 3 columnas
        valores=[[0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0]
                 ]
        treeview = CTkTable(self.second_frame,column=10, values=valores)# values=resultado)
        treeview.grid(row= 1, column=0, pady=10)

        # Configurar encabezados de columna
        """treeview.heading('fecha', text='Fecha')
        treeview.heading('clave', text='Clave')
        treeview.heading('nombre', text='Nombre')
        treeview.heading('completado', text='Completado?')
        completado = "NO"
        
        if resultado[0][10] :
            completado = "SI"

        # Agregar datos
        for result in resultado:
            treeview.insert('', tk.END , text=result[0], values=(result[6], result[1], result[2], completado))
        
        # Establecer ancho de columna
        treeview.column('fecha', width=100)
        treeview.column('clave', width=100)
        treeview.column('nombre', width=100)
        treeview.column('completado', width=90)
"""
        # Mostrar Treeview
        #treeview.pack(side=LEFT, padx=10, pady=10)

        # Crear un botón "Generar Formulario" que muestra la ventana con los datos correspondientes
        btn_formulario = Button(self.second_frame, text="Abrir Formulario")
        #, command=lambda:formularios(treeview.item(treeview.focus(), "values"))
        btn_formulario.grid(row= 4, column=0, padx=10, pady=10, sticky="w")

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


if __name__ == "__main__":
    app = App()
    app.mainloop()

