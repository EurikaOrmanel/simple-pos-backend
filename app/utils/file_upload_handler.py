from fastapi import UploadFile

from .media_name import MediaNameUtil
from fastapi import UploadFile
import aiofiles
from os import path
from pathlib import Path

class FileUploadHandler:
    @staticmethod
    async def save(file: UploadFile):
        result_file_name = MediaNameUtil.generate_name(file.content_type)
        result_path = f"public/images/{result_file_name}"
        file_home_path, filename = path.split(result_path)
        if not path.isdir(file_home_path):
            Path(file_home_path).mkdir(exist_ok=True, parents=True)

        open_write = await aiofiles.open(result_path, "wb")

        content = await file.read()
        await open_write.write(content)

        return result_file_name
