from typing import List, Dict, Optional
import re
from collections import Counter
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable


class TranscriptFetcher:
    """
    Real YouTube transcript fetcher using youtube-transcript-api.
    """

    def fetch(self, url_or_query: str) -> str:
        """
        Fetch the actual transcript from a YouTube video.
        
        Args:
            url_or_query: YouTube URL or video ID
            
        Returns:
            The complete transcript as a single string
            
        Raises:
            ValueError: If video ID cannot be extracted or transcript is unavailable
        """
        video_id = self._extract_video_id(url_or_query)
        
        if not video_id:
            raise ValueError(f"Could not extract video ID from: {url_or_query}")
        
        try:
            # Fetch the transcript
            api = YouTubeTranscriptApi()
            
            # List available transcripts
            transcript_list = api.list(video_id)
            
            # Try to find English transcript, or use first available
            try:
                transcript = transcript_list.find_transcript(['en'])
            except:
                # If English not available, use the first available transcript
                transcript = transcript_list.find_generated_transcript(['en']) if transcript_list else None
                if not transcript:
                    available = list(transcript_list)
                    if available:
                        transcript = available[0]
                    else:
                        raise ValueError("No transcripts available")
            
            # Fetch the actual transcript data
            transcript_result = api.fetch(transcript.video_id, [transcript.language_code])
            
            # Combine all transcript segments into a single string
            full_transcript = " ".join([snippet.text for snippet in transcript_result])
            
            return full_transcript
            
        except TranscriptsDisabled:
            raise ValueError(f"Transcripts are disabled for video: {video_id}")
        except NoTranscriptFound:
            raise ValueError(f"No transcript found for video: {video_id}")
        except VideoUnavailable:
            raise ValueError(f"Video is unavailable: {video_id}")
        except Exception as e:
            raise ValueError(f"Error fetching transcript: {str(e)}")
    
    def _extract_video_id(self, url_or_query: str) -> Optional[str]:
        """
        Extract video ID from various YouTube URL formats.
        
        Supports:
        - https://www.youtube.com/watch?v=VIDEO_ID
        - https://youtu.be/VIDEO_ID
        - https://www.youtube.com/embed/VIDEO_ID
        - https://www.youtube.com/v/VIDEO_ID
        - Just the video ID itself
        """
        # Pattern for youtube.com/watch?v=
        pattern1 = r'(?:youtube\.com\/watch\?v=)([a-zA-Z0-9_-]{11})'
        # Pattern for youtu.be/
        pattern2 = r'(?:youtu\.be\/)([a-zA-Z0-9_-]{11})'
        # Pattern for youtube.com/embed/ or youtube.com/v/
        pattern3 = r'(?:youtube\.com\/(?:embed|v)\/)([a-zA-Z0-9_-]{11})'
        # Pattern for just the video ID (11 characters)
        pattern4 = r'^([a-zA-Z0-9_-]{11})$'
        
        for pattern in [pattern1, pattern2, pattern3, pattern4]:
            match = re.search(pattern, url_or_query)
            if match:
                return match.group(1)
        
        return None
    
    def fetch_with_timestamps(self, url_or_query: str) -> List[Dict]:
        """
        Fetch transcript with timestamp information.
        
        Returns:
            List of dicts with 'start', 'duration', 'text' keys
        """
        video_id = self._extract_video_id(url_or_query)
        
        if not video_id:
            raise ValueError(f"Could not extract video ID from: {url_or_query}")
        
        try:
            api = YouTubeTranscriptApi()
            
            # List available transcripts
            transcript_list = api.list(video_id)
            
            # Try to find English transcript, or use first available
            try:
                transcript = transcript_list.find_transcript(['en'])
            except:
                # If English not available, use the first available transcript
                transcript = transcript_list.find_generated_transcript(['en']) if transcript_list else None
                if not transcript:
                    available = list(transcript_list)
                    if available:
                        transcript = available[0]
                    else:
                        raise ValueError("No transcripts available")
            
            # Fetch the actual transcript data
            transcript_result = api.fetch(transcript.video_id, [transcript.language_code])
            
            # Return list of timestamped segments
            return [
                {
                    'start': snippet.start,
                    'duration': snippet.duration,
                    'text': snippet.text
                }
                for snippet in transcript_result
            ]
            
        except TranscriptsDisabled:
            raise ValueError(f"Transcripts are disabled for video: {video_id}")
        except NoTranscriptFound:
            raise ValueError(f"No transcript found for video: {video_id}")
        except VideoUnavailable:
            raise ValueError(f"Video is unavailable: {video_id}")
        except Exception as e:
            raise ValueError(f"Error fetching transcript: {str(e)}")


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
