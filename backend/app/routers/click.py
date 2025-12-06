import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.db import queries

logger = logging.getLogger(__name__)

router = APIRouter()


class ClickRequest(BaseModel):
    url_id: str


@router.post("/click")
async def log_click(request: ClickRequest):
    """
    Log a click on a search result

    Updates popularity score for the URL
    """
    try:
        url_id = request.url_id

        # Verify URL exists
        url_data = await queries.get_url_by_id(url_id)
        if not url_data:
            raise HTTPException(status_code=404, detail="URL not found")

        # Increment click count
        success = await queries.increment_click_count(url_id)
        if not success:
            raise HTTPException(status_code=500, detail="Failed to update click count")

        # Log the click event
        await queries.log_click(url_id)

        logger.info(f"✅ Logged click for URL: {url_data.get('url')}")

        return {
            "status": "success",
            "message": "Click recorded",
            "url_id": url_id,
            "new_click_count": url_data.get("click_count", 0) + 1,
        }

    except Exception as e:
        logger.error(f"❌ Click logging error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
