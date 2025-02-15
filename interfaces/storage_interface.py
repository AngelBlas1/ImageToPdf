from abc import ABC, abstractmethod

class StorageInterface(ABC):
    @abstractmethod
    def upload_file(self, file_path: str, file_name: str) -> str:
        pass

    @abstractmethod
    def save_user_data(self, name: str, email: str, pdf_url: str):
        pass
