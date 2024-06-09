import logging
from typing import Optional


def get_logger(level: Optional[str] = None) -> logging.Logger:
    logger = logging.getLogger(__name__)
    if not logger.hasHandlers():
        logger.addHandler(logging.StreamHandler())
    if level is not None:
        level = getattr(logging, level.upper())
        logger.setLevel(level)
    return logger
