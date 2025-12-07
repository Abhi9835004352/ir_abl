from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGO_URI, DATABASE_NAME
import logging

logger = logging.getLogger(__name__)

client = None
db = None


async def connect_to_mongo():
    """Initialize MongoDB connection"""
    global client, db
    try:
        # Connect to MongoDB Atlas with proper SSL
        client = AsyncIOMotorClient(
            MONGO_URI,
            serverSelectionTimeoutMS=15000,
            connectTimeoutMS=15000,
            retryWrites=True
        )
        db = client[DATABASE_NAME]
        
        # Test connection
        await db.command("ping")
        logger.info("✅ Connected to MongoDB Atlas")
        
        # Create collections
        collections = await db.list_collection_names()
        
        if "urls" not in collections:
            await db.create_collection("urls")
            await db["urls"].create_index("url", unique=True)
            logger.info("✅ Created 'urls' collection")
        
        if "click_logs" not in collections:
            await db.create_collection("click_logs")
            logger.info("✅ Created 'click_logs' collection")
        
        if "search_history" not in collections:
            await db.create_collection("search_history")
            logger.info("✅ Created 'search_history' collection")
            
    except Exception as e:
        logger.error(f"❌ Failed to connect to MongoDB: {e}")
        raise


async def close_mongo():
    """Close MongoDB connection"""
    global client
    if client:
        client.close()
        logger.info("✅ MongoDB connection closed")


def get_collection(collection_name: str):
    """Get a MongoDB collection"""
    return db[collection_name]
