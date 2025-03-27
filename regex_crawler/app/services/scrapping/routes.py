from fastapi import APIRouter
from typing import List, Dict

from services.scrapping import repository

router = APIRouter()


@router.get("/computers", response_model=List[Dict])
async def fetch_all_products(url: str = None, pages: int = 1, category: str = "laptops"):
    return repository.Scrapper.fetch_all_products(url=url, pages=pages, category=category)


@router.get("/computers/product/{id}", response_model=Dict)
async def fetch_by_id(id: int, url: str = None):
    return repository.Scrapper.fetch_by_id(id=id, url=url)


@router.get("/computers/page/{page}", response_model=List[Dict])
async def fetch_by_page(page: int, url: str = None, category: str = "laptops"):
    return repository.Scrapper.fetch_by_page(page=page, url=url, category=category)