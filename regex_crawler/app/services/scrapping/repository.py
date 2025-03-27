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
        fetch_by_page: Fetch products from a specific page.
    """  

    BASE_URL = "https://webscraper.io/test-sites/e-commerce/static/computers"
    LAPTOP_BASE = "/laptops"
    TABLET_BASE = "/tablets"
    PRODUCT_PATH = "/test-sites/e-commerce/static/product"

    @classmethod
    def fetch_all_products(cls, url=None, pages=1, category="laptops"):
        """Fetch all products across multiple pages."""
        if not url:
            # Build URL inline instead of using build_url
            base_url = cls.BASE_URL
            if category == "laptops":
                base_url += cls.LAPTOP_BASE
            elif category == "tablets":
                base_url += cls.TABLET_BASE
            url = base_url
            logger.info(f"Using default URL: {url}")
        
        try:
            products = []

            for page in range(1, pages + 1):
                page_url = f"{url}?page={page}"
                
                # make_request inline
                try:
                    response = requests.get(page_url)
                    response.raise_for_status()
                    html_content = response.text

                except requests.RequestException as e:
                    logger.error(f"Error fetching data from page {page}: {e}")
                    continue  # Try next page instead of failing completely
                
                if not html_content:
                    logger.warning(f"Empty content from page {page}, continuing to next page")
                    continue  # Try next page instead of failing

                logger.info(f"Parsing page {page}...")
                
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
                
                products.extend(page_products)
            
            return products
        
        except Exception as e:
            logger.error(f"Error processing data: {e}")
            return {"error": f"Error processing data: {e}"}

    @classmethod
    def fetch_by_id(cls, id=1, url=None):
        """Fetch a product by its ID."""
        if not url:
            # Build URL inline instead of using build_url
            url = f"https://webscraper.io{cls.PRODUCT_PATH}/{id}"
            logger.info(f"Using built URL: {url}")
        
        # make_request inline
        try:
            response = requests.get(url)
            response.raise_for_status()
            html_content = response.text
        except requests.RequestException as e:
            logger.error(f"Error fetching data: {e}")
            return {"error": "Failed to fetch product data"}
            
        if not html_content:
            return {"error": "Failed to fetch product data"}

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

    @classmethod
    def fetch_by_page(cls, page=1, url=None, category="laptops"):
        """Fetch products from a specific page."""
        if not url:
            # Build URL inline instead of using build_url
            base_url = cls.BASE_URL
            if category == "laptops":
                base_url += cls.LAPTOP_BASE
            elif category == "tablets":
                base_url += cls.TABLET_BASE
            url = base_url
            logger.info(f"Using default URL: {url}")

        page_url = f"{url}?page={page}"
        
        # make_request inline
        try:
            response = requests.get(page_url)
            response.raise_for_status()
            html_content = response.text
        except requests.RequestException as e:
            logger.error(f"Error fetching data: {e}")
            return {"error": "Failed to fetch page data"}
        
        if not html_content:
            return {"error": "Failed to fetch page data"}

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