# Global models
from enum import Enum as PyEnum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Table, Column, ForeignKey, DateTime
from datetime import datetime


class Style(str, PyEnum):
    futuristic = "futuristic"
    semirealistic = "semirealistic"
    realistic = "realistic"
    anime = "anime"
    kids = "kids"
    oil_painting = "oil-painting"
    vintage = "vintage"


class Base(DeclarativeBase):
    pass


movie_image_association = Table(
    "movies_images",
    Base.metadata,
    Column("movie_id", ForeignKey("movies.id"), primary_key=True),
    Column("image_id", ForeignKey("images.id"), primary_key=True),
)


class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    style: Mapped[Style]
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    modify_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    movie_key: Mapped[str]
    image_id: Mapped["Image"] = relationship(
        secondary=movie_image_association, back_populates="movie_id"
    )


class Image(Base):
    __tablename__ = "images"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    image_key: Mapped[str]
    style: Mapped[Style]
    movie_id: Mapped["Movie"] = relationship(
        secondary=movie_image_association, back_populates="image_id"
    )
