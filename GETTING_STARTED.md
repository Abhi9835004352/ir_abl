# 🚀 Getting Started Guide

## Prerequisites Installation

### 1. Install MongoDB

**macOS (Homebrew)**
```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community

# Verify installation
mongosh
# Type: exit()
```

**Windows**
- Download from: https://www.mongodb.com/try/download/community
- Run installer
- MongoDB will start automatically

**Docker (Any OS)**
```bash
docker run -d -p 27017:27017 --name mongodb mongo:7
```

### 2. Install Python 3.9+

- Download from: https://www.python.org
- Verify: `python3 --version`

### 3. Install Node.js 16+

- Download from: https://nodejs.org
- Verify: `node --version && npm --version`

### 4. Get SerpAPI Key

1. Visit: https://serpapi.com
2. Sign up (free tier available)
3. Go to Dashboard → API Key
4. Copy your API key

## Step-by-Step Setup

### Option A: Automated Setup (Recommended)

**macOS/Linux**
```bash
cd /Users/abhishek9835/Desktop/projects/ir_abl
chmod +x setup.sh
./setup.sh
```

**Windows**
```bash
cd C:\Users\abhishek9835\Desktop\projects\ir_abl
setup.bat
```

Then edit `backend/.env` and add your SerpAPI key.

### Option B: Manual Setup

#### Backend Setup

```bash
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate.bat  # Windows

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env file and add your SerpAPI key
# SERPAPI_KEY=your_key_here

# Start backend
uvicorn app.main:app --reload
```

Backend will be available at: **http://localhost:8000**

#### Frontend Setup (New Terminal)

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

Frontend will be available at: **http://localhost:5173**

## Verify Everything Works

### 1. Check Backend Health
```bash
curl http://localhost:8000/health
# Expected: {"status":"ok"}
```

### 2. View API Documentation
- Visit: http://localhost:8000/docs
- You'll see interactive Swagger UI for all endpoints

### 3. Test Search Endpoint
```bash
curl "http://localhost:8000/search?query=python%20programming"
```

### 4. Open Frontend
- Visit: http://localhost:5173
- Try a search!

## Docker Setup (Alternative)

If you have Docker installed:

```bash
cd /Users/abhishek9835/Desktop/projects/ir_abl

# Create .env file
echo "SERPAPI_KEY=your_key_here" > .env

# Start all services
docker-compose up

# In another terminal, verify
curl http://localhost:8000/health
```

Services will be available at:
- Backend API: http://localhost:8000
- Frontend: http://localhost:5173
- MongoDB: localhost:27017

## Troubleshooting

### MongoDB Connection Error

**Error**: `Error connecting to MongoDB`

**Solution**:
```bash
# Start MongoDB service
brew services start mongodb-community  # macOS
# or
docker run -d -p 27017:27017 mongo:7   # Docker

# Verify
mongosh
```

### SerpAPI Key Not Working

**Error**: `No results from SerpAPI`

**Solution**:
1. Check .env file has correct key: `cat backend/.env | grep SERPAPI`
2. Verify key at https://serpapi.com/dashboard
3. Check remaining quota
4. Try with different search query

### Port Already in Use

**Error**: `Address already in use: port 8000`

**Solution**:
```bash
# Find and kill process using port 8000
lsof -i :8000
kill -9 <PID>

# Or use different port
uvicorn app.main:app --port 8001
```

### Frontend Can't Connect to Backend

**Error**: `CORS error` or `Cannot reach localhost:8000`

**Solution**:
1. Make sure backend is running: `http://localhost:8000/health`
2. Check CORS settings in `backend/app/main.py`
3. Clear browser cache and reload
4. Check browser console for errors

### Virtual Environment Issues

**Error**: `command not found: python3` or `pip not found`

**Solution**:
```bash
# Verify Python installation
which python3
python3 --version

# Create new venv
rm -rf backend/venv
python3 -m venv backend/venv
source backend/venv/bin/activate
pip install -r backend/requirements.txt
```

## Common Commands

### Backend

```bash
# Start backend
cd backend && source venv/bin/activate && uvicorn app.main:app --reload

# Stop backend
Ctrl + C

# Install new package
pip install package_name

# Export dependencies
pip freeze > requirements.txt
```

### Frontend

```bash
# Start frontend dev server
cd frontend && npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Install new package
npm install package-name
```

### MongoDB

```bash
# Connect to database
mongosh

# List databases
show databases

# Use specific database
use search_engine_db

# List collections
show collections

# View documents
db.urls.find().limit(5)

# Count documents
db.urls.countDocuments()
```

## Project Structure Reminder

```
ir_abl/
├── backend/              # FastAPI application
│   ├── app/
│   │   ├── main.py      # Entry point
│   │   ├── routers/     # API endpoints
│   │   ├── services/    # Business logic
│   │   ├── db/          # Database operations
│   │   ├── models/      # Pydantic models
│   │   └── utils/       # Utilities
│   ├── requirements.txt
│   └── .env
│
├── frontend/             # React application
│   ├── src/
│   │   ├── main.jsx
│   │   ├── pages/       # Page components
│   │   ├── components/  # React components
│   │   ├── services/    # API client
│   │   └── styles/      # CSS files
│   ├── package.json
│   └── index.html
│
└── README.md
```

## Next Steps

1. **Explore the Code**: Check out the architecture in `README.md`
2. **Customize Ranking**: Edit weights in `backend/app/config.py`
3. **Add Features**: Consider adding filters, sorting, pagination
4. **Deploy**: Use Docker Compose or cloud platforms (Heroku, Vercel, etc.)

## Support

For detailed API documentation and architecture, see `README.md`

Happy searching! 🔍
