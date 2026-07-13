from app.logger import logger
from app.xml_loader import load_all_documents
from app.embeddings import EmbeddingManager


def main():
    """
    Build the vector database from the MedQuAD dataset.
    """

    logger.info("=" * 60)
    logger.info("Starting document ingestion...")
    logger.info("=" * 60)

    # Step 1: Load XML documents
    documents = load_all_documents()

    logger.info(f"Total documents loaded: {len(documents)}")

    # Step 2: Create embeddings and vector database
    embedding_manager = EmbeddingManager()

    vector_db = embedding_manager.create_vector_store(documents)

    logger.info("=" * 60)
    logger.info("Ingestion completed successfully!")
    logger.info("=" * 60)

    print("\n✅ Vector Database Created Successfully!")


if __name__ == "__main__":
    main()