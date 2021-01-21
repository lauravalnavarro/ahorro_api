from sqlalchemy import Column
from sqlalchemy import Integer, String, DateTime, ForeignKey
import datetime
from db.db_connection import Base, engine

class EgresoInDB(Base):
    __tablename__ = "egreso"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, ForeignKey("users.username"))
    tipo = Column(String)
    valor = Column(Integer)
    fecha = Column(DateTime, default=datetime.datetime.utcnow)
    actual_balance  = Column(Integer)
    
Base.metadata.create_all(bind=engine)