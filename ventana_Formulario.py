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
    ventana_formulario.title(f"Formulario: {fila_seleccionada[0]}")
    
    
    
    #Conexion a la base de datos
    conexionPrin = ConexionBD(user='root',password='root',host='localhost',database='datosalumnosbajas')
    conexionPrin.conectar()
    
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
    fecha_actual = date.today().strftime("%Y-%m-%d")
    etiqueta_fecha = customtkinter.CTkLabel(frame_central, text="Fecha:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_fecha.grid(row=0, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_fecha = customtkinter.CTkLabel(frame_central, text=fecha_actual, fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_fecha.grid(row=0, column=1, sticky="w", padx=20, pady=10)
    
    # Crear etiquetas con información del alumno dentro del frame central
    etiqueta_clave = customtkinter.CTkLabel(frame_central, text="Clave:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_clave.grid(row=1, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_clave = customtkinter.CTkLabel(frame_central, text=fila_seleccionada[0], fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_clave.grid(row=1, column=1, sticky="w", padx=20, pady=10)

    etiqueta_nombre = customtkinter.CTkLabel(frame_central, text="Nombre(s):", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_nombre.grid(row=2, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_nombre = customtkinter.CTkLabel(frame_central, text=fila_seleccionada[3], fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_nombre.grid(row=2, column=1, sticky="w", padx=20, pady=10)

    etiqueta_ap_pat = customtkinter.CTkLabel(frame_central, text="Apellido Paterno:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_ap_pat.grid(row=3, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_ap_pat = customtkinter.CTkLabel(frame_central, text=fila_seleccionada[1], fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_ap_pat.grid(row=3, column=1, sticky="w", padx=20, pady=10)

    etiqueta_ap_mat = customtkinter.CTkLabel(frame_central, text="Apellido Materno:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_ap_mat.grid(row=4, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_ap_mat = customtkinter.CTkLabel(frame_central, text=fila_seleccionada[2], fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_ap_mat.grid(row=4, column=1, sticky="w", padx=20, pady=10)

    etiqueta_carrera = customtkinter.CTkLabel(frame_central, text="Carrera:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_carrera.grid(row=5, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_carrera = customtkinter.CTkLabel(frame_central, text=fila_seleccionada[4], fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_carrera.grid(row=5, column=1, sticky="w", padx=20, pady=10)

    etiqueta_generacion = customtkinter.CTkLabel(frame_central, text="Generación:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_generacion.grid(row=6, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_generacion = customtkinter.CTkLabel(frame_central, text=fila_seleccionada[5], fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_valor_generacion.grid(row=6, column=1, sticky="w", padx=20, pady=10)
    
    # Crear entry para el correo electronico
    etiqueta_correo = customtkinter.CTkLabel(frame_central, text="Correo electronico:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_correo.grid(row=7, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_correo = customtkinter.CTkEntry(frame_central,width=250, corner_radius=10)
    etiqueta_valor_correo.grid(row=7, column=1, padx=20, pady=10) 
    
    # Crear entry para la materia dificil 1
    etiqueta_materia1 = customtkinter.CTkLabel(frame_central, text="Materia dificil 1:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_materia1.grid(row=8, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_materia1 = customtkinter.CTkComboBox(frame_central, values= listaMaterias, width=250, corner_radius=10 ,  state="readonly")
    etiqueta_valor_materia1.grid(row=8, column=1, padx=20, pady=10) 
    
    # Crear entry para la materia dificil 2
    etiqueta_materia2 = customtkinter.CTkLabel(frame_central, text="Materia dificil 2:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_materia2.grid(row=9, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_materia2 = customtkinter.CTkComboBox(frame_central, values= listaMaterias, width=250, corner_radius=10,  state="readonly")
    etiqueta_valor_materia2.grid(row=9, column=1, padx=20, pady=10) 
       
    # Crear entry para la materia dificil 3
    etiqueta_materia3 = customtkinter.CTkLabel(frame_central, text="Materia dificil 3:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_materia3.grid(row=10, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_materia3 = customtkinter.CTkComboBox(frame_central, values= listaMaterias, width=250, corner_radius=10,  state="readonly")
    etiqueta_valor_materia3.grid(row=10, column=1, padx=20, pady=10) 
    
    # Crear entry para la preparatoria de origen
    etiqueta_preparatoria = customtkinter.CTkLabel(frame_central, text="Preparatoria de origen:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_preparatoria.grid(row=11, column=0, sticky="w", padx=20, pady=10)
    etiqueta_valor_preparatoria = customtkinter.CTkComboBox(frame_central,values=listaPrepas, width=250, corner_radius=10,  state="readonly", command=lambda event:on_combobox3_change())
    etiqueta_valor_preparatoria.grid(row=11, column=1, padx=20, pady=10)

    etiqueta_otraPrepa = customtkinter.CTkLabel(frame_central, text="Escribe el nombre de tu preparatoria: ", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_otraPrepa.grid(row=3, column=2, sticky="w", padx=20, pady=10)
    etiqueta_otraPrepa.grid_remove()

    etiqueta_otraPrepa_valor =  customtkinter.CTkEntry(frame_central,width=250, corner_radius=10)
    etiqueta_otraPrepa_valor.grid(row=3, column=3, padx=20, pady=10)
    etiqueta_otraPrepa_valor.grid_remove()
    

    def on_combobox3_change():
        value = etiqueta_valor_preparatoria.get()
        if value == "Otra":
            etiqueta_otraPrepa.grid()
            etiqueta_otraPrepa_valor.grid()
        elif value == "Preparatoria Foránea":
            etiqueta_otraPrepa.grid()
            etiqueta_otraPrepa_valor.grid()
        else:
            etiqueta_otraPrepa.grid_remove()
            etiqueta_otraPrepa_valor.grid_remove()
    
    # Crear entry para el inconveniente de la carrera
    etiqueta_inconveniente = customtkinter.CTkLabel(frame_central, text="Inconveniente con la carrera:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_inconveniente.grid(row=4, column=2, sticky="w", padx=20, pady=10)
    etiqueta_valor_inconveniente = customtkinter.CTkEntry(frame_central, width=250, corner_radius=10)
    etiqueta_valor_inconveniente.grid(row=4, column=3, padx=20, pady=10)
    
    # Crear entry para caso de que trabaje
    etiqueta_actualizable = customtkinter.CTkLabel(frame_central, text=" ", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_actualizable.grid(row=2, column=2, sticky="w", padx=20, pady=10)
    etiqueta_actualizable.grid_remove()
    
    etiqueta_valor_trabajo = customtkinter.CTkEntry(frame_central,width=250, corner_radius=10)
    etiqueta_valor_trabajo.grid(row=2, column=3, padx=20, pady=10) 
    etiqueta_valor_trabajo.grid_remove()

    
    # Crear entry para el tipo de baja
    etiqueta_tipo_baja = customtkinter.CTkLabel(frame_central, text="Tipo de baja:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_tipo_baja.grid(row=0, column=2, sticky="w", padx=20, pady=10)
    etiqueta_valor_tipo_baja = customtkinter.CTkComboBox(frame_central,values= listaTiposBaja, width=250, corner_radius=10,  state="readonly")
    etiqueta_valor_tipo_baja.grid(row=0, column=3, padx=20, pady=10)
    
    # Crear entry para el motivo de la baja
    etiqueta_motivo_baja = customtkinter.CTkLabel(frame_central, text="Motivo de la baja:", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_motivo_baja.grid(row=1, column=2, sticky="w", padx=20, pady=10)
    etiqueta_valor_motivo_baja = customtkinter.CTkComboBox(frame_central,values=listaMotivosBaja,  state="readonly"  , width=250, corner_radius=10, command=lambda event: on_combobox1_change())
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
    forma_titulacion_Combo =  customtkinter.CTkComboBox(frame_central,  state="readonly",  width=250, corner_radius=10, values=listaFormaTitulacion, command=lambda event: on_combobox2_change())
    forma_titulacion_Combo.grid(row=2, column=3, padx=20, pady=10)
    forma_titulacion_Combo.grid_remove() 
    
    #etiqueta y campo de entrada para "Fecha Egel"
    #del Examen EGEL
    etiqueta_FechaEgel = customtkinter.CTkLabel(frame_central, text="Fecha aproximada de aplicación: ", fg_color="white", anchor="w", font=("Arial",16))
    etiqueta_FechaEgel.grid(row=3, column=2, sticky="w", padx=20, pady=10)
    etiqueta_FechaEgel.grid_remove()

    FechaEgel_Combo =  customtkinter.CTkComboBox(frame_central,  state="readonly",  width=250, corner_radius=10, values=["Marzo", "Agosto", "Diciembre"])
    FechaEgel_Combo.grid(row=3, column=3, padx=20, pady=10)
    FechaEgel_Combo.grid_remove() 



    def inserta_Form():
    
        #Obtención de las variables requeridas en el llenado del formulario
        fechaI = etiqueta_valor_fecha.cget("text")
        nombreI = etiqueta_valor_nombre.cget("text")
        ap_patI = etiqueta_valor_ap_pat.cget("text")
        ap_matI = etiqueta_valor_ap_mat.cget("text")
        cve_unicaI = etiqueta_valor_clave.cget("text")
        generacionI = etiqueta_valor_generacion.cget("text")
        carreraI = etiqueta_valor_carrera.cget("text")
        emailI = etiqueta_valor_correo.get()
        materia1I = etiqueta_valor_materia1.get()
        materia2I = etiqueta_valor_materia2.get()
        materia3I = etiqueta_valor_materia3.get()
        
        value = etiqueta_valor_preparatoria.get()
        if value == "Otra":
            prepaI = etiqueta_otraPrepa_valor.get()
        elif value == "Preparatoria Foránea":
            prepaI = etiqueta_otraPrepa_valor.get()
        else:
            prepaI = etiqueta_valor_preparatoria.get()    
            

        mot_realI = etiqueta_valor_motivo_baja.get()
        inconvenienteI = etiqueta_valor_inconveniente.get()
        trabajoI = etiqueta_valor_trabajo.get()
        formaTitI = forma_titulacion_Combo.get()
        tipo_bajaI = etiqueta_valor_tipo_baja.get()
        fechaEgelI = FechaEgel_Combo.get()

        #Conexión con la base de datos
        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')

        conexion.conectar()

        #Ejecución de las consultas
        insertar = f"INSERT INTO datosalumnosbajas.formulario (fecha_solicitud, clave_unica, nombre, ap_paterno, ap_materno, generacion, carrera, email_alumno, matdif1, matdif2, matdif3, prepa_origen, tipobaja, detalles_baja, empresa, formatit, fecha_egel, motbaja) VALUES ('{fechaI}','{cve_unicaI}','{nombreI}','{ap_patI}','{ap_matI}','{generacionI}','{carreraI}','{emailI}','{materia1I}','{materia2I}','{materia3I}','{prepaI}','{tipo_bajaI}','{inconvenienteI}','{trabajoI}','{formaTitI}','{fechaEgelI}','{mot_realI}')"
        resultado1 = conexion.ejecutar_consulta(insertar)
        #eliminar = f"DELETE FROM datosalumnosbajas.lista_de_espera WHERE clave_unica = {cve_unicaI}"
        #resultado2 = conexion.ejecutar_consulta(eliminar)

        print(resultado1)
        #print(resultado2)
        
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
        print("Fecha egel", FechaEgel_Combo.get())
        
    # Agrega un botón para cerrar la ventana de formulario debajo del frame
    #boton_cerrar = customtkinter.CTkButton(ventana_formulario, text="Enviar", width=250, height=50 , corner_radius=20 ,  command=ventana_formulario.destroy)
    boton_cerrar = customtkinter.CTkButton(ventana_formulario, text="Enviar", width=250, height=50, corner_radius=20, command=lambda: inserta_Form())
    boton_cerrar.pack(pady=20)

    ventana_formulario.mainloop()

