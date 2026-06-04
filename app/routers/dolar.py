from fastapi import APIRouter

from app.services.dolar import get_dolar_service
from app.utils import HttpxClientDep

dolar_router = APIRouter()

@dolar_router.get("/")
async def get_dolar(client :  HttpxClientDep):
    dolar_value = await get_dolar_service(client)
    return {"dolar" : dolar_value}