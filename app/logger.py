import logging
import os

from app.config import Config

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

LOG_FILE = os.path.join("logs", "healthcare_ai.log")

logger = logging.getLogger("HealthcareAI")

# Prevent duplicate handlers if the module is imported multiple times
if not logger.handlers:
    logger.setLevel(getattr(logging, Config.LOG_LEVEL.upper(), logging.INFO))

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # File Handler
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)