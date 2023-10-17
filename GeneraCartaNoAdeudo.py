from DBconection import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from PyPDF2 import PdfFileWriter, PdfFileReader
from datetime import date
import datetime
import locale

def GeneraCartaNoAdeudo(claveUnica):

    #obtener fecha actual
    
    fecha_actual=datetime.datetime.now()
    
    
    
    claveUnica =  claveUnica
    #Crear conexion a la base de datos
    conexion = ConexionBD(user='root',password='root',host='localhost',database='datosalumnosbajas')
    conexion.conectar()

    # Realizar una solicitud SQL para obtener los datos
    consulta = f"SELECT * FROM formulario WHERE clave_unica = {claveUnica}"
    resultados = conexion.ejecutar_consulta(consulta)
    #print(resultados[0])
    
    #Consulta de coordinador
    carrera= resultados[0][7]
    consulta = f"SELECT nom_coordinador FROM coordinadores WHERE Carrera = {carrera}"
    coordiandor = conexion.ejecutar_consulta(consulta)
    print(coordiandor)

    # Crear un archivo PDF en blanco
    pdf = canvas.Canvas(f"Carta de no adeudo {claveUnica}.pdf", pagesize=letter)

    # Agregar la imagen en la parte superior izquierda
    pdf.drawInlineImage("LogoUniversidad.png", 30, letter[1]-2.4*inch, width=1.2*inch, height=1.2*inch)

    # Agregar el texto en la parte superior central
    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(letter[0]/2, letter[1]-1.25*inch, "Universidad Autonoma de San Luis Potosí")
    pdf.drawCentredString(letter[0]/2, letter[1]-1.5*inch, "Facultad de Ingeniería")
    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(letter[0]/2, letter[1]-1.75*inch, "Area de ciencias de la computacion")
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawCentredString(letter[0]/2, letter[1]-2*inch, "CARTA DE NO ADEUDO")

    # Agregar la imagen en la parte superior derecha
    pdf.drawInlineImage("IngenieriaLogo.png", letter[0]-1.75*inch, letter[1]-2.2*inch, width=1.0*inch, height=1.0*inch)


    # Agregar ciudad
    pdf.setFont("Helvetica", 12)
    pdf.drawRightString(letter[0]-1.0*inch, letter[1]-3.0*inch, "SAN LUIS POTOSÍ S.L.P")
    
    #texto "a quien corresponda"
    pdf.drawRightString(letter[0]-5.5*inch, letter[1]-3.5*inch, "A QUIEN CORRESPONDA")
    
    #texto siguiente
    pdf.drawRightString(letter[0]-3.44*inch, letter[1]-4.0*inch, "Por este medio me permito manifestar que el alumno(a)")
    
    #nombre del alumno(a)
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawCentredString(letter[0]/2, letter[1]-4.5*inch, f"{resultados[0][2]} {resultados[0][3]} {resultados[0][4]}")
    
    #texto siguiente
    pdf.setFont("Helvetica", 12)
    pdf.drawRightString(letter[0]-1.2*inch, letter[1]-5.0*inch, f"De la Carrera de Ingeniería en {resultados[0][7]} con clave única {resultados[0][1]} Gen. {resultados[0][8]}")
    pdf.drawRightString(letter[0]-3.25*inch, letter[1]-5.25*inch, f"no tiene adeudos a la fecha en los laboratorios de la carrera")
    
    #espacio 
    pdf.drawRightString(letter[0]-1.24*inch, letter[1]-5.6*inch, f"A peticion del interesado y para fines que al mismo congengan se extiende la presente")
    pdf.drawRightString(letter[0]-5.15*inch, letter[1]-5.85*inch, f"a los veintinueve dias del mes de {fecha_actual}")




    
    # Parte de la firma
    pdf.setFont("Helvetica", 12)
    pdf.drawCentredString(letter[0]/2, letter[1]-7.75*inch, "ATENTAMENTE")
    pdf.drawCentredString(letter[0]/2, letter[1]-9.25*inch, "__________________________________________")
    
    pdf.drawCentredString(letter[0]/2, letter[1]-9.75*inch, f"Coordinador de la Carrera de Ingeniería en {resultados[0][7]}")


    # Guardar el archivo PDF generado
    pdf.save()

    # Cerrar la conexión a la base de datos
    conexion.desconectar()


#GeneraCartaNoAdeudo(280109)