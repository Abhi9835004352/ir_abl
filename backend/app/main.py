from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.db.connection import connect_to_mongo, close_mongo
from app.routers import search, click

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Intelligent Search Engine",
    description="TF-IDF + SEO + Popularity based ranking",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(search.router, tags=["search"])
app.include_router(click.router, tags=["click"])


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}


@app.on_event("startup")
async def startup():
    """Initialize on startup"""
    logger.info("🚀 Starting Intelligent Search Engine...")
    await connect_to_mongo()
    logger.info("✅ Application startup complete")


@app.on_event("shutdown")
async def shutdown():
    """Cleanup on shutdown"""
    logger.info("🛑 Shutting down...")
    await close_mongo()
    logger.info("✅ Application shutdown complete")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
