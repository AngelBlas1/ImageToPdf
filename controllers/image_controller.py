from fastapi import APIRouter, UploadFile
from services.image_service import ImageService
from repositories.firebase_repository import FirebaseRepository

router = APIRouter()
image_service = ImageService(FirebaseRepository())

@router.post("/upload/")
async def upload_file(
    file: UploadFile,
    name: str,
    email: str
): return image_service.process_image(file, name, email)