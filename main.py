from fastapi import FastAPI
from routers.url import router as url_router
from db.database import engine
from db import models

app = FastAPI()
app.include_router(url_router)

@app.get("/")
def root():
    return {"message": "Hello World"}


models.Base.metadata.create_all(bind=engine)
