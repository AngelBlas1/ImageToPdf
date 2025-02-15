from pathlib import Path
from utils.pdf_converter import convert_image_to_pdf

UPLOAD_FOLDER = "uploads"
PDF_FOLDER = "pdfs"
Path(UPLOAD_FOLDER).mkdir(exist_ok=True)
Path(PDF_FOLDER).mkdir(exist_ok=True)

class ImageService:

    def process_image(self, file, name, email):
    
        file_location = f"{UPLOAD_FOLDER}/{file.filename}"
        with open(file_location, "wb") as buffer:
            buffer.write(file.file.read())
    
        pdf_path = f"{PDF_FOLDER}/{Path(file.filename).stem}.pdf"
        convert_image_to_pdf(file_location, pdf_path)
