from pydantic import BaseModel

class UserModel(BaseModel):
    name: str
    email: str
    pdf_url: str
