from .database import Base
from sqlalchemy import Column, Integer, String, DateTime

class DbURL(Base):
    __tablename__ = "urls"
    id = Column(Integer, primary_key=True, index=True)
    long_url = Column(String, index=True)
    timestamp = Column(DateTime)

class DbShortURL(Base):
    __tablename__ = "short_urls"
    uuid = Column(String, primary_key=True, index=True)
    short_url = Column(String, index=True)
    long_url = Column(String, index=True)
    timestamp = Column(DateTime)

class DbStats(Base):
    __tablename__ = "stats"
    id = Column(Integer, primary_key=True, index=True)
    short_url = Column(String, index=True)
    long_url = Column(String, index=True)
    clicks = Column(Integer)