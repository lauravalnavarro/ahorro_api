from pydantic import BaseModel


class IngresoIn(BaseModel):
    tipo: str
    valor: float
   

class IngresoOut(BaseModel):
    id_ingreso: int
    tipo: str
    valor: float

    class Config:
        orm_mode = True






