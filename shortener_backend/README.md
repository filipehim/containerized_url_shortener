# URL Shortener API
This is the backend server of the [Containerized URL Shortener Project](../README.md), built using the FastAPI framework.

## Requirements

- [Docker](https://docs.docker.com/get-docker/) (recommended for running the project)
- [Poetry](https://python-poetry.org/) (if running locally without Docker)
- [MongoDB](https://www.mongodb.com/) instance running (local or cloud, e.g. MongoDB Atlas)

## Running the API

### Option 1: With Docker

1. Build the image:
   ```bash
   docker build -t url-shortener-api .
2. Run the container:
    ```bash
    docker run -d -p 8000:8000 --name url-api url-shortener-api
    ```
---
### Option 2: Local development with Poetry
For this option, it is assumed that you already have Python and Poetry installed on your machine.

1. If you are at the root of the project, move to the following folder:
    ```bash
    cd shortener_backend
2. Install dependencies:
    ```bash
    poetry install
3. Add environment variables in a .env file:
    ```bash
    MONGO_URL=mongodb://mongodb:27017/shortener
4. Run the server:
    ```bash
    poetry run uvicorn src.shortener_backend.main:app --reload
    ```
## Access the API:
After running the project using one of the methods above, you can access the API at:

> API http://localhost:8000

> Swagger docs: http://localhost:8000/docs

> Redoc docs: http://localhost:8000/redoc

## Api Routes

| route                | description                                          
|----------------------|-----------------------------------------------------
| <kbd>/shortener</kbd>   | Route to send a long URL
| <kbd>/{shorte_code}</kbd>| Route that receives the shortcode and redirects to the original URL
