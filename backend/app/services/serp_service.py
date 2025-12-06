import logging
import requests
from typing import List, Dict, Optional
from app.config import SERPAPI_KEY, MAX_RESULTS_PER_QUERY, REQUEST_TIMEOUT
from urllib.parse import urljoin, urlparse

logger = logging.getLogger(__name__)


class SerpAPIService:
    """Service to fetch URLs from SerpAPI"""

    def __init__(self):
        self.api_key = SERPAPI_KEY
        self.base_url = "https://serpapi.com/search"

    def fetch_urls(self, query: str) -> List[Dict[str, str]]:
        """Fetch top URLs from SerpAPI for a query"""
        if not self.api_key:
            logger.warning("SerpAPI key not configured")
            return []

        try:
            params = {
                "q": query,
                "api_key": self.api_key,
                "num": MAX_RESULTS_PER_QUERY,
                "engine": "google",
            }

            response = requests.get(
                self.base_url, params=params, timeout=REQUEST_TIMEOUT
            )
            response.raise_for_status()

            data = response.json()
            urls = []

            # Extract organic results
            if "organic_results" in data:
                for result in data["organic_results"]:
                    urls.append(
                        {
                            "url": result.get("link", ""),
                            "title": result.get("title", ""),
                            "meta_description": result.get("snippet", ""),
                        }
                    )

            logger.info(f"✅ Fetched {len(urls)} URLs from SerpAPI for query: {query}")
            return urls

        except requests.exceptions.RequestException as e:
            logger.error(f"❌ SerpAPI request failed: {e}")
            return []
        except Exception as e:
            logger.error(f"❌ Error parsing SerpAPI response: {e}")
            return []

    def normalize_url(self, url: str) -> str:
        """Normalize URL (remove fragments, trailing slashes, etc.)"""
        try:
            parsed = urlparse(url)
            # Reconstruct without fragment
            normalized = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
            if parsed.query:
                normalized += f"?{parsed.query}"
            return normalized.rstrip("/")
        except:
            return url


def get_serp_service() -> SerpAPIService:
    """Factory function to get SerpAPI service"""
    return SerpAPIService()
