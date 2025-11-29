from typing import Dict, Any, List

from project.tools.tools import SimpleSummarizer, SEOKeywordGenerator, estimate_reading_time
from project.core.observability import get_logger
from project.memory.session_memory import SessionMemory


class Worker:
    """
    Worker agent that turns a transcript plan into a blog-style article.
    """

    def __init__(self) -> None:
        self.logger = get_logger("Worker")
        self.summarizer = SimpleSummarizer()
        self.keyword_gen = SEOKeywordGenerator()

    def generate_blog(self, plan: Dict[str, Any], memory: SessionMemory) -> Dict[str, Any]:
        self.logger.info("Generating blog content from plan.")
        transcript: str = plan.get("transcript", "")
        timestamped_transcript: List[Dict] = plan.get("timestamped_transcript", [])
        sections: List[str] = plan.get("sections", [])
        style = plan.get("style", {})

        overall_summary = (
            self.summarizer.summarize(transcript, max_sentences=3)
            if transcript
            else ""
        )
        keywords = self.keyword_gen.generate(transcript)
        est_read_time = estimate_reading_time(transcript)

        title = "Blog Article based on YouTube Video"
        if keywords:
            title = f"{keywords[0].capitalize()} – A Blog Based on a YouTube Video"

        # Format timestamped transcript
        timestamped_sections: List[str] = []
        timestamped_sections.append("## Timestamped Transcript\n")
        
        for entry in timestamped_transcript:
            start_time = entry['start']
            end_time = start_time + entry['duration']
            text = entry['text']
            
            # Format time as MM:SS
            start_min = int(start_time // 60)
            start_sec = int(start_time % 60)
            end_min = int(end_time // 60)
            end_sec = int(end_time % 60)
            
            timestamped_sections.append(
                f"{start_min:02d}:{start_sec:02d} - {end_min:02d}:{end_sec:02d}: {text}\n"
            )

        header_meta = [
            f"# {title}",
            "",
            f"**Estimated reading time:** {est_read_time:.1f} minutes",
            "",
        ]

        if overall_summary:
            header_meta.append(f"**Summary:** {overall_summary}\n")

        if keywords:
            header_meta.append(f"**SEO Keywords:** {', '.join(keywords)}\n")

        # Combine all parts with developer credit at the end
        article_body = (
            "\n".join(header_meta) + 
            "\n".join(timestamped_sections) +
            "\n" + "="*60 + "\n" +
            "Developed by Raqibul Islam Ratul\n" +
            "="*60
        )

        draft: Dict[str, Any] = {
            "title": title,
            "summary": overall_summary,
            "keywords": keywords,
            "body": article_body,
            "style": style,
        }

        memory.set("last_draft", draft)
        self.logger.info("Draft generated with length %d characters.", len(article_body))
        return draft
