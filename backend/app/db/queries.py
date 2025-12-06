from typing import Optional, List, Dict, Any
from bson import ObjectId
from app.db.connection import get_collection
from app.models.url import URLModel
import logging

logger = logging.getLogger(__name__)


async def insert_url(url_data: Dict[str, Any]) -> Optional[str]:
    """Insert new URL into database"""
    try:
        urls_collection = get_collection("urls")

        # Check if URL already exists
        existing = await urls_collection.find_one({"url": url_data["url"]})
        if existing:
            return str(existing["_id"])

        result = await urls_collection.insert_one(url_data)
        return str(result.inserted_id)
    except Exception as e:
        logger.error(f"Error inserting URL: {e}")
        return None


async def get_url_by_id(url_id: str) -> Optional[Dict[str, Any]]:
    """Fetch URL by ID"""
    try:
        urls_collection = get_collection("urls")
        return await urls_collection.find_one({"_id": ObjectId(url_id)})
    except Exception as e:
        logger.error(f"Error fetching URL: {e}")
        return None


async def get_url_by_string(url: str) -> Optional[Dict[str, Any]]:
    """Fetch URL by URL string"""
    try:
        urls_collection = get_collection("urls")
        return await urls_collection.find_one({"url": url})
    except Exception as e:
        logger.error(f"Error fetching URL: {e}")
        return None


async def update_url_metadata(url_id: str, metadata: Dict[str, Any]) -> bool:
    """Update URL metadata, vector, and score"""
    try:
        urls_collection = get_collection("urls")
        result = await urls_collection.update_one(
            {"_id": ObjectId(url_id)}, {"$set": metadata}
        )
        return result.modified_count > 0
    except Exception as e:
        logger.error(f"Error updating URL: {e}")
        return False


async def increment_click_count(url_id: str) -> bool:
    """Increment click count for a URL"""
    try:
        urls_collection = get_collection("urls")
        result = await urls_collection.update_one(
            {"_id": ObjectId(url_id)}, {"$inc": {"click_count": 1}}
        )
        return result.modified_count > 0
    except Exception as e:
        logger.error(f"Error incrementing click count: {e}")
        return False


async def log_click(url_id: str) -> bool:
    """Log a click event"""
    try:
        click_logs_collection = get_collection("click_logs")
        await click_logs_collection.insert_one(
            {
                "url_id": ObjectId(url_id),
                "timestamp": __import__("datetime").datetime.utcnow(),
            }
        )
        return True
    except Exception as e:
        logger.error(f"Error logging click: {e}")
        return False


async def get_all_urls() -> List[Dict[str, Any]]:
    """Fetch all URLs from database"""
    try:
        urls_collection = get_collection("urls")
        return await urls_collection.find({}).to_list(None)
    except Exception as e:
        logger.error(f"Error fetching URLs: {e}")
        return []


async def log_search_query(query: str, result_count: int) -> bool:
    """Log search query for analytics"""
    try:
        search_history_collection = get_collection("search_history")
        await search_history_collection.insert_one(
            {
                "query": query,
                "result_count": result_count,
                "timestamp": __import__("datetime").datetime.utcnow(),
            }
        )
        return True
    except Exception as e:
        logger.error(f"Error logging search: {e}")
        return False
