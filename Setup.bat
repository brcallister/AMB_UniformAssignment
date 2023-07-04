@echo off
echo Checking dependencies...

REM Check if Python is installed
python --version 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    exit /b 1
)

REM Check if pip is installed
pip --version 2>nul
if %errorlevel% neq 0 (
    echo pip is not installed. Installing pip...
    python -m ensurepip --default-pip
)

REM Check if pandas is installed
pip show pandas 2>nul
if %errorlevel% neq 0 (
    echo pandas is not installed. Installing pandas...
    pip install pandas
)

REM Check if openpyxl is installed
pip show openpyxl 2>nul
if %errorlevel% neq 0 (
    echo openpyxl is not installed. Installing openpyxl...
    pip install openpyxl
)

echo ========================================
echo All required dependencies are installed.
echo ========================================

REM Wait so the user can read the messages
timeout /t 3 >nul