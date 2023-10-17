from DBconection import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime
from reportlab.lib.units import inch

def GeneraCartaNoAdeudo(claveUnica):
    # Obtener fecha actual
    fecha_actual = datetime.now()
    
    # Crear conexión a la base de datos
    conexion = ConexionBD(user='root', password='root', host='localhost', database='datosalumnosbajas')
    conexion.conectar()

    # Realizar una solicitud SQL para obtener los datos
    consulta = f"SELECT * FROM formulario WHERE clave_unica = {claveUnica}"
    resultados = conexion.ejecutar_consulta(consulta)[0]
    
    # Realizar solicitud para obtener el coordinador de la carrera
    consulta2 = f"SELECT * FROM coordinadores WHERE Carrera = {resultados[7]}"
    coordinador = conexion.ejecutar_consulta(consulta2)
    print(coordinador)
    

    # Crear un archivo PDF en blanco
    pdf_filename = f"Carta_de_no_adeudo_{claveUnica}.pdf"
    pdf = canvas.Canvas(pdf_filename, pagesize=letter)

    # Definir posiciones y tamaños de fuente
    x_center = letter[0] / 2
    y_top = letter[1] - 1.25 * inch
    font_size_title = 14
    font_size_text = 12

   
    
    # Agregar la imagen en la parte superior derecha (segundo logotipo)
    pdf.drawInlineImage("LogoUniversidad.png", 30, letter[1] - 2.4 * inch, width=1.2 * inch, height=1.2 * inch)
    # Agregar la imagen en la parte superior derecha (segundo logotipo)
    pdf.drawInlineImage("IngenieriaLogo.png", letter[0] - 1.75 * inch, letter[1] - 2.2 * inch, width=1.0 * inch, height=1.0 * inch)

    # Agregar contenido estático
    pdf.setFont("Helvetica", font_size_title)
    pdf.drawCentredString(x_center, y_top, "Universidad Autónoma de San Luis Potosí")
    y_top -= 0.25 * inch
    pdf.drawCentredString(x_center, y_top, "Facultad de Ingeniería")
    y_top -= 0.50 * inch
    pdf.setFont("Helvetica-Bold", font_size_title)
    pdf.drawCentredString(x_center, y_top, "CARTA DE NO ADEUDO")
    y_top -= 1.0 * inch

    # Agregar texto dinámico
    pdf.setFont("Helvetica", font_size_text)
    pdf.drawRightString(letter[0] - 1.0 * inch, y_top, "SAN LUIS POTOSÍ S.L.P")
    y_top -= 0.75 * inch

    pdf.setFont("Helvetica", font_size_text)
    pdf.drawRightString(letter[0] - 3.5 * inch, y_top, f"Por este medio me permito manifestar que el alumno(a)")
    y_top -= 0.75 * inch

    pdf.setFont("Helvetica-Bold", font_size_text)
    pdf.drawCentredString(x_center, y_top, f"{resultados[2]} {resultados[3]} {resultados[4]}")
    y_top -= 0.75 * inch

    pdf.setFont("Helvetica", font_size_text)
    pdf.drawRightString(letter[0] - 1.2 * inch, y_top,
                        f"De la Carrera de Ingeniería en {resultados[7]} con clave única {resultados[1]} Gen. {resultados[8]}")
    y_top -= 0.25 * inch
    pdf.drawRightString(letter[0] - 3.25 * inch, y_top, f"no tiene adeudos a la fecha en los laboratorios de la carrera")
    y_top -= 0.5 * inch

    pdf.drawRightString(letter[0] - 1.35 * inch, y_top,
                        f"A petición del interesado y para fines que al mismo convengan se extiende la presente")
    y_top -= 0.25 * inch
    pdf.drawRightString(letter[0] - 3.75 * inch, y_top, f"a los veintinueve días del mes de {fecha_actual:%B de %Y}")

    # Parte de la firma
    y_top -= 2.0 * inch
    pdf.setFont("Helvetica", font_size_text)
    pdf.drawCentredString(x_center, y_top, "ATENTAMENTE")
    y_top -= 1.5 * inch
    pdf.line(x_center - 2 * inch, y_top, x_center + 2 * inch, y_top)
    y_top -= 0.35 * inch
    pdf.drawCentredString(x_center, y_top, f"Coordinador de la Carrera de Ingeniería en {resultados[7]}")
    y_top -= 0.25 * inch
    pdf.drawCentredString(x_center, y_top, f"Coordinador de la Carrera de Ingeniería en {resultados[7]}")

    # Guardar el archivo PDF generado
    pdf.save()

    # Cerrar la conexión a la base de datos
    conexion.desconectar()

GeneraCartaNoAdeudo(280108)
