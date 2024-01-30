# Database models for images
# from sqlalchemy.orm import  Mapped, mapped_column, relationship
# from src.models import Style, Base

# class Image(Base):
#     __tablename__ = "images"

#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     image_key: Mapped[str]
#     style: Mapped[Style]
#     movie_id: Mapped[Movie] = relationship(
#         secondary=movie_image_association, back_populates="image_id"
#     )