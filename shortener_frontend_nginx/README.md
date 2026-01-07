# Nginx Server - URL Shortener Project 

This is the **frontend server** for the [Containerized URL Shortener](../README.md). It uses [Nginx](https://nginx.org/) to serve static files (HTML, CSS, JS), custom error pages, and acts as a **reverse proxy** to the FastAPI backend.

## Requirements

- [Docker](https://docs.docker.com/get-docker/) installed  
- Optional: [Docker Compose](https://docs.docker.com/compose/) for orchestration with the backend

## Running the Nginx Server

1. Build the image:
   ```bash
   docker build -t url-shortener-nginx .
2. Run the container:
    ```bash
    docker run -d -p 80:80 --name url-nginx url-shortener-nginx
3. Access the frontend:
    > http://localhost

## Rotas do Servidor Nginx
| route                | description                                          
|----------------------|-----------------------------------------------------
| <kbd>/</kbd>   | Route to access the main page where the user submits a URL
| <kbd>/shorten</kbd>    | Route that proxies requests to the backend API
