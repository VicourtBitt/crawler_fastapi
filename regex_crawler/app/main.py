from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.scrapping.routes import router as scrapping_router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(scrapping_router, prefix="/api/v1/products")