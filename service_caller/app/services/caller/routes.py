from fastapi import APIRouter
from typing import List, Dict

from . import repository

router = APIRouter()


@router.get("/")
async def fetch_all_products(url: str = None, pages: int = 1):
    return repository.get_all_products(url, pages)


@router.get("/{id}")
async def fetch_by_id(url: str = None, id: int = 1):
    return repository.get_product_by_id(url, id)


@router.get("/page/{pages}")
async def fetch_by_page(url: str = None, page: int = 1):
    return repository.get_products_by_page(url, page)