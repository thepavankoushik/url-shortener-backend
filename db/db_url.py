from routers.schemas import ShortUrl
from sqlalchemy.orm import Session
from db.models import DbShortURL, DbStats


def create_short_url(db: Session, short_url: ShortUrl):
    db_short_url = DbShortURL(uuid=short_url.uuid, short_url=short_url.short_url, long_url=short_url.long_url, timestamp=short_url.timestamp)
    db.add(db_short_url)
    db.commit()
    db.refresh(db_short_url)
    return db_short_url

def find_long_url(db: Session, short_url):
    return db.query(DbShortURL).filter(DbShortURL.short_url == short_url).first()


def update_stats(db: Session, short_url: str, long_url: str):
    db_short_url = db.query(DbStats).filter(DbStats.short_url == short_url).first()
    if db_short_url:
        db_short_url.clicks += 1
    else:
        db_short_url = DbStats(short_url=short_url, clicks=1, long_url=long_url)
        db.add(db_short_url)
    db.commit()
    db.refresh(db_short_url)
    return db_short_url

def get_stats(db: Session, short_url: str):
    return db.query(DbStats).filter(DbStats.short_url == short_url).first()