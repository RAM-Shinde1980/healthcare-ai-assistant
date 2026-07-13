from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


class Config:
    """
    Central configuration for the Healthcare AI Assistant.
    """

    MODEL_NAME = os.getenv("MODEL_NAME", "llama3")

    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "BAAI/bge-small-en-v1.5"
    )

    VECTOR_DB_PATH = os.getenv(
        "VECTOR_DB_PATH",
        "vector_store"
    )

    DATA_FOLDER = os.getenv(
        "DATA_FOLDER",
        "data"
    )

    LOG_LEVEL = os.getenv(
        "LOG_LEVEL",
        "INFO"
    )

    CHUNK_SIZE = int(
        os.getenv("CHUNK_SIZE", 700)
    )

    CHUNK_OVERLAP = int(
        os.getenv("CHUNK_OVERLAP", 150)
    )

    TOP_K = int(
        os.getenv("TOP_K", 3)
    )