from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter
import inicio_recepcion
import Inicio_Admin
from interRecepcion import crear_y_ejecutar
from ventana_Admin import crea_y_ejecuta
from DBconection import *
import os

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()
root.geometry("600x400")
root.title("Sistema de bajas")
root.attributes('-fullscreen', False)  # Establece la ventana en modo de pantalla completa

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=30, padx=30, fill="both", expand=True, anchor="center")

label = customtkinter.CTkLabel(master=frame, text="Inicio de sesión", font=("Arial", 20))  # Aumenta el tamaño de la fuente del label
label.pack(pady=12, padx=10)

global entry1
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Usuario", font=("Arial", 14))  # Aumenta el tamaño de la fuente del entry
entry1.pack(pady=12, padx=10)

global entry2
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Contraseña", font=("Arial", 14), show='*')  # Aumenta el tamaño de la fuente del entry
entry2.bind("<Return>",lambda event: realizar_busqueda(event))
entry2.pack(pady=12, padx=10)

def realizar_busqueda(event):
        # Coloca aquí el código para realizar la búsqueda
        # Por ejemplo, puedes obtener el texto del Entry con entry.get()
        
   verificaInicio()

# Función que detecta el tipo de usuario que se está loggeando
def verificaInicio():

    # Se toman las variables nombre de usuario y clave del usuario que se loggea
    usuario = entry1.get()
    clave = entry2.get()

    # Consulta para buscar al usuario en la base de datos
    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT tipo_usuario FROM usuarios WHERE nom_usuario = '{usuario}' AND password = '{clave}'"
    resultado = conexion.ejecutar_consulta(consulta)
    

    # Condicional para iniciar la pantalla de inicio del usuario correspondiente
    if resultado:
        conexion.desconectar()
        if resultado[0][0] == 1:  
            root.destroy()
            # mandar llamar interRecepcion.App
            app_instance = crear_y_ejecutar()

        elif resultado[0][0] == 0:        
            root.destroy()  
            app_instance = crea_y_ejecuta()

    # Si no se encuentra al usuario, notifica un error
    else:
        messagebox.showinfo("Error", "Usuario o contraseña incorrectos")
        conexion.desconectar()


btnlogin = customtkinter.CTkButton(master=frame, text="Login", command=verificaInicio)
btnlogin.pack(pady=12, padx=10)



def run():
    root.mainloop()