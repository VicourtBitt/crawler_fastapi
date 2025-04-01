#!/bin/bash

# Function to handle errors
handle_error() {
    echo "Error: $1"
    exit 1
}

# Function to run Docker services in the root directory
run_docker() {
    echo "Starting Docker services..."
    
    # Get the absolute path to the root directory (where docker-compose.yml is located)
    ROOT_DIR="$(dirname "$(readlink -f "$0")")"
    cd "$ROOT_DIR" || handle_error "Failed to navigate to root directory"
    
    echo "Running docker-compose in: $(pwd)"
    sudo docker compose up "$@" || handle_error "Failed to start Docker services"
}

# Process arguments
if [ $# -eq 0 ]; then
    # No arguments, just run docker compose up
    run_docker
else
    # Pass all arguments to docker compose
    run_docker "$@"
fi
