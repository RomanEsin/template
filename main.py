from fastapi import FastAPI
from typing import List, Optional
from starlette.middleware.cors import CORSMiddleware


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
