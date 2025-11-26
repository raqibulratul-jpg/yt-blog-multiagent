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

        body_parts: List[str] = []
        for idx, sec in enumerate(sections, start=1):
            sec_summary = self.summarizer.summarize(sec, max_sentences=2)
            body_parts.append(f"## Section {idx}\n\n{sec_summary}\n")

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

        article_body = "\n".join(header_meta) + "\n".join(body_parts)

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
