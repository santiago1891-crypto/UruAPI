from fastapi import APIRouter

from app.schemas.utils import GetHTMLSchema
from app.utils import get_page_html, HttpxClientDep

utils_router = APIRouter()

@utils_router.post("/get-page-html")
async def get_page_html_with_endpoint(html : GetHTMLSchema, client : HttpxClientDep):
    page_html = await get_page_html(html.endpoint, client)
    return page_html