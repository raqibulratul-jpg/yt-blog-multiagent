from typing import Dict, Any

from project.tools.tools import TranscriptFetcher
from project.core.context_engineering import chunk_text
from project.core.observability import get_logger
from project.memory.session_memory import SessionMemory


class Planner:
    """
    Planner agent for the YouTube → Blog Article Converter.

    Responsibilities:
    - Fetch a transcript (simulated here)
    - Break it into sections
    - Build a high-level plan for the worker
    """

    def __init__(self) -> None:
        self.logger = get_logger("Planner")
        self.transcript_fetcher = TranscriptFetcher()

    def create_plan(self, user_input: str, memory: SessionMemory) -> Dict[str, Any]:
        self.logger.info("Creating plan for user input.")
        style_prefs = memory.get(
            "style_preferences",
            {"tone": "simple", "length": "medium"},
        )

        transcript = self.transcript_fetcher.fetch(user_input)
        sections = chunk_text(transcript, max_chars=800)

        plan: Dict[str, Any] = {
            "task": "youtube_to_blog",
            "original_input": user_input,
            "transcript": transcript,
            "sections": sections,
            "style": style_prefs,
        }

        memory.set("last_plan", plan)
        self.logger.info("Plan created with %d sections.", len(sections))
        return plan
