# Description: Dockerfile for the regex_crawler project

# Use the official Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /root

# Copy the requirements file
COPY ./regex_crawler/requirements.txt .

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project
COPY ./regex_crawler/ .

# Expose the port
EXPOSE 3000