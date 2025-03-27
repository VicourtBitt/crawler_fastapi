# Project Documentation: Regex Crawler

This document provides a detailed overview of the **Regex Crawler** project structure, including the organization of directories and files, as well as descriptions of their functions and contents.

## Directory Structure

The project is organized as follows:

```
root
├── regex_crawler
│   ├── docs/
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── app
│       ├── core
│       │   └── config.py
│       ├── main.py
│       └── services
│           └── scrapping
│               ├── repository.py
│               └── routes.py
```

### Directory and File Descriptions

- **root/**: Root directory containing all files and subdirectories of the project.

  - **regex_crawler/**: Main project directory.

    - **docs/**: Directory reserved for project documentation.

    - **requirements.txt**: File listing all project dependencies. This file is used to install the required packages with the command `pip install -r requirements.txt`.

    - **Dockerfile**: File containing instructions for creating the project's Docker image. This file defines the environment required to run the application, including dependency installation and configuration settings.

    - **docker-compose.yml**: Docker Compose configuration file. This file allows for orchestrating multiple containers, facilitating the setup and execution of complex environments that may include databases, caching services, and more.

    - **app/**: Directory containing the application's main source code.

      - **core/**: Module responsible for the application's central configurations.

        - **config.py**: File managing the application's global settings, such as environment variables, configuration parameters, and other essential definitions.

      - **main.py**: Main file that starts the FastAPI application. This file sets up the application, including routes and necessary middleware, and starts the server.

      - **services/**: Directory containing the application's service modules.

        - **scrapping/**: Module dedicated to web scraping operations.

          - **repository.py**: File containing the business logic related to scraping operations. It implements functions that send HTTP requests, process responses, and extract necessary data using regular expressions.

          - **routes.py**: File defining API routes related to scraping operations. This file maps API endpoints to corresponding functions in `repository.py`, allowing API clients to trigger scraping operations via HTTP requests.

## Dependencies

The `Scrapper` class is responsible for scraping data from the target website. It has static methods that perform different data extraction operations.

### Main Methods:

- **fetch_all_products(url: str = None, pages: int = 1, category: str = "laptops") -> list:** This method iterates through the specified website pages, extracts product information for the given category (laptops or tablets), and returns a list of dictionaries containing product details.

- **fetch_by_id(id: int = 1, url: str = None) -> dict:** Extracts information for a specific product based on its ID. Uses specific regex patterns to extract detailed product information including price, title, description, available options (swatches), and rating.

- **fetch_by_page(page: int = 1, url: str = None, category: str = "laptops") -> list:** Extracts information for all products on a specific page for the given category. Returns a list of product dictionaries.


## Breakdown of the `fetch_all_products` Method

This method follows these steps:

- **URL Construction:** If no URL is provided, it constructs a URL based on the category (laptops or tablets).

- **Page Iteration:** Loops through the specified number of pages, constructing the corresponding URL for each one.

- **HTTP Request:** Uses the `requests` library to retrieve the page's HTML content with error handling for each page.

- **Content Parsing:** Employs regular expressions to locate and extract relevant information, such as title, price, product link, description, and rating.

- **Data Storage:** Extracted data is stored in a list of dictionaries, which is returned at the end of the process.

## Additional Considerations

- **Modularity**: Organizing the code into specific modules, such as `core` for configurations and `services` for specific functionalities, promotes a clean architecture and facilitates project maintenance and scalability.

This structure follows best practices for FastAPI-based projects, ensuring a clear and efficient organization of the source code.