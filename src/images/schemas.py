# Pydantic models for images
from pydantic import BaseModel
from src.models import Style


class ImageBase(BaseModel):
    image_key: str
    style: Style


class ImageCreate(ImageBase):
    pass


class ImageUpdate(ImageBase):
    image_key: str | None = None
    style: Style | None = None


class Image(ImageBase):
    id: int

    class Config:
        from_attributes = True

