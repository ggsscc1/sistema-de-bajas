from tkinter import *
from DBconection import *
from tkinter import messagebox
import os

#Función que hace el registro del usuario en la base de datos
def registro():
    #Consultar los datos necesarios
    bd_nom_usuario = username_entry.get()
    bd_password = password_entry.get()
    bd_nombre = name_entry.get()
    bd_ap_paterno = apellido1_entry.get()
    bd_ap_materno = apellido2_entry.get()
    bd_email = email_entry.get()
    
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
        ventana_regUsuario.destroy()
        messagebox.showinfo(message="Usuario registrado con éxito", title="Éxito")
    else:
        ventana_regUsuario.destroy()
        messagebox.showerror(message="Error en el registro", title="Error")


#Función para mostrar la ventana de registro de usuario Recepción
def ventana_regU():
    #Inicializar la ventana
    global ventana_regUsuario
    ventana_regUsuario = Tk() 

    #Valores comunes
    font_size = 19
    font_family = 'Arial'

    # Obtener el tamaño de la pantalla
    screen_width = ventana_regUsuario.winfo_screenwidth()
    screen_height = ventana_regUsuario.winfo_screenheight()
    maxsize= f'{screen_width}x{screen_height}'

    #Titulo de la ventana
    ventana_regUsuario.title("Sistema de Bajas") 

    # Establecer el tamaño máximo de la ventana
    ventana_regUsuario.geometry(maxsize)

    #-------------------------------------------------------

    # Crear un Frame para la franja superior
    bar_Sup =Frame(ventana_regUsuario, bg='blue', height=50)
    bar_Sup.pack(side='top', fill='x')

    # Agregar elementos dentro del Frame
    label_Bar_Sup =Label(bar_Sup, text='Sistema de Bajas', fg='white', bg='blue')
    label_Bar_Sup.pack(pady=50)
    label_Bar_Sup.config(font=(font_family, font_size))

    # Crear un Frame para la segunda franja superior
    bar_Med =Frame(ventana_regUsuario, bg='white', height=50, highlightbackground="black", highlightthickness=2)
    bar_Med.pack(side='top', fill='x')

    # Agregar elementos dentro del Frame
    label_Med =Label(bar_Med, text='Registrar nuevo usuario', fg='black', bg="white")
    label_Med.pack(pady=10,padx=20)
    label_Med.config(font=(font_family, font_size))

    # Crear el botón a la derecha del frame
    button_Salir = Button(label_Med, text="Cerrar sesion", width=10, bg="red", fg="white",borderwidth=5)
    button_Salir.pack(side="right",pady=10,padx=(600,0))

    # Crear el botón a la izquierda del frame
    button_Salir = Button(label_Med, text="<-  Cancelar", width=10, borderwidth=5)
    button_Salir.pack(side="left",pady=10,padx=(0,600))
    #--------------------------------------------------

    #Formulario

    # Crear el frame para el registro de usuario
    user_frame = Frame(ventana_regUsuario,bg='gray',width=300,height=500,padx=60, pady=40)

    # Crear las etiquetas y campos de entrada para el registro de usuario\
    name_label = Label(user_frame, text="Nombre:", bg="gray",font=(font_family, 10))
    global name_entry
    name_entry = Entry(user_frame,width=35)  

    apellido1_label = Label(user_frame, text="Primer apellido:", bg="gray",font=(font_family, 10))
    global apellido1_entry
    apellido1_entry = Entry(user_frame,width=35)  


    apellido2_label = Label(user_frame, text="Segundo apellido:",bg="gray",font=(font_family, 10))
    global apellido2_entry
    apellido2_entry = Entry(user_frame,width=35)    
        
    email_label = Label(user_frame, text="Email:",bg="gray",font=(font_family, 10))
    global email_entry
    email_entry = Entry(user_frame,width=35)

    username_label = Label(user_frame, text="Nuevo nombre de usuario:", bg="gray",font=(font_family, 10))
    global username_entry
    username_entry = Entry(user_frame,width=35)

    password_label = Label(user_frame, text="Nueva contraseña:", bg="gray",font=(font_family, 10))
    global password_entry
    password_entry = Entry(user_frame, show="*",width=35)

    # Alinear las etiquetas y campos de entrada en el frame
    name_label.grid(row=0, column=0, padx=(30,70), pady=10, sticky="w")
    name_entry.grid(row=1, column=0, padx=(30,70), pady=(0,20),sticky="w")

    apellido1_label.grid(row=2, column=0, padx=(30,70), pady=5, sticky="w")
    apellido1_entry.grid(row=3, column=0, padx=(30,70), pady=(0,20),sticky="w")

    apellido2_label.grid(row=4, column=0, padx=(30,70), pady=5, sticky="w")
    apellido2_entry.grid(row=5, column=0, padx=(30,70), pady=(0,20),sticky="w")

    email_label.grid(row=6, column=0, padx=(30,70), pady=5, sticky="w")
    email_entry.grid(row=7, column=0, padx=(30,70), pady=(0,20),sticky="w")

    username_label.grid(row=0, column=1, padx=(70,30), pady=5, sticky="w")
    username_entry.grid(row=1, column=1, padx=(70,30), pady=(0,20),sticky="w")

    password_label.grid(row=2, column=1, padx=(70,30), pady=5, sticky="w")
    password_entry.grid(row=3, column=1, padx=(70,30), pady=(0,20),sticky="w")

    # Crear el botón de registro
    register_button =Button(user_frame, text="Registrar", borderwidth=5, command=registro)

    # Alinear el botón de registro en el frame
    register_button.grid(row=8, column=0, columnspan=2, padx=5, pady=15)

    # Centrar el frame en la ventana principal
    user_frame.place(relx=0.5, rely=0.6, anchor="center")

    ventana_regUsuario.mainloop()