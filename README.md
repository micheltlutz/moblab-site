# Mob Lab

This project is intended to be educational to test web and mobile resources. Feel free to collaborate with the project.

The project uses a library I wrote in Python to generate HTML called [Winged-Python](https://github.com/micheltlutz/Winged-Python).

### Other Links:

- [MobLab - iOS](https://github.com/micheltlutz/moblab-site)
- [Universal Links post EN-US](https://github.com/micheltlutz/moblab-site)
- [Universal Links post PT-BR](https://github.com/micheltlutz/moblab-site)
- [Author Links](https://linktr.ee/micheltlutz)


## Configuração do Ambiente Virtual

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


## Deploy

```bash
fly deploy
```