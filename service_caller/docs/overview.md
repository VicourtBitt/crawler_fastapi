# FastAPI Crawler API Documentation

## Overview
This project provides a FastAPI-based API for retrieving product data from an external source. The API includes endpoints to fetch all products, retrieve a product by ID, and get paginated results. The application is containerized using Docker and configured with CORS middleware.

---

## 1. **Helper Functions for API Calls (`repository.py`)**
### Purpose
These functions send HTTP requests to an external API to retrieve product data.

### Implementation
```python
import requests

BASE_URL = "http://localhost:3000/api/v1/products/computers"
CHG_URL = ""

def get_all_products(url: str = None, pages: int = 1, category: str = "laptops"):
    """
    Fetches all products from the given URL, paginated.
    
    Args:
        url (str): The API endpoint. Defaults to CHG_URL.
        pages (int): Page number to fetch.
        category (str): Product category (laptops/tablets).

    Returns:
        dict: JSON response or error message.
    """
    try:
        if not url:
            url = CHG_URL
        
        request_url = f"{BASE_URL}?pages={pages}&category={category}"
        if url:
            request_url += f"&url={url}"
            
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Error fetching data: {e}"}

def get_product_by_id(url: str = None, product_id: int = 1):
    """
    Fetches product details by ID.

    Args:
        url (str): The API endpoint. Defaults to CHG_URL.
        product_id (int): ID of the product to fetch.

    Returns:
        dict: JSON response or error message.
    """
    try:
        if not url:
            url = CHG_URL
        
        request_url = f"{BASE_URL}/product/{product_id}"
        if url:
            request_url += f"?url={url}"
            
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Error fetching data: {e}"}

def get_products_by_page(url: str = None, page: int = 1, category: str = "laptops"):
    """
    Fetches products from a specific page.

    Args:
        url (str): The API endpoint. Defaults to CHG_URL.
        page (int): Page number.
        category (str): Product category (laptops/tablets).

    Returns:
        dict: JSON response or error message.
    """
    try:
        if not url:
            url = CHG_URL
        
        request_url = f"{BASE_URL}/page/{page}?category={category}"
        if url:
            request_url += f"&url={url}"
            
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Error fetching data: {e}"}
```

---

## 2. **API Routes (`routes.py`)**
### Purpose
Defines the API endpoints for retrieving product data.

### Implementation
```python
from fastapi import APIRouter
from . import repository

router = APIRouter()

@router.get("/")
async def fetch_all_products(url: str = None, pages: int = 1, category: str = "laptops"):
    """
    Endpoint to fetch all products with pagination.
    """
    return repository.get_all_products(url, pages, category)

@router.get("/product/{id}")
async def fetch_by_id(id: int, url: str = None):
    """
    Endpoint to fetch a product by ID.
    """
    return repository.get_product_by_id(url, id)

@router.get("/page/{page}")
async def fetch_by_page(page: int, url: str = None, category: str = "laptops"):
    """
    Endpoint to fetch products by page.
    """
    return repository.get_products_by_page(url, page, category)
```

---

## 3. **FastAPI Application Setup (`main.py`)**
### Purpose
Initializes the FastAPI application, sets up CORS middleware, and registers routes.

### Implementation
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .services.caller.routes import router as caller_routes

app = FastAPI()

# Define allowed origins for CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
]

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API router
app.include_router(caller_routes, prefix="/api/v1/crawler")
```