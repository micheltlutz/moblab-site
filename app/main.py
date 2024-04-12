import logging
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

# Importing routes
from app.home import home_routes

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(os.getenv("LOGGER_FILE")),  # Salvar logs em um arquivo
        logging.StreamHandler()  # Imprimir logs no console
    ]
)

app = FastAPI()

# Configuração para servir arquivos estáticos
app.mount("/static", StaticFiles(directory="app/assets"), name="static")
app.mount("/.well-known", StaticFiles(directory="app/well-known"), name=".well-known")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows any origin. Don't do this in production!
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],
)

# Middleware para registrar todas as requisições
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger = logging.getLogger(os.getenv("LOGGER_NAME"))
    response = await call_next(request)
    logger.info(f"{request.method} {request.url.path} - {response.status_code}")
    return response

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger = logging.getLogger(os.getenv("LOGGER_NAME"))
    logger.error(f"Erro de validação para: {request.method} {request.url} - {exc.errors()}")
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
    )

@app.on_event("startup")
async def startup_event():
    # init_db()
    pass

app.include_router(home_routes.router, tags=["home"])