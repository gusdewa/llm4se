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

REM Function to get a value from .env file
:get_env_value
FOR /F "tokens=*" %%i IN ('type .env ^| findstr /B /C:"%~1="') DO (
    SET var=%%i
    FOR /F "tokens=2 delims==" %%a IN ("!var!") DO (
        SET value=%%a
        goto :eof
    )
)

REM Check if Docker is installed
call :print_step "Checking for Docker installation..."
docker --version >nul 2>&1 || call :handle_error "Docker is not installed."

REM Step 1: Kill API Docker container
call :print_step "Killing API Docker container..."
docker ps -q --filter "name=fastapi" | xargs --no-run-if-empty docker kill || call :handle_error "Killing API Docker container"

REM Check if Python 3 is installed
call :print_step "Checking for Python 3 installation..."
python3 --version >nul 2>&1 || call :handle_error "Python 3 is not installed."

REM Step 2: Run API locally
call :print_step "Running API locally..."
python3 -m main || call :handle_error "Running API"

REM Get the APP_PORT from .env file
call :get_env_value "APP_PORT"
call :print_step "API is now running locally. Open http://localhost:%value%"

:end
ENDLOCAL
