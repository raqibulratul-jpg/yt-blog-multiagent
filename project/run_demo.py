import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from project.main_agent import run_agent


if __name__ == "__main__":
    print("=" * 60)
    print("YouTube → Blog Article Converter")
    print("=" * 60)
    
    youtube_url = input("\nEnter YouTube URL: ").strip()
    
    if not youtube_url:
        print("Error: No URL provided. Exiting...")
        sys.exit(1)
    
    print("\nProcessing your video...\n")
    
    result = run_agent(youtube_url)
    
    print("\n" + "=" * 60)
    print("GENERATED BLOG ARTICLE")
    print("=" * 60)
    print(result)
    
    # Ask user if they want to save to a file
    print("\n" + "=" * 60)
    save_choice = input("\nDo you want to save this transcript to a file? (yes/no): ").strip().lower()
    
    if save_choice in ['yes', 'y']:
        # Generate unique filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"youtube_transcript_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"\n✓ Transcript saved successfully to: {filename}")
        except Exception as e:
            print(f"\n✗ Error saving file: {e}")
    else:
        print("\n✓ File not saved. Thank you for using the YouTube → Blog Converter!")
