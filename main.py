from fastapi import FastAPI
from typing import List, Optional
from starlette.middleware.cors import CORSMiddleware

from Database.database import engine
from Models import models

models.Base.metadata.create_all(bind=engine)


origins = [
    "*"
]

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def home():
    return {"Hello": "World!"}
