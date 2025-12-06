@echo off
echo 🚀 Starting Intelligent Search Engine...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.9 or higher.
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Node.js is not installed. Please install Node.js 16 or higher.
    exit /b 1
)

REM Setup Backend
echo 📦 Setting up backend...
cd backend

REM Check if venv exists
if not exist "venv" (
    echo   Creating virtual environment...
    python -m venv venv
)

REM Activate venv
call venv\Scripts\activate.bat

REM Install dependencies
echo   Installing Python dependencies...
pip install -q -r requirements.txt

REM Check if .env exists
if not exist ".env" (
    echo   Creating .env file from .env.example...
    copy .env.example .env
    echo   ⚠️  Please edit backend\.env with your SerpAPI key
)

cd ..

REM Setup Frontend
echo.
echo 🎨 Setting up frontend...
cd frontend

REM Install dependencies
if not exist "node_modules" (
    echo   Installing Node dependencies...
    npm install -q
)

cd ..

echo.
echo ✅ Setup complete!
echo.
echo 📝 Next steps:
echo   1. Edit backend\.env and add your SerpAPI key
echo   2. Make sure MongoDB is running
echo   3. Start backend: cd backend && venv\Scripts\activate.bat && uvicorn app.main:app --reload
echo   4. Start frontend: cd frontend && npm run dev
echo.
echo 🌐 URLs:
echo   Backend API: http://localhost:8000
echo   Frontend: http://localhost:5173
echo   API Docs: http://localhost:8000/docs
