from fastapi import FastAPI
from controllers.image_controller import router

app = FastAPI()

# Registrar controladores
app.include_router(router, prefix="/api")

@app.get("/")
def home():
    return {"message": "API funcionando correctamente"}