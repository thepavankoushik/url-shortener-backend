from pydantic import BaseModel
from datetime import datetime

class Url(BaseModel):
    url: str

class ShortUrl(BaseModel):
    uuid: str
    short_url: str
    long_url: str
    timestamp: datetime

class ShortUrlBase(BaseModel):
    short_url: str

class ShortUrlView(BaseModel):
    short_url: str
    long_url: str
    class Config:
        orm_mode = True

class Stats(BaseModel):
    short_url: str
    clicks: int

class StatsView(BaseModel):
    short_url: str
    long_url: str
    clicks: int
    class Config:
        orm_mode = True

