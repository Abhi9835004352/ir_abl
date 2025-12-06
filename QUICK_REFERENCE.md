# 📚 Quick Reference Guide

## 🚀 Start Here

```bash
# 1. Clone/Setup project
cd /Users/abhishek9835/Desktop/projects/ir_abl

# 2. Run setup script
chmod +x setup.sh && ./setup.sh

# 3. Configure
# Edit backend/.env and add your SerpAPI key

# 4. Start backend (Terminal 1)
cd backend
source venv/bin/activate
uvicorn app.main:app --reload

# 5. Start frontend (Terminal 2)
cd frontend
npm run dev

# 6. Open browser
# http://localhost:5173
```

---

## 📁 File Location Quick Links

### Backend
- **Main App**: `backend/app/main.py`
- **Config**: `backend/app/config.py`
- **Search Endpoint**: `backend/app/routers/search.py`
- **Click Endpoint**: `backend/app/routers/click.py`
- **Database**: `backend/app/db/`

### Frontend
- **Home Page**: `frontend/src/pages/ResultsPage.jsx`
- **Search Bar**: `frontend/src/components/SearchBar.jsx`
- **Result Cards**: `frontend/src/components/ResultCard.jsx`
- **Styles**: `frontend/src/styles/`

### Configuration
- **Backend Env**: `backend/.env.example`
- **Requirements**: `backend/requirements.txt`
- **Dependencies**: `frontend/package.json`

---

## 🔧 Common Tasks

### Add a New Python Dependency
```bash
cd backend
source venv/bin/activate
pip install package_name
pip freeze > requirements.txt
```

### Add a New NPM Package
```bash
cd frontend
npm install package-name
```

### Update Ranking Weights
Edit `backend/app/config.py`:
```python
TFIDF_WEIGHT = 0.55      # Change these values
SEO_WEIGHT = 0.25
POPULARITY_WEIGHT = 0.20
```

### View MongoDB Data
```bash
mongosh
use search_engine_db
db.urls.find().limit(5)
db.click_logs.find().limit(5)
```

### Kill Port Process
```bash
# Port 8000 (backend)
lsof -i :8000 | grep LISTEN | awk '{print $2}' | xargs kill -9

# Port 5173 (frontend)
lsof -i :5173 | grep LISTEN | awk '{print $2}' | xargs kill -9

# Port 27017 (MongoDB)
lsof -i :27017 | grep LISTEN | awk '{print $2}' | xargs kill -9
```

---

## 🧪 Testing

### Test Backend
```bash
# Health check
curl http://localhost:8000/health

# Search
curl "http://localhost:8000/search?query=python"

# Log click
curl -X POST http://localhost:8000/click \
  -H "Content-Type: application/json" \
  -d '{"url_id": "YOUR_URL_ID"}'
```

### View API Docs
```
http://localhost:8000/docs
```

---

## 📊 Database Queries

### Count documents
```mongodb
db.urls.countDocuments()
db.click_logs.countDocuments()
db.search_history.countDocuments()
```

### Find top URLs by clicks
```mongodb
db.urls.find().sort({click_count: -1}).limit(10)
```

### Find URLs by domain
```mongodb
db.urls.find({url: /example.com/})
```

### Clear all data
```mongodb
db.urls.deleteMany({})
db.click_logs.deleteMany({})
db.search_history.deleteMany({})
```

---

## 🐛 Debug Mode

