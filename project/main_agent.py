from typing import Dict, Any

from project.agents.planner import Planner
from project.agents.worker import Worker
from project.agents.evaluator import Evaluator
from project.memory.session_memory import SessionMemory
from project.core.observability import get_logger
from project.core.a2a_protocol import A2AProtocol, AgentMessage


class MainAgent:
    """
    Orchestrates Planner → Worker → Evaluator for the YouTube → Blog Article Converter.
    """

    def __init__(self) -> None:
        self.logger = get_logger("MainAgent")
        self.memory = SessionMemory()
        self.planner = Planner()
        self.worker = Worker()
        self.evaluator = Evaluator()
        self.protocol = A2AProtocol()

    def handle_message(self, user_input: str) -> Dict[str, Any]:
        self.logger.info("Handling user input through MainAgent.")

        plan_msg: AgentMessage = self.protocol.build_message(
            sender="user",
            receiver="planner",
            task="plan_youtube_to_blog",
            payload={"user_input": user_input},
        )

        plan = self.planner.create_plan(
            user_input=plan_msg.payload["user_input"],
            memory=self.memory,
        )

        worker_msg: AgentMessage = self.protocol.build_message(
            sender="planner",
            receiver="worker",
            task="generate_blog",
            payload={"plan": plan},
        )

        draft = self.worker.generate_blog(
            plan=worker_msg.payload["plan"],
            memory=self.memory,
        )

        evaluator_msg: AgentMessage = self.protocol.build_message(
            sender="worker",
            receiver="evaluator",
            task="evaluate_blog",
            payload={"draft": draft, "plan": plan},
        )

        evaluation = self.evaluator.evaluate(
            draft=evaluator_msg.payload["draft"],
            plan=evaluator_msg.payload["plan"],
            memory=self.memory,
        )

        response_text = evaluation.get("final_article", "")

        result: Dict[str, Any] = {
            "response": response_text,
            "plan": plan,
            "draft": draft,
            "evaluation": evaluation,
        }

        self.logger.info("MainAgent finished processing.")
        return result


def run_agent(user_input: str):
    agent = MainAgent()
    result = agent.handle_message(user_input)
    return result["response"]
