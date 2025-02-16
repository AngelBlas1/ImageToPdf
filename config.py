from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class databaseCredential:
    FIREBASE_CREDENTIALS = "archivo.json" #es el archivo que te da el proyecto en firestore
    FIREBASE_STORAGE_BUCKET = "img-to-ps.firebasestorage.app"

