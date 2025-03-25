# Documentação do Projeto: Regex Crawler

Este documento fornece uma visão detalhada da estrutura do projeto **Regex Crawler**, incluindo a organização dos diretórios e arquivos, bem como descrições de suas funções e conteúdos.

## Estrutura de Diretórios

A estrutura do projeto é organizada da seguinte forma:

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

### Descrição dos Diretórios e Arquivos

- **root/**: Diretório raiz que contém todos os arquivos e subdiretórios do projeto.

  - **regex_crawler/**: Diretório principal do projeto.

    - **docs/**: Diretório reservado para a documentação do projeto.

    - **requirements.txt**: Arquivo que lista todas as dependências do projeto. Este arquivo é utilizado para instalar os pacotes necessários com o comando `pip install -r requirements.txt`.

    - **Dockerfile**: Arquivo que contém as instruções para a criação da imagem Docker do projeto. Este arquivo define o ambiente necessário para a execução da aplicação, incluindo a instalação de dependências e a configuração do ambiente.

    - **docker-compose.yml**: Arquivo de configuração do Docker Compose. Este arquivo permite orquestrar múltiplos contêineres, facilitando a configuração e execução de ambientes complexos que podem incluir bancos de dados, serviços de cache, entre outros.

    - **app/**: Diretório que contém o código-fonte principal da aplicação.

      - **core/**: Módulo responsável pelas configurações centrais da aplicação.

        - **config.py**: Arquivo que gerencia as configurações globais da aplicação, como variáveis de ambiente, parâmetros de configuração e outras definições essenciais.

      - **main.py**: Arquivo principal que inicia a aplicação FastAPI. Este arquivo configura a aplicação, incluindo as rotas e middleware necessários, e inicia o servidor.

      - **services/**: Diretório que contém os módulos de serviços da aplicação.

        - **scrapping/**: Módulo específico para operações de web scraping.

          - **repository.py**: Arquivo que contém a lógica de negócio relacionada às operações de scraping. Aqui são implementadas as funções que realizam as requisições HTTP, processam as respostas e extraem os dados necessários utilizando expressões regulares.

          - **routes.py**: Arquivo que define as rotas da API relacionadas às operações de scraping. Este arquivo mapeia os endpoints da API para as funções correspondentes no `repository.py`, permitindo que os clientes da API acionem as operações de scraping através de requisições HTTP.

## Dependências

A classe Scrapper é responsável por realizar a raspagem de dados do site alvo. Ela possui métodos estáticos que executam diferentes operações de extração de dados.

### Métodos Principais:

- ***fetch_all_products(url: str = None, pages: int = 1) -> list:*** Este método percorre as páginas do site especificado, extrai informações sobre os produtos e retorna uma lista de dicionários contendo os detalhes de cada produto.

- ***fetch_by_id(url: str = None, id: int = 1) -> dict:*** Extrai informações de um produto específico com base no seu ID.

- ***fetch_by_page(url: str = None, page: int = 1) -> list:*** Extrai informações de todos os produtos presentes em uma página específica.

## Detalhamento do Método fetch_all_products

Este método realiza as seguintes etapas:

- **Definição da URL Base:** Se nenhuma URL for fornecida, utiliza uma URL padrão.

- **Iteração pelas Páginas:** Percorre o número especificado de páginas, construindo a URL correspondente para cada uma.

- **Requisição HTTP:** Utiliza a biblioteca Requests para obter o conteúdo HTML da página. 

- **Parsing do Conteúdo:** Emprega expressões regulares para localizar e extrair informações relevantes, como título, preço, link do produto, descrição e avaliação.

- **Armazenamento dos Dados:** Os dados extraídos são armazenados em uma lista de dicionários, que é retornada ao final do processo.

## Considerações Adicionais

- **Modularidade**: A organização do código em módulos específicos, como `core` para configurações e `services` para funcionalidades específicas, promove uma arquitetura limpa e facilita a manutenção e escalabilidade do projeto.

Esta estrutura segue as melhores práticas recomendadas para projetos desenvolvidos com FastAPI, promovendo uma organização clara e eficiente do código-fonte. 