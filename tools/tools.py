from typing import List, Dict
import re
from collections import Counter


class TranscriptFetcher:
    """
    Dummy YouTube transcript fetcher.

    In a real deployment, replace this with actual YouTube API / transcript fetching logic.
    """

    def fetch(self, url_or_query: str) -> str:
        # For demo purposes, we simulate a transcript.
        base_text = (
            "Welcome to this YouTube video. In this session, we discuss how to convert videos into blog articles. "
            "We cover the main ideas, break down the content into sections, and show how AI can automate this process. "
            "By the end, you will understand how to design a YouTube to blog converter using multi-agent systems."
        )
        simulated = f"Simulated transcript for: {url_or_query}\n\n{base_text}"
        return simulated


class SimpleSummarizer:
    """
    Very simple extractive summarizer based on sentence splitting.
    """

    def summarize(self, text: str, max_sentences: int = 3) -> str:
        if not text:
            return ""
        # Split on '.', '!', '?'
        sentences = re.split(r'(?<=[.!?])\s+', text.strip())
        sentences = [s.strip() for s in sentences if s.strip()]
        return " ".join(sentences[:max_sentences])


class SEOKeywordGenerator:
    """
    Naive keyword extractor based on word frequency.
    """

    def generate(self, text: str, max_keywords: int = 8) -> List[str]:
        if not text:
            return []
        # Lowercase and keep simple words
        tokens = re.findall(r"[a-zA-Z]{4,}", text.lower())
        stopwords = {
            "this", "that", "with", "from", "your", "will", "into", "about",
            "have", "there", "their", "which", "such", "also", "been", "they",
            "them", "then", "than", "when", "where", "what", "would", "could",
            "should", "video", "youtube", "using"
        }
        tokens = [t for t in tokens if t not in stopwords]
        freq = Counter(tokens)
        most_common = [w for w, _ in freq.most_common(max_keywords)]
        return most_common


def estimate_reading_time(text: str, words_per_minute: int = 200) -> float:
    """
    Rough estimate of reading time in minutes.
    """
    words = re.findall(r"\w+", text)
    if not words:
        return 0.0
    return max(0.1, len(words) / float(words_per_minute))
