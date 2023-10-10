from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import inicio_recepcion
import Inicio_Admin
from DBconection import *
import os
import customtkinter
from registroUsuarioNew import App

#Función que detecta el tipo de usuario que se esta loggeando
def verificaInicio():
    #Se toman las variables nombre de usuario y clave del usuario que se loggea
    usuario = verifica_usuario.get()
    clave = verifica_clave.get()

    #Consulta para buscar al usuario en la base de datos
    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()
    consulta = f"SELECT tipo_usuario FROM usuarios WHERE nom_usuario = '{usuario}' AND password = '{clave}'"
    resultado = conexion.ejecutar_consulta(consulta)

    #Condicional para iniciar la pantalla de inicio del usuario correspondiente
    if resultado:
        conexion.desconectar()
        if resultado[0][0] == 1:  
            ventana_principal.destroy()
            inicio_recepcion.ventana_InicioR()
        elif resultado[0][0] == 0:        
            ventana_principal.destroy()  
            Inicio_Admin.ventana_IniA()

    #Si no se encuentra al usuario, notifica un error
    else:
        messagebox.showinfo("Error","Checar credenciales")
        conexion.desconectar()

#Función para el cierre de sesión    
def cerrar_sesion():
    inicio_recepcion.ventana_InicioR.destroy()

#Función para colocar la ventana de Login
def ventana_inicio():
    #Variables para la colocación de la pantalla

    global ventana_principal
    ventana_principal=Tk()
    screen_width = ventana_principal.winfo_screenwidth()
    screen_height = ventana_principal.winfo_screenheight()
    screen_resolution = str(screen_width)+'x'+str(screen_height)
    ventana_principal.geometry(screen_resolution)
    ventana_principal.title("Sistema de bajas de INFOCOMP")
    
    # definir un nuevo estilo "My.TFrame"
    estilo = ttk.Style()
    estilo.configure("My.TFrame", background="gray")

    #Barra Superior "Sistema de bajas"
    lbl_SB = Label(text="Sistema de bajas", fg="white", bg="darkblue", width="300", height="2", font=("Calibri", 30))
    lbl_SB.pack(fill=X)
    
    separator = ttk.Separator(ventana_principal, orient='horizontal')
    separator.pack(fill=X, padx=20, pady=50)

    #Frame para formulario de login con estilo "My.TFrame"
    frame_login = ttk.Frame(ventana_principal, padding=(50, 20), style="My.TFrame")
    frame_login.pack(pady=50)

    #Entrys
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()

    #Nombre de usuario
    lblNombreUsuario = Label(frame_login, text="Nombre de usuario:", font=("Calibri", 14))
    lblNombreUsuario.grid(row=0, column=0, sticky="w")
    
    entrada_login_usuario = ttk.Entry(frame_login, width=30, textvariable=verifica_usuario, font=("Calibri", 14))
    entrada_login_usuario.grid(row=0, column=1, padx=10, pady=10)

    #Contraseña
    lblContraseña = Label(frame_login, text="Contraseña:", font=("Calibri", 14))
    lblContraseña.grid(row=1, column=0, sticky="w")
     
    entrada_login_clave = ttk.Entry(frame_login, width=30, show= '*', textvariable=verifica_clave, font=("Calibri", 14))
    entrada_login_clave.grid(row=1, column=1, padx=10, pady=10)

    #Boton Acceder
    btnAcceder = Button(frame_login, text="Acceder", width=15, height=2, font=("Calibri", 12), command=verificaInicio)
    btnAcceder.grid(row=2, column=1, pady=20)

    #Texto de pie de página
    lblPie = Label(text="©2023 INFOCOMP. Todos los derechos reservados.", font=("Calibri", 10))
    lblPie.pack(side=BOTTOM, fill=X)
    

    ventana_principal.mainloop()


