# Docker Setup Documentation: Regex Crawler

This document describes the approach used to containerize the **Regex Crawler** project using **Docker** and **Docker Compose**.

---

## **Observation**
Be sure that you are inside the ***regex_crawler*** folder before doing anything *build-related*, so the project will run as expected.

## **Dockerfile Overview**

The `Dockerfile` is responsible for building the containerized environment for the **Regex Crawler** project. Below is a breakdown of its structure:

```dockerfile
# Use the official Python image
FROM python:3.12-slim
```
- Uses the official **Python 3.12-slim** image as a lightweight base for the container.

```dockerfile
# Set the working directory
WORKDIR /root
```
- Sets the working directory inside the container to `/root`.

```dockerfile
# Copy the requirements file
COPY requirements.txt .
```
- Copies the `requirements.txt` file from the project directory into the container.

```dockerfile
# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt
```
- Installs the necessary dependencies listed in `requirements.txt`, ensuring a clean installation by avoiding cache storage.

```dockerfile
# Copy the project
COPY . .
```
- Copies all project files into the container.

```dockerfile
# Expose the port
EXPOSE 3000
```
- Exposes **port 3000**, allowing the application to be accessible from outside the container.

---

## **Docker Compose Configuration (`docker-compose.yml`)**

The `docker-compose.yml` file orchestrates the container execution.

```yaml
version: "3.9"
```
- Specifies the **Docker Compose version** being used.

### **Service Definition**
```yaml
services:
  regex_crawler:
```
- Defines the **regex_crawler** service, which runs the application.

```yaml
    build: .
```
- Builds the container using the **Dockerfile** located in the project root.

```yaml
    container_name: regex_crawler
```
- Assigns a custom name (`regex_crawler`) to the container for easier management.

```yaml
    command: uvicorn main:app --host 0.0.0.0 --port 3000
```
- Defines the command to run **Uvicorn**, launching the FastAPI application:
  - `main:app`: Specifies the FastAPI app instance inside `main.py`.
  - `--host 0.0.0.0`: Ensures the application is accessible from outside the container.
  - `--port 3000`: Runs the application on **port 3000**.

```yaml
    working_dir: /root/app/
```
- Sets the working directory inside the container to `/root/app/`.

```yaml
    ports:
      - "3000:3000"
```
- Maps **container port 3000** to **host port 3000**, making the API accessible via `http://localhost:3000`.

---

## **How to Build and Run the Containers**

1. **Build the container** (if running for the first time or after changes):
   ```sh
   docker-compose build
   ```
2. **Run the container**:
   ```sh
   docker-compose up -d
   ```
   - The `-d` flag runs the container in **detached mode** (in the background).

3. **Check running containers**:
   ```sh
   docker ps
   ```

4. **Stop the container**:
   ```sh
   docker-compose down
   ```

---

## **Summary**
- The **Dockerfile** sets up a lightweight Python environment, installs dependencies, and exposes port 3000.
- The **Docker Compose file** defines the `regex_crawler` service, builds the container, sets the working directory, and runs **FastAPI** with **Uvicorn**.
- The API is accessible at:  
  ```
  http://localhost:3000
  ```

This setup ensures a **consistent and easily deployable** environment for running the **Regex Crawler** application. 🚀