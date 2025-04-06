from app.utils.file_upload_handler import FileUploadHandler
from fastapi import File, UploadFile


class ImagesController:
    @staticmethod
    def resize(
        width: int,
        height: int,
    ):
        pass

    @staticmethod
    async def upload(file: UploadFile):
        result_name = await FileUploadHandler.save(file)
        return {"image": result_name}