### Enable verbose logging
```python
# In backend/app/main.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check environment variables
```bash
cd backend
cat .env
```

### View request/response
```bash
# Backend API docs
http://localhost:8000/docs
```

---

## 📱 Frontend Customization

### Change theme colors
Edit `frontend/src/styles/index.css`:
```css
body {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

### Change search bar placeholder
Edit `frontend/src/components/SearchBar.jsx`:
```jsx
placeholder="Your custom text here..."
```

### Modify result card layout
Edit `frontend/src/components/ResultCard.jsx`

---

## 🚀 Deployment Quick Steps

### Docker
```bash
docker-compose up
```

### Heroku Backend
```bash
heroku create app-name
git push heroku main
```

### Vercel Frontend
```bash
vercel
```

---

## 📝 Environment Variables

### Backend `.env`
```
MONGO_URI=mongodb://localhost:27017
DATABASE_NAME=search_engine_db
SERPAPI_KEY=your_key_here
DEBUG=True
```

### Frontend `.env.local`
```
VITE_API_URL=http://localhost:8000
```

---

## 🆘 Error Messages

| Error | Solution |
|-------|----------|
| `Address already in use` | Kill process: `lsof -i :PORT` → `kill -9 PID` |
| `MongoDB connection failed` | Start MongoDB: `brew services start mongodb-community` |
| `SerpAPI quota exceeded` | Wait or upgrade plan at https://serpapi.com |
| `CORS error` | Backend CORS is configured in `app/main.py` |
| `Module not found` | Install: `pip install -r requirements.txt` or `npm install` |

---

## 📞 Documentation Links

| Document | Purpose |
|----------|---------|
| `README.md` | Project overview |
| `GETTING_STARTED.md` | Setup guide |
| `API_REFERENCE.md` | API documentation |
| `DEPLOYMENT.md` | Production deployment |
| `PROJECT_SUMMARY.md` | Completion summary |

---

## 🎯 Key Files to Edit

### Change Ranking Algorithm
- File: `backend/app/services/ranking_engine.py`
- Method: `calculate_final_score()`

### Change SEO Scoring
- File: `backend/app/services/seo_scoring.py`
- Method: `calculate_score()`

### Change TF-IDF Settings
- File: `backend/app/services/tfidf_engine.py`
- Method: `__init__()` - TfidfVectorizer params

### Change Frontend Appearance
- Files: `frontend/src/styles/*.css`

---

## ⚡ Performance Tips

1. **Cache searches** → Redis
2. **Index MongoDB** → Query optimization
3. **Optimize images** → Smaller frontend bundle
4. **Lazy load results** → Pagination
5. **Use CDN** → Static files

---

## 🔐 Security Checklist

- [ ] `.env` files not committed to git
- [ ] SerpAPI key has minimal scope
- [ ] MongoDB has authentication
- [ ] HTTPS enabled in production
- [ ] API rate limiting implemented
- [ ] Input validation on all endpoints
- [ ] CORS properly configured

---

## 📈 Monitoring

### Backend Logs
```bash
cd backend && tail -f app.log
```

### Frontend Errors
```javascript
// Browser console (F12)
console.error()  // Shows errors
console.log()    // Show info
```

### Database Performance
```bash
mongosh
db.admin.command({currentOp: true})
```

---

## 🔄 Restart Services

### Backend
```bash
# Stop: Ctrl+C
# Start: uvicorn app.main:app --reload
```

### Frontend
```bash
# Stop: Ctrl+C
# Start: npm run dev
```

### MongoDB
```bash
brew services restart mongodb-community
```

---

## 💾 Backup Commands

```bash
# Backup MongoDB
mongodump --out ./backup

# Restore MongoDB
mongorestore ./backup

# Backup project
tar -czf project-backup.tar.gz .
```

---

## 🚀 Deploy Commands

```bash
# Docker
docker-compose up -d

# Heroku
git push heroku main

# Vercel
vercel

# AWS
aws deploy
```

---

## 📚 Learning Resources

| Topic | Resource |
|-------|----------|
| FastAPI | https://fastapi.tiangolo.com/tutorial/ |
| React | https://react.dev/learn |
| MongoDB | https://docs.mongodb.com/manual/ |
| TF-IDF | https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting |
| Vite | https://vitejs.dev/guide/ |

---

## 🎊 Success Checklist

- [ ] Backend running on http://localhost:8000
- [ ] Frontend running on http://localhost:5173
- [ ] MongoDB connected
- [ ] Search working
- [ ] Results displaying
- [ ] Click tracking working
- [ ] API docs accessible

---

**Happy coding! 🚀**

*For more details, see the full documentation files.*
