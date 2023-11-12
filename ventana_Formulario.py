import tkinter as tk
from tkinter import *
from tkinter import ttk
from DBconection import *
from datetime import date
from tkinter import messagebox
import customtkinter
from CTkMessagebox import CTkMessagebox
from tkcalendar import DateEntry


# Función principal para mostrar la lista de espera
def ventana_Formulario(fila_seleccionada):
    print(fila_seleccionada)
    
    customtkinter.deactivate_automatic_dpi_awareness()
    customtkinter.set_appearance_mode("light")
    ventana_formulario = customtkinter.CTk()

    # Configurar el tamaño y el título de la ventana
    screen_width = ventana_formulario.winfo_screenwidth()
    screen_height = ventana_formulario.winfo_screenheight()
    screen_resolution = str(screen_width) + 'x' + str(screen_height)
    ventana_formulario.geometry(screen_resolution)
    ventana_formulario.title(f"Formulario: {fila_seleccionada}")
    
    #Inicialización de variables 
    global fechaF
    global nombreF
    global ap_patF
    global ap_matF
    global cve_unicaF
    global generacionF
    global carreraF
    global emailF
    global materia1F
    global materia2F
    global materia3F
    global preparatoriaF
    global inconvenienteF
    global tipo_bajaF
    global motivo_bajaF
    global trabajoF
    global formaTitF
    global fechaEgelF
     
    fechaF= StringVar()
    nombreF= StringVar()
    ap_patF= StringVar()
    ap_matF= StringVar()
    cve_unicaF= StringVar()
    generacionF= StringVar()
    carreraF= StringVar()
    emailF = StringVar()
    materia1F= customtkinter.StringVar()
    materia2F= StringVar()
    materia3F= StringVar()
    preparatoriaF= StringVar()
    inconvenienteF= StringVar()
    tipo_bajaF= StringVar()
    motivo_bajaF=StringVar()
    trabajoF = StringVar()
    formaTitF = StringVar()
    fechaEgelF = StringVar()

    #Conexion a la base de datos
    conexionPrin = ConexionBD(user='root',password='root',host='localhost',database='datosalumnosbajas')
    conexionPrin.conectar()
    
    
    consulta = f"SELECT * FROM formulario WHERE clave_unica = {fila_seleccionada}"
    res = conexionPrin.ejecutar_consulta(consulta)
    print(res)
    
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


    # Crea un frame con fondo blanco en el centro de la ventana de formulario
    frame_central = tk.Frame(ventana_formulario, bg="white")
    frame_central.pack( padx=30, pady=30)

    #crear etiqueta para la fecha
    #fecha_actual = date.today().strftime("%Y-%m-%d")
    fecha_actual = date.today().strftime("%d-%m-%Y")
    etiqueta_fecha = customtkinter.CTkLabel(frame_central, text="Fecha:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_fecha.grid(row=0, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_fecha = customtkinter.CTkLabel(frame_central, text=fecha_actual, fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_fecha.grid(row=0, column=1, sticky="w", padx=20, pady=10)
    
    # Crear etiquetas con información del alumno dentro del frame central
    etiqueta_clave = customtkinter.CTkLabel(frame_central, text="Clave:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_clave.grid(row=1, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_clave = customtkinter.CTkLabel(frame_central, text=res[0][1], fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_clave.grid(row=1, column=1, sticky="w", padx=20, pady=10)

    etiqueta_nombre = customtkinter.CTkLabel(frame_central, text="Nombre(s):", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_nombre.grid(row=2, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_nombre = customtkinter.CTkLabel(frame_central, text=res[0][2], fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_nombre.grid(row=2, column=1, sticky="w", padx=20, pady=10)

    etiqueta_ap_pat = customtkinter.CTkLabel(frame_central, text="Apellido Paterno:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_ap_pat.grid(row=3, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_ap_pat = customtkinter.CTkLabel(frame_central, text=res[0][3], fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_ap_pat.grid(row=3, column=1, sticky="w", padx=20, pady=10)

    etiqueta_ap_mat = customtkinter.CTkLabel(frame_central, text="Apellido Materno:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_ap_mat.grid(row=4, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_ap_mat = customtkinter.CTkLabel(frame_central, text=res[0][4], fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_ap_mat.grid(row=4, column=1, sticky="w", padx=20, pady=10)

    etiqueta_carrera = customtkinter.CTkLabel(frame_central, text="Carrera:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_carrera.grid(row=5, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_carrera = customtkinter.CTkLabel(frame_central, text=res[0][7], fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_carrera.grid(row=5, column=1, sticky="w", padx=20, pady=10)

    etiqueta_generacion = customtkinter.CTkLabel(frame_central, text="Generación:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_generacion.grid(row=6, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_generacion = customtkinter.CTkLabel(frame_central, text=res[0][8], fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_generacion.grid(row=6, column=1, sticky="w", padx=20, pady=10)

     # Crear entry para el correo electronico
    etiqueta_correo = customtkinter.CTkLabel(frame_central, text="Correo electronico:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_correo.grid(row=7, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_correo = customtkinter.CTkEntry(frame_central,width=250, corner_radius=10, textvariable=emailF)
    etiqueta_valor_correo.grid(row=7, column=1, padx=20, pady=10) 
    
    # Crear entry para la materia dificil 1
    etiqueta_materia1 = customtkinter.CTkLabel(frame_central, text="Materia dificil 1:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_materia1.grid(row=8, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_materia1 = customtkinter.CTkComboBox(frame_central, values= listaMaterias, width=250, corner_radius=10 ,  state="readonly", variable=materia1F)
    etiqueta_valor_materia1.grid(row=8, column=1, padx=20, pady=10) 
    
    # Crear entry para la materia dificil 2
    etiqueta_materia2 = customtkinter.CTkLabel(frame_central, text="Materia dificil 2:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_materia2.grid(row=9, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_materia2 = customtkinter.CTkComboBox(frame_central, values= listaMaterias, width=250, corner_radius=10,  state="readonly", variable=materia2F)
    etiqueta_valor_materia2.grid(row=9, column=1, padx=20, pady=10) 
       
    # Crear entry para la materia dificil 3
    etiqueta_materia3 = customtkinter.CTkLabel(frame_central, text="Materia dificil 3:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_materia3.grid(row=10, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_materia3 = customtkinter.CTkComboBox(frame_central, values= listaMaterias, width=250, corner_radius=10,  state="readonly", variable=materia3F)
    etiqueta_valor_materia3.grid(row=10, column=1, padx=20, pady=10) 
    
    # Crear entry para la preparatoria de origen
    etiqueta_preparatoria = customtkinter.CTkLabel(frame_central, text="Preparatoria de origen:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_preparatoria.grid(row=11, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_preparatoria = customtkinter.CTkComboBox(frame_central,values=listaPrepas, width=250, corner_radius=10,  state="readonly", variable= preparatoriaF)
    etiqueta_valor_preparatoria.grid(row=11, column=1, padx=20, pady=10)
    
    # Crear entry para el inconveniente de la carrera
    etiqueta_inconveniente = customtkinter.CTkLabel(frame_central, text="Inconveniente con la carrera:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_inconveniente.grid(row=12, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_inconveniente = customtkinter.CTkEntry(frame_central, width=250, corner_radius=10, textvariable= inconvenienteF)
    etiqueta_valor_inconveniente.grid(row=12, column=1, padx=20, pady=10)
    
    # Crear entry para caso de que trabaje
    etiqueta_actualizable = customtkinter.CTkLabel(frame_central, text=" ", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_actualizable.grid(row=2, column=2, sticky="w", padx=20, pady=10)
    etiqueta_actualizable.grid_remove()
    
    etiqueta_valor_trabajo = customtkinter.CTkEntry(frame_central,width=250, corner_radius=10, textvariable=trabajoF)
    etiqueta_valor_trabajo.grid(row=2, column=3, padx=20, pady=10) 
    etiqueta_valor_trabajo.grid_remove()

    
    # Crear entry para el tipo de baja
    etiqueta_tipo_baja = customtkinter.CTkLabel(frame_central, text="Tipo de baja:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_tipo_baja.grid(row=0, column=2, sticky="w", padx=20, pady=10)
    etiqueta_valor_tipo_baja = customtkinter.CTkComboBox(frame_central,values= listaTiposBaja, width=250, corner_radius=10,  state="readonly", variable= tipo_bajaF)
    etiqueta_valor_tipo_baja.grid(row=0, column=3, padx=20, pady=10)
    
    # Crear entry para el motivo de la baja
    etiqueta_motivo_baja = customtkinter.CTkLabel(frame_central, text="Motivo de la baja:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_motivo_baja.grid(row=1, column=2, sticky="w", padx=20, pady=10)
    etiqueta_valor_motivo_baja = customtkinter.CTkComboBox(frame_central,values=listaMotivosBaja  , width=250, corner_radius=10, variable= motivo_bajaF, command=lambda event: on_combobox1_change())
    etiqueta_valor_motivo_baja.grid(row=1, column=3, padx=20, pady=10)


    def on_combobox1_change():
        value = etiqueta_valor_motivo_baja.get()
        if value == "Titulación":
            etiqueta_FechaEgel.grid_remove()
            FechaEgel_Combo.grid_remove()
            etiqueta_valor_trabajo.grid_remove()
            etiqueta_actualizable.configure(text="Forma de Titulación:")
            etiqueta_actualizable.grid()
            forma_titulacion_Combo.grid()
        elif value == "Trabajo":
            etiqueta_FechaEgel.grid_remove()
            FechaEgel_Combo.grid_remove()
            forma_titulacion_Combo.grid_remove()
            etiqueta_actualizable.configure( text="Nombre de la empresa:")
            etiqueta_actualizable.grid()            
            etiqueta_valor_trabajo.grid()
        else:
            etiqueta_actualizable.configure( text=" ")
            forma_titulacion_Combo.grid_remove()
            etiqueta_actualizable.grid_remove()
            etiqueta_valor_trabajo.grid_remove()
            etiqueta_FechaEgel.grid_remove()
            FechaEgel_Combo.grid_remove()
    
    def on_combobox2_change():
        value = forma_titulacion_Combo.get()
        if value == "EGEL":
            etiqueta_FechaEgel.grid()
            FechaEgel_Combo.grid()
        else:
            etiqueta_FechaEgel.grid_remove()
            FechaEgel_Combo.grid_remove()
 
    #campo de entrada para "Forma de Titulación"
    forma_titulacion_Combo =  customtkinter.CTkComboBox(frame_central,  width=250, corner_radius=10, values=listaFormaTitulacion,variable=formaTitF, command=lambda event: on_combobox2_change())
    forma_titulacion_Combo.grid(row=2, column=3, padx=20, pady=10)
    forma_titulacion_Combo.grid_remove() 
    
    #etiqueta y campo de entrada para "Fecha Egel"
    #del Examen EGEL
    etiqueta_FechaEgel = customtkinter.CTkLabel(frame_central, text="Fecha aproximada de aplicación: ", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_FechaEgel.grid(row=3, column=2, sticky="w", padx=20, pady=10)
    etiqueta_FechaEgel.grid_remove()

    FechaEgel_Combo =  customtkinter.CTkComboBox(frame_central,  width=250, corner_radius=10, values=["Marzo", "Agosto", "Diciembre"])
    FechaEgel_Combo.grid(row=3, column=3, padx=20, pady=10)
    FechaEgel_Combo.grid_remove() 

    
    


    fechaF = fecha_actual
    cve_unicaF = res[0][1]
    ap_patF = res[0][3]
    ap_matF = res[0][4]
    nombreF = res[0][2]
    carreraF = res[0][7]
    generacionF = res[0][8]
    
    def imprimir_informacion():
       
        print("Fecha:",etiqueta_valor_fecha.cget("text"))
        print("Nombre:", etiqueta_valor_nombre.cget("text"))
        print("Apellido Paterno:", etiqueta_valor_ap_pat.cget("text"))
        print("Apellido Materno:", etiqueta_valor_ap_mat.cget("text"))
        print("Clave Única:", etiqueta_valor_clave.cget("text"))
        print("Generación:", etiqueta_valor_generacion.cget("text"))
        print("Carrera:", etiqueta_valor_carrera.cget("text"))
        print("Correo Electrónico:", etiqueta_valor_correo.get())
        print("Materia Difícil 1:",  etiqueta_valor_materia1.get())
        print("Materia Difícil 2:", etiqueta_valor_materia2.get())
        print("Materia Difícil 3:", etiqueta_valor_materia3.get())
        print("Preparatoria de Origen:", etiqueta_valor_preparatoria.get())
        print("Inconveniente con la Carrera:", etiqueta_valor_inconveniente.get())
        print("Tipo de Baja:", etiqueta_valor_tipo_baja.get())
        print("Motivo de Baja:", etiqueta_valor_motivo_baja.get())
        print("Trabajo (Nombre de la Empresa):", etiqueta_valor_trabajo.get())
        print("Forma de Titulación:", forma_titulacion_Combo.get())

    def actualizar_informacion():
        
        
        fechaF = etiqueta_valor_fecha.cget("text")
        nombreF = etiqueta_valor_nombre.cget("text")
        apPatF = etiqueta_valor_ap_pat.cget("text")
        apMatF = etiqueta_valor_ap_mat.cget("text")
        cveUnicaF = etiqueta_valor_clave.cget("text")
        genF = etiqueta_valor_generacion.cget("text")
        carreraF = etiqueta_valor_carrera.cget("text")
        correoF = etiqueta_valor_correo.get()
        matdif1F = etiqueta_valor_materia1.get()
        matdif2F = etiqueta_valor_materia2.get()
        matdif3F = etiqueta_valor_materia3.get()
        prepa_origenF = etiqueta_valor_preparatoria.get()
        inconvenienteF = etiqueta_valor_inconveniente.get()
        tipoBajaF = etiqueta_valor_tipo_baja.get()
        motivoBajaF = etiqueta_valor_motivo_baja.get()
        trabajoF = etiqueta_valor_trabajo.get()
        fTitulacionF = forma_titulacion_Combo.get()  

        #Consulta a base de datos para las materias
        print(correoF)
        #actualizaInf = f"update formulario set email_alumno = '{correoF}' where clave_unica = '{cveUnicaF}'"
        actualizaInf = f"update formulario set email_alumno = '{correoF}', matdif1 = '{matdif1F}', matdif2 = '{matdif2F}', matdif3 = '{matdif3F}', prepa_origen = '{prepa_origenF}', detalles_baja = '{inconvenienteF}', tipobaja = '{tipoBajaF}' where   clave_unica = '{cveUnicaF}'"
        actualizaInf = conexionPrin.ejecutar_consulta(actualizaInf)

    # Agrega un botón para cerrar la ventana de formulario debajo del frame
    #boton_cerrar = customtkinter.CTkButton(ventana_formulario, text="Enviar", width=250, height=50 , corner_radius=20 ,  command=ventana_formulario.destroy)
    #boton_cerrar = customtkinter.CTkButton(ventana_formulario, text="Enviar", width=250, height=50, corner_radius=20, command=actualizar_informacion)
    boton_cerrar = customtkinter.CTkButton(ventana_formulario, text="Enviar", width=250, height=50, corner_radius=20, command=lambda: [actualizar_informacion(), ventana_formulario.destroy()])
    boton_cerrar.pack(pady=20)

    ventana_formulario.mainloop()
