from pathlib import Path
from utils.pdf_converter import convert_image_to_pdf
from interfaces.storage_interface import StorageInterface
from repositories.firebase_repository import FirebaseRepository

UPLOAD_FOLDER = "uploads"
PDF_FOLDER = "pdfs"
Path(UPLOAD_FOLDER).mkdir(exist_ok=True)
Path(PDF_FOLDER).mkdir(exist_ok=True)

class ImageService:
    def __init__(self, storage_repo: StorageInterface = FirebaseRepository()):
        self.storage_repo = storage_repo 

    def process_image(self, file, name, email):
    
        file_location = f"{UPLOAD_FOLDER}/{file.filename}"
        with open(file_location, "wb") as buffer:
            buffer.write(file.file.read())
    
        pdf_path = f"{PDF_FOLDER}/{Path(file.filename).stem}.pdf"
        convert_image_to_pdf(file_location, pdf_path)
        
        pdf_path = f"{PDF_FOLDER}/{Path(file.filename).stem}.pdf"
        convert_image_to_pdf(file_location, pdf_path)
    
        pdf_url = self.storage_repo.upload_file(pdf_path, Path(file.filename).stem)
        self.storage_repo.save_user_data(name, email, pdf_url)
    
        return {"message": "Archivo subido y convertido con éxito", "pdf_url": pdf_url}
