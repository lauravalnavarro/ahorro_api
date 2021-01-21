from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session


from db.db_connection import get_db

from db.user_db         import UserInDB
from db.egreso_db         import EgresoInDB
from db.ingreso_db  import IngresoInDB

from models.user         import UserIn, UserOut
from models.ingreso  import IngresoIn, IngresoOut
from models.egreso  import EgresoIn, EgresoOut



router = APIRouter()



@router.put("/user/egreso/", response_model=EgresoOut)
async def make_egreso(egreso_in: EgresoIn, db: Session = Depends(get_db)):
    

    egreso_in_db = EgresoInDB(**egreso_in.dict(), actual_balance = 100)
    db.add(egreso_in_db)
    db.commit()
    db.refresh(egreso_in_db)

    return  egreso_in_db

