from fastapi import APIRouter, Depends
import uuid
from datetime import datetime
from .schemas import ShortUrl, ShortUrlView, ShortUrlBase, Url, StatsView
from db.db_url import create_short_url as db_create_short_url
from db.db_url import find_long_url as db_find_long_url
from db.db_url import get_stats as db_get_stats
from db.database import get_db
from sqlalchemy.orm import Session
from utils.url_utils import check_url_validity

router = APIRouter(
    prefix="/url",
    tags=["url"]
)

@router.post("/", response_model=ShortUrlView)
def get_long_url(request: ShortUrlBase, db: Session = Depends(get_db)):
    if not check_url_validity(request.short_url):
        return {"error": "Invalid URL"}
    return db_find_long_url(db, request.short_url)

@router.post('/shorten/', response_model=ShortUrlView)
def shorten_url(request: Url, db: Session = Depends(get_db)):
    if not check_url_validity(request.url):
        return {"error": "Invalid URL"}
    unique_id = uuid.uuid4()
    base62_id = uuid.uuid4().int
    short_base62_id = str(base62_id)[:7]
    return db_create_short_url(
        db, 
        ShortUrl(
            uuid=str(unique_id), 
            short_url=f"http://localhost:8000/url/{short_base62_id}", 
            long_url=request.url, 
            timestamp=datetime.now()
            )
    )

@router.post('/stats/', response_model=StatsView)
def get_stats(request: ShortUrlBase, db: Session = Depends(get_db)):
    if not check_url_validity(request.short_url):
        return {"error": "Invalid URL"}
    return db_get_stats(db, request.short_url)