from dataclasses import dataclass, field
from typing import Any, Dict, Optional


@dataclass
class AgentMessage:
    """
    Message format for agent-to-agent communication.
    """
    sender: str
    receiver: str
    task: str
    payload: Dict[str, Any] = field(default_factory=dict)
    meta: Optional[Dict[str, Any]] = None


class A2AProtocol:
    """
    Simple helper to build messages between agents.
    """

    def build_message(
        self,
        sender: str,
        receiver: str,
        task: str,
        payload: Dict[str, Any],
        meta: Optional[Dict[str, Any]] = None,
    ) -> AgentMessage:
        return AgentMessage(
            sender=sender,
            receiver=receiver,
            task=task,
            payload=payload,
            meta=meta,
        )
