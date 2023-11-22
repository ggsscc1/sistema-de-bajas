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
    #customtkinter.deactivate_automatic_dpi_awareness()
    customtkinter.set_appearance_mode("light")
    ventana_formulario = customtkinter.CTk()


    # Configurar el tamaño y el título de la ventana
    screen_width = ventana_formulario.winfo_screenwidth()
    screen_height = ventana_formulario.winfo_screenheight()
    screen_resolution = str(screen_width) + 'x' + str(screen_height)
    ventana_formulario.geometry(screen_resolution)
    ventana_formulario.title(f"Formulario: {fila_seleccionada[0]}")
    ventana_formulario.state('zoomed')
    
    
    
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

    consultaformulario = f"SELECT * FROM lista_de_espera WHERE clave_unica = '{fila_seleccionada[0]}'"
    resFormulario = conexionPrin.ejecutar_consulta(consultaformulario)
    print(resFormulario)

    conexionPrin.desconectar()


    # Crea un frame con fondo blanco en el centro de la ventana de formulario
    frame_central = customtkinter.CTkFrame(ventana_formulario, fg_color="white")
    frame_central.pack( padx=30, pady=30)

    inter_frame1 = customtkinter.CTkFrame(frame_central)
    inter_frame1.grid(row=0, column=0, padx=5, pady=5, rowspan=1)

    inter_frame2 = customtkinter.CTkFrame(frame_central)
    inter_frame2.grid(row=0, column=1, padx=5, pady=5, rowspan=1)

    """ CAMPOS OBLIGATORIOS fechaI, nombreI, ap_patI, cve_unicaI, generacionI, 
                            carreraI, emailI, value,
                             materia1I, mot_realI, tipo_bajaI"""

    #crear etiqueta para la fecha
    #fecha_actual = date.today().strftime("%Y-%m-%d")
    fecha_actual = date.today().strftime("%Y-%m-%d")
    etiqueta_fecha = customtkinter.CTkLabel(inter_frame1, text="Fecha:",  anchor="w", font=("Arial",16))
    etiqueta_fecha.grid(row=0, column=0, sticky="e", padx=10, pady=10)
    etiqueta_valor_fecha = customtkinter.CTkLabel(inter_frame1, text=fecha_actual,  anchor="w", font=("Arial",16))
    etiqueta_valor_fecha.grid(row=0, column=1, sticky="w", padx=10, pady=10)
    
    # Crear etiquetas con información del alumno dentro del frame central
    etiqueta_clave = customtkinter.CTkLabel(inter_frame1, text="Clave:",  anchor="w", font=("Arial",16))
    etiqueta_clave.grid(row=1, column=0, sticky="e", padx=10, pady=10)
    etiqueta_valor_clave = customtkinter.CTkLabel(inter_frame1, text=fila_seleccionada[0],  anchor="w", font=("Arial",16))
    etiqueta_valor_clave.grid(row=1, column=1, sticky="w", padx=10, pady=10)

    etiqueta_nombre = customtkinter.CTkLabel(inter_frame1, text="Nombre(s):",  anchor="w", font=("Arial",16))
    etiqueta_nombre.grid(row=2, column=0, sticky="e", padx=10, pady=10)
    etiqueta_valor_nombre = customtkinter.CTkLabel(inter_frame1, text=fila_seleccionada[3],  anchor="w", font=("Arial",16))
    etiqueta_valor_nombre.grid(row=2, column=1, sticky="w", padx=10, pady=10)

    etiqueta_ap_pat = customtkinter.CTkLabel(inter_frame1, text="Apellido Paterno:",  anchor="w", font=("Arial",16))
    etiqueta_ap_pat.grid(row=3, column=0, sticky="e", padx=10, pady=10)
    etiqueta_valor_ap_pat = customtkinter.CTkLabel(inter_frame1, text=fila_seleccionada[1],  anchor="w", font=("Arial",16))
    etiqueta_valor_ap_pat.grid(row=3, column=1, sticky="w", padx=10, pady=10)

    etiqueta_ap_mat = customtkinter.CTkLabel(inter_frame1, text="Apellido Materno:",  anchor="w", font=("Arial",16))
    etiqueta_ap_mat.grid(row=4, column=0, sticky="e", padx=10, pady=10)
    etiqueta_valor_ap_mat = customtkinter.CTkLabel(inter_frame1, text=fila_seleccionada[2],  anchor="w", font=("Arial",16))
    etiqueta_valor_ap_mat.grid(row=4, column=1, sticky="w", padx=10, pady=10)

    etiqueta_carrera = customtkinter.CTkLabel(inter_frame1, text="Carrera:",  anchor="w", font=("Arial",16))
    etiqueta_carrera.grid(row=5, column=0, sticky="e", padx=10, pady=10)
    etiqueta_valor_carrera = customtkinter.CTkLabel(inter_frame1, text=fila_seleccionada[4],  anchor="w", font=("Arial",16))
    etiqueta_valor_carrera.grid(row=5, column=1, sticky="w", padx=10, pady=10)

    etiqueta_generacion = customtkinter.CTkLabel(inter_frame1, text="Generación:",  anchor="w", font=("Arial",16))
    etiqueta_generacion.grid(row=6, column=0, sticky="e", padx=10, pady=10)
    etiqueta_valor_generacion = customtkinter.CTkLabel(inter_frame1, text=fila_seleccionada[5],  anchor="w", font=("Arial",16))
    etiqueta_valor_generacion.grid(row=6, column=1, sticky="w", padx=10, pady=10)
    
    # Crear entry para el correo electronico
    etiqueta_correo = customtkinter.CTkLabel(inter_frame1, text="*Correo electrónico:",  anchor="w", font=("Arial",16), text_color="red")
    etiqueta_correo.grid(row=7, column=0, sticky="e", padx=10, pady=10)
    etiqueta_valor_correo = customtkinter.CTkEntry(inter_frame1,width=250, corner_radius=10)
    if resFormulario and len(resFormulario) > 0:
        if len(resFormulario[0]) > 6:
            if resFormulario[0][6] is not None:
                etiqueta_valor_correo.delete(0, tk.END)
                etiqueta_valor_correo.insert(0, resFormulario[0][6])
    etiqueta_valor_correo.grid(row=7, column=1, padx=10, pady=10) 
    
    # Crear entry para la materia dificil 1
    etiqueta_materia1 = customtkinter.CTkLabel(inter_frame1, text="*Materia difícil 1:",  anchor="w", font=("Arial",16), text_color="red")
    etiqueta_materia1.grid(row=8, column=0, sticky="e", padx=10, pady=10)
    etiqueta_valor_materia1 = customtkinter.CTkComboBox(inter_frame1, values= listaMaterias, width=250, corner_radius=10 ,  state="readonly")
    if resFormulario and len(resFormulario[0]) > 11:
        if resFormulario[0][11] is not None:
            etiqueta_valor_materia1.set("")
            etiqueta_valor_materia1.set(resFormulario[0][11])
    etiqueta_valor_materia1.grid(row=8, column=1, padx=10, pady=10) 
    
    # Crear entry para la materia dificil 2
    etiqueta_materia2 = customtkinter.CTkLabel(inter_frame2, text="Materia difícil 2:",  anchor="w", font=("Arial",16))
    etiqueta_materia2.grid(row=0, column=0, sticky="e", padx=10, pady=10)
    etiqueta_valor_materia2 = customtkinter.CTkComboBox(inter_frame2, values= listaMaterias, width=250, corner_radius=10,  state="readonly")
    if resFormulario and len(resFormulario[0]) > 12:
        if resFormulario[0][12] is not None:
            etiqueta_valor_materia2.set("")
            etiqueta_valor_materia2.set(resFormulario[0][12])
    etiqueta_valor_materia2.grid(row=0, column=1, padx=10, pady=10) 
       
    # Crear entry para la materia dificil 3
    etiqueta_materia3 = customtkinter.CTkLabel(inter_frame2, text="Materia difícil 3:",  anchor="w", font=("Arial",16))
    etiqueta_materia3.grid(row=1, column=0, sticky="e", padx=10, pady=10)
    etiqueta_valor_materia3 = customtkinter.CTkComboBox(inter_frame2, values= listaMaterias, width=250, corner_radius=10,  state="readonly")
    if resFormulario and len(resFormulario[0]) > 13:
        if resFormulario[0][13] is not None:
            etiqueta_valor_materia3.set("")
            etiqueta_valor_materia3.set(resFormulario[0][13])
    etiqueta_valor_materia3.grid(row=1, column=1, padx=10, pady=10) 
    
    # Crear entry para la preparatoria de origen
    etiqueta_preparatoria = customtkinter.CTkLabel(inter_frame2, text="*Preparatoria de origen:",  anchor="w", font=("Arial",16), text_color="red")
    etiqueta_preparatoria.grid(row=2, column=0, sticky="e", padx=10, pady=10)
    etiqueta_valor_preparatoria = customtkinter.CTkComboBox(inter_frame2,values=listaPrepas, width=250, corner_radius=10,  state="readonly", command=lambda event:on_combobox3_change())
    if resFormulario and len(resFormulario[0]) > 10:
        if resFormulario[0][10] is not None:
            etiqueta_valor_preparatoria.set("")
            etiqueta_valor_preparatoria.set(resFormulario[0][10])
    etiqueta_valor_preparatoria.grid(row=2, column=1, padx=10, pady=10)

    etiqueta_otraPrepa = customtkinter.CTkLabel(inter_frame2, text="Escribe el nombre de tu preparatoria: ",  anchor="w", font=("Arial",16))
    etiqueta_otraPrepa.grid(row=3, column=0, sticky="e", padx=10, pady=10)
    etiqueta_otraPrepa.grid_remove()

    etiqueta_otraPrepa_valor =  customtkinter.CTkEntry(inter_frame2,width=250, corner_radius=10, placeholder_text="Porfavor escribe correctamente el nombre de tu escuela de procedencia.")
    etiqueta_otraPrepa_valor.grid(row=3, column=1, padx=10, pady=10)
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
    etiqueta_inconveniente = customtkinter.CTkLabel(inter_frame2, text="Inconveniente con la carrera:",  anchor="w", font=("Arial",16))
    etiqueta_inconveniente.grid(row=4, column=0, sticky="e", padx=10, pady=10)
    etiqueta_valor_inconveniente = customtkinter.CTkEntry(inter_frame2, width=250, corner_radius=10)
    if resFormulario and len(resFormulario[0]) > 16:
        if resFormulario[0][16] is not None:
            etiqueta_valor_inconveniente.delete(0, tk.END)
            etiqueta_valor_inconveniente.insert(0, resFormulario[0][16])
    etiqueta_valor_inconveniente.grid(row=4, column=1, padx=10, pady=10)
    
    # Crear entry para caso de que trabaje
    etiqueta_actualizable = customtkinter.CTkLabel(inter_frame2, text=" ",  anchor="w", font=("Arial",16))
    etiqueta_actualizable.grid(row=8, column=0, sticky="e", padx=10, pady=10)
    etiqueta_actualizable.grid_remove()
    
    etiqueta_valor_trabajo = customtkinter.CTkEntry(inter_frame2,width=250, corner_radius=10)
    etiqueta_valor_trabajo.grid(row=8, column=1, padx=10, pady=10)
    if resFormulario and len(resFormulario[0]) > 17:
        if resFormulario[0][17] is not None:
            etiqueta_valor_trabajo.delete(0, tk.END)
            etiqueta_valor_trabajo.insert(0, resFormulario[0][17])
    etiqueta_valor_trabajo.grid_remove()

    
    # Crear entry para el tipo de baja
    etiqueta_tipo_baja = customtkinter.CTkLabel(inter_frame2, text="*Tipo de baja:",  anchor="w", font=("Arial",16), text_color="red")
    etiqueta_tipo_baja.grid(row=6, column=0, sticky="e", padx=10, pady=10)
    etiqueta_valor_tipo_baja = customtkinter.CTkComboBox(inter_frame2,values= listaTiposBaja, width=250, corner_radius=10,  state="readonly")
    if resFormulario and len(resFormulario[0]) > 8:
        if resFormulario[0][8] is not None:
            etiqueta_valor_tipo_baja.set("")
            etiqueta_valor_tipo_baja.set(resFormulario[0][8])
    etiqueta_valor_tipo_baja.grid(row=6, column=1, padx=10, pady=10)
    
    # Crear entry para el motivo de la baja
    etiqueta_motivo_baja = customtkinter.CTkLabel(inter_frame2, text="*Motivo de la baja:",  anchor="w", font=("Arial",16), text_color="red")
    etiqueta_motivo_baja.grid(row=7, column=0, sticky="e", padx=10, pady=10)
    etiqueta_valor_motivo_baja = customtkinter.CTkComboBox(inter_frame2,values=listaMotivosBaja,  state="readonly"  , width=250, corner_radius=10, command=lambda event: on_combobox1_change())
    if resFormulario and len(resFormulario[0]) > 9:
        if resFormulario[0][9] is not None:
            etiqueta_valor_motivo_baja.set("")
            etiqueta_valor_motivo_baja.set(resFormulario[0][9])
    etiqueta_valor_motivo_baja.grid(row=7, column=1, padx=10, pady=10)

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
    forma_titulacion_Combo =  customtkinter.CTkComboBox(inter_frame2,  state="readonly",  width=250, corner_radius=10, values=listaFormaTitulacion, command=lambda event: on_combobox2_change())
    forma_titulacion_Combo.grid(row=8, column=1, padx=10, pady=10)
    if resFormulario and len(resFormulario[0]) > 14:
        if resFormulario[0][14] is not None:
            forma_titulacion_Combo.set("")
            forma_titulacion_Combo.set(resFormulario[0][14])
    forma_titulacion_Combo.grid_remove() 
    
    #etiqueta y campo de entrada para "Fecha Egel"
    #del Examen EGEL
    etiqueta_FechaEgel = customtkinter.CTkLabel(inter_frame2, text="Fecha aproximada de aplicación: ",  anchor="w", font=("Arial",16))
    etiqueta_FechaEgel.grid(row=9, column=0, sticky="w", padx=10, pady=10)
    etiqueta_FechaEgel.grid_remove()

    FechaEgel_Combo =  customtkinter.CTkComboBox(inter_frame2,  state="readonly",  width=250, corner_radius=10, values=["Marzo", "Agosto", "Diciembre"])
    FechaEgel_Combo.grid(row=9, column=1, padx=10, pady=10)
    if resFormulario and len(resFormulario[0]) > 15:
        if resFormulario[0][15] is not None:
            FechaEgel_Combo.set("")
            FechaEgel_Combo.set(resFormulario[0][15])
    FechaEgel_Combo.grid_remove() 

    boton_cerrar = customtkinter.CTkButton(ventana_formulario, text="Enviar", width=250, height=50, corner_radius=20, command=lambda: insertaValidacion())
    boton_cerrar.pack(pady=20)

    btn_guardar = customtkinter.CTkButton(ventana_formulario, text="Guardar temporalmente", width=250, height=50, corner_radius=20, command=lambda: inserta_Form())
    btn_guardar.pack(pady=20)


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
            conexion = ConexionBD(user='root',password='root',host='localhost',database='datosalumnosbajas')

            conexion.conectar()

            #Ejecución de las consultas
            insertar = f"INSERT INTO datosalumnosbajas.prepa_procedencia (nombre_prepa) VALUES ('{prepaI}')"
            resultado1 = conexion.ejecutar_consulta(insertar)
            #eliminar = f"DELETE FROM datosalumnosbajas.lista_de_espera WHERE clave_unica = {cve_unicaI}"
            #resultado2 = conexion.ejecutar_consulta(eliminar)

            conexion.desconectar()
        elif value == "Preparatoria Foránea":
            prepaI = etiqueta_otraPrepa_valor.get()
            conexion = ConexionBD(user='root',password='root',host='localhost',database='datosalumnosbajas')

            conexion.conectar()

            #Ejecución de las consultas
            insertar = f"INSERT INTO datosalumnosbajas.prepa_procedencia (nombre_prepa) VALUES ('{prepaI}')"
            resultado1 = conexion.ejecutar_consulta(insertar)
            #eliminar = f"DELETE FROM datosalumnosbajas.lista_de_espera WHERE clave_unica = {cve_unicaI}"
            #resultado2 = conexion.ejecutar_consulta(eliminar)
            conexion.desconectar()
        else:
            prepaI = etiqueta_valor_preparatoria.get()    
            

        mot_realI = etiqueta_valor_motivo_baja.get()
        inconvenienteI = etiqueta_valor_inconveniente.get()
        trabajoI = etiqueta_valor_trabajo.get()
        formaTitI = forma_titulacion_Combo.get()
        tipo_bajaI = etiqueta_valor_tipo_baja.get()
        fechaEgelI = FechaEgel_Combo.get()

        #Conexión con la base de datos
        conexion = ConexionBD(user='root',password='root',host='localhost',database='datosalumnosbajas')

        conexion.conectar()

        #Ejecución de las consultas
        query = f"UPDATE lista_de_espera SET fecha = '{fechaI}', clave_unica = '{cve_unicaI}', email = '{emailI}', carrera = '{carreraI}', generacion = '{generacionI}', motbaja = '{mot_realI}', prepa_origen = '{prepaI}', tipobaja = '{tipo_bajaI}'"
        #, materia_dificil = '{materia_valor}', materia_dificil2 = '{materia2_valor}', materia_dificil3 = '{materia3_valor}', detalles_baja = '{motivotexto_valor}', forma_titulacion = '{formatexto_valor}', fecha_egel = '{fechaTtexto_valor}'

        if materia1I is not None:
            query += f", matdif1 = '{materia1I}'"
        if materia2I is not None:
            query += f", matdif2 = '{materia2I}'"
        if materia3I is not None:
            query += f", matdif3 = '{materia3I}'"
        if inconvenienteI is not None:
            query += f", detalles_baja = '{inconvenienteI}'"
        if formaTitI is not None:
            query += f", formatit = '{formaTitI}'"
        if fechaEgelI is not None:
            query += f", fecha_egel = '{fechaEgelI}'"
        if trabajoI is not None:
            query += f", empresa = '{trabajoI}'"

        query2 = f"WHERE clave_unica = '{cve_unicaI}'"
        queryFinal = query + " " +query2
        
        # Ejecutar la consulta SQL
        conexion.ejecutar_consulta(queryFinal)
        #eliminar = f"DELETE FROM datosalumnosbajas.lista_de_espera WHERE clave_unica = {cve_unicaI}"
        #resultado2 = conexion.ejecutar_consulta(eliminar)


        conexion.desconectar()

        ventana_formulario.destroy()


        #print(resultado2)

    def insertaValidacion():
        #obtine los valores de los campos del formulario
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
        mot_realI = etiqueta_valor_motivo_baja.get()
        inconvenienteI = etiqueta_valor_inconveniente.get()
        trabajoI = etiqueta_valor_trabajo.get()
        formaTitI = forma_titulacion_Combo.get()
        tipo_bajaI = etiqueta_valor_tipo_baja.get()
        fechaEgelI = FechaEgel_Combo.get()

        value = etiqueta_valor_preparatoria.get()

        if value == "Otra":
            prepaI = etiqueta_otraPrepa_valor.get()
            conexion = ConexionBD(user='root',password='root',host='localhost',database='datosalumnosbajas')

            conexion.conectar()

            #Ejecución de las consultas
            insertar = f"INSERT INTO datosalumnosbajas.prepa_procedencia (nombre_prepa) VALUES ('{prepaI}')"
            resultado1 = conexion.ejecutar_consulta(insertar)
  

            conexion.desconectar()
        elif value == "Preparatoria Foránea":
            prepaI = etiqueta_otraPrepa_valor.get()
            conexion = ConexionBD(user='root',password='root',host='localhost',database='datosalumnosbajas')

            conexion.conectar()

            #Ejecución de las consultas
            insertar = f"INSERT INTO datosalumnosbajas.prepa_procedencia (nombre_prepa) VALUES ('{prepaI}')"
            resultado1 = conexion.ejecutar_consulta(insertar)

            conexion.desconectar()
        else:
            prepaI = etiqueta_valor_preparatoria.get()

        

        #si no se llenaron los campos obligatorios muestra un mensaje de error
        if not all([fechaI, nombreI, ap_patI, cve_unicaI, generacionI, carreraI, emailI, value,
                    materia1I, mot_realI, tipo_bajaI]):
            messagebox.showerror(message="Porfavor llena los campos obligatorios", title="Error")
            return

           
            

            # Database interaction
        conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
        conexion.conectar()

        #hace la insercion en el formulario
        insertar = f"INSERT INTO datosalumnosbajas.formulario (fecha_solicitud, clave_unica, nombre, ap_paterno, ap_materno, generacion, carrera, email_alumno, matdif1, matdif2, matdif3, prepa_origen, tipobaja, detalles_baja, empresa, formatit, fecha_egel, motbaja) VALUES ('{fechaI}','{cve_unicaI}','{nombreI}','{ap_patI}','{ap_matI}','{generacionI}','{carreraI}','{emailI}','{materia1I}','{materia2I}','{materia3I}','{prepaI}','{tipo_bajaI}','{inconvenienteI}','{trabajoI}','{formaTitI}','{fechaEgelI}','{mot_realI}')"

        # Execute the query and check for errors
        try:
            #verifica la insercion
            resultado = conexion.ejecutar_consulta(insertar)
            

            if resultado is not None:
                #si la insercion se realizo correctamente muestra un mensaje de exito
                messagebox.showinfo(message="Formulario registrado con éxito", title="Éxito")
                eliminar = f"DELETE FROM datosalumnosbajas.lista_de_espera WHERE clave_unica = {cve_unicaI}"
                resultado2 = conexion.ejecutar_consulta(eliminar)
                print(resultado2)
                ventana_formulario.destroy()
            else:
                #muestra mensaje de error
                messagebox.showerror(message="Error en el registro", title="Error")
        except Exception as e:
            messagebox.showerror(message=f"Error en el registro: {str(e)}", title="Error")

        
        conexion.desconectar()
        
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
    #boton_cerrar = customtkinter.CTkButton(ventana_formulario, text="rr", width=250, height=50 , corner_radius=20 ,  command=ventana_formulario.destroy)
    

    ventana_formulario.mainloop()

