import requests
import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Scrapper:
    """ It's responsible for the data scrapping operations in the webscraper.io site passed 
    during the technical test with Devnology. 
    
    Methods:
        fetch_all_products: Fetch all products from the given URL.
        fetch_by_id: Fetch a product by its ID.

    Documentation:
        
    """  

    @staticmethod
    def fetch_all_products(url: str = None, pages: int = 1) -> list:
        if not url:
            logger.error("Setting default technical test URL")
            url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"
        
        try:
            products = []

            # Iterate through the pages
            for page in list(range(0, pages)):
                page_url = f"{url}?page={page}"
                response = requests.get(page_url)
                html_content = response.text

                logger.info(f"Parsing page {page + 1}...")
                
                # Combine the regex patterns
                product_pattern = re.compile(
                    r'<div class="card thumbnail">.*?'
                    r'<h4 class="price.*?">\$(\d+\.\d+)</h4>.*?'
                    r'<a href="(/test-sites/e-commerce/static/product/\d+)" class="title" title="([^"]+)">.*?'
                    r'<p class="description card-text">(.*?)</p>.*?'
                    r'<p data-rating="(\d+)">',
                    re.DOTALL
                )
                
                page_products = []
                for match in product_pattern.finditer(html_content):
                    product = {
                        "title": match.group(3),
                        "price": match.group(1),
                        "product_link": f"https://webscraper.io{match.group(2)}",
                        "description": match.group(4),
                        "rating": match.group(5),
                    }
                    page_products.append(product)
                
                if not page_products:
                    break
                
                products.extend(page_products)
            
            return products
        
        except requests.RequestException as e:
            logger.error(f"Error fetching data: {e}")
            return {"error": f"Error fetching data: {e}"}


    @staticmethod
    def fetch_by_id(url: str = None, id: int = 1) -> dict:
        if not url:
            logger.info("Setting default technical test URL")
            url = f"https://webscraper.io/test-sites/e-commerce/static/product/{id}"
            
        try:
            response = requests.get(url)
            response.raise_for_status()
            html_content = response.text

            # Compile optimized regex patterns
            card_pattern = re.compile(r'<div class="card thumbnail">(.*?)</div>\s*</div>', re.DOTALL)
            price_pattern = re.compile(r'<h4 class="price.*?">\$(\d+\.\d+)</h4>')
            title_pattern = re.compile(r'<h4 class="title card-title">(.*?)</h4>')
            description_pattern = re.compile(r'<p class="description card-text">(.*?)</p>')
            swatch_pattern = re.compile(r'<button[^>]+value="(\d+)"[^>]*>.*?</button>')
            rating_pattern = re.compile(r'<p class="review-count">(\d+) reviews[\s\S]*?</p>')

            # Ensure the card section exists
            card_match = card_pattern.search(html_content)
            if not card_match:
                logger.error("Product card section not found in HTML.")
                return {"error": "Product card section not found."}

            # Extract details using individual patterns
            price_match = price_pattern.search(html_content)
            title_match = title_pattern.search(html_content)
            description_match = description_pattern.search(html_content)
            swatch_matches = swatch_pattern.findall(html_content)
            rating_match = rating_pattern.search(html_content)

            product = {
                "price": price_match.group(1) if price_match else None,
                "title": title_match.group(1) if title_match else None,
                "description": description_match.group(1) if description_match else None,
                "swatches": swatch_matches,  # All swatch values extracted
                "rating": rating_match.group(1) if rating_match else None,
            }

            return product

        except requests.RequestException as e:
            logger.error(f"Error fetching data: {e}")
            return {"error": f"Error fetching data: {e}"}
        

    @staticmethod
    def fetch_by_page(url: str = None, page: int = 1) -> list:
        if not url:
            logger.info("Setting default technical test URL")
            url = f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={page}"

        try:
            response = requests.get(f"{url}?page={page}")
            response.raise_for_status()
            html_content = response.text

            # Combine the regex patterns
            product_pattern = re.compile(
                r'<div class="card thumbnail">.*?'
                r'<h4 class="price.*?">\$(\d+\.\d+)</h4>.*?'
                r'<a href="(/test-sites/e-commerce/static/product/\d+)" class="title" title="([^"]+)">.*?'
                r'<p class="description card-text">(.*?)</p>.*?'
                r'<p data-rating="(\d+)">',
                re.DOTALL
            )

            page_products = []
            for match in product_pattern.finditer(html_content):
                product = {
                    "title": match.group(3),
                    "price": match.group(1),
                    "product_link": f"https://webscraper.io{match.group(2)}",
                    "description": match.group(4),
                    "rating": match.group(5),
                }
                page_products.append(product)

            return page_products
        
        except requests.RequestException as e:
            logger.error(f"Error fetching data: {e}")
            return {"error": f"Error fetching data: {e}"}   