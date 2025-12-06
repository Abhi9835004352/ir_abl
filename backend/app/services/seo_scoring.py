import logging
from typing import Dict, Optional
import re

logger = logging.getLogger(__name__)


class SEOScorer:
    """Compute SEO meta score based on various metrics"""

    @staticmethod
    def calculate_score(
        title: str,
        meta_description: str,
        meta_keywords: str,
        visible_text: str,
        url: str,
    ) -> float:
        """
        Calculate SEO score on a scale of 0-100

        Scoring criteria:
        - Title present and reasonable length: 20 points
        - Meta description present and reasonable length: 20 points
        - Meta keywords present: 15 points
        - Content length: 25 points
        - URL structure (hyphens, no underscores): 10 points
        - Keyword in title: 10 points (bonus)
        """
        score = 0.0

        # Title score (0-20)
        if title and len(title) > 10:
            score += min(20, len(title) / 5)  # Max 20 for reasonable title length

        # Meta description score (0-20)
        if meta_description and 50 <= len(meta_description) <= 160:
            score += 20
        elif meta_description and 20 < len(meta_description) < 200:
            score += 15

        # Meta keywords score (0-15)
        if meta_keywords and len(meta_keywords) > 10:
            score += 15

        # Content length score (0-25)
        if visible_text:
            text_len = len(visible_text)
            if text_len > 5000:
                score += 25
            elif text_len > 2000:
                score += 20
            elif text_len > 500:
                score += 15
            elif text_len > 100:
                score += 10

        # URL structure score (0-10)
        score += SEOScorer._score_url_structure(url)

        # Ensure score is within 0-100
        return min(100.0, max(0.0, score))

    @staticmethod
    def _score_url_structure(url: str) -> float:
        """Score URL structure quality"""
        score = 0.0

        # Prefer hyphens over underscores
        hyphens = url.count("-")
        underscores = url.count("_")
        if hyphens > underscores:
            score += 5

        # Prefer clean URLs without excessive parameters
        if url.count("?") == 0:
            score += 3
        elif url.count("?") == 1 and url.count("&") < 3:
            score += 2

        # Prefer meaningful paths
        path_parts = url.split("/")
        if len(path_parts) > 2:  # Domain + at least one path
            score += 2

        return min(10.0, score)


def get_seo_scorer() -> SEOScorer:
    """Factory function to get SEO scorer"""
    return SEOScorer()
