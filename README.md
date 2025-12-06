# 🔍 Intelligent Search Engine

A fully automated intelligent search engine built with FastAPI, React, MongoDB, and advanced IR techniques.

## 🎯 Features

- **TF-IDF Ranking**: Semantic relevance scoring using TF-IDF vectorization
- **SEO Scoring**: Automatic SEO quality assessment
- **Popularity Ranking**: Click-based popularity tracking
- **Intelligent Combination**: Weighted scoring algorithm
- **Web Crawling**: Automatic URL fetching and content extraction
- **SerpAPI Integration**: Top search results from Google
- **MongoDB Storage**: Persistent database for URLs and clicks
- **Modern Frontend**: React + Vite with real-time search

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│            FastAPI Backend (Port 8000)              │
├─────────────────────────────────────────────────────┤
│                                                      │
│  ┌──────────────┐        ┌──────────────────────┐  │
│  │ SerpAPI      │───────▶│ URL Crawler          │  │
│  │ Integration  │        │ (BeautifulSoup)      │  │
│  └──────────────┘        └──────────────────────┘  │
│                                  │                  │
│  ┌──────────────┐        ┌──────▼──────────────┐  │
│  │ TF-IDF       │───────▶│ SEO Scorer          │  │
│  │ Engine       │        │ (Metadata Analysis) │  │
│  └──────────────┘        └──────────────────────┘  │
│                                  │                  │
│         ┌────────────────────────▼──────────────┐  │
│         │    Final Ranking Engine               │  │
│         │  (Weighted Score Calculation)         │  │
│         └────────────────────────┬──────────────┘  │
│                                  │                  │
│              ┌───────────────────▼──────────────┐  │
│              │  MongoDB Database                │  │
│              │  - URLs Collection               │  │
│              │  - Click Logs Collection         │  │
│              │  - Search History Collection     │  │
│              └────────────────────────────────────┘ │
└─────────────────────────────────────────────────────┘
                        │
                        │ HTTP REST API
                        │
