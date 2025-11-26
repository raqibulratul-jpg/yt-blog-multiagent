from typing import Dict, Any

from project.core.observability import get_logger
from project.memory.session_memory import SessionMemory


class Evaluator:
    """
    Evaluator agent that scores and returns the final article.
    """

    def __init__(self) -> None:
        self.logger = get_logger("Evaluator")

    def evaluate(self, draft: Dict[str, Any], plan: Dict[str, Any], memory: SessionMemory) -> Dict[str, Any]:
        self.logger.info("Evaluating draft.")
        body = draft.get("body", "").strip()

        if not body:
            score = 0.0
            feedback = "No article content generated."
            final_article = "No article generated."
        else:
            score = 1.0
            feedback = "For this demo, the generated article looks acceptable."
            final_article = body

        result: Dict[str, Any] = {
            "score": score,
            "feedback": feedback,
            "final_article": final_article,
        }

        memory.set("last_evaluation", result)
        self.logger.info("Evaluation complete with score %.2f.", score)
        return result
