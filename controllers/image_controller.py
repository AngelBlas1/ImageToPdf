from fastapi import APIRouter, UploadFile
from services.image_service import ImageService

router = APIRouter()
image_service = ImageService()

@router.post("/upload/")
async def upload_file(
    file: UploadFile,
    name: str,
    email: str
): return image_service.process_image(file, name, email)