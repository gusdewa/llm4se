@echo off
SETLOCAL EnableDelayedExpansion

REM Function to print messages with a specific format
:print_step
echo ---------------------------------
echo %~1
echo ---------------------------------
goto :eof

REM Error handling function
:handle_error
echo Error occurred in: %~1
echo Please check the error message above and try to resolve it.
exit /b 1

REM Check if Python 3 is installed
call :print_step "Checking for Python 3 installation..."
python3 --version >nul 2>&1 || call :handle_error "Python 3 is not installed."

REM Step 1: Copy env.sample to .env
call :print_step "Copying env.sample to .env..."
copy env.sample .env >nul 2>&1 || call :handle_error "Copying env.sample to .env"

REM Step 2: Create a new local venv
call :print_step "Creating a new virtual environment..."
python3 -m venv venv >nul 2>&1 || call :handle_error "Creating virtual environment"

REM Step 3: Activate the venv
call :print_step "Activating the virtual environment..."
call venv\Scripts\activate.bat || call :handle_error "Activating virtual environment"

REM Step 4: Install requirements using pip
call :print_step "Installing requirements from requirements.txt..."
pip install -r requirements.txt >nul 2>&1 || call :handle_error "Installing requirements"

REM New Step: Unzip amazon_review.zip
call :print_step "Unzipping data/amazon_review.zip..."
if not exist "data/amazon_review.zip" call :handle_error "amazon_review.zip not found."
powershell -command "Expand-Archive 'data/amazon_review.zip' -DestinationPath 'data'" >nul 2>&1 || call :handle_error "Unzipping amazon_review.zip"

REM New Step: Remove unwanted files and rename 1429_1.csv
call :print_step "Cleaning up and renaming files..."
del /q data\* >nul 2>&1
move data\1429_1.csv data\amazon_reviews.csv >nul 2>&1 || call :handle_error "Renaming 1429_1.csv to amazon_reviews.csv"

REM Check if Docker Compose is installed
call :print_step "Checking for Docker Compose installation..."
docker-compose --version >nul 2>&1 || call :handle_error "Docker Compose is not installed."

REM Step 5: Run docker-compose up
call :print_step "Starting Docker containers with docker-compose..."
docker-compose up -d >nul 2>&1 || call :handle_error "Starting Docker containers"

call :print_step "Setup Completed Successfully!"
echo All services should be up and running. Go to localhost:3000 for the UI and localhost:8080 for the API to check.

:end
ENDLOCAL
