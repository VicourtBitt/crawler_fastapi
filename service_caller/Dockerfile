# Description: Dockerfile for the service caller

FROM python:3.12-slim

# Set the working directory
WORKDIR /root

# Copy the requirements file
COPY requirements.txt .

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project
COPY . .

# Expose the port
EXPOSE 8000