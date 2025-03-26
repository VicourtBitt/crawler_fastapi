import requests

BASE_URL = "http://localhost:3000/api/v1/products/computers"
CHG_URL = ""

def get_all_products(url: str = None, pages: int = 1):
    """
    Fetches all products from the given URL, paginated.
    
    Args:
        url (str): The API endpoint. Defaults to BASE_URL.
        pages (int): Page number to fetch.

    Returns:
        dict: JSON response or error message.
    """
    try:
        if not url:
            url = CHG_URL
        response = requests.get(f"{BASE_URL}?page={pages}&url={url}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Error fetching data: {e}"}

def get_product_by_id(url: str = None, product_id: int = 1):
    """
    Fetches product details by ID.

    Args:
        url (str): The API endpoint. Defaults to BASE_URL.
        product_id (int): ID of the product to fetch.

    Returns:
        dict: JSON response or error message.
    """
    try:
        if not url:
            url = CHG_URL
        response = requests.get(f"{BASE_URL}/{product_id}?url={url}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Error fetching data: {e}"}

def get_products_by_page(url: str = None, page: int = 1):
    """
    Fetches products from a specific page.

    Args:
        url (str): The API endpoint. Defaults to BASE_URL.
        page (int): Page number.

    Returns:
        dict: JSON response or error message.
    """
    try:
        if not url:
            url = CHG_URL
        response = requests.get(f"{BASE_URL}/page/{page}?url={url}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Error fetching data: {e}"}
