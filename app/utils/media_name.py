from uuid import uuid4


class MediaNameUtil:
    @staticmethod
    def extension_from_content_type(content_type: str):
        content_type_mapping = {
            "image/jpeg": "jpeg",
            "image/jpg": "jpg",
            "image/png": "png",
            "image/gif": "gif",
            "image/webp": "webp",
            "video/mp4": "mp4",
            "video/mpeg": "mpeg",
            "video/3gpp": "3gp",
        }
        return content_type_mapping.get(content_type)

    @staticmethod
    def ext_to_content_type(extension: str):
        ext_type_mapping = {
            "jpg": "image/jpeg",
            "png": "image/png",
            "gif": "image/gif",
            "webp": "image/webp",
            "mp4": "video/mp4",
            "mpeg": "video/mpeg",
            "3gp": "video/3gpp",
        }

        return ext_type_mapping.get(extension)

    @staticmethod
    def generate_name(content_type: str):
        img_extension = MediaNameUtil.extension_from_content_type(content_type)
        return f"{uuid4()}.{img_extension}"
