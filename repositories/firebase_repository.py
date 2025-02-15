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