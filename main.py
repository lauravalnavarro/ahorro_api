from fastapi import Depends, FastAPI

from routers.user_router   import router as router_users
from routers.egreso_router   import router as router_egresos  
from routers.ingreso_router import router as router_ingresos


api = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost", 
    "http://localhost:8080",
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

api.include_router(router_users)
api.include_router(router_egresos)
api.include_router(router_ingresos)

