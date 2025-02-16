import firebase_admin
from firebase_admin import credentials, storage, firestore
from config import databaseCredential
from interfaces.storage_interface import StorageInterface

# Inicializar Firebase con credenciales desde config.py para evitar el uso de informacion sensible en el código

cred = credentials.Certificate(databaseCredential.FIREBASE_CREDENTIALS)
firebase_admin.initialize_app(cred, {
    "storageBucket": databaseCredential.FIREBASE_STORAGE_BUCKET
})

db = firestore.client()
storage_bucket = storage.bucket()

class FirebaseRepository(StorageInterface):
    def upload_file(self, file_path: str, file_name: str) -> str:
        
        pdfFirestore = storage_bucket.blob(f"pdfs/{file_name}.pdf")
        pdfFirestore.upload_from_filename(file_path)
        
        return pdfFirestore.public_url

    def save_user_data(self, name: str, email: str, pdf_url: str):
        
        user_data = {"name": name, "email": email, "pdf_url": pdf_url}
        
        db.collection("users").add(user_data)