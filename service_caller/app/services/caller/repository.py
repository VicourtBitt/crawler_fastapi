import requests

BASE_URL = "http://regex_crawler:3000/api/v1/products/computers"
CHG_URL = ""

def get_all_products(url: str = None, pages: int = 1, category: str = "laptops"):
    """
    Fetches all products from the given URL, paginated.
    
    Args:
        url (str): The API endpoint. Defaults to BASE_URL.
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
        url (str): The API endpoint. Defaults to BASE_URL.
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
        url (str): The API endpoint. Defaults to BASE_URL.
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