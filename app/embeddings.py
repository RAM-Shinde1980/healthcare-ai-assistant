from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from app.config import Config
from app.logger import logger


class EmbeddingManager:
    """
    Handles text splitting, embedding generation,
    and vector database operations.
    """

    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name=Config.EMBEDDING_MODEL
        )

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP,
        )

    def create_vector_store(self, documents):
        """
        Split documents and create ChromaDB.
        """

        logger.info("Splitting documents...")

        chunks = self.text_splitter.split_documents(documents)

        logger.info(f"Created {len(chunks)} chunks.")

        logger.info("Generating embeddings...")

        vector_db = Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding_model,
            persist_directory=Config.VECTOR_DB_PATH,
        )

        logger.info("Vector Store Created Successfully.")

        return vector_db

    def load_vector_store(self):
        """
        Load existing ChromaDB.
        """

        logger.info("Loading existing vector database...")

        return Chroma(
            persist_directory=Config.VECTOR_DB_PATH,
            embedding_function=self.embedding_model,
        )