@echo off
SETLOCAL ENABLEEXTENSIONS
SETLOCAL DISABLEDELAYEDEXPANSION

:: Function to print messages
:print_step
    echo ---------------------------------
    echo %*
    echo ---------------------------------
    goto :eof

:: Error handling function
:handle_error
    echo Error occurred in: %1
    echo Please check the error message above and try to resolve it.
    exit /b 1

:: Check if Python 3 is installed
call :print_step "Checking for Python 3 installation..."
python --version >nul 2>&1 || (
    echo Please make sure you have installed Python 3, recommended version: Python 3.9
    exit /b 1
)

:: Step 1: Copy sample.env to .env
call :print_step "Copying sample.env to .env..."
copy sample.env .env >nul 2>&1 || call :handle_error "Copying sample.env to .env"

:: Step 2: Create a new local venv
call :print_step "Creating a new virtual environment..."
python -m venv venv >nul 2>&1 || call :handle_error "Creating virtual environment"

:: Step 3: Activate the venv
call :print_step "Activating the virtual environment..."
call venv\Scripts\activate.bat || call :handle_error "Activating virtual environment"

:: Check if pip3 or pip is installed
call :print_step "Checking for pip installation..."
where pip3 >nul 2>&1 || (
    where pip >nul 2>&1 || (
        echo pip3 or pip is not installed. Please install it before proceeding.
        exit /b 1
    )
)

:: Step 4: Install requirements using pip3 or pip
call :print_step "Installing requirements from requirements.txt..."
pip install -r requirements.txt >nul 2>&1 || call :handle_error "Installing requirements"

:: Check if Docker Compose is installed
call :print_step "Checking for Docker Compose installation..."
where docker-compose >nul 2>&1 || (
    echo Docker Compose is not installed. Please install it before proceeding.
    exit /b 1
)

:: Step 5: Run docker-compose up -d
call :print_step "Starting Docker containers with docker-compose..."
docker-compose up -d >nul 2>&1 || call :handle_error "Starting Docker containers"

call :print_step "Setup Completed Successfully!"
echo All services should be up and running.

ENDLOCAL
