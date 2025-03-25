
# Scrapper (Docker, FastAPI)

This project simulates the usage of a Scrapper Class to gather info from a fetched web page [WebScrapper.io](https://webscraper.io/test-sites/e-commerce/static/computers), such as their items in both categories (tablets and laptops).

---

### Summary
The project uses an SOA (Service-Oriented-Architecture) approach to handle routes and their inner complexities such as repositories, services and others (if needed). Also, it's separated in two parts:

- Outer FastAPI (Calling a service);
- Inner FastAPI with Scrapper Class (Docker Service to be called);
---

### Requirements
Those are the following requirements to start and run the project.

```plaintext
annotated-types==0.7.0
anyio==4.9.0
certifi==2025.1.31
charset-normalizer==3.4.1
click==8.1.8
exceptiongroup==1.2.2
fastapi==0.115.12
h11==0.14.0
idna==3.10
pydantic==2.10.6
pydantic_core==2.27.2
requests==2.32.3
sniffio==1.3.1
starlette==0.46.1
typing_extensions==4.12.2
urllib3==2.3.0
uvicorn==0.34.0
```
To install those requirements and run them into your server, first do the following:

```sh
python3 -m venv venv            # To create a virtual enviroment
source venv/bin/activate        # To activate the venv
pip install -r requirements.txt 
```

---

### Folder Structure
```plaintext
    root
    ├── regex_crawler
    │   ├── docs/
    │   ├── requirements.txt
    │   ├── Dockerfile
    │   ├── docker-compose.yml
    │   └── app                         # project root
    │       ├── core                    # configuration and setup  
    │       │   └── config.py           
    │       ├── main.py                 # main app file
    │       └── services                # modular services
    │           └── scrapping
    │               ├── repository.py   # business logic
    │               └── routes.py       # routes
    └── caller
        ├── docs/
        └── app
            ├── core 
            │   └── config.py           
            ├── main.py
            └── services 
                └── caller
                    ├── repository.py 
                    └── routes.py     
```

---

### Documentation
[FastAPI Scrapper Container]()

[FastAPI Local]()
