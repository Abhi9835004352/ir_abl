import os
from dotenv import load_dotenv

load_dotenv()

# Environment Variables
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "search_engine_db")
SERPAPI_KEY = os.getenv("SERPAPI_KEY", "")
DEBUG = os.getenv("DEBUG", "True") == "True"

# Ranking weights
TFIDF_WEIGHT = 0.55
SEO_WEIGHT = 0.25
POPULARITY_WEIGHT = 0.20

# Settings
MAX_RESULTS_PER_QUERY = 20
CRAWL_TIMEOUT = 10
REQUEST_TIMEOUT = 30
