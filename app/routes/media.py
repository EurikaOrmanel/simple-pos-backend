import io
import os
import aiofiles
from fastapi import APIRouter, File
from fastapi.responses import StreamingResponse


media_router = APIRouter(prefix="/media")

@media_router.get("/image/{filename}")
async def file_name(filename: str):
    image_file = os.path.join("public/images", filename)
    if os.path.isfile(image_file):
        file_byte = await aiofiles.open(image_file, "rb")
        return StreamingResponse(
            io.BytesIO(
                await file_byte.read(),
            ),
            media_type="image/png",
        )
