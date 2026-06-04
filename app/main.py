from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.routers import utils_router

app = FastAPI()

app.include_router(router=utils_router, prefix="/utils")

@app.get("/")
def root():
    return RedirectResponse("/docs")