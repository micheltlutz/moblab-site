# Mob Lab

## Configuração do Ambiente Virtual

O Poetry cria e gerencia automaticamente um ambiente virtual para o seu projeto. Para ativá-lo, você pode simplesmente usar:

```bash
poetry shell
```

## Adicionando Dependências

Para adicionar dependências ao seu projeto, use o comando:

```bash
poetry add <nome_da_dependência>
```

## Adicionando Scripts

No pyproject.toml, você também pode adicionar scripts para facilitar a execução de comandos comuns. Por exemplo:

```toml
[tool.poetry.scripts]
start = "seu_modulo:main"
```

Depois, você pode iniciar o projeto com:

```bash
poetry run start
```

## Usando venv



```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

### Instalando dependências

```bash
pip install --upgrade pip && pip install -r requirements.txt
```

### Rodando o projeto

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## 1. Create Image

```bash
docker build -t "moblab" .
```

### 2. Check if image was created

```bash
docker images
```
## 3. Run container

```bash
docker run -d --name moblab -p 8000:8000 moblab:latest
```

## 4. Check if container is running

```bash
docker ps
```

## 5. Access the API

- [http://localhost:8000](http://localhost:8000)

## Stop container

When you need to stop the container, run the code below in your terminal

```bash
docker stop moblab
```

## Api Documentation information

The project documentation uses swagger, you can access it after running the docker container and accessing the address below in the browser, where you will find the routes, parameters and schemes of each of the routes created for your challenge, in addition to being able to execute the routes directly in the documentation.

- [http://localhost:8000/docs](http://localhost:8000/docs)
