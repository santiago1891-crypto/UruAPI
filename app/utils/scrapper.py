import httpx
from bs4 import BeautifulSoup

from app.threading import run_in_thread

async def get_page_html(endpoint :  str, client : httpx.AsyncClient):
    page = await client.get(url=f"https://datosuruguay.com/{endpoint}")
    html = page.text
    return html

def _get_span_element(html: str, element_class: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    element = soup.find("span", class_=element_class)
    value = element.get_text(strip=True)
    return value


async def get_span_element(html: str, element_class: str) -> str:
    return await run_in_thread(_get_span_element, html, element_class)


def _get_div_element(html: str, element_class: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    element = soup.find("div", class_=element_class)
    value = element.get_text(strip=True)
    return value

async def get_div_element(html: str, element_class: str) -> str:
    return await run_in_thread(_get_div_element, html, element_class)
