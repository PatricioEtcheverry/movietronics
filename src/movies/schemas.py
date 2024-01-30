# Pydantic models for movies

from pydantic import BaseModel
from src.models import Style
from datetime import datetime
from typing import List
from src.images.schemas import Image


class MovieBase(BaseModel):
    title: str
    style: Style
    created_at: datetime
    modify_at: datetime
    movie_key: str
    images: List[Image] = []


class MovieCreate(MovieBase):
    pass


class MovieUpdate(MovieBase):
    title: str | None = None
    style: Style | None = None
    created_at: datetime | None = None
    modify_at: datetime | None = datetime.utcnow()
    movie_key: str | None = None
    images: List[Image] | None = None


class Movie(MovieBase):
    id: int

    class Config:
        from_attributes = True
