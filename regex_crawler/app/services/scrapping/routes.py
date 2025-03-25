from fastapi import APIRouter
from typing import List, Dict

from services.scrapping import repository

router = APIRouter()


@router.get("/computers", response_model=List[Dict])
async def fetch_all_products(url: str = None, pages: int = 1):
    return repository.Scrapper.fetch_all_products(url, pages)


@router.get("/computers/{id}", response_model=Dict)
async def fetch_by_id(url: str = None, id: int = 1):
    return repository.Scrapper.fetch_by_id(url, id)


@router.get("/computers/page/{pages}", response_model=List[Dict])
async def fetch_by_page(url: str = None, page: int = 1):
    return repository.Scrapper.fetch_by_page(url, page)