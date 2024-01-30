from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# TODO - pasar a variable de entorno
# Esto es la url de la base de datos trabajando con postgres localmente
# base de datos :// user : contraseña @ host : puerto / nombre de la base de datos
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost:5432/movietronics"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
