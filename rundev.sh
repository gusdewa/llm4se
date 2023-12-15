#!/bin/bash

# Function to print messages with a specific format
print_step() {
    echo "---------------------------------"
    echo "$1"
    echo "---------------------------------"
}

# Error handling function
handle_error() {
    echo "Error occurred in: $1"
    echo "Please check the error message above and try to resolve it."
    exit 1
}

# Function to get a value from .env file
get_env_value() {
    grep "^$1=" .env | cut -d '=' -f2
}

# Check if Docker is installed
print_step "Checking for Docker installation..."
if ! command -v docker &>/dev/null; then
    echo "Docker is not installed. Please install it before proceeding."
    exit 1
fi

# Step 1: Kill API Docker container
print_step "Killing API Docker container..."
docker ps -q --filter "name=fastapi" | xargs --no-run-if-empty docker kill || handle_error "Killing API Docker container"

# Check if Python 3 is installed
print_step "Checking for Python 3 installation..."
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Please install it before proceeding."
    exit 1
fi

# Step 2: Run API locally
print_step "Running API locally..."
python3 -m main || handle_error "Running API"

# Get the APP_PORT from .env file
APP_PORT=$(get_env_value APP_PORT)

print_step "API is now running locally. Open http://localhost:${APP_PORT}"
