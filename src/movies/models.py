# Databse models for movies
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from src.models import Style, Base
# from sqlalchemy import DateTime
# from datetime import datetime


# class Movie(Base):
#     __tablename__ = "movies"

#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     title: Mapped[str]
#     style: Mapped[Style]
#     created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
#     modify_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
#     movie_key: Mapped[str]
#     image_id: Mapped[Image] = relationship(
#         secondary=movie_image_association, back_populates="movie_id"
#     )
