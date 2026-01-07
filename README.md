# Containerized URL Shortener

<p align="center">
    <img src="./.github/shortener.png" alt="Image Example" width="400px">
</p>

This project is a **URL shortener** that uses Docker to run all parts of the application simultaneously in separate containers using Docker Compose.

## Technologies Used
![icone](https://img.icons8.com/?size=30&id=cdYUlRaag9G9&format=png&color=000000)
![icone](https://img.icons8.com/?size=30&id=t2x6DtCn5Zzx&format=png&color=000000)
![icone](https://img.icons8.com/?size=30&id=8rKdRqZFLurS&format=png&color=000000)
![icone](https://img.icons8.com/?size=30&id=108784&format=png&color=000000)
![icone](data:image/svg+xml;utf8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill%3D%22none%22%20viewBox%3D%220%200%2030%2030%22%20id%3D%22Fastapi-Icon--Streamline-Svg-Logos%22%20height%3D%2230%22%20width%3D%2230%22%3E%0A%20%20%3Cdesc%3E%0A%20%20%20%20Fastapi%20Icon%20Streamline%20Icon%3A%20https%3A%2F%2Fstreamlinehq.com%0A%20%20%3C%2Fdesc%3E%0A%20%20%3Cpath%20fill%3D%22%23009688%22%20d%3D%22M15.000031250000001%200.3125C6.890968750000001%200.3125%200.3125%206.890968750000001%200.3125%2015s6.578468750000001%2014.6875%2014.687531250000001%2014.6875C23.109031249999997%2029.6875%2029.6875%2023.109031249999997%2029.6875%2015S23.109031249999997%200.3125%2015.000031250000001%200.3125Zm-0.7653125%2026.461031249999998V17.56075H9.11325l7.3584375%20-14.33428125v9.212781249999999H21.401875L14.234718749999999%2026.773531249999998Z%22%20stroke-width%3D%220.3125%22%3E%3C%2Fpath%3E%0A%3C%2Fsvg%3E)

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed 

## 1. Cloning
```bash
git clone https://github.com/seuusuario/seuprojeto.git
```
## 2. Running with Docker Compose
Navigate into the repository:
```bash
cd containerized_url_shortener
```
Build the images:
```bash
docker compose build
```
Start the containers:
```bash
docker compose up -d
```
## 3. Access
You can now access the created containers through the following addresses:

**URL Shortener Frontend**
> http://localhost:80/ 

**Backend Server**
> http://localhost:8000/docs or http://localhost:80/shorten

**MongoDB Database**
> mongodb://mongodb:27017/shortener

## Additional Documentation

[NGINX SERVER FRONTEND](./shortener_frontend_nginx/README.md)

[FASTAPI SERVER BACKEND](shortener_backend/README.md)