┌─────────────────────────────────────────────────────┐
│          React Frontend (Port 5173)                 │
├─────────────────────────────────────────────────────┤
│                                                      │
│  ┌────────────────┐        ┌──────────────────┐   │
│  │ Search Bar     │───────▶│ Results Page     │   │
│  │ Component      │        │ Component        │   │
│  └────────────────┘        └──────────────────┘   │
│                                  │                 │
│                    ┌─────────────▼─────────────┐  │
│                    │  Result Cards              │  │
│                    │  - Title                   │  │
│                    │  - URL                     │  │
│                    │  - SEO Score               │  │
│                    │  - Relevance %             │  │
│                    │  - Final Ranking Score     │  │
│                    └────────────────────────────┘  │
│                                                      │
└─────────────────────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Node.js 16+
- MongoDB running locally or remote connection string
- SerpAPI key (get from https://serpapi.com)

### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```
   
   Example `.env`:
   ```
   MONGO_URI=mongodb://localhost:27017
   DATABASE_NAME=search_engine_db
   SERPAPI_KEY=your_serpapi_key_here
   DEBUG=True
   ```

5. **Start backend server**
   ```bash
   uvicorn app.main:app --reload
   ```

   Backend will be available at: `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

   Frontend will be available at: `http://localhost:5173`

### Database Setup

Make sure MongoDB is running:

```bash
# If using macOS with Homebrew
brew services start mongodb-community

# Or using Docker
docker run -d -p 27017:27017 --name mongodb mongo:latest
```

## 📚 API Documentation

### Endpoints

#### 1. Search Endpoint
```
GET /search?query=<search_query>

Response:
[
  {
    "url_id": "ObjectId",
    "url": "https://example.com",
    "title": "Example Title",
    "meta_description": "Example description",
    "meta_score": 75.5,
    "relevance_score": 0.85,
    "popularity_score": 0.5,
    "final_score": 0.72
  },
  ...
]
```

#### 2. Click Logging Endpoint
```
POST /click

Request Body:
{
  "url_id": "ObjectId"
}

Response:
{
  "status": "success",
  "message": "Click recorded",
  "url_id": "ObjectId",
  "new_click_count": 42
}
```

## 🧮 Ranking Algorithm

The final ranking score is calculated as:

```
Final Score = (0.55 × TF-IDF Score) + (0.25 × SEO Score) + (0.20 × Popularity Score)
```

Where:

- **TF-IDF Score (0-1)**: Semantic relevance between query and webpage content
- **SEO Score (0-100)**: Quality assessment based on:
  - Title presence and length
  - Meta description quality
  - Meta keywords
  - Content length
  - URL structure
- **Popularity Score (0-1)**: Normalized click count

## 📁 Project Structure

```
ir_abl/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI app entry point
│   │   ├── config.py               # Configuration settings
│   │   ├── routers/
│   │   │   ├── search.py           # Search endpoint
│   │   │   └── click.py            # Click logging endpoint
│   │   ├── services/
│   │   │   ├── serp_service.py     # SerpAPI integration
│   │   │   ├── crawler.py          # Web crawler
│   │   │   ├── seo_scoring.py      # SEO scoring engine
│   │   │   ├── tfidf_engine.py     # TF-IDF vectorization
│   │   │   └── ranking_engine.py   # Final ranking engine
│   │   ├── db/
│   │   │   ├── connection.py       # MongoDB connection
│   │   │   └── queries.py          # Database operations
│   │   ├── models/
│   │   │   └── url.py              # Pydantic models
│   │   └── utils/
│   │       ├── text_cleaner.py     # Text processing
│   │       └── tokenizer.py        # Tokenization
│   ├── requirements.txt
│   ├── .env.example
│   └── .gitignore
│
├── frontend/
│   ├── src/
│   │   ├── main.jsx                # React entry point
│   │   ├── App.jsx                 # Root component
│   │   ├── pages/
│   │   │   └── ResultsPage.jsx     # Results page
│   │   ├── components/
│   │   │   ├── SearchBar.jsx       # Search input
│   │   │   └── ResultCard.jsx      # Result card display
│   │   ├── services/
│   │   │   └── api.js              # API client
│   │   └── styles/
│   │       ├── index.css           # Global styles
│   │       ├── App.css
│   │       ├── SearchBar.css
│   │       ├── ResultCard.css
│   │       └── ResultsPage.css
│   ├── index.html
│   ├── vite.config.js
│   ├── package.json
│   └── .gitignore
│
└── README.md
```

## 🔧 Configuration

### Backend Configuration (`app/config.py`)

```python
# Ranking weights
TFIDF_WEIGHT = 0.55          # TF-IDF relevance weight
SEO_WEIGHT = 0.25            # SEO score weight
POPULARITY_WEIGHT = 0.20     # Click popularity weight

# Settings
MAX_RESULTS_PER_QUERY = 20   # Results from SerpAPI
CRAWL_TIMEOUT = 10           # Seconds for URL crawl
REQUEST_TIMEOUT = 30         # Seconds for HTTP requests
```

### Database Collections

#### URLs Collection
```json
{
  "_id": ObjectId,
  "url": "string",
  "title": "string",
  "meta_description": "string",
  "meta_keywords": "string",
  "visible_text": "string (up to 5000 chars)",
  "meta_score": number (0-100),
  "tfidf_vector": [floats],
  "click_count": number,
  "last_updated": ISODate
}
```

#### Click Logs Collection
```json
{
  "_id": ObjectId,
  "url_id": ObjectId,
  "timestamp": ISODate
}
```

#### Search History Collection
```json
{
  "_id": ObjectId,
  "query": "string",
  "result_count": number,
  "timestamp": ISODate
}
```

## 🧪 Testing

### Backend Testing

```bash
cd backend

# Run a test search
curl "http://localhost:8000/search?query=machine%20learning"

# Log a click
curl -X POST http://localhost:8000/click \
  -H "Content-Type: application/json" \
  -d '{"url_id": "your_url_id_here"}'

# Health check
curl http://localhost:8000/health
```

## 📊 How It Works

### Search Flow

1. **User enters query** → Frontend sends to `/search` endpoint
2. **SerpAPI fetch** → Retrieves top 20 URLs from Google
3. **URL processing**:
   - Check if URL exists in database
   - If new: Crawl the page with BeautifulSoup
   - Extract title, meta description, keywords, content
4. **SEO scoring** → Analyze metadata quality
5. **TF-IDF vectorization**:
   - Create TF-IDF vectors for all documents
   - Compute cosine similarity with query
6. **Final ranking** → Combine three scores:
   - TF-IDF relevance (55%)
   - SEO quality (25%)
   - Click popularity (20%)
7. **Return ranked results** → Frontend displays top results

### Click Tracking

1. User clicks "Visit Website" on a result
2. Frontend calls `/click` endpoint with `url_id`
3. Backend increments `click_count` and logs event
4. Next search will boost popular pages in ranking

## 🚦 Performance Tips

1. **Caching**: URLs are cached in MongoDB after first crawl
2. **Timeout handling**: Failed crawls are logged but don't block results
3. **Text limiting**: Visible text capped at 5000 chars for storage efficiency
4. **Async operations**: MongoDB queries are async for better performance

## 🐛 Troubleshooting

### Backend won't start
- Check MongoDB is running: `mongosh` or `mongo`
- Check port 8000 is not in use: `lsof -i :8000`
- Verify `.env` file exists with correct values

### Frontend won't connect to backend
- Check backend is running on http://localhost:8000
- Check CORS settings in `app/main.py`
- Check browser console for error messages

### No results from search
- Verify SerpAPI key is set correctly
- Check internet connection
- Try a different search query

### MongoDB connection error
- Ensure MongoDB service is running
- Check connection string in `.env`
- Verify database name

## 📝 Environment Variables

Create `.env` file in `backend/` folder:

```
# MongoDB Configuration
MONGO_URI=mongodb://localhost:27017
DATABASE_NAME=search_engine_db

# SerpAPI Configuration
SERPAPI_KEY=your_key_here

# Debug Mode
DEBUG=True
```

## 📦 Dependencies

### Backend
- FastAPI: Web framework
- Uvicorn: ASGI server
- Motor: Async MongoDB driver
- pymongo: MongoDB client
- Requests: HTTP client
- BeautifulSoup4: HTML parsing
- scikit-learn: TF-IDF vectorization
- nltk: Natural language processing

### Frontend
- React 18: UI framework
- Vite: Build tool
- Axios: HTTP client

## 🎨 UI Features

- **Modern gradient design** with purple/blue theme
- **Responsive layout** for mobile and desktop
- **Real-time search** with loading indicators
- **Detailed result cards** showing:
  - Page title and URL
  - Meta description
  - Relevance percentage
  - SEO score with color-coded bar
  - Popularity percentage
  - Final ranking score
- **One-click website visit** with click tracking

## 🔐 Security Considerations

- Input validation on query strings
- Timeout protection for web crawls
- Error handling without exposing internals
- CORS enabled for frontend communication
- Async operations to prevent blocking

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## 📞 Support

For questions or issues, please open an issue on the GitHub repository.

---

**Built with ❤️ using FastAPI, React, and MongoDB**
# ir_abl
# ir_abl
# ir_abl
