import httpx
from typing import Annotated
from fastapi import Depends

async def get_httpx_client():
    async with httpx.AsyncClient(
        headers={"User-Agent": "Mozilla/5.0 ..."},
        timeout=httpx.Timeout(10.0, connect=5.0),
        follow_redirects=True,
        limits=httpx.Limits(max_connections=10, max_keepalive_connections=5)) as client:
        
        yield client

HttpxClientDep = Annotated[httpx.AsyncClient, Depends(get_httpx_client)]