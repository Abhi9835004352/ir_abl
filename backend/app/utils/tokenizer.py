import re
import logging

logger = logging.getLogger(__name__)


def tokenize(text: str) -> list:
    """Simple word tokenizer"""
    if not text:
        return []

    # Convert to lowercase
    text = text.lower()

    # Split on whitespace and punctuation
    tokens = re.findall(r"\b\w+\b", text)

    return tokens


def get_ngrams(tokens: list, n: int = 2) -> list:
    """Generate n-grams from tokens"""
    ngrams = []
    for i in range(len(tokens) - n + 1):
        ngram = " ".join(tokens[i : i + n])
        ngrams.append(ngram)
    return ngrams
