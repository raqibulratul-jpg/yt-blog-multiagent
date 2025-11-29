"""
Quick test script to verify YouTube transcript fetching works.
"""

from project.tools.tools import TranscriptFetcher

def test_transcript_fetch():
    fetcher = TranscriptFetcher()
    
    # Test with a popular YouTube video (replace with any video that has transcripts)
    # Using a TED talk as an example - they usually have transcripts
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    
    print("Testing YouTube transcript fetching...")
    print(f"URL: {test_url}")
    print("-" * 50)
    
    try:
        transcript = fetcher.fetch(test_url)
        print(f"✓ Success! Fetched transcript with {len(transcript)} characters")
        print(f"\nFirst 200 characters:\n{transcript[:200]}...")
        return True
    except ValueError as e:
        print(f"✗ Error: {e}")
        print("\nTip: Try with a different video URL that has captions enabled.")
        return False

if __name__ == "__main__":
    test_transcript_fetch()
