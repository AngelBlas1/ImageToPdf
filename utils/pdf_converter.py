from reportlab.pdfgen import canvas
from pathlib import Path

# Utilicé esta librería debido a que me guíe de un video para poder transformar la imagen en pdf
# además de que utilice una carpeta de nombre utils porque investigué que esa carpeta es para archivos que no pertenecen a las otras

def convert_image_to_pdf(image_path: str, pdf_path: str):
    """Convierte una imagen en un archivo PDF."""
    pdf_folder = Path(pdf_path).parent
    pdf_folder.mkdir(parents=True, exist_ok=True)
    
    imagePdf = canvas.Canvas(pdf_path)
    imagePdf.drawImage(image_path, 0, 0, width=500, height=700)
    imagePdf.save()
