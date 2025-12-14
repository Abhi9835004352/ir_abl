# 🎯 Intelligent Search Engine - Start Here

Welcome to your completed Intelligent Search Engine project! 🚀

This document helps you navigate everything.

---

## 🚀 Quick Start (2 Minutes)

### For macOS/Linux:
```bash
cd /Users/abhishek9835/Desktop/projects/ir_abl
chmod +x setup.sh && ./setup.sh
# Edit backend/.env and add your SerpAPI key
cd backend && source venv/bin/activate && uvicorn app.main:app --reload
# In another terminal: cd frontend && npm run dev
```

### For Windows:
```bash
cd C:\Users\abhishek9835\Desktop\projects\ir_abl
setup.bat
# Edit backend\.env and add your SerpAPI key
cd backend && venv\Scripts\activate.bat && uvicorn app.main:app --reload
# In another terminal: cd frontend && npm run dev
```

**Then visit**: http://localhost:5173

---

## 📚 Documentation Guide

### 👶 Start With These (for first-time users)
1. **`GETTING_STARTED.md`** ← Start here for setup
2. **`QUICK_REFERENCE.md`** ← Quick commands and tips

### 📖 Main Documentation (for understanding the project)
1. **`README.md`** ← Project overview and features
2. **`PROJECT_SUMMARY.md`** ← What's been built

### 🔌 Technical Documentation (for developers)
1. **`API_REFERENCE.md`** ← API endpoints and examples
2. **`FILE_MANIFEST.md`** ← Project file structure

### 🚀 Deployment Documentation (for production)
1. **`DEPLOYMENT.md`** ← Production deployment options

---

## 🗺️ Documentation Map

```
📍 Are you a...

├─ 🌟 First-time user?
│  └─ Start: GETTING_STARTED.md
│
├─ 👨‍💼 Project manager?
│  └─ Start: README.md → PROJECT_SUMMARY.md
│
├─ 👨‍💻 Developer?
│  └─ Start: FILE_MANIFEST.md → API_REFERENCE.md
│
├─ 🔧 DevOps/Deployment?
│  └─ Start: DEPLOYMENT.md
│
├─ ⚡ In a hurry?
│  └─ Start: QUICK_REFERENCE.md
│
└─ 🤔 Not sure where to start?
   └─ Read: This file (INDEX.md)
```

---

## 🎯 Common Tasks & Where to Find Help

### Setup & Installation
- **Step-by-step setup**: `GETTING_STARTED.md`
- **Troubleshooting**: `GETTING_STARTED.md` → Troubleshooting section
- **Environment variables**: `GETTING_STARTED.md` → Step-by-Step Setup

### Using the Application
- **Frontend features**: `README.md` → UI Features section
- **Search API**: `API_REFERENCE.md` → Search endpoint
- **Click tracking**: `API_REFERENCE.md` → Click endpoint

### Development
- **Project structure**: `FILE_MANIFEST.md`
- **Ranking algorithm**: `README.md` → Ranking Algorithm section
- **Database schema**: `API_REFERENCE.md` → Data Models
- **Code modifications**: `QUICK_REFERENCE.md` → Key Files to Edit

### Deployment
- **Docker deployment**: `DEPLOYMENT.md` → Docker Compose
- **Heroku deployment**: `DEPLOYMENT.md` → Heroku Deployment
- **AWS deployment**: `DEPLOYMENT.md` → AWS Deployment
- **Best practices**: `DEPLOYMENT.md` → Production Best Practices

### Performance & Optimization
- **Performance tips**: `QUICK_REFERENCE.md` → Performance Tips
- **Database optimization**: `DEPLOYMENT.md` → Performance
- **Frontend optimization**: `DEPLOYMENT.md` → Performance

### Security
- **Security setup**: `DEPLOYMENT.md` → Security
- **Security checklist**: `QUICK_REFERENCE.md` → Security Checklist
- **Environment variables**: `GETTING_STARTED.md` → Environment variables

---

## 🏗️ Project Structure Quick Overview

```
ir_abl/
├── backend/          ← FastAPI + MongoDB backend
├── frontend/         ← React + Vite frontend
├── Documentation/    ← All guides and references
└── Infrastructure/   ← Docker, setup scripts
```

**Full structure**: See `FILE_MANIFEST.md`

---

## 🔗 Quick Links

| Resource | Purpose |
|----------|---------|
| `README.md` | 📖 Main documentation |
| `GETTING_STARTED.md` | 🚀 Setup guide |
| `API_REFERENCE.md` | 🔌 API endpoints |
| `DEPLOYMENT.md` | 🚀 Production setup |
| `PROJECT_SUMMARY.md` | ✅ What's built |
| `QUICK_REFERENCE.md` | ⚡ Quick commands |
| `FILE_MANIFEST.md` | 📁 File structure |

---

## 🌐 Access Points

Once running, access these URLs:

