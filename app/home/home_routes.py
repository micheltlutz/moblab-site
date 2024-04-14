import os

from dotenv import load_dotenv
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, HTMLResponse

from app.site_renderer.renderer import SiteRenderer
from app.home.page_home import PageHome
from app.home.page_ulink import PageUlink
from app.home.page_login import PageLogin

load_dotenv()
router = APIRouter()


@router.get('/', response_class=HTMLResponse)
def home():
    renderer = SiteRenderer()  # Instancia o renderer
    html_content = PageUlink()
    renderer.add_element(html_content)  # Adiciona o HTML gerado ao renderer
    return renderer.generate()  # Retorna o HTML como string


@router.get('/ulink', response_class=HTMLResponse)
def home():
    renderer = SiteRenderer()  # Instancia o renderer
    html_content = PageUlink()
    renderer.add_element(html_content)  # Adiciona o HTML gerado ao renderer
    return renderer.generate()  # Retorna o HTML como string

@router.get("/health-check")
def health_check():
    return JSONResponse(
        content={"status": "ok"},
        status_code=status.HTTP_200_OK
    )


@router.get("/version")
def health_check():
    return JSONResponse(
        content={"version": os.getenv("VERSION")},
        status_code=status.HTTP_200_OK
    )

@router.get("/login", response_class=HTMLResponse)
def health_check():
    renderer = SiteRenderer()  # Instancia o renderer
    html_content = PageLogin()
    renderer.add_element(html_content)  # Adiciona o HTML gerado ao renderer
    return renderer.generate()  # Retorna o HTML como string

@router.get("/logged", response_class=HTMLResponse)
def health_check():
    renderer = SiteRenderer()  # Instancia o renderer
    html_content = PageHome()
    renderer.add_element(html_content)  # Adiciona o HTML gerado ao renderer
    return renderer.generate()  # Retorna o HTML como string