from fastapi import APIRouter

from app.services.boleto import get_boleto_service
from app.utils import HttpxClientDep

boleto_router = APIRouter()


@boleto_router.get("/")
async def get_boleto(client: HttpxClientDep):
    return await get_boleto_service(client)
