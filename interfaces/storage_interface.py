from abc import ABC, abstractmethod

# Me guíe de un video para realizar las clase en cuestión de utilizar la librería ABC y abstractmethod
# debido a que explica que con esta librería nos ayudará a que cada almacenamiento deberá implementar estas funciones
# y la librería ABC permite que sea una clase abstracta

class StorageInterface(ABC):
    @abstractmethod
    def upload_file(self, file_path: str, file_name: str) -> str:
        pass

    @abstractmethod
    def save_user_data(self, name: str, email: str, pdf_url: str):
        pass
