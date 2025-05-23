from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.caller.routes import router as caller_routes

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(caller_routes, prefix="/api/v1/crawler")