from sqlalchemy import Column 
from sqlalchemy import Integer, String, DateTime

from db.db_connection import Base, engine


class IngresoInDB(Base):
    __tablename__ = "ingreso"

    id = Column(Integer, primary_key=True, unique=True)
    tipo = Column(String)
    valor = Column(Integer)
        
    Base.metadata.create_all(bind=engine)




