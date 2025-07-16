@echo off
echo ============================================
echo         Homework Helper Setup
echo ============================================

echo.
echo [1/4] Checking if Python is installed...
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found!
    echo Please install Python from: https://www.python.org/downloads/
    pause
    exit
)

echo.
echo [2/4] Installing Python libraries...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo [3/4] Installing Ollama...
start /wait OllamaSetup.exe

echo Pulling AI model (tinyllama)...
ollama pull tinyllama

echo.
echo [4/4] Launching Homework Helper...
start HomeworkHelper.exe

echo Setup complete. You may now use the app.
pause
