import os

from dotenv import load_dotenv
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.exceptions import HTTPException

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

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


def _load_private_key(file_path: str) -> serialization.load_pem_private_key:
    try:
        with open(file_path, 'rb') as f:
            private_key_bytes = f.read()

        private_key = serialization.load_pem_private_key(
            private_key_bytes,
            password=None,
            backend=default_backend()
        )
        return private_key
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao carregar a chave privada")


@router.post("/logged", response_class=HTMLResponse)
async def logged_check():
    try:
        private_key = _load_private_key('app/authfiles/AuthKey_92M35KR4BV.p8')
        # Aqui você usaria a chave privada para assinar a solicitação JWT
        # Por exemplo:
        # signed_token = sign_with_private_key(private_key, payload)
        # O payload seria a carga útil que você deseja incluir no token JWT
        print("PKEY")
        print(private_key)

        # Retorne o token assinado ou outra resposta conforme necessário
        # return {"message": "JWT signed successfully"}
        renderer = SiteRenderer()  # Instancia o renderer
        html_content = PageHome()
        renderer.add_element(html_content)  # Adiciona o HTML gerado ao renderer
        return renderer.generate()  # Retorna o HTML como string
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"message": e.detail})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})

    