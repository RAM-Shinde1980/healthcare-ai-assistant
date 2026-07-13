from app.rag import RAGRetriever
from app.llm import LLMManager
from app.logger import logger


class HealthcareAgent:
    """
    Complete RAG pipeline:
    User Question
        ↓
    Retrieve Documents
        ↓
    Generate Answer
        ↓
    Return Response
    """

    def __init__(self):
        logger.info("Initializing Healthcare Agent...")

        self.retriever = RAGRetriever()
        self.llm = LLMManager()

    def ask(self, question: str):
        """
        Ask a medical question and receive an AI-generated answer.
        """

        logger.info(f"Question: {question}")

        documents = self.retriever.retrieve(question)

        answer = self.llm.generate_answer(
            question,
            documents,
        )

        return answer