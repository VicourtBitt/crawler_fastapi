#!/bin/bash

# Function to handle errors
handle_error() {
    echo "Error: $1"
    exit 1
}

# Function to run Docker services
run_docker() {
    echo "Starting Docker services..."
    docker compose up --build $1 || handle_error "Failed to start Docker services"
}

# Function to run service_caller application
run_service_caller() {
    echo "Starting service_caller application..."
    cd service_caller || handle_error "Failed to enter service_caller directory"
    uvicorn app.main:app --host 0.0.0.0 --port 8000 || handle_error "Failed to start uvicorn server"
}

# Check if command line argument is provided
if [ $# -eq 0 ]; then
    # No arguments, run everything by default
    echo "Running all services by default..."
    run_docker "-d"
    run_service_caller
else
    # Process provided argument
    case "$1" in
        docker)
            run_docker
            ;;
        service)
            run_service_caller
            ;;
        all)
            run_docker "-d"
            run_service_caller
            ;;
        *)
            echo "Usage: $0 {docker|service|all}"
            echo "  docker  - Run Docker services"
            echo "  service - Run service_caller application"
            echo "  all     - Run both Docker services and service_caller application"
            echo "  (no args) - Same as 'all'"
            exit 1
            ;;
    esac
fi