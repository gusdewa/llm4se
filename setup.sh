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

# Check if Python 3 and venv module are installed
print_step "Checking for Python 3 and venv installation..."
if ! command -v python3 &>/dev/null || ! python3 -c "import venv" &>/dev/null; then
    echo "Please make sure you have Python 3 with the venv module installed, recommended version: Python 3.9"
    exit 1
fi

# Step 1: Copy env.sample to .env
print_step "Copying env.sample to .env..."
cp env.sample .env || handle_error "Copying env.sample to .env"

# Step 2: Create a new local venv
print_step "Creating a new virtual environment..."
python3 -m venv venv || handle_error "Creating virtual environment"

# Step 3: Activate the venv
print_step "Activating the virtual environment..."
source venv/bin/activate || handle_error "Activating virtual environment"

# Check if pip3 is installed, else use pip
print_step "Checking for pip installation..."
PIP_COMMAND="pip3"
if ! command -v pip3 &>/dev/null; then
    if command -v pip &>/dev/null; then
        PIP_COMMAND="pip"
    else
        echo "pip3 or pip is not installed. Please install it before proceeding."
        exit 1
    fi
fi

# Step 4: Install requirements using pip3 or pip
print_step "Installing requirements from requirements.txt..."
$PIP_COMMAND install -r requirements.txt || handle_error "Installing requirements"

# Check if Docker Compose is installed
print_step "Checking for Docker Compose installation..."
if ! command -v docker-compose &>/dev/null; then
    echo "Docker Compose is not installed. Please install it before proceeding."
    exit 1
fi

# Step 5: Run docker-compose up -d
print_step "Starting Docker containers with docker-compose..."
docker-compose up -d || handle_error "Starting Docker containers"

print_step "Setup Completed Successfully!"
echo "All services should be up and running. Go to localhost:3000 for the UI and localhost:8080 for the API to check."
