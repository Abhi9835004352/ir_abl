import logging
import numpy as np
from typing import List, Dict, Tuple, Optional
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.utils.tokenizer import tokenize
from app.utils.text_cleaner import clean_text, remove_stopwords

logger = logging.getLogger(__name__)


class TFIDFEngine:
    """TF-IDF vectorization and ranking engine"""

    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            max_features=500,
            min_df=1,
            max_df=0.8,
            ngram_range=(1, 2),
            lowercase=True,
            stop_words="english",
        )
        self.fitted = False
        self.vectors = None
        self.texts = None

    def fit(self, documents: List[str]) -> bool:
        """
        Fit TF-IDF vectorizer on documents

        Args:
            documents: List of document texts

        Returns:
            True if successful
        """
        try:
            if not documents or all(not doc for doc in documents):
                logger.warning("⚠️ Empty documents list for TF-IDF fitting")
                return False

            # Filter out empty documents
            valid_docs = [doc if doc else " " for doc in documents]

            self.vectors = self.vectorizer.fit_transform(valid_docs)
            self.texts = valid_docs
            self.fitted = True

            logger.info(f"✅ Fitted TF-IDF vectorizer on {len(documents)} documents")
            return True

        except Exception as e:
            logger.error(f"❌ Error fitting TF-IDF: {e}")
            return False

    def rank_documents(
        self, query: str, documents: List[str], doc_ids: List[str]
    ) -> List[Tuple[str, float]]:
        """
        Rank documents by similarity to query

        Args:
            query: Search query
            documents: List of document texts
            doc_ids: List of document IDs

        Returns:
            List of (doc_id, relevance_score) tuples, sorted by score
        """
        try:
            if not documents or not doc_ids:
                return []

            if len(documents) != len(doc_ids):
                logger.error("❌ Documents and IDs length mismatch")
                return []

            # Vectorize query
            query_vector = self.vectorizer.transform([query])

            # Vectorize documents
            doc_vectors = self.vectorizer.transform(documents)

            # Calculate cosine similarity
            similarities = cosine_similarity(query_vector, doc_vectors)[0]

            # Create results tuples
            results = list(zip(doc_ids, similarities))

            # Sort by similarity (descending)
            results.sort(key=lambda x: x[1], reverse=True)

            return results

        except Exception as e:
            logger.error(f"❌ Error ranking documents: {e}")
            return []

    def get_query_vector(self, query: str) -> Optional[List[float]]:
        """Get TF-IDF vector for a query"""
        try:
            vector = self.vectorizer.transform([query]).toarray()[0]
            return vector.tolist()
        except Exception as e:
            logger.error(f"❌ Error getting query vector: {e}")
            return None

    def get_document_vector(self, document: str) -> Optional[List[float]]:
        """Get TF-IDF vector for a document"""
        try:
            vector = self.vectorizer.transform([document]).toarray()[0]
            return vector.tolist()
        except Exception as e:
            logger.error(f"❌ Error getting document vector: {e}")
            return None


def get_tfidf_engine() -> TFIDFEngine:
    """Factory function to get TF-IDF engine"""
    return TFIDFEngine()
