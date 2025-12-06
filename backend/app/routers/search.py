import logging
from fastapi import APIRouter, Query, HTTPException
from typing import List
from app.models.url import SearchResultModel
from app.services.serp_service import get_serp_service
from app.services.crawler import get_crawler
from app.services.seo_scoring import get_seo_scorer
from app.services.tfidf_engine import get_tfidf_engine
from app.services.ranking_engine import get_ranking_engine
from app.db import queries
from app.utils.text_cleaner import clean_text

logger = logging.getLogger(__name__)

router = APIRouter()

serp_service = get_serp_service()
crawler = get_crawler()
seo_scorer = get_seo_scorer()
tfidf_engine = get_tfidf_engine()
ranking_engine = get_ranking_engine()


@router.get("/search", response_model=List[SearchResultModel])
async def search(query: str = Query(..., min_length=1, max_length=200)):
    """
    Main search endpoint

    1. Fetch URLs from SerpAPI
    2. Crawl each URL
    3. Compute SEO scores
    4. Compute TF-IDF vectors
    5. Rank results
    6. Return ranked results
    """
    try:
        logger.info(f"🔍 Processing search query: {query}")

        # Step 1: Fetch URLs from SerpAPI
        serp_results = serp_service.fetch_urls(query)
        if not serp_results:
            logger.warning(f"⚠️ No results from SerpAPI for query: {query}")
            return []

        logger.info(f"📍 Got {len(serp_results)} URLs from SerpAPI")

        # Step 2 & 3: Crawl URLs and compute metadata
        crawled_data = []
        for result in serp_results:
            url = result.get("url", "")
            if not url:
                continue

            # Check if URL already in database
            existing_url = await queries.get_url_by_string(url)

            if existing_url:
                crawled_data.append(existing_url)
                logger.info(f"📚 Using cached data for {url}")
            else:
                # Crawl the URL
                crawl_result = crawler.crawl_url(url)
                if not crawl_result:
                    logger.warning(f"⚠️ Failed to crawl {url}")
                    continue

                # Compute SEO score
                meta_score = seo_scorer.calculate_score(
                    crawl_result.get("title", ""),
                    crawl_result.get("meta_description", ""),
                    crawl_result.get("meta_keywords", ""),
                    crawl_result.get("visible_text", ""),
                    url,
                )

                # Prepare URL data for insertion
                url_data = {
                    "url": url,
                    "title": crawl_result.get("title", result.get("title", "")),
                    "meta_description": crawl_result.get(
                        "meta_description", result.get("meta_description", "")
                    ),
                    "meta_keywords": crawl_result.get("meta_keywords", ""),
                    "visible_text": crawl_result.get("visible_text", ""),
                    "meta_score": meta_score,
                    "click_count": 0,
                }

                # Insert into database
                url_id = await queries.insert_url(url_data)
                if url_id:
                    url_data["_id"] = url_id
                    crawled_data.append(url_data)
                    logger.info(f"💾 Inserted new URL to DB: {url}")

        if not crawled_data:
            logger.warning(f"⚠️ No URLs were successfully processed")
            return []

        logger.info(f"✅ Crawled and stored {len(crawled_data)} URLs")

        # Step 4: Prepare data for TF-IDF ranking
        documents = []
        doc_ids = []
        meta_scores = []
        click_counts = []

        for item in crawled_data:
            # Combine title, description, keywords, and visible text for TF-IDF
            combined_text = " ".join(
                [
                    item.get("title", ""),
                    item.get("meta_description", ""),
                    item.get("meta_keywords", ""),
                    item.get("visible_text", "")[:2000],  # Limit text size
                ]
            )

            documents.append(clean_text(combined_text))
            doc_ids.append(str(item.get("_id", "")))
            meta_scores.append(item.get("meta_score", 0.0))
            click_counts.append(item.get("click_count", 0))

        # Fit TF-IDF and rank
        tfidf_engine.fit(documents)
        ranked_docs = tfidf_engine.rank_documents(query, documents, doc_ids)

        # Step 5: Combine scores and rank
        results = []
        max_click_count = max(click_counts) if click_counts else 1

        for url_id, relevance_score in ranked_docs:
            # Find the original data
            url_data = next(
                (d for d in crawled_data if str(d.get("_id", "")) == url_id), None
            )
            if not url_data:
                continue

            result = {
                "url_id": url_id,
                "url": url_data.get("url", ""),
                "title": url_data.get("title", ""),
                "meta_description": url_data.get("meta_description", ""),
                "meta_score": url_data.get("meta_score", 0.0),
                "relevance_score": float(relevance_score),
                "click_count": url_data.get("click_count", 0),
            }
            results.append(result)

        # Apply final ranking
        final_results = ranking_engine.rank_results(results, max_click_count)

        # Log search query
        await queries.log_search_query(query, len(final_results))

        logger.info(
            f"✅ Successfully returned {len(final_results)} ranked results for query: {query}"
        )

        return final_results

    except Exception as e:
        logger.error(f"❌ Search error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
