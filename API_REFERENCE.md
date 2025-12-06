# API Reference

## Base URL

```
http://localhost:8000
```

## Endpoints

### 1. Health Check

Check if the API is running.

**Endpoint**
```
GET /health
```

**Response**
```json
{
  "status": "ok"
}
```

---

### 2. Search

Perform an intelligent search with ranking.

**Endpoint**
```
GET /search?query=<search_query>
```

**Parameters**
- `query` (required): Search query string (1-200 characters)

**Example Request**
```bash
curl "http://localhost:8000/search?query=machine%20learning%20python"
```

**Response**
```json
[
  {
    "url_id": "507f1f77bcf86cd799439011",
    "url": "https://example.com/ml",
    "title": "Machine Learning with Python",
    "meta_description": "Learn machine learning concepts and libraries",
    "meta_score": 85.5,
    "relevance_score": 0.92,
    "popularity_score": 0.45,
    "final_score": 0.78
  },
  {
    "url_id": "507f1f77bcf86cd799439012",
    "url": "https://tutorial.example.com/ml",
    "title": "Python ML Tutorial",
    "meta_description": "Complete guide to machine learning",
    "meta_score": 72.3,
    "relevance_score": 0.88,
    "popularity_score": 0.30,
    "final_score": 0.71
  }
]
```

**Response Fields**
- `url_id`: Unique MongoDB ObjectId for tracking clicks
- `url`: The webpage URL
- `title`: Page title extracted from HTML
- `meta_description`: Meta description tag from HTML
- `meta_score`: SEO quality score (0-100)
- `relevance_score`: TF-IDF relevance to query (0-1)
- `popularity_score`: Normalized click count (0-1)
- `final_score`: Combined ranking score (0-1)

**Status Codes**
- `200`: Success
- `422`: Invalid query parameter
- `500`: Server error

---

### 3. Log Click

Record a user click on a search result.

**Endpoint**
```
POST /click
```

**Request Body**
```json
{
  "url_id": "507f1f77bcf86cd799439011"
}
```

**Example Request**
```bash
curl -X POST http://localhost:8000/click \
  -H "Content-Type: application/json" \
  -d '{"url_id": "507f1f77bcf86cd799439011"}'
```

**Response**
```json
{
  "status": "success",
  "message": "Click recorded",
  "url_id": "507f1f77bcf86cd799439011",
  "new_click_count": 42
}
```

**Status Codes**
- `200`: Click recorded
- `404`: URL not found
- `422`: Invalid request body
- `500`: Server error

---

## Data Models

### URL Model

```json
{
  "_id": "ObjectId",
  "url": "string",
  "title": "string (0-200 chars)",
  "meta_description": "string (0-500 chars)",
  "meta_keywords": "string (0-200 chars)",
  "visible_text": "string (0-5000 chars)",
  "meta_score": "float (0-100)",
  "tfidf_vector": "[float, ...]",
  "click_count": "integer (0+)",
  "last_updated": "ISO 8601 timestamp"
}
```

### Click Log Model

```json
{
  "_id": "ObjectId",
  "url_id": "ObjectId",
  "timestamp": "ISO 8601 timestamp"
}
```

### Search History Model

```json
{
  "_id": "ObjectId",
  "query": "string",
  "result_count": "integer",
  "timestamp": "ISO 8601 timestamp"
}
```

---

## Ranking Algorithm

The search results are ranked using a combination of three scores:

### Formula

```
Final Score = (0.55 × TF-IDF Score) + (0.25 × SEO Score) + (0.20 × Popularity Score)
```

### Score Components

#### 1. TF-IDF Relevance Score (0-1)

Measures semantic similarity between the query and page content.

- Uses scikit-learn's TfidfVectorizer
- Computes cosine similarity
- Higher score = more relevant to query

#### 2. SEO Meta Score (0-100)

Measures page quality based on metadata:

- **Title Quality** (0-20): Length between 10-50 chars, reasonable content
- **Meta Description** (0-20): Optimal length 50-160 chars
- **Keywords** (0-15): Presence and reasonableness of keywords
- **Content Length** (0-25): 5000+ chars = full score, scales down
- **URL Structure** (0-10): Hyphens preferred, minimal parameters
- **Path Depth** (0-10): More meaningful path segments = higher score

#### 3. Popularity Score (0-1)

Based on click-through rate normalized to maximum observed clicks.

```
Popularity Score = click_count / max_click_count
```

---

## Usage Examples

### Python

```python
import requests

# Search
response = requests.get(
    "http://localhost:8000/search",
    params={"query": "machine learning"}
)
results = response.json()

for result in results:
    print(f"{result['title']} - {result['final_score']:.2f}")

# Log click
click_response = requests.post(
    "http://localhost:8000/click",
    json={"url_id": results[0]["url_id"]}
)
print(click_response.json())
```

### JavaScript/Node.js

```javascript
// Search
const response = await fetch(
  'http://localhost:8000/search?query=machine%20learning'
);
const results = await response.json();

results.forEach(result => {
  console.log(`${result.title} - ${result.final_score.toFixed(2)}`);
});

// Log click
const clickResponse = await fetch(
  'http://localhost:8000/click',
  {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ url_id: results[0].url_id })
  }
);
const clickData = await clickResponse.json();
console.log(clickData);
```

### cURL

```bash
# Search
curl -s "http://localhost:8000/search?query=python" | jq '.'

# Log click
curl -X POST http://localhost:8000/click \
  -H "Content-Type: application/json" \
  -d '{"url_id": "YOUR_URL_ID"}' | jq '.'
```

---

## Error Handling

### Error Response Format

```json
{
  "detail": "Error message explaining what went wrong"
}
```

### Common Errors

**Invalid Query**
```json
{
  "detail": [
    {
      "loc": ["query", "query"],
      "msg": "ensure this value has at least 1 characters",
      "type": "value_error.any_str.min_length"
    }
  ]
}
```

**URL Not Found**
```json
{
  "detail": "URL not found"
}
```

**Server Error**
```json
{
  "detail": "Database connection failed"
}
```

---

## Rate Limiting

Currently no rate limiting is implemented. For production, consider:

- Implementing per-IP rate limiting
- Cache frequent searches
- Use Redis for caching

---

## Performance

### Response Times

- **Search**: 2-5 seconds (includes SerpAPI call + crawling)
- **Cached Search**: <100ms
- **Click Logging**: <50ms

### Database Indexes

- `urls.url` (unique): For fast URL lookup
- `click_logs.url_id`: For click aggregation
- `search_history.query`: For search analytics

---

## Interactive API Documentation

Visit **http://localhost:8000/docs** for interactive Swagger UI where you can:

- Test all endpoints
- See live request/response examples
- Download OpenAPI specification

---

## Pagination (Future)

For large result sets, consider adding:

```
GET /search?query=...&page=1&limit=10
```

Response would include:

```json
{
  "results": [...],
  "total": 100,
  "page": 1,
  "pages": 10
}
```

---

## Webhooks (Future)

For real-time updates when new results are indexed:

```
POST /webhooks/subscribe
{
  "url": "https://your-server.com/callback",
  "events": ["index_complete"]
}
```

---

## API Versioning

Current API version: **v1**

Future versions would use:
```
GET /api/v2/search
```

---

## Support

For issues or questions about the API, please refer to:
- Main README: `README.md`
- Getting Started: `GETTING_STARTED.md`
- Source Code: `backend/app/routers/`
