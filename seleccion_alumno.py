# Importa las bibliotecas necesarias
from tkinter import *
from tkinter import ttk
from DBconection import *
from recorrido_listaEspera import lectura_listaEspera
from datetime import date
from tkinter import messagebox
import customtkinter
from tkinter import messagebox
from ventana_Formulario import ventana_Formulario  

        
# Función para seleccionar un formulario y mostrar la ventana de formulario
def seleccionar_formulario(treeview):
    # Obtener la fila seleccionada
    seleccion = treeview.selection()
    if seleccion:
        fila_seleccionada = treeview.item(seleccion)['values']
        # Mostrar la ventana del formulario con la fila seleccionada
        ventana_Formulario(fila_seleccionada)
    else:
        messagebox.showerror("Error", "Por favor, selecciona un formulario primero.")


 
        

# Función principal para mostrar la lista de espera
def ventana_InicioForm():
    customtkinter.deactivate_automatic_dpi_awareness()
    customtkinter.set_appearance_mode("light")
    ventana_Iniform = customtkinter.CTk()


  # Configurar el tamaño y el título de la ventana
    screen_width = ventana_Iniform.winfo_screenwidth()
    screen_height = ventana_Iniform.winfo_screenheight()
    screen_resolution = str(screen_width) + 'x' + str(screen_height)
    ventana_Iniform.geometry(screen_resolution)
    ventana_Iniform.title("Sistema de Bajas")


    # Agregar el título sistema de bajas
    lbl_SB = Label(text="Sistema de bajas", fg="white", bg="darkblue", width="300", height="2", font=("Arial", 30))
    lbl_SB.pack()

    # label formulario
    iniform = customtkinter.CTkLabel(master=ventana_Iniform,text="Selecciona tu formulario",font=("Arial",18),pady=15)
    iniform.pack()

    # Crear un frame para la tabla y el botón
    frame = Frame(bg="lightgrey")
    frame.pack(expand=YES, fill=BOTH)

    #Estilo para la tabla
    style = ttk.Style()
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 13)) # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 16,'bold')) # Modify the font of the headings
    style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

    # Crear un Treeview con 3 columnas
    treeview = ttk.Treeview(frame, columns=('clave', 'ap_pat', 'ap_mat', 'nombre', 'carrera', 'generacion'), show='headings',style="mystyle.Treeview")

    def open_formularios(event):

        seleccionar_formulario(treeview)

    treeview.bind("<Double-1>", lambda event: open_formularios(event))

    # Configurar encabezados de columna
    treeview.heading('clave', text='Clave')
    treeview.heading('ap_pat', text='Apellido Paterno')
    treeview.heading('ap_mat', text='Apellido Materno')
    treeview.heading('nombre', text='Nombre(s)')
    treeview.heading('carrera', text='Carrera')
    treeview.heading('generacion', text='Generación')

    treeview.column('clave', width=100)
    treeview.column('ap_pat', width=200)
    treeview.column('ap_mat', width=200)
    treeview.column('nombre', width=200)
    treeview.column('carrera', width=200)
    treeview.column('generacion', width=100)

    # Leer la lista de espera y preparar los datos para ser mostrados
    datos_listaEspera = lectura_listaEspera()
    if datos_listaEspera is not None and isinstance(datos_listaEspera, list):
        for elemento in datos_listaEspera:
            clave, nombre, ap_pat, ap_mat, carrera, generacion = elemento
            treeview.insert(parent='', index='end', values=(clave, ap_pat, ap_mat, nombre, carrera, generacion))
    else:
        # Manejar el caso en que datos_listaEspera es None o no es una lista
        print("datos_listaEspera no es una lista válida.")

    # Configurar el scrollbar
    scrollbar = Scrollbar(frame, orient=VERTICAL, command=treeview.yview)
    treeview.configure(yscroll=scrollbar.set)

    # Posicionar el Treeview y el Scrollbar en el frame
    treeview.pack(side=LEFT, expand=YES, fill=BOTH)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Agregar un botón para seleccionar el formulario
    btn_seleccionar_formulario = customtkinter.CTkButton(master=ventana_Iniform, text="Abrir Formulario", command=lambda: seleccionar_formulario(treeview), width=250, height=50 , corner_radius=20)
    btn_seleccionar_formulario.pack(pady=30)

    ventana_Iniform.mainloop()

# Iniciar la aplicación llamando a la función ventana_InicioForm
if __name__ == "__main__":
    ventana_InicioForm()
