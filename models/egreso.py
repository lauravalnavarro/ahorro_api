from datetime import date, datetime
from pydantic import BaseModel


class EgresoIn(BaseModel):
    tipo    : str
    valor : int
    fecha: date


class EgresoOut(BaseModel):
    id    : int
    tipo : str
    valor : int
    fecha: datetime
    actual_balance : int    

    class Config:
        orm_mode = True


