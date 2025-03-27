from fastapi import APIRouter

from . import repository

router = APIRouter()


@router.get("/")
async def fetch_all_products(url: str = None, pages: int = 1, category: str = "laptops"):
    return repository.get_all_products(url, pages, category)


@router.get("/product/{id}")
async def fetch_by_id(id: int, url: str = None):
    return repository.get_product_by_id(url, id)


@router.get("/page/{page}")
async def fetch_by_page(page: int, url: str = None, category: str = "laptops"):
    return repository.get_products_by_page(url, page, category)