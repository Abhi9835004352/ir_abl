import logging
import requests
from typing import Dict, Optional
from bs4 import BeautifulSoup
from app.config import CRAWL_TIMEOUT, REQUEST_TIMEOUT
from app.utils.text_cleaner import extract_visible_text, clean_text

logger = logging.getLogger(__name__)


class WebCrawler:
    """Service to crawl and extract content from URLs"""

    def __init__(self):
        self.timeout = CRAWL_TIMEOUT
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

    def crawl_url(self, url: str) -> Optional[Dict[str, str]]:
        """Fetch and parse URL content"""
        try:
            response = requests.get(
                url, headers=self.headers, timeout=REQUEST_TIMEOUT, allow_redirects=True
            )
            response.raise_for_status()
            response.encoding = response.apparent_encoding or "utf-8"

            html_content = response.text
            return self._parse_html(html_content, url)

        except requests.exceptions.Timeout:
            logger.warning(f"⏱️ Timeout crawling {url}")
            return None
        except requests.exceptions.RequestException as e:
            logger.warning(f"⚠️ Error crawling {url}: {e}")
            return None
        except Exception as e:
            logger.error(f"❌ Unexpected error crawling {url}: {e}")
            return None

    def _parse_html(self, html_content: str, url: str) -> Dict[str, str]:
        """Parse HTML and extract metadata and content"""
        try:
            soup = BeautifulSoup(html_content, "html.parser")

            # Extract title
            title = ""
            if soup.title:
                title = soup.title.string or ""
            title_tag = soup.find("meta", {"property": "og:title"})
            if title_tag:
                title = title_tag.get("content", title)

            # Extract meta description
            meta_description = ""
            meta_tag = soup.find("meta", {"name": "description"})
            if meta_tag:
                meta_description = meta_tag.get("content", "")

            # Extract keywords
            meta_keywords = ""
            keywords_tag = soup.find("meta", {"name": "keywords"})
            if keywords_tag:
                meta_keywords = keywords_tag.get("content", "")

            # Extract visible text
            visible_text = extract_visible_text(html_content)

            # Limit visible text to first 5000 characters for storage efficiency
            visible_text = visible_text[:5000]

            logger.info(f"✅ Crawled {url}")

            return {
                "title": clean_text(title)[:200],
                "meta_description": clean_text(meta_description)[:500],
                "meta_keywords": clean_text(meta_keywords)[:200],
                "visible_text": visible_text,
            }

        except Exception as e:
            logger.error(f"❌ Error parsing HTML: {e}")
            return {
                "title": "",
                "meta_description": "",
                "meta_keywords": "",
                "visible_text": "",
            }


def get_crawler() -> WebCrawler:
    """Factory function to get WebCrawler"""
    return WebCrawler()
