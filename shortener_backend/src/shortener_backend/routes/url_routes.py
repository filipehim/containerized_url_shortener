from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
# from sqlalchemy.orm import Session
from src.shortener_backend.functions import generate_short_code
from src.shortener_backend.model.url_model import db
from src.shortener_backend.schemas.url_schema import URLRequest

router_url = APIRouter()

@router_url.post("/shorten")
async def post_url(request: URLRequest):
    short_code = generate_short_code()
    await db['url'].insert_one({ 
        "shortCode": short_code, 
        "url": request.url }) 
    return { "shortUrl": f"http://localhost:8000/{short_code}", "code": short_code }   

@router_url.get("/{short_code}")
async def redirect(short_code: str):
    entry = await db['url'].find_one({"shortCode": short_code})
    if not entry:
        raise HTTPException(status_code=404, detail="URL não encontrada")
    return RedirectResponse(url=entry['url'], status_code=302)