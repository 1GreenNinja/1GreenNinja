@echo off
echo.
echo ===============================
echo   Typing Speed Test Launcher
echo ===============================
echo.

REM Try to run with python3 first, then python
python3 typing_speed_test.py 2>nul
if %errorlevel% neq 0 (
    python typing_speed_test.py 2>nul
    if %errorlevel% neq 0 (
        echo Error: Python not found or application failed to start
        echo.
        echo Please make sure Python 3.6+ is installed and added to your PATH
        echo You can download Python from: https://python.org
        echo.
        pause
        exit /b 1
    )
)

echo.
echo Application closed.
pause