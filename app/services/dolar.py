from app.utils import get_page_html, get_span_element
import httpx

async def get_dolar_service(client : httpx.AsyncClient):
    html = await get_page_html("dolar", client)
    dolar_value = await get_span_element(html, "font-semibold text-green-600")
    return dolar_value