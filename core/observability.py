import logging
from typing import Optional

_LOGGER_INITIALIZED = False


def _init_logging() -> None:
    global _LOGGER_INITIALIZED
    if not _LOGGER_INITIALIZED:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        )
        _LOGGER_INITIALIZED = True


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Returns a module-level logger configured with a simple formatter.
    """
    _init_logging()
    return logging.getLogger(name or "project")
