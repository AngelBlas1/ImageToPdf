from fastapi import APIRouter, UploadFile

router = APIRouter()

@router.post("/upload/")
async def upload_file(
    file: UploadFile,
    name: str,
    email: str
): return {"filename": file.filename, "name": name, "email": email}