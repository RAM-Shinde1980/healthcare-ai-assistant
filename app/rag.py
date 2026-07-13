from app.embeddings import EmbeddingManager
from app.logger import logger


class RAGRetriever:
    """
    Handles retrieval from the vector database.
    """

    def __init__(self):
        self.embedding_manager = EmbeddingManager()
        self.vector_db = self.embedding_manager.load_vector_store()

    def retrieve(self, query: str, k: int = 5):
        """
        Retrieve the top-k most relevant documents.
        """

        logger.info(f"Searching for: {query}")

        documents = self.vector_db.similarity_search(
            query=query,
            k=k
        )

        logger.info(f"Retrieved {len(documents)} documents.")

        return documents