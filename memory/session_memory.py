from typing import Any, Dict


class SessionMemory:
    """
    Simple in-memory key-value store for agent sessions.
    """

    def __init__(self) -> None:
        self._store: Dict[str, Any] = {}

    def set(self, key: str, value: Any) -> None:
        self._store[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self._store.get(key, default)

    def to_dict(self) -> Dict[str, Any]:
        return dict(self._store)