| URL | Purpose |
|-----|---------|
| http://localhost:5173 | 🎨 Frontend (main UI) |
| http://localhost:8000 | 🔌 Backend API |
| http://localhost:8000/docs | 📚 API Swagger UI |
| http://localhost:8000/health | ✅ Health check |

---

## 📋 What's Included

✅ **Backend**
- FastAPI application with async operations
- MongoDB integration
- SerpAPI search integration
- Web crawler
- TF-IDF ranking engine
- SEO scoring system
- Click tracking
- 2 REST API endpoints

✅ **Frontend**
- React application with Vite
- Search bar component
- Results display with scoring
- Responsive design
- Click tracking

✅ **Documentation**
- 7 comprehensive guide documents
- API reference with examples
- Deployment instructions
- Quick reference guide
- File manifest

✅ **Infrastructure**
- Docker & Docker Compose
- Setup scripts (macOS/Linux/Windows)
- Environment configuration
- Dockerfile for both services

---

## ⚡ Most Common Commands

### Backend
```bash
cd backend
source venv/bin/activate          # Activate venv
pip install -r requirements.txt   # Install packages
uvicorn app.main:app --reload     # Start server
```

### Frontend
```bash
cd frontend
npm install                        # Install packages
npm run dev                        # Start dev server
npm run build                      # Build for production
```

### Database
```bash
mongosh                           # Connect to MongoDB
show databases                    # List databases
db.urls.find().limit(5)          # View URLs
```
---

## 🔑 Key Concepts

### Search Ranking
The system combines three scores to rank results:
- **TF-IDF (55%)**: Relevance to query
- **SEO Score (25%)**: Page quality
- **Popularity (20%)**: Click count

Formula: `Final Score = 0.55×TF-IDF + 0.25×SEO + 0.20×Popularity`

### Data Flow
1. User searches → 2. SerpAPI fetches URLs → 3. Crawler extracts content
→ 4. Compute scores → 5. Rank results → 6. Display to user

### Click Tracking
Each click increments a URL's popularity, automatically boosting it in future searches.

---

## 🎓 Technology Stack Summary

| Layer | Technology |
|-------|-----------|
| **Frontend** | React 18 + Vite |
| **Backend** | FastAPI + Python |
| **Database** | MongoDB |
| **ML/Ranking** | scikit-learn (TF-IDF) |
| **Web Crawling** | BeautifulSoup4 |
| **Search API** | SerpAPI |
| **Deployment** | Docker |

---

## ❓ FAQ

**Q: I'm new to this project. Where do I start?**
→ Read `GETTING_STARTED.md` for setup instructions.

**Q: How do I modify the search ranking?**
→ Edit `backend/app/services/ranking_engine.py` and weights in `backend/app/config.py`.

**Q: How do I deploy this to production?**
→ Follow `DEPLOYMENT.md` for various cloud options.

**Q: Where are my search results stored?**
→ MongoDB database, check `FILE_MANIFEST.md` for schema.

**Q: How do I add a new feature?**
→ See `QUICK_REFERENCE.md` → Key Files to Edit.

**Q: Why aren't I getting search results?**
→ Check `GETTING_STARTED.md` → Troubleshooting section.

**Q: How do I get a SerpAPI key?**
→ Visit https://serpapi.com and sign up (free tier available).

---

## 🚨 Important Files

**Never commit to Git:**
- `backend/.env` (contains API keys)
- `venv/` directory
- `node_modules/` directory

**Always commit to Git:**
- All source code files
- `backend/.env.example` (template)
- All documentation files
- Configuration files

---

## 📞 Getting Help

1. **Setup Issues** → `GETTING_STARTED.md` → Troubleshooting
2. **API Questions** → `API_REFERENCE.md`
3. **Deployment Help** → `DEPLOYMENT.md`
4. **Quick Questions** → `QUICK_REFERENCE.md`
5. **Code Structure** → `FILE_MANIFEST.md`

---

## ✅ Verification Checklist

Before you start, verify:

- [ ] Python 3.9+ installed: `python3 --version`
- [ ] Node.js 16+ installed: `node --version`
- [ ] MongoDB running: `mongosh`
- [ ] SerpAPI key obtained: https://serpapi.com
- [ ] `.env` file created with key
- [ ] Backend starts: `http://localhost:8000/health`
- [ ] Frontend starts: `http://localhost:5173`

---

## 🎯 Next Steps

1. **Read** `GETTING_STARTED.md` for setup
2. **Configure** your SerpAPI key in `backend/.env`
3. **Run** setup script
4. **Start** backend and frontend
5. **Visit** http://localhost:5173
6. **Try** a search!

---

## 🎉 You're All Set!

Your Intelligent Search Engine is ready to use.

**Start here**: `GETTING_STARTED.md` →  **Then**: http://localhost:5173

---

**Questions?** Check the relevant documentation above.

**Happy coding!** 🚀

---

*Last updated: December 6, 2025*
