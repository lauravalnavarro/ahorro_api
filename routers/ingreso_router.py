from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import update

from db.db_connection import get_db

from db.egreso_db        import EgresoInDB
from db.ingreso_db  import IngresoInDB

from models.egreso         import EgresoIn, EgresoOut
from models.ingreso  import IngresoIn, IngresoOut


router = APIRouter()


@router.put("/user/ingreso/", response_model=IngresoOut)
async def make_ingreso(ingreso_in: IngresoIn, db: Session = Depends(get_db)):
   
  
    ingreso_in_db = IngresoInDB(**ingreso_in.dict())
  
    
    db.add(ingreso_in_db)
    db.commit()
    db.refresh(ingreso_in_db)
     


    return  ingreso_in_db



