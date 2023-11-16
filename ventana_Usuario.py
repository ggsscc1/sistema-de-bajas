import tkinter as tk
from tkinter import *
from tkinter import ttk
from DBconection import *
from datetime import date
from tkinter import messagebox
import customtkinter
from CTkMessagebox import CTkMessagebox
from tkcalendar import DateEntry


# Función principal para mostrar los usuarios
def ventana_Usuario(fila_seleccionada):
    print(fila_seleccionada)
    
    customtkinter.deactivate_automatic_dpi_awareness()
    customtkinter.set_appearance_mode("light")
    ventana_usuario = customtkinter.CTk()
    
    # Configurar el tamaño y el título de la ventana
    screen_width = ventana_usuario.winfo_screenwidth()
    screen_height = ventana_usuario.winfo_screenheight()
    screen_resolution = str(screen_width) + 'x' + str(screen_height)
    ventana_usuario.geometry(screen_resolution)
    ventana_usuario.title(f"Usuario: {fila_seleccionada}")
    
    #Inicialización de variables 
    global nomUsuarioU
    global passwordU
    global nombreU
    global ap_patU
    global ap_matU
    global emailU
    global tipoUsuarioU
    global activoU
   
    nomUsuarioU = StringVar() 
    passwordU = StringVar()
    nombreU = StringVar()
    ap_patU = StringVar()
    ap_matU = StringVar()
    emailU = StringVar()
    tipoUsuarioU = StringVar()
    activoU = StringVar()

    #Conexion a la base de datos
    conexionUsuario = ConexionBD(user='root',password='root',host='localhost',database='datosalumnosbajas')
    conexionUsuario.conectar()

    consulta = f"SELECT * FROM usuarios WHERE nom_usuario = '{fila_seleccionada}'"
    res = conexionUsuario.ejecutar_consulta(consulta)
    print(res)

    #Si es 0 esta activo si es 1 esta inactivo
    if res[0][7] != 1:
        activo = "Si"
    else:
        activo = "No"

    # Crea un frame con fondo blanco en el centro de la ventana de usuario
    frame_central = tk.Frame(ventana_usuario, bg="white")
    frame_central.pack( padx=30, pady=30)

    #crear etiqueta para la fecha
    #fecha_actual = date.today().strftime("%Y-%m-%d")
    fecha_actual = date.today().strftime("%d-%m-%Y")
    etiqueta_fecha = customtkinter.CTkLabel(frame_central, text="Fecha:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_fecha.grid(row=0, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_fecha = customtkinter.CTkLabel(frame_central, text=fecha_actual, fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_fecha.grid(row=0, column=1, sticky="w", padx=20, pady=10)

    # Crear etiquetas con información del usuario dentro del frame central
    etiqueta_nomUsuario = customtkinter.CTkLabel(frame_central, text="Nombre Usuario:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_nomUsuario.grid(row=1, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_nomUsuario = customtkinter.CTkLabel(frame_central, text=res[0][0], fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_nomUsuario.grid(row=1, column=1, sticky="w", padx=20, pady=10)

    etiqueta_password = customtkinter.CTkLabel(frame_central, text="Password:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_password.grid(row=2, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_password = customtkinter.CTkLabel(frame_central, text=res[0][1], fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_password.grid(row=2, column=1, sticky="w", padx=20, pady=10)

    etiqueta_nombre = customtkinter.CTkLabel(frame_central, text="Nombre(s):", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_nombre.grid(row=3, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_nombre = customtkinter.CTkLabel(frame_central, text=res[0][2], fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_nombre.grid(row=3, column=1, sticky="w", padx=20, pady=10)

    etiqueta_ap_pat = customtkinter.CTkLabel(frame_central, text="Apellido Paterno:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_ap_pat.grid(row=4, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_ap_pat = customtkinter.CTkLabel(frame_central, text=res[0][3], fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_ap_pat.grid(row=4, column=1, sticky="w", padx=20, pady=10)

    etiqueta_ap_mat = customtkinter.CTkLabel(frame_central, text="Apellido Materno:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_ap_mat.grid(row=5, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_ap_mat = customtkinter.CTkLabel(frame_central, text=res[0][4], fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_ap_mat.grid(row=5, column=1, sticky="w", padx=20, pady=10)

    etiqueta_correo = customtkinter.CTkLabel(frame_central, text="Correo electronico:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_correo.grid(row=6, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_correo = customtkinter.CTkLabel(frame_central, text=res[0][5], fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_correo.grid(row=6, column=1, padx=20, pady=10) 

    etiqueta_tipoUsuario = customtkinter.CTkLabel(frame_central, text="Tipo usuario:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_tipoUsuario.grid(row=7, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_tipoUsuario = customtkinter.CTkLabel(frame_central, text=res[0][6], fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_tipoUsuario.grid(row=7, column=1, padx=20, pady=10)  

    etiqueta_activo = customtkinter.CTkLabel(frame_central, text="Activo:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_activo.grid(row=8, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_activo = customtkinter.CTkLabel(frame_central, text=activo, fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_activo.grid(row=8, column=1, padx=20, pady=10)  

    nomUsuarioU = res[0][0]
    passwordU = res[0][1]
    nombreU = res[0][2]
    ap_patU = res[0][3]
    ap_matU = res[0][4]
    emailU = res[0][5]
    tipoUsuarioU = res[0][6]

    def elimina_usuario():
        #updateElimina = f"SELECT * FROM usuarios WHERE nom_usuario = '{fila_seleccionada}'"
        updateElimina = f"update usuarios set activo = 1 where nom_usuario = '{nomUsuarioU}'"
        
        res = conexionUsuario.ejecutar_consulta(updateElimina)

    print(res)
    #boton_cerrar = customtkinter.CTkButton(ventana_usuario, text="Enviar", width=250, height=50, corner_radius=20, command=lambda: [actualizar_informacion(), ventana_formulario.destroy()])
    boton_cerrar = customtkinter.CTkButton(ventana_usuario, text="Enviar", width=250, height=50, corner_radius=20, command = ventana_usuario.destroy)
    boton_cerrar.pack(pady=20)

    #boton eliminar usuario
    boton_eliminar = customtkinter.CTkButton(ventana_usuario, text="Eliminar usuario", width=250, height=50, corner_radius=20, command = elimina_usuario())
    boton_eliminar.pack(pady=30)

    ventana_usuario.mainloop()

