from DBconection import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from PyPDF2 import PdfFileWriter, PdfFileReader
from datetime import date
from tkinter import filedialog
from pathlib import Path
from tkinter import *

#Función auxiliar para la creación de la carta de no adeudo
def GeneraCarta(claveUnica):
    claveUnica =  claveUnica
    #Crear conexion a la base de datos
    conexion = ConexionBD(user='root',password='root',host='localhost',database='datosalumnosbajas')
    conexion.conectar()

    # Realizar una solicitud SQL para obtener los datos
    consulta = f"SELECT * FROM formulario WHERE clave_unica = {claveUnica}"
    resultados = conexion.ejecutar_consulta(consulta)
    print(resultados[0])
    
    # Crear un archivo PDF en blanco
    pdf = canvas.Canvas(f"{claveUnica}.pdf", pagesize=letter)

    # Agregar la imagen en la parte superior izquierda
    pdf.drawInlineImage("LogoUniversidad.png", 30, letter[1]-2*inch, width=1.5*inch, height=1.5*inch)

    # Agregar el texto en la parte superior central
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawCentredString(letter[0]/2, letter[1]-0.75*inch, "Universidad Autonoma de San Luis Potosi")
    pdf.drawCentredString(letter[0]/2, letter[1]-1*inch, "Facultad de Ingenieria")
    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(letter[0]/2, letter[1]-1.25*inch, "Area de ciencias de la computacion")
    pdf.drawCentredString(letter[0]/2, letter[1]-1.5*inch, "CARTA DE NO ADEUDO")

    # Agregar la imagen en la parte superior derecha
    pdf.drawInlineImage("IngenieriaLogo.png", letter[0]-1.75*inch, letter[1]-1.75*inch, width=1.25*inch, height=1.25*inch)

    # Agregar la fecha
    pdf.setFont("Helvetica", 12)
    fecha_actual = date.today().strftime("San Luis Potosi, SLP a día:  %d  de   %B  de   %Y")
    
    pdf.drawRightString(letter[0]-0.5*inch, letter[1]-2.5*inch, fecha_actual)

    # Agregar la info basica del alumno
    dif = 200
    pdf.drawString(letter[0]/2 - dif, letter[1]-3*inch, f"Se hace constar que el alumno (a) {resultados[0][2]} {resultados[0][3]} {resultados[0][4]} ")
    pdf.drawString(letter[0]/2 - dif, letter[1]-3.25*inch, f"con clave unica   {resultados[0][1]}    generacion   {resultados[0][8]}   se encuentra en la carrera de")
    pdf.drawString(letter[0]/2 - dif, letter[1]-3.5*inch, f"Ingenieria en  {resultados[0][7]}  y no tiene adeudos pendientes, presentamos a su")
    pdf.drawString(letter[0]/2 - dif, letter[1]-3.75*inch, f"nombre o algun asunto a tratar dentro de los laboratorios o con profesores.")

    # Agregar espacio para sello

    # Dibujamos el rectángulo 1
    pdf.drawString((letter[0]/2-100), letter[1]-5.5*inch, "LRT")
    pdf.rect(letter[0]/2-200, letter[1]-5.5*inch, 200, 100)

    # Dibujamos el rectángulo 2
    pdf.drawString((letter[0]/2+75), letter[1]-5.5*inch, "LESD")
    pdf.rect(letter[0]/2, letter[1]-5.5*inch, 200, 100)

    # Dibujamos texto debajo de los rectangulos
    pdf.drawCentredString(letter[0]/2, letter[1]-5.75*inch, "Aval del jefe de laboratorio: nombre, firma y sello.")

    # Parte de datos adicionales
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawCentredString(letter[0]/2, letter[1]-6.25*inch, "Datos adicionales")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(letter[0]/2-dif, letter[1]-6.5*inch, f"Correo electronico:                   {resultados[0][5]}")

    # Comprobar si alguna materia dificil se dejo en blanco
    if resultados[0][12] is not None:
        materia1 = resultados[0][12]
    else:
        materia1 = ""
    if resultados[0][13] is not None:
        materia2 = resultados[0][13] 
    else:
        materia2 = ""
    if resultados[0][14] is not None:
        materia3 = resultados[0][14]
    else:
        materia3 = ""
    pdf.drawString(letter[0]/2-dif, letter[1]-6.75*inch, f"Materia(s) mas dificil(es):         {materia1}")

    pdf.drawString(letter[0]/2-dif, letter[1]-7*inch,    f"Preparatoria de origen:             {resultados[0][11]}")

    pdf.drawString(letter[0]/2-dif, letter[1]-7.25*inch, f"Motivo real de la baja:              {resultados[0][10]}")

    pdf.drawString(letter[0]/2-dif, letter[1]-7.5*inch,  f"Inconveniente de carrera:         {resultados[0][17]}")

    # Revisar si hay empresa
    if resultados[0][18] is not None:
        empresa= resultados[0][18]
    else:
        empresa = "No aplica"
    pdf.drawString(letter[0]/2-dif, letter[1]-7.75*inch,  f"Si trabaja, cual es la empresa:  {empresa}")

    # Comprobar si hay forma de titulacion
    if resultados[0][15] is not None:
        ftitulacion = resultados[0][15]
    else: 
        ftitulacion = "No aplica"
    pdf.drawString(letter[0]/2-dif, letter[1]-8*inch,  f"Forma de titulacion:                   {ftitulacion}")

    # Comprobar si es egel
    if resultados[0][15] == "EGEL":
        esEgel = "S"
        fechaEgel = resultados[0][16] if esEgel == "S" else None
    else:
        esEgel = "N"
        fechaEgel = "No aplica"


    pdf.drawString(letter[0]/2-dif, letter[1]-8.25*inch,  f"Si es EGEL(S/N):  {esEgel}       Fecha de presentacion de examen: {fechaEgel} ")

    pdf.drawString(letter[0]/2-dif, letter[1]-8.75*inch,  f"Atendiendo la solicitud de la presente por el motivo de:")

    pdf.drawString(letter[0]/2-dif, letter[1]-9*inch,  f"X Baja {resultados[0][9]}")

    pdf.drawString(letter[0]/2-dif, letter[1]-9.25*inch,  f"Para cualquier otro tramite que el alumno disponga, se da fe de el(la) solicitante")
    pdf.drawString(letter[0]/2-dif, letter[1]-9.5*inch,  f"esta aucente de las responsabilidades con los laboratorios del presente documento")

    # Parte de la firma
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawCentredString(letter[0]/2, letter[1]-10*inch, "ATENTAMENTE")
    pdf.drawCentredString(letter[0]/2, letter[1]-10.5*inch, "__________________________________________")
    pdf.drawCentredString(letter[0]/2, letter[1]-10.75*inch, "Nombre y firma del coordinador de carrera")

    pdf.save()
    # Cerrar la conexión a la base de datos
    conexion.desconectar()