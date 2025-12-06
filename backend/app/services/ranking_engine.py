import logging
from typing import List, Dict, Tuple, Optional
from app.config import TFIDF_WEIGHT, SEO_WEIGHT, POPULARITY_WEIGHT

logger = logging.getLogger(__name__)


class RankingEngine:
    """Final ranking engine combining all scores"""

    @staticmethod
    def calculate_final_score(
        tfidf_score: float, seo_score: float, popularity_score: float
    ) -> float:
        """
        Calculate final ranking score

        Formula:
        Final Score = (0.55 × TF-IDF) + (0.25 × SEO) + (0.20 × Popularity)

        Args:
            tfidf_score: TF-IDF relevance score (0-1)
            seo_score: SEO meta score (0-100), normalized to 0-1
            popularity_score: Click popularity score (0-1)

        Returns:
            Final score (0-1)
        """
        # Normalize SEO score to 0-1
        seo_normalized = min(1.0, max(0.0, seo_score / 100.0))

        # Calculate weighted sum
        final_score = (
            TFIDF_WEIGHT * min(1.0, max(0.0, tfidf_score))
            + SEO_WEIGHT * seo_normalized
            + POPULARITY_WEIGHT * min(1.0, max(0.0, popularity_score))
        )

        return min(1.0, max(0.0, final_score))

    @staticmethod
    def rank_results(results: List[Dict], max_click_count: int = 100) -> List[Dict]:
        """
        Rank search results and sort them

        Args:
            results: List of result dictionaries with scores
            max_click_count: Maximum click count for normalization

        Returns:
            Sorted list of results by final score
        """
        try:
            ranked = []

            for result in results:
                # Normalize popularity score based on max clicks
                if max_click_count > 0:
                    popularity = result.get("click_count", 0) / max_click_count
                else:
                    popularity = 0.0

                # Calculate final score
                final_score = RankingEngine.calculate_final_score(
                    result.get("relevance_score", 0.0),
                    result.get("meta_score", 0.0),
                    popularity,
                )

                result["popularity_score"] = min(1.0, popularity)
                result["final_score"] = final_score
                ranked.append(result)

            # Sort by final score descending
            ranked.sort(key=lambda x: x["final_score"], reverse=True)

            logger.info(f"✅ Ranked {len(ranked)} results")
            return ranked

        except Exception as e:
            logger.error(f"❌ Error ranking results: {e}")
            return results


def get_ranking_engine() -> RankingEngine:
    """Factory function to get ranking engine"""
    return RankingEngine()
