#!/bin/bash

echo "🚀 Starting Intelligent Search Engine..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.9 or higher."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 16 or higher."
    exit 1
fi

# Check if MongoDB is running
if ! command -v mongosh &> /dev/null && ! command -v mongo &> /dev/null; then
    echo "⚠️  MongoDB client not found. Make sure MongoDB server is running."
fi

# Setup Backend
echo "📦 Setting up backend..."
cd backend

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "  Creating virtual environment..."
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Install dependencies
echo "  Installing Python dependencies..."
pip install -q -r requirements.txt

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "  Creating .env file from .env.example..."
    cp .env.example .env
    echo "  ⚠️  Please edit backend/.env with your SerpAPI key"
fi

cd ..

# Setup Frontend
echo ""
echo "🎨 Setting up frontend..."
cd frontend

# Install dependencies
if [ ! -d "node_modules" ]; then
    echo "  Installing Node dependencies..."
    npm install -q
fi

cd ..

echo ""
echo "✅ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "  1. Edit backend/.env and add your SerpAPI key"
echo "  2. Make sure MongoDB is running"
echo "  3. Start backend: cd backend && source venv/bin/activate && uvicorn app.main:app --reload"
echo "  4. Start frontend: cd frontend && npm run dev"
echo ""
echo "🌐 URLs:"
echo "  Backend API: http://localhost:8000"
echo "  Frontend: http://localhost:5173"
echo "  API Docs: http://localhost:8000/docs"
